from tthAnalysis.HiggsToTauTau.jobTools import run_cmd
from tthAnalysis.HiggsToTauTau.common import logging

import os.path
import re
import multiprocessing
import signal
import psutil
import sys

HLT_SUFFIX = re.compile(r'(.*_v\*$)|(.*_v[0-9]+)$')
DATASET    = re.compile(r'^/.*/Run(?P<year>[\d]{4})(?P<era>[ABCDEFGH]{1}).*/MINIAOD$')
LUMI_UNITS = [ '/fb', '/pb', '/nb', '/ub' ]

trigger_results = {}

def hlt_version(hlt_path):
  if not HLT_SUFFIX.match(hlt_path):
    new_hlt_path = '{}_v*'.format(hlt_path)
    logging.debug("Changing {} to {} in brilcalc queries".format(hlt_path, new_hlt_path))
    return new_hlt_path
  else:
    return hlt_path

def process_hlt(hlt_path, golden_json, brilcalc_path, normtag, units):
  brilcalc_cmd = '{brilcalc_path} lumi -c web {json} {normtag} --output-style csv --hltpath "{hlt_path}" -u {units}'.format(
    brilcalc_path = brilcalc_path,
    json          = ('-i {}'.format(golden_json)    if golden_json else ''),
    normtag       = ('--normtag {}'.format(normtag) if normtag     else ''),
    hlt_path      = hlt_path,
    units         = units,
  )
  logging.debug("Running: {}".format(brilcalc_cmd))
  brilcalc_out, brilcalc_err = run_cmd(brilcalc_cmd, do_not_log = True, return_stderr = True)
  if brilcalc_err:
    raise ValueError("brilcalc return an error: %s" % brilcalc_err)
  logging.debug("Parsing results for {}".format(hlt_path))
  brilcalc_out_split = brilcalc_out.rstrip('\n').split('\n')
  brilcalc_out_split = list(map(lambda line: line.rstrip('\r'), brilcalc_out_split))

  read_runs = 0
  delivered, recorded = 0., 0.
  runs = []
  hlt_paths = []
  for line in brilcalc_out_split:
    if line.startswith("#run:fill,time,ncms,hltpath"):
      if read_runs == 0:
        read_runs = 1
    elif line.startswith("#Summary:"):
      read_runs = -1
    elif line.startswith("#HLT_"):
      line_split = line.replace('#', '').split(',')
      hlt_paths.append({
        'hltpath'      : line_split[0],
        'nfill'        : int(line_split[1]),
        'nrun'         : int(line_split[2]),
        'ncms'         : int(line_split[3]),
        'totdelivered' : float(line_split[4]),
        'totrecorded'  : float(line_split[5]),
      })
    elif line.startswith("#Sum delivered"):
      delivered = float(line.split()[-1])
    elif line.startswith("#Sum recorded"):
      recorded = float(line.split()[-1])
    else:
      if read_runs > 0:
        runs.append(int(line.split(':')[0]))
      else:
        pass

  dict_entry = {
    'runs' : runs,
    'delivered' : delivered,
    'recorded'  : recorded,
    'paths'     : hlt_paths,
  }
  return hlt_path, dict_entry

def get_trigger_results(results):
  trigger_results[results[0]] = results[1]

parent_id = os.getpid()
def handle_worker():
  def sig_int(signal_num, frame):
    parent = psutil.Process(parent_id)
    for child in parent.children():
      if child.pid != os.getpid():
        child.kill()
    parent.kill()
    psutil.Process(os.getpid()).kill()
  signal.signal(signal.SIGINT, sig_int)

