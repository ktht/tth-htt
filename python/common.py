import sys
import logging
import psutil
import signal
import subprocess
import shlex
import importlib
import argparse

logging.basicConfig(
  stream = sys.stdout,
  level  = logging.INFO,
  format = '%(asctime)s - %(levelname)s: %(message)s',
)

class SmartFormatter(argparse.ArgumentDefaultsHelpFormatter):
  def _split_lines(self, text, width):
    if text.startswith('R|'):
      return text[2:].splitlines()
    return argparse.ArgumentDefaultsHelpFormatter._split_lines(self, text, width)

def load_samples(era, is_postproc = True, base = 'tth', suffix = '', analysis_type = 'default'):
  assert(analysis_type in [ 'default', 'aux' ])
  if base == 'tth':
    base_str = 'tthAnalysis.HiggsToTauTau'
    sample_prefix = 'tthAnalyzeSamples'
  elif base == 'hh_multilepton':
    base_str = 'hhAnalysis.multilepton'
    sample_prefix = 'hhAnalyzeSamples'
  elif base == 'hh_bbww':
    base_str = 'hhAnalysis.bbww'
    sample_prefix = 'hhAnalyzeSamples'
  else:
    raise ValueError("Invalid base: %s" % base)
  assert(base_str and sample_prefix)
  assert(era in [ "2016", "2017", "2018" ])

  sample_name = 'samples_{}'.format(era)
  if analysis_type != 'default':
    sample_name = '{}_{}'.format(sample_name, analysis_type)
  sample_location = "{}.samples.{}_{}".format(base_str, sample_prefix, era)

  if not is_postproc:
    suffix_tmp = "nanoAOD"
    if suffix:
      suffix_tmp += "_{}".format(suffix)
    suffix = suffix_tmp

  if suffix:
    sample_location += "_{}".format(suffix)

  sample_module = importlib.import_module(sample_location)
  sample = getattr(sample_module, sample_name)

  return sample

def load_samples_aux(era, is_postproc = True, base = 'tth', suffix = ''):
  return load_samples(era, is_postproc, base, suffix, analysis_type = 'aux')

def load_samples_hh_multilepton(era, is_postproc = True, suffix = ''):
  return load_samples(era, is_postproc, "hh_multilepton", suffix)

def load_samples_hh_bbww(era, is_postproc = True, suffix = ''):
  return load_samples(era, is_postproc, "hh_bbww", suffix)

def load_samples_stitched(samples, era, load_dy = True, load_wjets = True):
  sample_module = importlib.import_module('tthAnalysis.HiggsToTauTau.samples.stitch')

  if load_dy and load_wjets:
    samples_binned = getattr(sample_module, 'samples_to_stitch_{}'.format(era))
  elif load_dy:
    samples_binned = getattr(sample_module, 'samples_to_stitch_DYJets_{}'.format(era))
  elif load_wjets:
    samples_binned = getattr(sample_module, 'samples_to_stitch_WJets_{}'.format(era))
  else:
    raise ValueError("Must load binned DY, binned W+jets or both")

  sample_names = []
  for sample_set in samples_binned:
    for sample_key, sample_value in sample_set.items():
      if sample_key == 'inclusive':
        sample_names.extend(sample_value['samples'])
      else:
        for sample_binned_value in sample_value:
          sample_names.extend(sample_binned_value['samples'])

  for sample_key, sample_info in samples.items():
    if sample_key == 'sum_events':
      continue
    if load_dy and sample_info['process_name_specific'].startswith('DY'):
      sample_info['use_it'] = sample_info['process_name_specific'] in sample_names
    if load_wjets and sample_info['process_name_specific'].startswith(
          ('WJetsToLNu', 'W1JetsToLNu', 'W2JetsToLNu', 'W3JetsToLNu', 'W4JetsToLNu')
        ):
      sample_info['use_it'] = sample_info['process_name_specific'] in sample_names

  return samples

class Alarm(Exception):
  pass

def alarm_handler(signum, frame):
  raise Alarm

class Command(object):
  def __init__(self, cmd):
    self.cmd = cmd
    self.process = None
    self.out = None
    self.err = None
    self.success = False

  def run(self, max_tries = 20, timeout = 5):
    ntries = 0
    while not self.success:
      if ntries > max_tries:
        break
      ntries += 1
      signal.signal(signal.SIGALRM, alarm_handler)
      signal.alarm(timeout)
      self.process = subprocess.Popen(shlex.split(self.cmd), stdout = subprocess.PIPE, stderr = subprocess.PIPE)
      try:
        self.out, self.err = self.process.communicate()
        signal.alarm(0)
      except Alarm:
        parent = psutil.Process(self.process.pid)
        for child in parent.children(recursive = True):
          child.kill()
        parent.kill()
      else:
        self.success = True
