#!/usr/bin/env python

from tthAnalysis.HiggsToTauTau.jobTools import human_size
from tthAnalysis.HiggsToTauTau.common import logging, SmartFormatter, Command
from tthAnalysis.HiggsToTauTau.analysisSettings import Triggers
from tthAnalysis.HiggsToTauTau.safe_root import ROOT
from tthAnalysis.HiggsToTauTau.hdfs import hdfs
from tthAnalysis.HiggsToTauTau.dictTools import HEADER_STR, SUM_EVENTS_STR, BRANCHES_LIST_STR, LHE_REGEX, LHE_DOC_REGEX, \
                                                BRANCH_NLHEREWEIGHTINGWEIGHT, BRANCH_LHEPDFWEIGHT, LHE_DOC, \
                                                get_triggers, round_sign, load_meta_dict

import argparse
import jinja2
import datetime
import os
import sys
import json
import array
import math

DICTIONARY_ENTRY_STR = """{{ dict_name }}["{{ dbs_name }}"] = OD([
  ("type",                            "{{ sample_type }}"),
  ("sample_category",                 "{{ sample_category }}"),
  ("parent",                          "{{ parent }}"),
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
  ("local_paths",
    [
{{ local_paths }}
    ]
  ),
  ("missing_paths",
    [
{{ missing_paths }}
    ]
  ),
  ("missing_completely",           [
{{ missing_completely }}
  ]),
  ("missing_from_superset",        [
{{ missing_from_superset }}
  ]),
  ("missing_hlt_paths",            [
{{ missing_hlt_paths }}
  ]),
  ("hlt_paths",                    [
{{ hlt_paths }}
  ]),
])
"""

def fmt_path(paths, name_str, nevents_str):
  path_arr = [ [ path[name_str], path[nevents_str] ] for path in paths ]
  output = []
  if path_arr:
    max_str = max(map(lambda path: len(path[0]), path_arr))
    max_int = max(map(lambda path: int(math.ceil(math.log10(path[1]))), path_arr))
    pads = list(map(lambda path: max_str - len(path[0]) + max_int - int(math.ceil(math.log10(path[1]))), path_arr))
    for path_idx, path in enumerate(path_arr):
      output.append('{}[ "{}",{} {} ]'.format(' ' * 6, path[0], ' ' * pads[path_idx], path[1]))
  return output

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
  triggerTable = Triggers(str(args.era))
  required_paths = set.union(*[ triggerTable.triggers_all[trigger_name] for trigger_name in get_triggers('', False) ])

  output = jinja2.Template(HEADER_STR).render(
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
      logging.info("No files found for dataset {}".format(dbs_key))
      continue
    if files_missing:
      logging.info("Missing {} files out of {} files in dataset {}".format(len(files_missing), len(files), dbs_key))

    is_data = dbs_entry['sample_category'] == 'data_obs'
    local_size = sum(map(lambda f: f['size'], files_present))
    local_events = sum(map(lambda f: f['nevents'], files_present))

    branch_names = []
    lhe_doc = ''
    lhe_tried = False
    reweighting_tried = False
    nof_reweighting_weights = 0

    for f in files_present:
      fp = ROOT.TFile.Open(f['name_local'], 'read')
      tree = fp.Get('Events')
      assert(tree.GetEntries() == f['nevents'])

      branches = [ br.GetName() for br in tree.GetListOfBranches() ]
      branch_names.append(branches)

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

    branch_names_union = set.union(*[ set(branch_arr) for branch_arr in branch_names ])
    branch_names_intersection = set.intersection(*[ set(branch_arr) for branch_arr in branch_names ])
    has_lhe = any(map(lambda br: LHE_REGEX.match(br), branch_names_union))

    hlt_paths = list(filter(lambda branch_name: branch_name.startswith('HLT_'), list(branch_names_union)))
    hlt_paths_filled = jinja2.Template(BRANCHES_LIST_STR).render(
      is_available = is_data,
      missing_branches = sorted(hlt_paths, key = lambda br: br.lower()),
    ).lstrip('\n')

    missing_hlt_paths = list(sorted(list(required_paths - branch_names_intersection), key = lambda br: br.lower()))
    missing_hlt_paths_filled = jinja2.Template(BRANCHES_LIST_STR).render(
      is_available = True,
      missing_branches = sorted(missing_hlt_paths, key = lambda br: br.lower()),
    ).lstrip('\n')

    missing_from_superset = set()
    if args.missing_branches:
      for branch_arr in branch_names:
        missing_from_superset.update(branch_names_union - set(branch_arr))
    missing_from_superset_filled = jinja2.Template(BRANCHES_LIST_STR).render(
      is_available = args.missing_branches and is_data,
      missing_branches = sorted(list(missing_from_superset), key = lambda br: br.lower()),
    ).lstrip('\n')

    missing_completely = list(triggerTable.triggers_flat & set(missing_from_superset))
    missing_completely_filled = jinja2.Template(BRANCHES_LIST_STR).render(
      is_available = args.missing_branches and is_data,
      missing_branches = sorted(list(missing_completely), key = lambda br: br.lower()),
    ).lstrip('\n')
    if missing_completely:
      logging.error(
        "Found an overlap b/w the list of required triggers and the list of missing branches in "
        "sample {}: {}".format(dbs_entry['process_name_specific'], ', '.join(missing_completely))
       )

    output += jinja2.Template(DICTIONARY_ENTRY_STR).render(
          dict_name                       = args.output_dict_name,
          dbs_name                        = dbs_key,
          sample_type                     = 'data' if is_data else 'mc',
          sample_category                 = dbs_entry['sample_category'],
          process_name_specific           = dbs_entry['process_name_specific'],
          parent                          = dbs_entry['parent_db'],
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
          missing_from_superset           = missing_from_superset_filled,
          missing_completely              = missing_completely_filled,
          missing_hlt_paths               = missing_hlt_paths_filled,
          hlt_paths                       = hlt_paths_filled,
          local_paths                     = ',\n'.join(fmt_path(files_present, 'name_local', 'nevents')),
          missing_paths                   = ',\n'.join(fmt_path(files_missing, 'name',       'nevents')),
        ) + '\n\n'

  output += jinja2.Template(SUM_EVENTS_STR).render(
    dict_name = args.output_dict_name,
    sample_lists = sum_events,
  ) + '\n\n'

  dictionary_path = os.path.join(args.output_directory, args.generate_python)
  with open(dictionary_path, 'w') as f:
    f.write(output)
  logging.info("Wrote the dictionary to {path}".format(path = dictionary_path))