def parse_data(data_file):
  if not os.path.isfile(data_file):
    raise ValueError("No such file: %s" % data_file)

  runs = {}
  read_runs = 0
  golden_json = ""
  normtag = ""
  tot_delivered_all, tot_recorded_all = 0., 0.
  units = ""
  with open(data_file, 'r') as data:
    for line in data:
      line_stripped = line.rstrip('\n')
      if not line_stripped:
        continue
      if line_stripped.startswith("# DAS name"):
        read_runs = 1
      else:
        line_split = line_stripped.split()

        if read_runs > 0:
          dataset_match = DATASET.match(line_split[0])
          if not dataset_match:
            raise RuntimeError("Invalid line in file %s: %s" % (data_file, line_stripped))
          run_era = dataset_match.group('era')
          run_start, run_end = line_split[1].split('-')
          tot_delivered = float(line_split[3])
          tot_recorded = float(line_split[4])
          if run_era not in runs:
            runs[run_era] = {
              'run_start'     : run_start,
              'run_end'       : run_end,
              'tot_delivered' : tot_delivered,
              'tot_recorded'  : tot_recorded,
            }
          runs[run_era]['run_start']     = min(runs[run_era]['run_start'],     run_start)
          runs[run_era]['run_end']       = max(runs[run_era]['run_end'],       run_end)
          runs[run_era]['tot_delivered'] = max(runs[run_era]['tot_delivered'], tot_delivered)
          runs[run_era]['tot_recorded']  = max(runs[run_era]['tot_recorded'],  tot_recorded)
        else:
          if line_stripped.startswith("# file generated"):
            read_runs = -1
          elif line_stripped.startswith("# golden JSON"):
            golden_json = line_split[3]
          elif line_stripped.startswith("# normtag"):
            normtag = line_split[2]
          elif line_stripped.startswith("# totdelivered"):
            tot_delivered_all = float(line_split[2])
            if not units:
              units = re.match('totdelivered\((?P<units>.*)\)', line_split[1]).group('units')
          elif line_stripped.startswith("# totrecorded"):
            tot_recorded_all = float(line_split[2])
            if not units:
              units = re.match('totrecorded\((?P<units>.*)\)', line_split[1]).group('units')
          else:
            continue

  data = {
    'runs'         : runs,
    'json'         : golden_json,
    'normtag'      : normtag,
    'totdelivered' : tot_delivered_all,
    'totrecorded'  : tot_recorded_all,
  }

  return data

def run_brilcalc(hlt_paths_in, json, normtag, units, brilcalc_path, data_file):
  assert (all(map(lambda hlt_path: hlt_path.startswith('HLT'), hlt_paths_in)))
  hlt_paths = {hlt_path: hlt_version(hlt_path) for hlt_path in hlt_paths_in}

  for input_file in (json, normtag):
    if input_file and not os.path.isfile(input_file):
      raise ValueError("No such file: %s" % input_file)
  if not os.path.isfile(brilcalc_path):
    raise ValueError("No such file: %s" % brilcalc_path)

  if data_file:
    data = parse_data(data_file)
    if data['normtag'] != os.path.basename(normtag):
      logging.warning("File {} is generated with normtag '{}' but requested using normtag '{}'".format(
        data_file, data['normtag'], normtag
      ))
    if data['json'] != os.path.basename(json):
      logging.warning("File {} is generated with JSON '{}' but requested using JSON '{}'".format(
        data_file, data['json'], json
      ))
  else:
    data = None

  sys.exit(1)

  # prepare the jobs
  pool_size = 12
  pool = multiprocessing.Pool(pool_size, handle_worker)

  logging.debug("Constructing pool for {} HLT paths".format(len(hlt_paths)))
  for hlt_path in hlt_paths:
    pool.apply_async(
      process_hlt,
      args     = (hlt_paths[hlt_path], json, brilcalc_path, normtag, units),
      callback = get_trigger_results,
    )
  pool.close()
  pool.join()
  logging.debug("Pool finished")

  # parse trigger_results
  for hlt_path in hlt_paths:
    dict_entry = trigger_results[hlt_paths[hlt_path]]
    print("HLT path: {} nrun = {} totdelivered = {} totrecorded = {} (units = {})".format(
      hlt_path, len(dict_entry['runs']), dict_entry['delivered'], dict_entry['recorded'], units,
    ))
    for hlt_dict in dict_entry['paths']:
      print("\t{} nfill = {} nrun = {} ncms = {} totdelivered = {} totrecorded = {}".format(
        hlt_dict['hltpath'], hlt_dict['nfill'], hlt_dict['nrun'], hlt_dict['ncms'], hlt_dict['totdelivered'],
        hlt_dict['totrecorded'],
      ))