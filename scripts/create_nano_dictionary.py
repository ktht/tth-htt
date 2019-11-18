#!/usr/bin/env python

from tthAnalysis.HiggsToTauTau.jobTools import human_size
from tthAnalysis.HiggsToTauTau.common import logging, SmartFormatter, load_meta_dict, Command
from tthAnalysis.HiggsToTauTau.safe_root import ROOT
from tthAnalysis.HiggsToTauTau.hdfs import hdfs

import argparse
import jinja2
import datetime
import os
import sys
import json
import math
import re
import array

header_str = """from collections import OrderedDict as OD

# file generated at {{ date }} with the following command:
# {{ command }}

{{ dict_name }} = OD()

"""

dictionary_entry_str = """{{ dict_name }}["{{ dbs_name }}"] = OD([
  ("type",                            "{{ sample_type }}"),
  ("sample_category",                 "{{ sample_category }}"),
  ("process_name_specific",           "{{ process_name_specific }}"),
  ("nof_files",                       {{ nof_files }}),
  ("nof_db_files",                    {{ nof_db_files }}),
  ("nof_events",                      { {%- for histogram_name, event_counts in nof_events.items() %}
    {{ "%-60s"|format("'%s'"|format(histogram_name)) }} : [ {% for event_count in event_counts -%}{{ '%12d'|format(event_count) }}, {% endfor %}],
  {%- endfor %}
  }),
  ("nof_tree_events",                 {{ nof_tree_events }}),
  ("nof_db_events",                   {{ nof_db_events }}),
  ("fsize_local",                     {{ fsize_local }}), # {{ fsize_local_human }}, avg file size {{ avg_fsize_local_human }}
  ("fsize_db",                        {{ fsize_db }}), # {{ fsize_db_human }}, avg file size {{ avg_fsize_db_human }}
  ("use_it",                          {{ use_it }}),{% if sample_type == "mc" %}
  ("xsection",                        {{ xsection }}),
  ("genWeight",                       {{ genWeight }}),{% endif %}
  ("triggers",                        {{ triggers }}),
  ("has_LHE",                         {{ has_LHE }}),
  ("LHE_set",                         "{{ LHE_set }}"),
  ("nof_reweighting",                 {{ nof_reweighting }}),
])
"""

dictionary_sum_events_str = """{{ dict_name }}["sum_events"] = [{%- for sample_list in sample_lists %}
  [ {% for sample in sample_list %}{{ "%-50s"|format("'%s',"|format(sample)) }} {% endfor %} ],
{%- endfor %}
]
"""

missing_branches_str = """{%- if is_available -%}
  {%- for missing_branch in missing_branches %}
    "{{ missing_branch }}",
  {%- endfor -%}
{%- else %}
    # not computed
{%- endif -%}
"""

LHE_REGEX = re.compile('(n|)LHE(Scale|Pdf)Weight')
BRANCH_NLHEREWEIGHTINGWEIGHT = 'nLHEReweightingWeight'
LHE_DOC_REGEX = re.compile('LHE pdf variation weights \(w_var \/ w\_nominal\) for LHA IDs (?P<lha_start>[0-9]+) - (?P<lha_end>[0-9]+)')
BRANCH_LHEPDFWEIGHT = 'LHEPdfWeight'
LHE_DOC = {
  91400  : { 'name' : 'PDF4LHC15_nnlo_30_pdfas',    'count' : 33  },
  306000 : { 'name' : 'NNPDF31_nnlo_hessian_pdfas', 'count' : 103 },
  260000 : { 'name' : 'NNPDF30_nlo_as_0118',        'count' : 101 },
  262000 : { 'name' : 'NNPDF30_lo_as_0130',         'count' : 101 },
  292000 : { 'name' : 'NNPDF30_nlo_nf_4_pdfas',     'count' : 103 },
  292200 : { 'name' : 'NNPDF30_nlo_nf_5_pdfas',     'count' : 103 },
}

def get_triggers(process_name_specific, is_data):
  if 'SingleElec' in process_name_specific:
    return ['1e', '1e1tau']
  if 'SingleMuon' in process_name_specific:
    return ['1mu', '1mu1tau']
  if 'DoubleEG' in process_name_specific:
    return ['2e', '3e']
  if 'DoubleMuon' in process_name_specific:
    return ['2mu', '3mu']
  if 'MuonEG' in process_name_specific:
    return ['1e1mu', '2e1mu', '1e2mu']
  if 'Tau' in process_name_specific:
    return ['1e1tau', '1mu1tau', '2tau']
  if 'EGamma' in process_name_specific: # merge of SingleElectron and DoubleEG PDs
    return ['1e', '1e1tau', '2e', '3e']
  if is_data:
    raise ValueError("Expected MC!")
  return [
    '1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau'
  ]

