#!/usr/bin/env python

from tthAnalysis.HiggsToTauTau.configs.analyzeConfig_3l import analyzeConfig_3l
from tthAnalysis.HiggsToTauTau.jobTools import query_yes_no
from tthAnalysis.HiggsToTauTau.analysisSettings import systematics, get_lumi
from tthAnalysis.HiggsToTauTau.runConfig import tthAnalyzeParser, filter_samples
from tthAnalysis.HiggsToTauTau.common import logging, load_samples

import os
import sys
import getpass

# E.g.: ./test/tthAnalyzeRun_3l.py -v 2017Dec13 -m default -e 2017

mode_choices     = [
  'default', 'addMEM', 'forBDTtraining_beforeAddMEM', 'forBDTtraining_afterAddMEM', 'sync', 'sync_wMEM'
]
sys_choices      = [ 'full' ] + systematics.an_extended_opts
systematics.full = systematics.an_extended

parser = tthAnalyzeParser()
parser.add_modes(mode_choices)
parser.add_sys(sys_choices)
parser.add_rle_select()
parser.add_nonnominal()
parser.add_hlt_filter()
parser.add_files_per_job()
parser.add_use_home()
parser.add_jet_cleaning()
parser.add_gen_matching()
args = parser.parse_args()

# Common arguments
era                = args.era
version            = args.version
dry_run            = args.dry_run
no_exec            = args.no_exec
auto_exec          = args.auto_exec
check_output_files = not args.not_check_input_files
debug              = args.debug
sample_filter      = args.filter
num_parallel_jobs  = args.num_parallel_jobs
running_method     = args.running_method

# Additional arguments
mode              = args.mode
systematics_label = args.systematics
rle_select        = os.path.expanduser(args.rle_select)
use_nonnominal    = args.original_central
hlt_filter        = args.hlt_filter
files_per_job     = args.files_per_job
use_home          = args.use_home
jet_cleaning      = args.jet_cleaning
gen_matching      = args.gen_matching

# Use the arguments
central_or_shifts = []
for systematic_label in systematics_label:
  for central_or_shift in getattr(systematics, systematic_label):
    if central_or_shift not in central_or_shifts:
      central_or_shifts.append(central_or_shift)
do_sync = mode.startswith('sync')
lumi = get_lumi(era)
jet_cleaning_by_index = (jet_cleaning == 'by_index')
gen_matching_by_index = (gen_matching == 'by_index')

chargeSumSelections = [ "OS", "SS" ]

if mode == "default":
  samples = load_samples(era)
elif mode == "addMEM":
  samples = load_samples(era, suffix = "addMEM_3l")
  MEMbranch = 'memObjects_3l_lepFakeable'
elif mode == "forBDTtraining_beforeAddMEM":
  samples = load_samples(era, suffix = "BDT")
  chargeSumSelections = [ "OS" ]
elif mode == "forBDTtraining_afterAddMEM":
  samples = load_samples(era, suffix = "BDT_addMEM_3l")
  MEMbranch = 'memObjects_3l_lepFakeable'
elif mode == "sync_wMEM":
  samples = load_samples(era, suffix = "addMEM_sync")
elif mode == "sync":
  samples = load_samples(era, suffix = "sync" if use_nonnominal else "sync_nom")
else:
  raise ValueError("Invalid mode: %s" % mode)

for sample_name, sample_info in samples.items():
  if sample_name == 'sum_events': continue
  if sample_name.startswith('/Tau/Run'):
    sample_info["use_it"] = False

if __name__ == '__main__':
  logging.info(
    "Running the jobs with the following systematic uncertainties enabled: %s" % \
    ', '.join(central_or_shifts)
  )

  if sample_filter:
    samples = filter_samples(samples, sample_filter)

  analysis = analyzeConfig_3l(
    configDir = os.path.join("/home",       getpass.getuser(), "ttHAnalysis", era, version),
    outputDir = os.path.join("/hdfs/local", getpass.getuser(), "ttHAnalysis", era, version),
    executable_analyze                    = "analyze_3l",
    cfgFile_analyze                       = "analyze_3l_cfg.py",
    samples                               = samples,
    MEMbranch                             = None, # CV: MEM not implemented for 3l channel yet
    hadTauVeto_selection                  = "dR03mvaLoose", # veto events containing taus that pass tau ID WP applied in 3l+1tau channel,
    applyFakeRateWeights                  = "3lepton",
    chargeSumSelections                   = chargeSumSelections,
    jet_cleaning_by_index                 = jet_cleaning_by_index,
    gen_matching_by_index                 = gen_matching_by_index,
    central_or_shifts                     = central_or_shifts,
    max_files_per_job                     = files_per_job,
    era                                   = era,
    use_lumi                              = True,
    lumi                                  = lumi,
    check_output_files                    = check_output_files,
    running_method                        = running_method,
    num_parallel_jobs                     = num_parallel_jobs,
    executable_addBackgrounds             = "addBackgrounds",
    executable_addBackgroundJetToTauFakes = "addBackgroundLeptonFakes",
    histograms_to_fit                     = {
      "EventCounter" : {},
      "numJets"      : {},
      "mvaDiscr_3l"  : {},
    },
    select_rle_output                     = True,
    select_root_output                    = False,
    dry_run                               = dry_run,
    do_sync                               = do_sync,
    isDebug                               = debug,
    rle_select                            = rle_select,
    use_nonnominal                        = use_nonnominal,
    hlt_filter                            = hlt_filter,
    use_home                              = use_home,
  )

  if "forBDTtraining" in mode :
    analysis.set_BDT_training()

  job_statistics = analysis.create()
  for job_type, num_jobs in job_statistics.items():
    logging.info(" #jobs of type '%s' = %i" % (job_type, num_jobs))

  if auto_exec:
    run_analysis = True
  elif no_exec:
    run_analysis = False
  else:
    run_analysis = query_yes_no("Start jobs ?")
  if run_analysis:
    analysis.run()
  else:
    sys.exit(0)
