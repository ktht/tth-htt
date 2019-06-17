from tthAnalysis.HiggsToTauTau.samples.hhAnalyzeSamples_2017_bkg import samples_2017

for sample_name, sample_info in samples_2017.items():
  if sample_name == 'sum_events':
    continue
  if sample_info["process_name_specific"] in [
        #"ttHToNonbb_M125_powheg",
        #"TTZJets_LO",
        #"TTZJets_LO_ext1",
        #"TTWJets_LO",
        #"TTWJets_LO_ext1",
        #"TTTo2L2Nu",
        #"TTTo2L2Nu_PSweights",
        #"TTToSemiLeptonic",
        #"TTToSemiLeptonic_PSweights",
        ##"TTToHadronic",
        ##"TTToHadronic_PSweights",
        #"GluGluHToZZTo4L",
        #"GluGluHToZZTo4L_ext1",
        #"TTWW",
        #"ST_s-channel_4f_leptonDecays",
        #"ST_s-channel_4f_leptonDecays_PSweights",
        #"ST_t-channel_antitop_4f_inclusiveDecays",
        #"ST_t-channel_top_4f_inclusiveDecays",
        #"ST_tW_antitop_5f_inclusiveDecays",
        #"ST_tW_antitop_5f_inclusiveDecays_PSweights",
        #"ST_tW_top_5f_inclusiveDecays",
        #"ST_tW_top_5f_inclusiveDecays_PSweights",
        #"DYJetsToLL_M-10to50",
        #-"DYJetsToLL_M-50",
        #-"DYJetsToLL_M-50_ext1",
        #-"DYJetsToLL_M-50_LO",
        #-"DYJetsToLL_M-50_LO_ext1",
        #"DY1JetsToLL_M-50",
        #"DY1JetsToLL_M-50_ext1",
        #"DY2JetsToLL_M-50",
        #"DY2JetsToLL_M-50_ext1",
        #"DY3JetsToLL_M-50",
        #"DY3JetsToLL_M-50_ext1",
        #"DY4JetsToLL_M-50",
        #"DYJetsToLL_M-4to50_HT-100to200",
        #"DYJetsToLL_M-4to50_HT-100to200_ext1",
        #"DYJetsToLL_M-4to50_HT-200to400",
        #"DYJetsToLL_M-4to50_HT-200to400_ext1",
        #"DYJetsToLL_M-4to50_HT-400to600",
        #"DYJetsToLL_M-4to50_HT-400to600_ext1",
        #"DYJetsToLL_M-4to50_HT-600toInf",
        ##
        #"DYJetsToLL_M50_HT100to200",
        #"DYJetsToLL_M50_HT100to200_ext1",
        #"DYJetsToLL_M50_HT200to400",
        #"DYJetsToLL_M50_HT200to400_ext1",
        #"DYJetsToLL_M50_HT400to600",
        #"DYJetsToLL_M50_HT400to600_ext1",
        #"DYJetsToLL_M50_HT600to800",
        #"DYJetsToLL_M50_HT800to1200",
        #"DYJetsToLL_M50_HT1200to2500",
        #"DYJetsToLL_M50_HT2500toInf",
        ###
        #"DYBBJetsToLL_M-50",
        #"WJetsToLNu",
        #"WWTo2L2Nu",
        #"WWTo2L2Nu_PSweights",
        #"WWToLNuQQ",
        #"WWToLNuQQ_ext1",
        #"WWToLNuQQ_PSweights",
        #"WWTo1L1Nu2Q",
        #"WWTo4Q",
        #"WWTo4Q_PSweights",
        ###"WZTo3LNu",
        #"WZTo3LNu_powheg",
        #"WZTo2L2Q",
        #"WZTo1L1Nu2Q",
        ###"ZZTo4L",
        ###"ZZTo4L_ext1",
        #"ZZTo2L2Nu",
        #"ZZTo2L2Q",
        #"GluGluHToTauTau",
        #"GluGluHToTauTau_ext1",
        #"VBFHToTauTau",
        #"VHToNonbb_M125_v14-v2",
        #"ZH_HToBB_ZToLL",
        #"ZHToTauTau",
        "THQ_ctcvcp",
        "THW_ctcvcp",
        ##"VHToNonbb_M125"
        #"THQ",
        #"THW",
      ]:
    sample_info["use_it"] = True
  else:
    sample_info["use_it"] = False