def round_sign(x, sign_digits = 6):
  return round(x, max(int(abs(math.floor(math.log10(x)))) + sign_digits, 0))

if __name__ == '__main__':
  parser = argparse.ArgumentParser(
    formatter_class = lambda prog: SmartFormatter(prog, max_help_position = 35)
  )
  parser.add_argument('-m', '--meta-dictionary', dest = 'meta_dictionary', metavar = 'file',
                      required = True, type = str,
                      help = 'R|Path to the meta dictionary')
  parser.add_argument('-N', '--output-dict-name', dest = 'output_dict_name', metavar = 'name',
                      type = str, default = 'sample',
                      help = 'R|Name of the output dictionary')
  parser.add_argument('-f', '--filter', dest = 'filter', metavar = 'name', required = False,
                      type = str, default = '.*',
                      help = 'R|Regular expression for selecting only specific samples')
  parser.add_argument('-o', '--output-directory', dest = 'output_directory', metavar = 'path',
                      type = str, default = '.',
                      help = 'R|Output directory')
  parser.add_argument('-g', '--generate-python', dest = 'generate_python', metavar = 'name',
                      type = str, default = 'dict.py',
                      help = 'R|File name of the new python dictionary')
  parser.add_argument('-s', '--skip-header', dest = 'skip_header', action = 'store_true',
                      default = False,
                      help = 'R|Skip dictionary definitions in the output')
  parser.add_argument('-E', '--era', dest = 'era', metavar = 'era', type = int, default = -1,
                      required = True, choices = (2016,2017,2018),
                      help = 'R|Era of the samples')
  parser.add_argument('-M', '--find-missing-branches', dest = 'missing_branches', action = 'store_true',
                      default = False,
                      help = 'R|Find missing branches from the superset of branches in a sample')
  parser.add_argument('-F', '--force', dest = 'force', action = 'store_true', default = False,
                      help = 'R|Force the creation of missing directories')
  parser.add_argument('-v', '--verbose', dest = 'verbose', action = 'store_true', default = False,
                      help = 'R|Enable verbose printout')
  args = parser.parse_args()

  if args.verbose:
    logging.getLogger().setLevel(logging.DEBUG)

  meta_dict = load_meta_dict(args.meta_dictionary, "meta_dictionary")
  sum_events = load_meta_dict(args.meta_dictionary, "sum_events")

  output = jinja2.Template(header_str).render(
    command = ' '.join([os.path.basename(__file__)] + sys.argv[1:]),
    date = '{date:%Y-%m-%d %H:%M:%S}'.format(date = datetime.datetime.now()),
    dict_name = args.output_dict_name,
  ) if not args.skip_header else ''

  for dbs_key, dbs_entry in meta_dict.items():
    logging.info('Creating entry for: {}'.format(dbs_key))
    assert(dbs_key.endswith(('/NANOAOD', '/NANOAODSIM')))
    dbs_query_str = "dasgoclient -query='file dataset={}' -json".format(dbs_key)
    dbs_query = Command(dbs_query_str)
    dbs_query.run()
    if not dbs_query.out or dbs_query.err:
      raise RuntimeError("Query %s threw an error: %s" % (dbs_query_str, dbs_query.err))
    files_json = json.loads(dbs_query.out)
    files = []
    for entry in files_json:
      file_name = entry['file'][0]['name']
      file_nevents = entry['file'][0]['nevents']
      file_size = entry['file'][0]['size']
      file_name_local = '/hdfs/cms{}'.format(file_name)
      file_present = hdfs.isfile(file_name_local) and file_size == hdfs.getsize(file_name_local)
      files.append({
        'name'       : file_name,
        'name_local' : file_name_local,
        'nevents'    : file_nevents,
        'size'       : file_size,
        'present'    : file_present,
      })
    files = sorted(files, key = lambda f: f['name'])
    files_present = list(filter(lambda f: f['present'], files))
    files_missing = list(filter(lambda f: not f['present'], files))
    if 'status: VALID' in dbs_entry['comment']:
      assert(sum(map(lambda f: f['nevents'], files)) == dbs_entry['nof_db_events'])
    if not files_present:
      continue

    is_data = dbs_entry['sample_category'] == 'data_obs'
    local_size = sum(map(lambda f: f['size'], files_present))
    local_events = sum(map(lambda f: f['nevents'], files_present))

    branch_names = set()

    lhe_doc = ''
    lhe_tried = False
    reweighting_tried = False
    nof_reweighting_weights = 0
    if not is_data:
      f = files_present[0]
      fp = ROOT.TFile.Open(f['name_local'], 'read')
      tree = fp.Get('Events')
      assert(tree.GetEntries() == f['nevents'])
      branches = [ br.GetName() for br in tree.GetListOfBranches() ]
      branch_names.update(branches)
      if not reweighting_tried:
        reweighting_tried = True
        if BRANCH_NLHEREWEIGHTINGWEIGHT in branches:
          nof_reweighting_weights_br = array.array('I', [0])
          tree.SetBranchAddress(BRANCH_NLHEREWEIGHTINGWEIGHT, nof_reweighting_weights_br)
          tree.GetEntry(0)
          nof_reweighting_weights = nof_reweighting_weights_br[0]
      if not lhe_tried:
        lhe_tried = True
        lhe_branch = tree.GetBranch(BRANCH_LHEPDFWEIGHT)
        if lhe_branch:
          lhe_doc = lhe_branch.GetTitle()
          lhe_match = LHE_DOC_REGEX.match(lhe_doc)
          if lhe_match:
            lhe_start = int(lhe_match.group('lha_start'))
            lhe_end = int(lhe_match.group('lha_end'))
            lhe_doc = 'LHA IDs {} - {}'.format(lhe_start, lhe_end)
            lhe_count = lhe_end - lhe_start + 1
            lhe_val = {}
            if lhe_start in LHE_DOC:
              lhe_val = LHE_DOC[lhe_start]
            elif (lhe_start - 1) in LHE_DOC:
              lhe_val = LHE_DOC[lhe_start - 1]
            if lhe_val:
              lhe_doc += ' -> {name} PDF set, expecting {count} weights'.format(**lhe_val)
            else:
              lhe_doc += ' -> unrecognizable PDF set'
            lhe_doc += ' (counted {} weights)'.format(lhe_count)
        fp.Close()
    has_lhe = any(map(lambda br: LHE_REGEX.match(br), branch_names))

    output += jinja2.Template(dictionary_entry_str).render(
          dict_name                       = args.output_dict_name,
          dbs_name                        = dbs_key,
          sample_type                     = 'data' if is_data else 'mc',
          sample_category                 = dbs_entry['sample_category'],
          process_name_specific           = dbs_entry['process_name_specific'],
          nof_files                       = len(files_present),
          nof_events                      = {}, # the vanilla NanoAOD Ntuples don't contain the event histograms
          nof_tree_events                 = local_events,
          nof_db_events                   = dbs_entry['nof_db_events'],
          nof_db_files                    = len(files),
          fsize_db                        = dbs_entry['fsize_db'],
          fsize_db_human                  = human_size(dbs_entry['fsize_db']),
          avg_fsize_db_human              = human_size(float(dbs_entry['fsize_db']) / dbs_entry['nof_db_files']),
          fsize_local                     = local_size,
          fsize_local_human               = human_size(local_size),
          avg_fsize_local_human           = human_size(float(local_size) / len(files_present)),
          use_it                          = dbs_entry['use_it'],
          xsection                        = round_sign(dbs_entry['xsection'], 6) if not is_data else None,
          genWeight                       = not is_data,
          triggers                        = get_triggers(dbs_entry['process_name_specific'], is_data),
          has_LHE                         = False if is_data else has_lhe,
          LHE_set                         = lhe_doc,
          nof_reweighting                 = nof_reweighting_weights,
#          missing_from_superset           = missing_branches_template_filled, #TODO
#          missing_completely              = completely_missing_branches_template_filled, #TODO
#          missing_hlt_paths               = missing_hlt_paths_filled, #TODO
#          hlt_paths                       = hlt_paths_filled, #TODO
#          paths                           = '\n'.join(path_entries_arr), #TODO
        ) + '\n\n'

  output += jinja2.Template(dictionary_sum_events_str).render(
    dict_name = args.output_dict_name,
    sample_lists = sum_events,
  ) + '\n\n'

  dictionary_path = os.path.join(args.output_directory, args.generate_python)
  with open(dictionary_path, 'w') as f:
    f.write(output)
  logging.info("Wrote the dictionary to {path}".format(path = dictionary_path))
