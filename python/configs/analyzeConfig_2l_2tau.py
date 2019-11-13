from tthAnalysis.HiggsToTauTau.configs.analyzeConfig import *
from tthAnalysis.HiggsToTauTau.jobTools import create_if_not_exists
from tthAnalysis.HiggsToTauTau.analysisTools import initDict, getKey, create_cfg, generateInputFileList
from tthAnalysis.HiggsToTauTau.common import logging

import re

def get_lepton_and_hadTau_selection_and_frWeight(lepton_and_hadTau_selection, lepton_and_hadTau_frWeight):
  lepton_and_hadTau_selection_and_frWeight = lepton_and_hadTau_selection
  if lepton_and_hadTau_selection.startswith("Fakeable"):
    if lepton_and_hadTau_frWeight == "enabled":
      lepton_and_hadTau_selection_and_frWeight += "_wFakeRateWeights"
    elif lepton_and_hadTau_frWeight == "disabled":
      lepton_and_hadTau_selection_and_frWeight += "_woFakeRateWeights"
  lepton_and_hadTau_selection_and_frWeight = lepton_and_hadTau_selection_and_frWeight.replace("|", "_")
  return lepton_and_hadTau_selection_and_frWeight

def getHistogramDir(lepton_selection, hadTau_selection, lepton_and_hadTau_frWeight, lepton_charge_selection, hadTau_charge_selection, chargeSumSelection):
  histogramDir = "2l_2tau"
  if lepton_charge_selection != "disabled":
    histogramDir += "_lep%s" % lepton_charge_selection
  if hadTau_charge_selection != "disabled":
    histogramDir += "_hadTau%s" % hadTau_charge_selection
  histogramDir += "_sum%s_%s" % (chargeSumSelection, lepton_selection)
  if lepton_selection.find("Fakeable") != -1 or hadTau_selection.find("Fakeable") != -1:
    if lepton_and_hadTau_frWeight == "enabled":
      histogramDir += "_wFakeRateWeights"
    elif lepton_and_hadTau_frWeight == "disabled":
      histogramDir += "_woFakeRateWeights"
  return histogramDir

