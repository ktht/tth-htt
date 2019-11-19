from tthAnalysis.HiggsToTauTau.common import logging

import math
import re
import os
import imp
import sys

HEADER_STR = """from collections import OrderedDict as OD

# file generated at {{ date }} with the following command:
# {{ command }}

{{ dict_name }} = OD()

"""

SUM_EVENTS_STR = """{{ dict_name }}["sum_events"] = [{%- for sample_list in sample_lists %}
  [ {% for sample in sample_list %}{{ "%-50s"|format("'%s',"|format(sample)) }} {% endfor %} ],
{%- endfor %}
]
"""

BRANCHES_LIST_STR = """{%- if is_available -%}
  {%- for missing_branch in missing_branches %}
    "{{ missing_branch }}",
  {%- endfor -%}
{%- else %}
    # not computed
{%- endif -%}
"""

LHE_REGEX = re.compile('(n|)LHE(Scale|Pdf)Weight')
LHE_DOC_REGEX = re.compile('LHE pdf variation weights \(w_var \/ w\_nominal\) for LHA IDs (?P<lha_start>[0-9]+) - (?P<lha_end>[0-9]+)')

BRANCH_NLHEREWEIGHTINGWEIGHT = 'nLHEReweightingWeight'
BRANCH_LHEPDFWEIGHT = 'LHEPdfWeight'

# see https://github.com/cms-nanoAOD/cmssw/blob/9a2728ac9f44fc45ba1aa56389e28c594207c0fe/PhysicsTools/NanoAOD/python/nano_cff.py#L99-L104
LHE_DOC = {
  91400  : { 'name' : 'PDF4LHC15_nnlo_30_pdfas',    'count' : 33  },
  306000 : { 'name' : 'NNPDF31_nnlo_hessian_pdfas', 'count' : 103 },
  260000 : { 'name' : 'NNPDF30_nlo_as_0118',        'count' : 101 },
  262000 : { 'name' : 'NNPDF30_lo_as_0130',         'count' : 101 },
  292000 : { 'name' : 'NNPDF30_nlo_nf_4_pdfas',     'count' : 103 },
  292200 : { 'name' : 'NNPDF30_nlo_nf_5_pdfas',     'count' : 103 },
}

def load_meta_dict(path, name):
  if not os.path.isfile(path):
    logging.error("No such dictionary file: {dict_path}".format(dict_path = path))
    sys.exit(1)
  imp_dict = imp.load_source('', path)
  if not hasattr(imp_dict, name):
    logging.error("No such dictionary in the file '{dict_path}': {dict_name}".format(
      dict_path = path, dict_name = name,
    ))
    sys.exit(1)
  samples = getattr(imp_dict, name)
  return samples

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