class analyzeConfig_2l_2tau(analyzeConfig):
  """Configuration metadata needed to run analysis in a single go.

  Sets up a folder structure by defining full path names; no directory creation is delegated here.

  Args specific to analyzeConfig_2l_2tau:
    hadTau_selection: either `Tight`, `Loose` or `Fakeable`
    hadTau_charge_selection: either `OS` or `SS` (opposite-sign or same-sign)

  See $CMSSW_BASE/src/tthAnalysis/HiggsToTauTau/python/analyzeConfig.py
  for documentation of further Args.

  """
  def __init__(self,
        configDir,
        outputDir,
        executable_analyze,
        cfgFile_analyze,
        samples,
        lepton_charge_selections,
        hadTau_selection,
        hadTau_charge_selections,
        applyFakeRateWeights,
        chargeSumSelections,
        jet_cleaning_by_index,
        gen_matching_by_index,
        central_or_shifts,
        max_files_per_job,
        era,
        use_lumi,
        lumi,
        check_output_files,
        running_method,
        num_parallel_jobs,
        executable_addBackgrounds,
        executable_addBackgroundJetToTauFakes,
        histograms_to_fit,
        select_rle_output         = False,
        executable_prep_dcard     = "prepareDatacards",
        executable_add_syst_dcard = "addSystDatacards",
        verbose                   = False,
        dry_run                   = False,
        do_sync                   = False,
        isDebug                   = False,
        rle_select                = '',
        use_nonnominal            = False,
        hlt_filter                = False,
        use_home                  = False,
      ):
    analyzeConfig.__init__(self,
      configDir                 = configDir,
      outputDir                 = outputDir,
      executable_analyze        = executable_analyze,
      channel                   = "2l_2tau",
      samples                   = samples,
      jet_cleaning_by_index     = jet_cleaning_by_index,
      gen_matching_by_index     = gen_matching_by_index,
      central_or_shifts         = central_or_shifts,
      max_files_per_job         = max_files_per_job,
      era                       = era,
      use_lumi                  = use_lumi,
      lumi                      = lumi,
      check_output_files        = check_output_files,
      running_method            = running_method,
      num_parallel_jobs         = num_parallel_jobs,
      histograms_to_fit         = histograms_to_fit,
      triggers                  = [ '1e', '1mu', '2e', '2mu', '1e1mu' ],
      executable_prep_dcard     = executable_prep_dcard,
      executable_add_syst_dcard = executable_add_syst_dcard,
      verbose                   = verbose,
      dry_run                   = dry_run,
      do_sync                   = do_sync,
      isDebug                   = isDebug,
      use_home                  = use_home,
    )

    self.lepton_and_hadTau_selections = [ "Tight", "Fakeable" ]
    self.lepton_and_hadTau_frWeights = [ "enabled", "disabled" ]
    self.hadTau_selection_part2 = hadTau_selection
    self.applyFakeRateWeights = applyFakeRateWeights
    self.lepton_charge_selections = lepton_charge_selections
    self.hadTau_charge_selections = hadTau_charge_selections
    run_mcClosure = 'central' not in self.central_or_shifts or len(central_or_shifts) > 1 or self.do_sync

    self.apply_leptonGenMatching = None
    self.apply_hadTauGenMatching = None
    if self.applyFakeRateWeights == "4L":
      self.apply_leptonGenMatching = True
      self.apply_hadTauGenMatching = True
      if run_mcClosure:
        self.lepton_and_hadTau_selections.extend([ "Fakeable_mcClosure_e", "Fakeable_mcClosure_m", "Fakeable_mcClosure_t" ])
      self.central_or_shifts_fr = systematics.FR_all
    elif applyFakeRateWeights == "2lepton":
      self.apply_leptonGenMatching = True
      self.apply_hadTauGenMatching = False
      if run_mcClosure:
        self.lepton_and_hadTau_selections.extend([ "Fakeable_mcClosure_e", "Fakeable_mcClosure_m" ])
      # in this regime data-to-MC SFs of jet-to-tau FR are applied and therefore the relevant systematics have to be preserved
      self.central_or_shifts_fr = systematics.FR_all
    elif applyFakeRateWeights == "2tau":
      self.apply_leptonGenMatching = False
      self.apply_hadTauGenMatching = True
      if run_mcClosure:
        self.lepton_and_hadTau_selections.extend([ "Fakeable_mcClosure_t" ])
      self.central_or_shifts_fr = systematics.FR_t
    else:
      raise ValueError("Invalid Configuration parameter 'applyFakeRateWeights' = %s !!" % applyFakeRateWeights)
    self.pruneSystematics()
    self.internalizeSystematics()

    self.chargeSumSelections = chargeSumSelections

    self.executable_addBackgrounds = executable_addBackgrounds
    self.executable_addFakes = executable_addBackgroundJetToTauFakes

    self.nonfake_backgrounds = [ "TT", "TTW", "TTZ", "TTWW", "EWK", "WZ", "ZZ", "Rares", "tHq", "tHW", "VH", "WH", "ZH", "HH", "ggH", "qqH", "TTWH", "TTZH" ]

    self.cfgFile_analyze = os.path.join(self.template_dir, cfgFile_analyze)
    samples_categories_MC = self.get_samples_categories_MC(self.nonfake_backgrounds)
    self.prep_dcard_processesToCopy = ["data_obs"] + samples_categories_MC + [ "data_fakes", "fakes_mc", "data_obs" ]
    self.histogramDir_prep_dcard = "2l_2tau_sumOS_Tight"
    self.histogramDir_prep_dcard_SS = "2l_2tau_sumSS_Tight"
    self.make_plots_backgrounds = [  "tHq", "tHW" ] + [ "TTW", "TTZ", "TTWW", "EWK", "Rares", "Convs", "data_fakes" ]
    self.cfgFile_make_plots = os.path.join(self.template_dir, "makePlots_2l_2tau_cfg.py")
    self.cfgFile_make_plots_mcClosure = os.path.join(self.template_dir, "makePlots_mcClosure_2l_2tau_cfg.py") #TODO

    self.select_rle_output = select_rle_output
    self.rle_select = rle_select
    self.use_nonnominal = use_nonnominal
    self.hlt_filter = hlt_filter

    self.isBDTtraining = False

  def set_BDT_training(self, hadTau_selection_relaxed):
    """Run analysis with loose selection criteria for leptons and hadronic taus,
       for the purpose of preparing event list files for BDT training.
    """
    self.lepton_and_hadTau_selections = [ "forBDTtraining" ]
    self.lepton_and_hadTau_frWeights  = [ "disabled" ]
    super(analyzeConfig_2l_2tau, self).set_BDT_training(hadTau_selection_relaxed)

  def accept_systematics(self, central_or_shift, is_mc, lepton_and_hadTau_selection, hadTau_charge_selection, sample_category, sample_name):
    if central_or_shift != "central":
      isFR_shape_shift = (central_or_shift in self.central_or_shifts_fr)
      if not ((lepton_and_hadTau_selection == "Fakeable" and hadTau_charge_selection == "OS" and isFR_shape_shift) or
              (lepton_and_hadTau_selection == "Tight" and hadTau_charge_selection == "OS")):
        return False
      if isFR_shape_shift and lepton_and_hadTau_selection == "Tight" and \
          not (self.applyFakeRateWeights == "2lepton" and central_or_shift in systematics.FR_t and is_mc):
        # If the FRs are applied only to the leptons, the tau FR is compensated with data-to-MC SF, even in the SR
        return False
      if not is_mc and not isFR_shape_shift:
        return False
      if not self.accept_central_or_shift(central_or_shift, sample_category, sample_name):
        return False
    return True

  def createCfg_analyze(self, jobOptions, sample_info, lepton_and_hadTau_selection):
    """Create python configuration file for the analyze_2l_2tau executable (analysis code)

    Args:
      inputFiles: list of input files (Ntuples)
      outputFile: output file of the job -- a ROOT file containing histogram
      process: either `TT`, `TTW`, `TTZ`, `EWK`, `Rares`, `data_obs`, `ttH_hww`, 'ttH_hzg', 'ttH_hmm', `ttH_hzz` or `ttH_htt`
      is_mc: flag indicating whether job runs on MC (True) or data (False)
      lumi_scale: event weight (= xsection * luminosity / number of events)
      central_or_shift: either 'central' or one of the systematic uncertainties defined in $CMSSW_BASE/src/tthAnalysis/HiggsToTauTau/bin/analyze_2l_2tau.cc
    """
    lepton_and_hadTau_frWeight = "disabled" if jobOptions['applyFakeRateWeights'] == "disabled" else "enabled"

    jobOptions['histogramDir'] = getHistogramDir(
      lepton_and_hadTau_selection, jobOptions['hadTauSelection'], lepton_and_hadTau_frWeight,
      jobOptions['leptonChargeSelection'], jobOptions['hadTauChargeSelection'], jobOptions['chargeSumSelection']
    )
    if 'mcClosure' in lepton_and_hadTau_selection:
      self.mcClosure_dir['%s_%s_%s' % (lepton_and_hadTau_selection, jobOptions['chargeSumSelection'], jobOptions['hadTauChargeSelection'])] = jobOptions['histogramDir']

    self.set_leptonFakeRateWeightHistogramNames(jobOptions['central_or_shift'], lepton_and_hadTau_selection)
    jobOptions['leptonFakeRateWeight.inputFileName'] = self.leptonFakeRateWeight_inputFile
    jobOptions['leptonFakeRateWeight.histogramName_e'] = self.leptonFakeRateWeight_histogramName_e
    jobOptions['leptonFakeRateWeight.histogramName_mu'] = self.leptonFakeRateWeight_histogramName_mu

    jobOptions['hadTauFakeRateWeight.inputFileName'] = self.hadTauFakeRateWeight_inputFile
    graphName = 'jetToTauFakeRate/%s/$etaBin/jetToTauFakeRate_mc_hadTaus_pt' % self.hadTau_selection_part2
    jobOptions['hadTauFakeRateWeight.lead.graphName'] = graphName
    jobOptions['hadTauFakeRateWeight.sublead.graphName'] = graphName
    fitFunctionName = 'jetToTauFakeRate/%s/$etaBin/fitFunction_data_div_mc_hadTaus_pt' % self.hadTau_selection_part2
    jobOptions['hadTauFakeRateWeight.lead.fitFunctionName'] = fitFunctionName
    jobOptions['hadTauFakeRateWeight.sublead.fitFunctionName'] = fitFunctionName
    if "mcClosure" in lepton_and_hadTau_selection:
      jobOptions['hadTauFakeRateWeight.applyGraph_lead'] = True
      jobOptions['hadTauFakeRateWeight.applyGraph_sublead'] = True
      jobOptions['hadTauFakeRateWeight.applyFitFunction_lead'] = False
      jobOptions['hadTauFakeRateWeight.applyFitFunction_sublead'] = False
      if self.applyFakeRateWeights not in [ "4L", "2tau" ] and not self.isBDTtraining:
        # We want to preserve the same logic as running in SR and applying the FF method only to leptons [*]
        jobOptions['hadTauFakeRateWeight.applyFitFunction_lead'] = True
        jobOptions['hadTauFakeRateWeight.applyFitFunction_sublead'] = True
    if jobOptions['hadTauSelection'].find("Tight") != -1 and self.applyFakeRateWeights not in [ "4L", "2tau" ] and not self.isBDTtraining:
      # [*] SR and applying the FF method only to leptons
      jobOptions['hadTauFakeRateWeight.applyGraph_lead'] = False # FR in MC for the leading tau
      jobOptions['hadTauFakeRateWeight.applyGraph_sublead'] = False
      jobOptions['hadTauFakeRateWeight.applyFitFunction_lead'] = True # data-to-MC SF for the leading tau
      jobOptions['hadTauFakeRateWeight.applyFitFunction_sublead'] = True
      jobOptions['apply_hadTauFakeRateSF'] = True

    lines = super(analyzeConfig_2l_2tau, self).createCfg_analyze(jobOptions, sample_info)
    create_cfg(self.cfgFile_analyze, jobOptions['cfgFile_modified'], lines)

  def create(self):
    """Creates all necessary config files and runs the complete analysis workfow -- either locally or on the batch system
    """

    for sample_name, sample_info in self.samples.items():
      if not sample_info["use_it"]:
        continue

      process_name = sample_info["process_name_specific"]
      sample_category = sample_info["sample_category"]
      is_mc = (sample_info["type"] == "mc")

      logging.info("Building dictionaries for sample %s..." % process_name)
      for lepton_charge_selection in self.lepton_charge_selections:
        for hadTau_charge_selection in self.hadTau_charge_selections:
          for lepton_and_hadTau_selection in self.lepton_and_hadTau_selections:
            for lepton_and_hadTau_frWeight in self.lepton_and_hadTau_frWeights:
              if lepton_and_hadTau_frWeight == "enabled" and not lepton_and_hadTau_selection.startswith("Fakeable"):
                continue
              if lepton_and_hadTau_frWeight == "disabled" and not lepton_and_hadTau_selection in [ "Tight", "forBDTtraining", "forBDTtraining_VHbb" ]:
                continue

              lepton_and_hadTau_selection_and_frWeight = get_lepton_and_hadTau_selection_and_frWeight(lepton_and_hadTau_selection, lepton_and_hadTau_frWeight)
              for chargeSumSelection in self.chargeSumSelections:
                lepton_and_hadTau_charge_selection = ""
                if lepton_charge_selection != "disabled":
                  lepton_and_hadTau_charge_selection += "_lep%s" % lepton_charge_selection
                if hadTau_charge_selection != "disabled":
                  lepton_and_hadTau_charge_selection += "_hadTau%s" % hadTau_charge_selection
                lepton_and_hadTau_charge_selection += "_sum%s" % chargeSumSelection
                central_or_shift_extensions = ["", "hadd", "addBackgrounds"]
                central_or_shift_dedicated = self.central_or_shifts if self.runTHweights(sample_info) else self.central_or_shifts_external
                central_or_shifts_extended = central_or_shift_extensions + central_or_shift_dedicated
                for central_or_shift_or_dummy in central_or_shifts_extended:
                  process_name_extended = [ process_name, "hadd" ]
                  for process_name_or_dummy in process_name_extended:
                    if central_or_shift_or_dummy in [ "hadd", "addBackgrounds" ] and process_name_or_dummy in [ "hadd" ]:
                      continue

                    if central_or_shift_or_dummy not in central_or_shift_extensions and not self.accept_systematics(
                        central_or_shift_or_dummy, is_mc, lepton_and_hadTau_selection, chargeSumSelection,
                        sample_category, sample_name
                    ):
                      continue

                    key_dir = getKey(process_name_or_dummy, lepton_charge_selection, hadTau_charge_selection,
                      lepton_and_hadTau_selection_and_frWeight, chargeSumSelection, central_or_shift_or_dummy)
                    for dir_type in [ DKEY_CFGS, DKEY_HIST, DKEY_LOGS, DKEY_ROOT, DKEY_RLES, DKEY_SYNC ]:
                      initDict(self.dirs, [ key_dir, dir_type ])
                      if dir_type in [ DKEY_CFGS, DKEY_LOGS ]:
                        self.dirs[key_dir][dir_type] = os.path.join(self.configDir, dir_type, self.channel,
                          "_".join([ lepton_and_hadTau_selection_and_frWeight + lepton_and_hadTau_charge_selection ]), process_name_or_dummy, central_or_shift_or_dummy)
                      else:
                        self.dirs[key_dir][dir_type] = os.path.join(self.outputDir, dir_type, self.channel,
                          "_".join([ lepton_and_hadTau_selection_and_frWeight + lepton_and_hadTau_charge_selection ]), process_name_or_dummy, central_or_shift_or_dummy)
    for subdirectory in [ "addBackgrounds", "addBackgroundLeptonFakes", "prepareDatacards", "addSystFakeRates", "makePlots" ]:
      key_dir = getKey(subdirectory)
      for dir_type in [ DKEY_CFGS, DKEY_HIST, DKEY_LOGS, DKEY_ROOT, DKEY_DCRD, DKEY_PLOT ]:
        initDict(self.dirs, [ key_dir, dir_type ])
        if dir_type in [ DKEY_CFGS, DKEY_LOGS, DKEY_DCRD, DKEY_PLOT ]:
          self.dirs[key_dir][dir_type] = os.path.join(self.configDir, dir_type, self.channel, subdirectory)
        else:
          self.dirs[key_dir][dir_type] = os.path.join(self.outputDir, dir_type, self.channel, subdirectory)
    for dir_type in [ DKEY_CFGS, DKEY_SCRIPTS, DKEY_HIST, DKEY_LOGS, DKEY_DCRD, DKEY_PLOT, DKEY_HADD_RT, DKEY_SYNC ]:
      initDict(self.dirs, [ dir_type ])
      if dir_type in [ DKEY_CFGS, DKEY_SCRIPTS, DKEY_LOGS, DKEY_DCRD, DKEY_PLOT, DKEY_HADD_RT ]:
        self.dirs[dir_type] = os.path.join(self.configDir, dir_type, self.channel)
      else:
        self.dirs[dir_type] = os.path.join(self.outputDir, dir_type, self.channel)

    numDirectories = 0
    for key in self.dirs.keys():
      if type(self.dirs[key]) == dict:
        numDirectories += len(self.dirs[key])
      else:
        numDirectories += 1
    logging.info("Creating directory structure (numDirectories = %i)" % numDirectories)
    numDirectories_created = 0;
    frac = 1
    for key in self.dirs.keys():
      if type(self.dirs[key]) == dict:
        for dir_type in self.dirs[key].keys():
          create_if_not_exists(self.dirs[key][dir_type])
        numDirectories_created += len(self.dirs[key])
      else:
        create_if_not_exists(self.dirs[key])
        numDirectories_created = numDirectories_created + 1
      while 100*numDirectories_created >= frac*numDirectories:
        logging.info(" %i%% completed" % frac)
        frac = frac + 1
    logging.info("Done.")

    inputFileLists = {}
    for sample_name, sample_info in self.samples.items():
      if not sample_info["use_it"]:
        continue
      logging.info("Checking input files for sample %s" % sample_info["process_name_specific"])
      inputFileLists[sample_name] = generateInputFileList(sample_info, self.max_files_per_job)

    mcClosure_regex = re.compile('Fakeable_mcClosure_(?P<type>m|e|t)_wFakeRateWeights')
    for lepton_charge_selection in self.lepton_charge_selections:
      for hadTau_charge_selection in self.hadTau_charge_selections:
        for lepton_and_hadTau_selection in self.lepton_and_hadTau_selections:
          lepton_selection = lepton_and_hadTau_selection
          hadTau_selection = lepton_and_hadTau_selection
          electron_selection = lepton_selection
          muon_selection = lepton_selection

          if self.applyFakeRateWeights == "2tau":
            lepton_selection = "Tight"
            electron_selection = "Tight"
            muon_selection = "Tight"
          elif self.applyFakeRateWeights == "2lepton":
            hadTau_selection = "Tight"
          hadTau_selection = "|".join([ hadTau_selection, self.hadTau_selection_part2 ])

          if "forBDTtraining" in lepton_and_hadTau_selection :
            electron_selection = "Loose"
            muon_selection = "Loose"
            hadTau_selection = "Tight|%s" % self.hadTau_selection_relaxed
          elif lepton_and_hadTau_selection == "Fakeable_mcClosure_e":
            electron_selection = "Fakeable"
            muon_selection = "Tight"
            hadTau_selection = "Tight"
            hadTau_selection = "|".join([hadTau_selection, self.hadTau_selection_part2])
          elif lepton_and_hadTau_selection == "Fakeable_mcClosure_m":
            electron_selection = "Tight"
            muon_selection = "Fakeable"
            hadTau_selection = "Tight"
            hadTau_selection = "|".join([hadTau_selection, self.hadTau_selection_part2])
          elif lepton_and_hadTau_selection == "Fakeable_mcClosure_t":
            electron_selection = "Tight"
            muon_selection = "Tight"
            hadTau_selection = "Fakeable"
            hadTau_selection = "|".join([hadTau_selection, self.hadTau_selection_part2])

          for lepton_and_hadTau_frWeight in self.lepton_and_hadTau_frWeights:
            if lepton_and_hadTau_frWeight == "enabled" and not lepton_and_hadTau_selection.startswith("Fakeable"):
              continue
            if lepton_and_hadTau_frWeight == "disabled" and not lepton_and_hadTau_selection in [ "Tight", "forBDTtraining", "forBDTtraining_VHbb" ]:
              continue
            lepton_and_hadTau_selection_and_frWeight = get_lepton_and_hadTau_selection_and_frWeight(lepton_and_hadTau_selection, lepton_and_hadTau_frWeight)

            for chargeSumSelection in self.chargeSumSelections:

              for sample_name, sample_info in self.samples.items():
                if not sample_info["use_it"]:
                  continue
                process_name = sample_info["process_name_specific"]
                logging.info("Creating configuration files to run '%s' for sample %s" % (self.executable_analyze, process_name))
                inputFileList = inputFileLists[sample_name]

                sample_category = sample_info["sample_category"]
                is_mc = (sample_info["type"] == "mc")
                use_th_weights = self.runTHweights(sample_info)

                central_or_shift_dedicated = self.central_or_shifts if use_th_weights else self.central_or_shifts_external
                for central_or_shift in central_or_shift_dedicated:
                  if not self.accept_systematics(
                      central_or_shift, is_mc, lepton_and_hadTau_selection, chargeSumSelection, sample_category,
                      sample_name
                  ):
                    continue

                  central_or_shifts_local = []
                  if central_or_shift == "central" and not use_th_weights:
                    for central_or_shift_local in self.central_or_shifts_internal:
                      if self.accept_systematics(
                          central_or_shift_local, is_mc, lepton_and_hadTau_selection, hadTau_charge_selection,
                          sample_category, sample_name
                      ):
                        central_or_shifts_local.append(central_or_shift_local)

                  logging.info(" ... for '%s' and systematic uncertainty option '%s'" % (lepton_and_hadTau_selection_and_frWeight, central_or_shift))

                  # build config files for executing analysis code
                  key_analyze_dir = getKey(process_name, lepton_charge_selection, hadTau_charge_selection,
                    lepton_and_hadTau_selection_and_frWeight, chargeSumSelection, central_or_shift)

                  for jobId in inputFileList.keys():

                    analyze_job_tuple = (process_name, lepton_charge_selection, hadTau_charge_selection,
                      lepton_and_hadTau_selection_and_frWeight, chargeSumSelection, central_or_shift, jobId)
                    key_analyze_job = getKey(*analyze_job_tuple)
                    ntupleFiles = inputFileList[jobId]
                    if len(ntupleFiles) == 0:
                      logging.warning("No input ntuples for %s --> skipping job !!" % (key_analyze_job))
                      continue

                    syncOutput = ''
                    syncTree = ''
                    mcClosure_match = mcClosure_regex.match(lepton_and_hadTau_selection_and_frWeight)
                    if self.do_sync:
                      if chargeSumSelection != 'OS':
                        continue
                      if lepton_and_hadTau_selection_and_frWeight == 'Tight':
                        syncOutput = os.path.join(self.dirs[key_analyze_dir][DKEY_SYNC], '%s_%s_SR.root' % (self.channel, central_or_shift))
                        syncTree = 'syncTree_%s_SR' % self.channel.replace('_', '')
                      elif lepton_and_hadTau_selection_and_frWeight == 'Fakeable_wFakeRateWeights':
                        syncOutput = os.path.join(self.dirs[key_analyze_dir][DKEY_SYNC], '%s_%s_Fake.root' % (self.channel, central_or_shift))
                        syncTree = 'syncTree_%s_Fake' % self.channel.replace('_', '')
                      elif mcClosure_match:
                        mcClosure_type = mcClosure_match.group('type')
                        syncOutput = os.path.join(self.dirs[key_analyze_dir][DKEY_SYNC], '%s_%s_mcClosure_%s.root' % (self.channel, central_or_shift, mcClosure_type))
                        syncTree = 'syncTree_%s_mcClosure_%s' % (self.channel.replace('_', ''), mcClosure_type)
                      else:
                        continue
                    if syncTree and central_or_shift != "central":
                      syncTree = os.path.join(central_or_shift, syncTree)
                    syncRLE = ''
                    if self.do_sync and self.rle_select:
                      syncRLE = self.rle_select % syncTree
                      if not os.path.isfile(syncRLE):
                        logging.warning("Input RLE file for the sync is missing: %s; skipping the job" % syncRLE)
                        continue
                    if syncOutput:
                      self.inputFiles_sync['sync'].append(syncOutput)

                    cfgFile_modified_path = os.path.join(self.dirs[key_analyze_dir][DKEY_CFGS], "analyze_%s_lep%s_tau%s_%s_sum%s_%s_%i_cfg.py" % analyze_job_tuple)
                    logFile_path = os.path.join(self.dirs[key_analyze_dir][DKEY_LOGS], "analyze_%s_lep%s_tau%s_%s_sum%s_%s_%i.log" % analyze_job_tuple)
                    rleOutputFile_path = os.path.join(self.dirs[key_analyze_dir][DKEY_RLES], "rle_%s_lep%s_tau%s_%s_sum%s_%s_%i.txt" % analyze_job_tuple) \
                                         if self.select_rle_output else ""
                    histogramFile_path = os.path.join(self.dirs[key_analyze_dir][DKEY_HIST], "analyze_%s_lep%s_tau%s_%s_sum%s_%s_%i.root" % analyze_job_tuple)
                    applyFakeRateWeights = self.applyFakeRateWeights \
                      if self.isBDTtraining or not (lepton_selection == "Tight" and hadTau_selection.find("Tight") != -1) \
                      else "disabled"

                    self.jobOptions_analyze[key_analyze_job] = {
                      'ntupleFiles'              : ntupleFiles,
                      'cfgFile_modified'         : cfgFile_modified_path,
                      'histogramFile'            : histogramFile_path,
                      'logFile'                  : logFile_path,
                      'selEventsFileName_output' : rleOutputFile_path,
                      'leptonChargeSelection'    : lepton_charge_selection,
                      'electronSelection'        : electron_selection,
                      'muonSelection'            : muon_selection,
                      'apply_leptonGenMatching'  : self.apply_leptonGenMatching,
                      'hadTauChargeSelection'    : hadTau_charge_selection,
                      'hadTauSelection'          : hadTau_selection,
                      'apply_hadTauGenMatching'  : self.apply_hadTauGenMatching,
                      'chargeSumSelection'       : chargeSumSelection,
                      'applyFakeRateWeights'     : applyFakeRateWeights,
                      'central_or_shift'         : central_or_shift,
                      'central_or_shifts_local'  : central_or_shifts_local,
                      'selectBDT'                : self.isBDTtraining,
                      'syncOutput'               : syncOutput,
                      'syncTree'                 : syncTree,
                      'syncRLE'                  : syncRLE,
                      'apply_hlt_filter'         : self.hlt_filter,
                      'useNonNominal'            : self.use_nonnominal,
                      'fillGenEvtHistograms'     : True,
                      'useObjectMultiplicity'    : True,
                    }
                    self.createCfg_analyze(self.jobOptions_analyze[key_analyze_job], sample_info, lepton_and_hadTau_selection)

                    # initialize input and output file names for hadd_stage1
                    key_hadd_stage1_dir = getKey(process_name, lepton_charge_selection, hadTau_charge_selection, lepton_and_hadTau_selection_and_frWeight, chargeSumSelection)
                    hadd_stage1_job_tuple = (process_name, lepton_charge_selection, hadTau_charge_selection, lepton_and_hadTau_selection_and_frWeight, chargeSumSelection)
                    key_hadd_stage1_job = getKey(*hadd_stage1_job_tuple)
                    if not key_hadd_stage1_job in self.inputFiles_hadd_stage1:
                      self.inputFiles_hadd_stage1[key_hadd_stage1_job] = []
                    self.inputFiles_hadd_stage1[key_hadd_stage1_job].append(self.jobOptions_analyze[key_analyze_job]['histogramFile'])
                    self.outputFile_hadd_stage1[key_hadd_stage1_job] = os.path.join(self.dirs[key_hadd_stage1_dir][DKEY_HIST],
                                                                                    "hadd_stage1_%s_lep%s_tau%s_%s_sum%s.root" % hadd_stage1_job_tuple)

                if self.isBDTtraining or self.do_sync:
                  continue

                # add output files of hadd_stage1 for data to list of input files for hadd_stage1_5
                key_hadd_stage1_job = getKey(process_name, lepton_charge_selection, hadTau_charge_selection, lepton_and_hadTau_selection_and_frWeight, chargeSumSelection)
                key_hadd_stage1_5_dir = getKey("hadd", lepton_charge_selection, hadTau_charge_selection, lepton_and_hadTau_selection_and_frWeight, chargeSumSelection)
                hadd_stage1_5_job_tuple = (lepton_charge_selection, hadTau_charge_selection, lepton_and_hadTau_selection_and_frWeight, chargeSumSelection)
                key_hadd_stage1_5_job = getKey(*hadd_stage1_5_job_tuple)
                if not key_hadd_stage1_5_job in self.inputFiles_hadd_stage1_5:
                  self.inputFiles_hadd_stage1_5[key_hadd_stage1_5_job] = []
                self.inputFiles_hadd_stage1_5[key_hadd_stage1_5_job].append(self.outputFile_hadd_stage1[key_hadd_stage1_job])
                self.outputFile_hadd_stage1_5[key_hadd_stage1_5_job] = os.path.join(self.dirs[key_hadd_stage1_5_dir][DKEY_HIST],
                                                                            "hadd_stage1_5_lep%s_tau%s_%s_sum%s.root" % hadd_stage1_5_job_tuple)

              if self.isBDTtraining or self.do_sync:
                continue

              ## doing list of processes to make the hadd in _Convs and _fake
              ## we could remove the tH ones with althernative couplings
              sample_categories = []
              sample_categories.extend(self.nonfake_backgrounds)
              sample_categories.extend(self.ttHProcs)
              processes_input_base = self.get_processes_input_base(sample_categories)

              # sum fake background contributions for the total of all MC sample
              # input processes: TT_fake, TTW_fake, TTWW_fake, ...
              # output process: fakes_mc
              key_hadd_stage1_5_job = getKey(lepton_charge_selection, hadTau_charge_selection, lepton_and_hadTau_selection_and_frWeight, chargeSumSelection)
              key_addBackgrounds_dir = getKey("addBackgrounds")
              addBackgrounds_job_fakes_tuple = ("fakes_mc", lepton_charge_selection, hadTau_charge_selection, lepton_and_hadTau_selection_and_frWeight, chargeSumSelection)
              key_addBackgrounds_job_fakes = getKey(*addBackgrounds_job_fakes_tuple)
              sample_categories = []
              sample_categories.extend(self.nonfake_backgrounds)
              sample_categories.extend(self.ttHProcs)
              processes_input = []
              for process_input_base in processes_input_base:
                processes_input.append("%s_fake" % process_input_base)
              self.jobOptions_addBackgrounds_sum[key_addBackgrounds_job_fakes] = {
                'inputFile' : self.outputFile_hadd_stage1_5[key_hadd_stage1_5_job],
                'cfgFile_modified' : os.path.join(self.dirs[key_addBackgrounds_dir][DKEY_CFGS], "addBackgrounds_%s_lep%s_tau%s_%s_sum%s_cfg.py" % addBackgrounds_job_fakes_tuple),
                'outputFile' : os.path.join(self.dirs[key_addBackgrounds_dir][DKEY_HIST], "addBackgrounds_%s_lep%s_tau%s_%s_sum%s.root" % addBackgrounds_job_fakes_tuple),
                'logFile' : os.path.join(self.dirs[key_addBackgrounds_dir][DKEY_LOGS], "addBackgrounds_%s_lep%s_tau%s_%s_sum%s.log" % addBackgrounds_job_fakes_tuple),
                'categories' : [ getHistogramDir(lepton_selection, hadTau_selection, lepton_and_hadTau_frWeight,
                  lepton_charge_selection, hadTau_charge_selection, chargeSumSelection) ],
                'processes_input' : processes_input,
                'process_output' : "fakes_mc"
              }
              self.createCfg_addBackgrounds(self.jobOptions_addBackgrounds_sum[key_addBackgrounds_job_fakes])

              # sum conversion background contributions for the total of all MC sample
              # input processes: TT_Convs, TTW_Convs, TTWW_Convs, ...
              # output process: Convs
              addBackgrounds_job_Convs_tuple = ("Convs", lepton_charge_selection, hadTau_charge_selection, lepton_and_hadTau_selection_and_frWeight, chargeSumSelection)
              key_addBackgrounds_job_Convs = getKey(*addBackgrounds_job_Convs_tuple)
              sample_categories = []
              sample_categories.extend(self.nonfake_backgrounds)
              sample_categories.extend(self.ttHProcs)
              processes_input = []
              for process_input_base in processes_input_base:
                processes_input.append("%s_Convs" % process_input_base)
              self.jobOptions_addBackgrounds_sum[key_addBackgrounds_job_Convs] = {
                'inputFile' : self.outputFile_hadd_stage1_5[key_hadd_stage1_5_job],
                'cfgFile_modified' : os.path.join(self.dirs[DKEY_CFGS], "addBackgrounds_%s_lep%s_tau%s_%s_sum%s_cfg.py" % addBackgrounds_job_Convs_tuple),
                'outputFile' : os.path.join(self.dirs[DKEY_HIST], "addBackgrounds_%s_lep%s_tau%s_%s_sum%s.root" % addBackgrounds_job_Convs_tuple),
                'logFile' : os.path.join(self.dirs[DKEY_LOGS], "addBackgrounds_%s_lep%s_tau%s_%s_sum%s.log" % addBackgrounds_job_Convs_tuple),
                'categories' : [ getHistogramDir(lepton_selection, hadTau_selection, lepton_and_hadTau_frWeight,
                  lepton_charge_selection, hadTau_charge_selection, chargeSumSelection) ],
                'processes_input' : processes_input,
                'process_output' : "Convs"
              }
              self.createCfg_addBackgrounds(self.jobOptions_addBackgrounds_sum[key_addBackgrounds_job_Convs])

              # initialize input and output file names for hadd_stage2
              key_hadd_stage1_5_job = getKey(lepton_charge_selection, hadTau_charge_selection, lepton_and_hadTau_selection_and_frWeight, chargeSumSelection)
              key_hadd_stage2_dir = getKey("hadd", lepton_charge_selection, hadTau_charge_selection, lepton_and_hadTau_selection_and_frWeight, chargeSumSelection)
              hadd_stage2_job_tuple = (lepton_charge_selection, hadTau_charge_selection, lepton_and_hadTau_selection_and_frWeight, chargeSumSelection)
              key_hadd_stage2_job = getKey(*hadd_stage2_job_tuple)
              if not key_hadd_stage2_job in self.inputFiles_hadd_stage2:
                self.inputFiles_hadd_stage2[key_hadd_stage2_job] = []
              if lepton_and_hadTau_selection == "Tight":
                self.inputFiles_hadd_stage2[key_hadd_stage2_job].append(self.jobOptions_addBackgrounds_sum[key_addBackgrounds_job_fakes]['outputFile'])
                self.inputFiles_hadd_stage2[key_hadd_stage2_job].append(self.jobOptions_addBackgrounds_sum[key_addBackgrounds_job_Convs]['outputFile'])
              self.inputFiles_hadd_stage2[key_hadd_stage2_job].append(self.outputFile_hadd_stage1_5[key_hadd_stage1_5_job])
              self.outputFile_hadd_stage2[key_hadd_stage2_job] = os.path.join(self.dirs[key_hadd_stage2_dir][DKEY_HIST],
                                                                              "hadd_stage2_lep%s_tau%s_%s_sum%s.root" % hadd_stage2_job_tuple)

    if self.isBDTtraining or self.do_sync:
      if self.is_sbatch:
        logging.info("Creating script for submitting '%s' jobs to batch system" % self.executable_analyze)
        self.sbatchFile_analyze = os.path.join(self.dirs[DKEY_SCRIPTS], "sbatch_analyze_%s.py" % self.channel)
        if self.isBDTtraining:
          self.createScript_sbatch_analyze(self.executable_analyze, self.sbatchFile_analyze, self.jobOptions_analyze)
        elif self.do_sync:
          self.createScript_sbatch_syncNtuple(self.executable_analyze, self.sbatchFile_analyze, self.jobOptions_analyze)
      logging.info("Creating Makefile")
      lines_makefile = []
      if self.isBDTtraining:
        self.addToMakefile_analyze(lines_makefile)
        self.addToMakefile_hadd_stage1(lines_makefile)
      elif self.do_sync:
        self.addToMakefile_syncNtuple(lines_makefile)
        outputFile_sync_path = os.path.join(self.outputDir, DKEY_SYNC, '%s.root' % self.channel)
        self.outputFile_sync['sync'] = outputFile_sync_path
        self.addToMakefile_hadd_sync(lines_makefile)
      else:
        raise ValueError("Internal logic error")
      self.addToMakefile_validate(lines_makefile)
      self.targets.extend(self.phoniesToAdd)
      self.createMakefile(lines_makefile)
      logging.info("Done.")
      return self.num_jobs

    logging.info("Creating configuration files to run 'addBackgroundFakes'")
    for lepton_charge_selection in self.lepton_charge_selections:
      for hadTau_charge_selection in self.hadTau_charge_selections:
        for chargeSumSelection in self.chargeSumSelections:
          key_hadd_stage1_5_job = getKey(lepton_charge_selection, hadTau_charge_selection, get_lepton_and_hadTau_selection_and_frWeight("Fakeable", "enabled"), chargeSumSelection)
          key_addFakes_dir = getKey("addBackgroundLeptonFakes")
          addFakes_job_tuple = (lepton_charge_selection, hadTau_charge_selection, chargeSumSelection)
          key_addFakes_job = getKey("data_fakes", *addFakes_job_tuple)
          category_sideband = None
          if self.applyFakeRateWeights == "2lepton":
            category_sideband = getHistogramDir("Fakeable", "Tight", "enabled", lepton_charge_selection, hadTau_charge_selection, chargeSumSelection)
          elif self.applyFakeRateWeights == "4L":
            category_sideband = getHistogramDir("Fakeable", "Fakeable", "enabled", lepton_charge_selection, hadTau_charge_selection, chargeSumSelection)
          elif self.applyFakeRateWeights == "2tau":
            category_sideband = getHistogramDir("Tight", "Fakeable", "enabled", lepton_charge_selection, hadTau_charge_selection, chargeSumSelection)
          else:
            raise ValueError("Invalid Configuration parameter 'applyFakeRateWeights' = %s !!" % self.applyFakeRateWeights)
          self.jobOptions_addFakes[key_addFakes_job] = {
            'inputFile' : self.outputFile_hadd_stage1_5[key_hadd_stage1_5_job],
            'cfgFile_modified' : os.path.join(self.dirs[key_addFakes_dir][DKEY_CFGS], "addBackgroundLeptonFakes_lep%s_tau%s_sum%s_cfg.py" % addFakes_job_tuple),
            'outputFile' : os.path.join(self.dirs[key_addFakes_dir][DKEY_HIST], "addBackgroundLeptonFakes_lep%s_tau%s_sum%s.root" % addFakes_job_tuple),
            'logFile' : os.path.join(self.dirs[key_addFakes_dir][DKEY_LOGS], "addBackgroundLeptonFakes_lep%s_tau%s_sum%s.log" % addFakes_job_tuple),
            'category_signal' : getHistogramDir("Tight", "Tight", "disabled", lepton_charge_selection, hadTau_charge_selection, chargeSumSelection),
            'category_sideband' : category_sideband
          }
          self.createCfg_addFakes(self.jobOptions_addFakes[key_addFakes_job])
          key_hadd_stage2_job = getKey(lepton_charge_selection, hadTau_charge_selection, get_lepton_and_hadTau_selection_and_frWeight("Tight", "disabled"), chargeSumSelection)
          self.inputFiles_hadd_stage2[key_hadd_stage2_job].append(self.jobOptions_addFakes[key_addFakes_job]['outputFile'])

    logging.info("Creating configuration files to run 'prepareDatacards'")
    for lepton_charge_selection in self.lepton_charge_selections:
      for hadTau_charge_selection in self.hadTau_charge_selections:
        lepton_and_hadTau_charge_selection = ""
        if lepton_charge_selection != "disabled":
          lepton_and_hadTau_charge_selection += "_lep%s" % lepton_charge_selection
        if hadTau_charge_selection != "disabled":
          lepton_and_hadTau_charge_selection += "_hadTau%s" % hadTau_charge_selection

        if self.applyFakeRateWeights == "2lepton":
          processesToCopy = []
          for process in self.prep_dcard_processesToCopy:
            processesToCopy.append(process)
            if not (process.find("data") != -1 or process.find("fakes") != -1 or process.find("Convs") != -1):
              processesToCopy.append("%s_gentau" % process)
              processesToCopy.append("%s_faketau" % process)
          self.prep_dcard_processesToCopy = processesToCopy
          processesToCopy = []
          for process in self.prep_dcard_signals:
            processesToCopy.append(process)
            processesToCopy.append("%s_gentau" % process)
            processesToCopy.append("%s_faketau" % process)
          self.prep_dcard_signals = processesToCopy

        key_prep_dcard_dir = getKey("prepareDatacards")
        if "OS" in self.chargeSumSelections:
          for histogramToFit in self.histograms_to_fit:
            key_hadd_stage2_job = getKey(lepton_charge_selection, hadTau_charge_selection, get_lepton_and_hadTau_selection_and_frWeight("Tight", "disabled"), "OS")
            prep_dcard_job_tuple = (self.channel, lepton_charge_selection, hadTau_charge_selection, "OS", histogramToFit)
            key_prep_dcard_job = getKey(lepton_charge_selection, hadTau_charge_selection, "OS", histogramToFit)
            self.jobOptions_prep_dcard[key_prep_dcard_job] = {
              'inputFile' : self.outputFile_hadd_stage2[key_hadd_stage2_job],
              'cfgFile_modified' : os.path.join(self.dirs[key_prep_dcard_dir][DKEY_CFGS], "prepareDatacards_%s_lep%s_tau%s_sum%s_%s_cfg.py" % prep_dcard_job_tuple),
              'datacardFile' : os.path.join(self.dirs[key_prep_dcard_dir][DKEY_DCRD], "prepareDatacards_%s_lep%s_tau%s_sum%s_%s.root" % prep_dcard_job_tuple),
              'histogramDir' : getHistogramDir("Tight", "Tight", "disabled", lepton_charge_selection, hadTau_charge_selection, "OS"),
              'histogramToFit' : histogramToFit,
              'label' : None
            }
            self.createCfg_prep_dcard(self.jobOptions_prep_dcard[key_prep_dcard_job])
        if "SS" in self.chargeSumSelections:
          for histogramToFit in self.histograms_to_fit:
            key_hadd_stage2_job = getKey(lepton_charge_selection, hadTau_charge_selection, get_lepton_and_hadTau_selection_and_frWeight("Tight", "disabled"), "SS")
            prep_dcard_job_tuple = (self.channel, lepton_charge_selection, hadTau_charge_selection, "SS", histogramToFit)
            key_prep_dcard_job = getKey(lepton_charge_selection, hadTau_charge_selection, "SS", histogramToFit)
            self.jobOptions_prep_dcard[key_prep_dcard_job] = {
              'inputFile' : self.outputFile_hadd_stage2[key_hadd_stage2_job],
              'cfgFile_modified' : os.path.join(self.dirs[key_prep_dcard_dir][DKEY_CFGS], "prepareDatacards_%s_lep%s_tau%s_sum%s_%s_cfg.py" % prep_dcard_job_tuple),
              'datacardFile' : os.path.join(self.dirs[key_prep_dcard_dir][DKEY_DCRD], "prepareDatacards_%s_lep%s_tau%s_sum%s_%s.root" % prep_dcard_job_tuple),
              'histogramDir' : getHistogramDir("Tight", "Tight", "disabled", lepton_charge_selection, hadTau_charge_selection, "SS"),
              'histogramToFit' : histogramToFit,
              'label' : 'SS'
            }
            self.createCfg_prep_dcard(self.jobOptions_prep_dcard[key_prep_dcard_job])

      # add shape templates for the following systematic uncertainties:
      #  - 'CMS_ttHl_Clos_norm_e'
      #  - 'CMS_ttHl_Clos_shape_e'
      #  - 'CMS_ttHl_Clos_norm_m'
      #  - 'CMS_ttHl_Clos_shape_m'
      #  - 'CMS_ttHl_Clos_norm_t'
      #  - 'CMS_ttHl_Clos_shape_t'
      for chargeSumSelection in self.chargeSumSelections:
        for hadTau_charge_selection in self.hadTau_charge_selections:
          for histogramToFit in self.histograms_to_fit:
            key_prep_dcard_job = getKey(lepton_charge_selection, hadTau_charge_selection, chargeSumSelection, histogramToFit)
            key_hadd_stage2_job = getKey(lepton_charge_selection, hadTau_charge_selection, get_lepton_and_hadTau_selection_and_frWeight("Tight", "disabled"), chargeSumSelection)
            key_add_syst_fakerate_dir = getKey("addSystFakeRates")
            add_syst_fakerate_job_tuple = (self.channel, lepton_charge_selection, hadTau_charge_selection, chargeSumSelection, histogramToFit)
            key_add_syst_fakerate_job = getKey(lepton_charge_selection, hadTau_charge_selection, chargeSumSelection, histogramToFit)
            self.jobOptions_add_syst_fakerate[key_add_syst_fakerate_job] = {
              'inputFile' : self.jobOptions_prep_dcard[key_prep_dcard_job]['datacardFile'],
              'cfgFile_modified' : os.path.join(self.dirs[key_add_syst_fakerate_dir][DKEY_CFGS], "addSystFakeRates_%s_lep%s_tau%s_sum%s_%s_cfg.py" % add_syst_fakerate_job_tuple),
              'outputFile' : os.path.join(self.dirs[key_add_syst_fakerate_dir][DKEY_DCRD], "addSystFakeRates_%s_lep%s_tau%s_sum%s_%s.root" % add_syst_fakerate_job_tuple),
              'category' : self.channel,
              'histogramToFit' : histogramToFit,
              'plots_outputFileName' : os.path.join(self.dirs[key_add_syst_fakerate_dir][DKEY_PLOT], "addSystFakeRates.png")
            }
            histogramDir_nominal = getHistogramDir("Tight", "Tight", "disabled", lepton_charge_selection, hadTau_charge_selection, chargeSumSelection)
            for lepton_and_hadTau_type in [ 'e', 'm', 't' ]:
              lepton_and_hadTau_mcClosure = "Fakeable_mcClosure_%s" % lepton_and_hadTau_type
              if lepton_and_hadTau_mcClosure not in self.lepton_and_hadTau_selections:
                continue
              lepton_and_hadTau_selection_and_frWeight = get_lepton_and_hadTau_selection_and_frWeight(lepton_and_hadTau_mcClosure, "enabled")
              key_addBackgrounds_job_fakes = getKey("fakes_mc", lepton_charge_selection, hadTau_charge_selection, lepton_and_hadTau_selection_and_frWeight, chargeSumSelection)
              histogramDir_mcClosure = self.mcClosure_dir['%s_%s_%s' % (lepton_and_hadTau_mcClosure, chargeSumSelection, hadTau_charge_selection)]
              self.jobOptions_add_syst_fakerate[key_add_syst_fakerate_job].update({
                'add_Clos_%s' % lepton_and_hadTau_type : ("Fakeable_mcClosure_%s" % lepton_and_hadTau_type) in self.lepton_and_hadTau_selections,
                'inputFile_nominal_%s' % lepton_and_hadTau_type : self.outputFile_hadd_stage2[key_hadd_stage2_job],
                'histogramName_nominal_%s' % lepton_and_hadTau_type : "%s/sel/evt/fakes_mc/%s" % (histogramDir_nominal, histogramToFit),
                'inputFile_mcClosure_%s' % lepton_and_hadTau_type : self.jobOptions_addBackgrounds_sum[key_addBackgrounds_job_fakes]['outputFile'],
                'histogramName_mcClosure_%s' % lepton_and_hadTau_type : "%s/sel/evt/fakes_mc/%s" % (histogramDir_mcClosure, histogramToFit)
              })
            self.createCfg_add_syst_fakerate(self.jobOptions_add_syst_fakerate[key_add_syst_fakerate_job])

    logging.info("Creating configuration files to run 'makePlots'")
    for lepton_charge_selection in self.lepton_charge_selections:
      for hadTau_charge_selection in self.hadTau_charge_selections:
        lepton_and_hadTau_charge_selection = ""
        if lepton_charge_selection != "disabled":
          lepton_and_hadTau_charge_selection += "_lep%s" % lepton_charge_selection
        if hadTau_charge_selection != "disabled":
          lepton_and_hadTau_charge_selection += "_tau%s" % hadTau_charge_selection
        key_makePlots_dir = getKey("makePlots")
        if "OS" in self.chargeSumSelections:
          key_hadd_stage2_job = getKey(lepton_charge_selection, hadTau_charge_selection, get_lepton_and_hadTau_selection_and_frWeight("Tight", "disabled"), "OS")
          key_makePlots_job = getKey(lepton_charge_selection, hadTau_charge_selection, "OS")
          self.jobOptions_make_plots[key_makePlots_job] = {
            'executable' : self.executable_make_plots,
            'inputFile' : self.outputFile_hadd_stage2[key_hadd_stage2_job],
            'cfgFile_modified' : os.path.join(self.dirs[key_makePlots_dir][DKEY_CFGS], "makePlots_%s_%s_sumOS_cfg.py" % (self.channel, lepton_and_hadTau_charge_selection)),
            'outputFile' : os.path.join(self.dirs[key_makePlots_dir][DKEY_PLOT], "makePlots_%s_%s_sumOS.png" % (self.channel, lepton_and_hadTau_charge_selection)),
            'histogramDir' : getHistogramDir("Tight", "Tight", "disabled", lepton_charge_selection, hadTau_charge_selection, "OS"),
            'label' : "2l+2#tau_{h}",
            'make_plots_backgrounds' : self.make_plots_backgrounds
          }
          self.createCfg_makePlots(self.jobOptions_make_plots[key_makePlots_job])
        if "SS" in self.chargeSumSelections:
          key_hadd_stage2_job = getKey(lepton_charge_selection, hadTau_charge_selection, get_lepton_and_hadTau_selection_and_frWeight("Tight", "disabled"), "SS")
          key_makePlots_job = getKey(lepton_charge_selection, hadTau_charge_selection, "SS")
          self.jobOptions_make_plots[key_makePlots_job] = {
            'executable' : self.executable_make_plots,
            'inputFile' : self.outputFile_hadd_stage2[key_hadd_stage2_job],
            'cfgFile_modified' : os.path.join(self.dirs[key_makePlots_dir][DKEY_CFGS], "makePlots_%s_%s_sumSS_cfg.py" % (self.channel, lepton_and_hadTau_charge_selection)),
            'outputFile' : os.path.join(self.dirs[key_makePlots_dir][DKEY_PLOT], "makePlots_%s_%s_sumSS.png" % (self.channel, lepton_and_hadTau_charge_selection)),
            'histogramDir' : getHistogramDir("Tight", "Tight", "disabled", lepton_charge_selection, hadTau_charge_selection, "SS"),
            'label' : "2l+2#tau_{h} SS",
            'make_plots_backgrounds' : self.make_plots_backgrounds
          }
          self.createCfg_makePlots(self.jobOptions_make_plots[key_makePlots_job])
        if "Fakeable_mcClosure" in self.lepton_and_hadTau_selections: #TODO
          key_hadd_stage2_job = getKey(lepton_charge_selection, hadTau_charge_selection, get_lepton_and_hadTau_selection_and_frWeight("Tight", "disabled"), "OS")
          key_makePlots_job = getKey(lepton_charge_selection, hadTau_charge_selection, "OS")
          self.jobOptions_make_plots[key_makePlots_job] = {
            'executable' : self.executable_make_plots_mcClosure,
            'inputFile' : self.outputFile_hadd_stage2[key_hadd_stage2_job],
            'cfgFile_modified' : os.path.join(self.dirs[key_makePlots_dir][DKEY_CFGS], "makePlots_mcClosure_%s_%s_sumOS_cfg.py" % (self.channel, lepton_and_hadTau_charge_selection)),
            'outputFile' : os.path.join(self.dirs[key_makePlots_dir][DKEY_PLOT], "makePlots_mcClosure_%s_%s_sumOS.png" % (self.channel, lepton_and_hadTau_charge_selection))
          }
          self.createCfg_makePlots_mcClosure(self.jobOptions_make_plots[key_makePlots_job])

    if self.is_sbatch:
      logging.info("Creating script for submitting '%s' jobs to batch system" % self.executable_analyze)
      self.sbatchFile_analyze = os.path.join(self.dirs[DKEY_SCRIPTS], "sbatch_analyze_%s.py" % self.channel)
      self.createScript_sbatch_analyze(self.executable_analyze, self.sbatchFile_analyze, self.jobOptions_analyze)
      logging.info("Creating script for submitting '%s' jobs to batch system" % self.executable_addBackgrounds)
      self.sbatchFile_addBackgrounds = os.path.join(self.dirs[DKEY_SCRIPTS], "sbatch_addBackgrounds_%s.py" % self.channel)
      self.createScript_sbatch_addBackgrounds(self.executable_addBackgrounds, self.sbatchFile_addBackgrounds, self.jobOptions_addBackgrounds)
      self.sbatchFile_addBackgrounds_sum = os.path.join(self.dirs[DKEY_SCRIPTS], "sbatch_addBackgrounds_sum_%s.py" % self.channel)
      self.createScript_sbatch_addBackgrounds(self.executable_addBackgrounds, self.sbatchFile_addBackgrounds_sum, self.jobOptions_addBackgrounds_sum)
      logging.info("Creating script for submitting '%s' jobs to batch system" % self.executable_addFakes)
      self.sbatchFile_addFakes = os.path.join(self.dirs[DKEY_SCRIPTS], "sbatch_addFakes_%s.py" % self.channel)
      self.createScript_sbatch_addFakes(self.executable_addFakes, self.sbatchFile_addFakes, self.jobOptions_addFakes)

    logging.info("Creating Makefile")
    lines_makefile = []
    self.addToMakefile_analyze(lines_makefile)
    self.addToMakefile_hadd_stage1(lines_makefile)
    self.addToMakefile_backgrounds_from_data(lines_makefile)
    self.addToMakefile_hadd_stage2(lines_makefile)
    self.addToMakefile_prep_dcard(lines_makefile)
    self.addToMakefile_add_syst_fakerate(lines_makefile)
    self.addToMakefile_make_plots(lines_makefile)
    self.addToMakefile_validate(lines_makefile)
    self.createMakefile(lines_makefile)

    logging.info("Done.")

    return self.num_jobs
