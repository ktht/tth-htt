from collections import OrderedDict as OD

# file generated at 2019-11-17 23:50:59 with the following command:
# find_samples.py -V -i ../NanoAOD/test/datasets/txt/nano_datasets_mc_2018_RunIIAutumn18MiniAOD.txt -m python/samples/metaDict_2018_mc_nano.py -s ../NanoAOD/test/datasets/txt/sum_datasets_2018_RunIIAutumn18MiniAOD.txt -T NANOAOD

meta_dictionary = OD()


### event sums

sum_events = { 
  ("GluGluHToMuMu_M125", "GluGluHToMuMu_M125_ext1"),
  ("TTWW_ext1", "TTWW_ext2"),
  ("ZH_HToBB_ZToLL", "ZH_HToBB_ZToLL_ext1"),
  ("DYJetsToLL_M-50_amcatnloFXFX", "DYJetsToLL_M-50_amcatnloFXFX_ext2"),
  ("DYJetsToLL_M50_HT400to600_PSweights", "DYJetsToLL_M50_HT400to600_PSweights_ext2"),
  ("WZTo3LNu", "WZTo3LNu_ext1"),
  ("ZZTo4L_ext1", "ZZTo4L_ext2"),
  ("ZZTo2L2Nu_ext1", "ZZTo2L2Nu_ext2"),
  ("QCD_Pt80to120_Mu5", "QCD_Pt80to120_Mu5_ext1"),
  ("QCD_Pt120to170_Mu5", "QCD_Pt120to170_Mu5_ext1"),
  ("QCD_Pt300to470_Mu5", "QCD_Pt300to470_Mu5_ext3"),
  ("QCD_Pt470to600_Mu5", "QCD_Pt470to600_Mu5_ext1"),
}


meta_dictionary["/ttHJetToNonbb_M125_TuneCP5_13TeV_amcatnloFXFX_madspin_pythia8/RunIIAutumn18NanoAODv6-Nano25Oct2019_102X_upgrade2018_realistic_v20-v1/NANOAODSIM"] =  OD([
  ("crab_string",           ""),
  ("sample_category",       "ttH"),
  ("process_name_specific", "ttHJetToNonbb_M125_amcatnlo"),
  ("nof_db_events",         9591829),
  ("nof_db_files",          14),
  ("fsize_db",              24432796691),
  ("parent_db",             "/ttHJetToNonbb_M125_TuneCP5_13TeV_amcatnloFXFX_madspin_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"),
  ("xsection",              0.2118),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 24.43GB; nevents: 9.59M; release: 10_2_18; last modified: 2019-11-09 10:46:09"),
])

meta_dictionary["/ttHToNonbb_M125_TuneCP5_13TeV-powheg-pythia8/RunIIAutumn18NanoAODv6-Nano25Oct2019_102X_upgrade2018_realistic_v20-v1/NANOAODSIM"] =  OD([
  ("crab_string",           ""),
  ("sample_category",       "ttH"),
  ("process_name_specific", "ttHToNonbb_M125_powheg"),
  ("nof_db_events",         7525991),
  ("nof_db_files",          12),
  ("fsize_db",              18552741417),
  ("parent_db",             "/ttHToNonbb_M125_TuneCP5_13TeV-powheg-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"),
  ("xsection",              0.2118),
  ("use_it",                False),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 18.55GB; nevents: 7.53M; release: 10_2_18; last modified: 2019-11-08 05:19:34"),
])

meta_dictionary["/TTH_4f_ctcvcp_TuneCP5_13TeV_madgraph_pythia8/RunIIAutumn18NanoAODv6-Nano25Oct2019_102X_upgrade2018_realistic_v20-v2/NANOAODSIM"] =  OD([
  ("crab_string",           ""),
  ("sample_category",       "ttH_ctcvcp"),
  ("process_name_specific", "TTH_4f_ctcvcp"),
  ("nof_db_events",         29093000),
  ("nof_db_files",          33),
  ("fsize_db",              73515601460),
  ("parent_db",             "/TTH_4f_ctcvcp_TuneCP5_13TeV_madgraph_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"),
  ("xsection",              0.5071),
  ("use_it",                False),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 73.52GB; nevents: 29.09M; release: 10_2_18; last modified: 2019-10-30 14:38:57"),
])

meta_dictionary["/THQ_ctcvcp_4f_Hincl_13TeV_madgraph_pythia8/RunIIAutumn18NanoAODv6-Nano25Oct2019_102X_upgrade2018_realistic_v20-v1/NANOAODSIM"] =  OD([
  ("crab_string",           ""),
  ("sample_category",       "tHq"),
  ("process_name_specific", "THQ_ctcvcp"),
  ("nof_db_events",         29587975),
  ("nof_db_files",          41),
  ("fsize_db",              66923890570),
  ("parent_db",             "/THQ_ctcvcp_4f_Hincl_13TeV_madgraph_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"),
  ("xsection",              0.07096),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 66.92GB; nevents: 29.59M; release: 10_2_18; last modified: 2019-11-06 18:13:26"),
])

meta_dictionary["/THW_ctcvcp_5f_Hincl_13TeV_madgraph_pythia8/RunIIAutumn18NanoAODv6-Nano25Oct2019_102X_upgrade2018_realistic_v20-v1/NANOAODSIM"] =  OD([
  ("crab_string",           ""),
  ("sample_category",       "tHW"),
  ("process_name_specific", "THW_ctcvcp"),
  ("nof_db_events",         14998988),
  ("nof_db_files",          22),
  ("fsize_db",              39245900677),
  ("parent_db",             "/THW_ctcvcp_5f_Hincl_13TeV_madgraph_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"),
  ("xsection",              0.01561),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 39.25GB; nevents: 15.00M; release: 10_2_18; last modified: 2019-11-08 08:31:53"),
])

meta_dictionary["/GluGluHToZZTo4L_M125_13TeV_powheg2_JHUGenV7011_pythia8/RunIIAutumn18NanoAODv6-Nano25Oct2019_102X_upgrade2018_realistic_v20-v1/NANOAODSIM"] =  OD([
  ("crab_string",           ""),
  ("sample_category",       "ggH"),
  ("process_name_specific", "GluGluHToZZTo4L"),
  ("nof_db_events",         958000),
  ("nof_db_files",          3),
  ("fsize_db",              1468746871),
  ("parent_db",             "/GluGluHToZZTo4L_M125_13TeV_powheg2_JHUGenV7011_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"),
  ("xsection",              0.01297),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 1.47GB; nevents: 958.00k; release: 10_2_18; last modified: 2019-11-07 03:38:32"),
])

meta_dictionary["/GluGluHToZZTo2L2Q_M125_13TeV_powheg2_JHUGenV7011_pythia8/RunIIAutumn18NanoAODv6-Nano25Oct2019_102X_upgrade2018_realistic_v20-v1/NANOAODSIM"] =  OD([
  ("crab_string",           ""),
  ("sample_category",       "ggH"),
  ("process_name_specific", "GluGluHToZZTo2L2Q_M125"),
  ("nof_db_events",         984000),
  ("nof_db_files",          3),
  ("fsize_db",              1368621244),
  ("parent_db",             "/GluGluHToZZTo2L2Q_M125_13TeV_powheg2_JHUGenV7011_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"),
  ("xsection",              0.17963),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 1.37GB; nevents: 984.00k; release: 10_2_18; last modified: 2019-11-04 04:32:23"),
])

meta_dictionary["/GluGluHToWWToLNuQQ_M125_13TeV_powheg2_JHUGenV714_pythia8/RunIIAutumn18NanoAODv6-Nano25Oct2019_102X_upgrade2018_realistic_v20-v1/NANOAODSIM"] =  OD([
  ("crab_string",           ""),
  ("sample_category",       "ggH"),
  ("process_name_specific", "GluGluHToWWToLNuQQ_M125"),
  ("nof_db_events",         1000000),
  ("nof_db_files",          3),
  ("fsize_db",              1229050866),
  ("parent_db",             "/GluGluHToWWToLNuQQ_M125_13TeV_powheg2_JHUGenV714_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"),
  ("xsection",              4.5621),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 1.23GB; nevents: 1.00M; release: 10_2_18; last modified: 2019-11-09 04:39:05"),
])

meta_dictionary["/GluGluHToWWTo2L2Nu_M125_13TeV_powheg2_JHUGenV714_pythia8/RunIIAutumn18NanoAODv6-Nano25Oct2019_102X_upgrade2018_realistic_v20-v1/NANOAODSIM"] =  OD([
  ("crab_string",           ""),
  ("sample_category",       "ggH"),
  ("process_name_specific", "GluGluHToWWTo2L2Nu_M125"),
  ("nof_db_events",         1000000),
  ("nof_db_files",          2),
  ("fsize_db",              1250487114),
  ("parent_db",             "/GluGluHToWWTo2L2Nu_M125_13TeV_powheg2_JHUGenV714_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"),
  ("xsection",              1.1033),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 1.25GB; nevents: 1.00M; release: 10_2_18; last modified: 2019-11-10 03:57:06"),
])

meta_dictionary["/GluGluHToMuMu_M-125_TuneCP5_PSweights_13TeV_powheg_pythia8/RunIIAutumn18NanoAODv6-Nano25Oct2019_102X_upgrade2018_realistic_v20-v1/NANOAODSIM"] =  OD([
  ("crab_string",           ""),
  ("sample_category",       "ggH"),
  ("process_name_specific", "GluGluHToMuMu_M125"),
  ("nof_db_events",         476000),
  ("nof_db_files",          1),
  ("fsize_db",              562166612),
  ("parent_db",             "/GluGluHToMuMu_M-125_TuneCP5_PSweights_13TeV_powheg_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"),
  ("xsection",              0.010571),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 562.17MB; nevents: 476.00k; release: 10_2_18; last modified: 2019-11-07 20:07:41"),
])

meta_dictionary["/GluGluHToMuMu_M-125_TuneCP5_PSweights_13TeV_powheg_pythia8/RunIIAutumn18NanoAODv6-Nano25Oct2019_102X_upgrade2018_realistic_v20_ext1-v1/NANOAODSIM"] =  OD([
  ("crab_string",           ""),
  ("sample_category",       "ggH"),
  ("process_name_specific", "GluGluHToMuMu_M125_ext1"),
  ("nof_db_events",         1444000),
  ("nof_db_files",          2),
  ("fsize_db",              1701751427),
  ("parent_db",             "/GluGluHToMuMu_M-125_TuneCP5_PSweights_13TeV_powheg_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext1-v1/MINIAODSIM"),
  ("xsection",              0.010571),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 1.70GB; nevents: 1.44M; release: 10_2_18; last modified: 2019-11-09 04:38:40"),
])

meta_dictionary["/GluGluHToBB_M125_13TeV_amcatnloFXFX_pythia8/RunIIAutumn18NanoAODv6-Nano25Oct2019_102X_upgrade2018_realistic_v20-v1/NANOAODSIM"] =  OD([
  ("crab_string",           ""),
  ("sample_category",       "ggH"),
  ("process_name_specific", "GluGluHToBB_M125"),
  ("nof_db_events",         15034579),
  ("nof_db_files",          16),
  ("fsize_db",              18919796528),
  ("parent_db",             "/GluGluHToBB_M125_13TeV_amcatnloFXFX_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"),
  ("xsection",              28.293),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 18.92GB; nevents: 15.03M; release: 10_2_18; last modified: 2019-11-10 00:49:46"),
])

meta_dictionary["/GluGluHToGG_M125_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIIAutumn18NanoAODv6-Nano25Oct2019_102X_upgrade2018_realistic_v20-v1/NANOAODSIM"] =  OD([
  ("crab_string",           ""),
  ("sample_category",       "ggH"),
  ("process_name_specific", "GluGluHToGG_M125"),
  ("nof_db_events",         1927927),
  ("nof_db_files",          3),
  ("fsize_db",              2227787792),
  ("parent_db",             "/GluGluHToGG_M125_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"),
  ("xsection",              0.11028),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 2.23GB; nevents: 1.93M; release: 10_2_18; last modified: 2019-11-06 08:50:57"),
])

meta_dictionary["/VBF_HToZZTo4L_M125_13TeV_powheg2_JHUGenV7011_pythia8/RunIIAutumn18NanoAODv6-Nano25Oct2019_102X_upgrade2018_realistic_v20-v1/NANOAODSIM"] =  OD([
  ("crab_string",           ""),
  ("sample_category",       "qqH"),
  ("process_name_specific", "VBF_HToZZTo4L"),
  ("nof_db_events",         500000),
  ("nof_db_files",          1),
  ("fsize_db",              887393048),
  ("parent_db",             "/VBF_HToZZTo4L_M125_13TeV_powheg2_JHUGenV7011_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"),
  ("xsection",              0.0010099),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 887.39MB; nevents: 500.00k; release: 10_2_18; last modified: 2019-11-07 19:58:55"),
])

meta_dictionary["/VBFHToWWToLNuQQ_M125_13TeV_powheg_JHUGen_pythia8/RunIIAutumn18NanoAODv6-Nano25Oct2019_102X_upgrade2018_realistic_v20-v1/NANOAODSIM"] =  OD([
  ("crab_string",           ""),
  ("sample_category",       "qqH"),
  ("process_name_specific", "VBFHToWWToLNuQQ_M125"),
  ("nof_db_events",         1000000),
  ("nof_db_files",          1),
  ("fsize_db",              1456821277),
  ("parent_db",             "/VBFHToWWToLNuQQ_M125_13TeV_powheg_JHUGen_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"),
  ("xsection",              0.35517),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 1.46GB; nevents: 1.00M; release: 10_2_18; last modified: 2019-11-09 10:48:14"),
])

meta_dictionary["/VBFHToWWTo2L2Nu_M125_13TeV_powheg2_JHUGenV714_pythia8/RunIIAutumn18NanoAODv6-Nano25Oct2019_102X_upgrade2018_realistic_v20-v1/NANOAODSIM"] =  OD([
  ("crab_string",           ""),
  ("sample_category",       "qqH"),
  ("process_name_specific", "VBFHToWWTo2L2Nu_M125"),
  ("nof_db_events",         1000000),
  ("nof_db_files",          4),
  ("fsize_db",              1561767950),
  ("parent_db",             "/VBFHToWWTo2L2Nu_M125_13TeV_powheg2_JHUGenV714_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"),
  ("xsection",              0.085894),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 1.56GB; nevents: 1.00M; release: 10_2_18; last modified: 2019-11-04 04:29:48"),
])

meta_dictionary["/VBFHToMuMu_M-125_TuneCP5_PSweights_13TeV_powheg_pythia8/RunIIAutumn18NanoAODv6-Nano25Oct2019_102X_upgrade2018_realistic_v20-v1/NANOAODSIM"] =  OD([
  ("crab_string",           ""),
  ("sample_category",       "qqH"),
  ("process_name_specific", "VBFHToMuMu_M125"),
  ("nof_db_events",         1000000),
  ("nof_db_files",          2),
  ("fsize_db",              1417746087),
  ("parent_db",             "/VBFHToMuMu_M-125_TuneCP5_PSweights_13TeV_powheg_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"),
  ("xsection",              0.00082296),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 1.42GB; nevents: 1.00M; release: 10_2_18; last modified: 2019-11-07 23:57:45"),
])

meta_dictionary["/VBFHToBB_M-125_13TeV_powheg_pythia8_weightfix/RunIIAutumn18NanoAODv6-Nano25Oct2019_102X_upgrade2018_realistic_v20-v1/NANOAODSIM"] =  OD([
  ("crab_string",           ""),
  ("sample_category",       "qqH"),
  ("process_name_specific", "VBFHToBB_M125"),
  ("nof_db_events",         7587200),
  ("nof_db_files",          9),
  ("fsize_db",              10608202218),
  ("parent_db",             "/VBFHToBB_M-125_13TeV_powheg_pythia8_weightfix/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"),
  ("xsection",              2.2026),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 10.61GB; nevents: 7.59M; release: 10_2_18; last modified: 2019-11-13 01:10:38"),
])

meta_dictionary["/VBFHToGG_M125_13TeV_amcatnlo_pythia8/RunIIAutumn18NanoAODv6-Nano25Oct2019_102X_upgrade2018_realistic_v20-v1/NANOAODSIM"] =  OD([
  ("crab_string",           ""),
  ("sample_category",       "qqH"),
  ("process_name_specific", "VBFHToGG_M125"),
  ("nof_db_events",         1918000),
  ("nof_db_files",          2),
  ("fsize_db",              2430412416),
  ("parent_db",             "/VBFHToGG_M125_13TeV_amcatnlo_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"),
  ("xsection",              0.0085851),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 2.43GB; nevents: 1.92M; release: 10_2_18; last modified: 2019-11-09 21:35:07"),
])

meta_dictionary["/TTZToLLNuNu_M-10_TuneCP5_13TeV-amcatnlo-pythia8/RunIIAutumn18NanoAODv6-Nano25Oct2019_102X_upgrade2018_realistic_v20_ext1-v1/NANOAODSIM"] =  OD([
  ("crab_string",           ""),
  ("sample_category",       "TTZ"),
  ("process_name_specific", "TTZToLL_M10_ext1"),
  ("nof_db_events",         13280000),
  ("nof_db_files",          15),
  ("fsize_db",              30715928115),
  ("parent_db",             "/TTZToLLNuNu_M-10_TuneCP5_13TeV-amcatnlo-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext1-v2/MINIAODSIM"),
  ("xsection",              0.2072),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 30.72GB; nevents: 13.28M; release: 10_2_18; last modified: 2019-11-13 01:12:58"),
])

meta_dictionary["/TTZToLL_M-1to10_TuneCP5_13TeV-amcatnlo-pythia8/RunIIAutumn18NanoAODv6-Nano25Oct2019_102X_upgrade2018_realistic_v20-v1/NANOAODSIM"] =  OD([
  ("crab_string",           ""),
  ("sample_category",       "TTZ"),
  ("process_name_specific", "TTZToLL_M-1to10"),
  ("nof_db_events",         250000),
  ("nof_db_files",          2),
  ("fsize_db",              559871839),
  ("parent_db",             "/TTZToLL_M-1to10_TuneCP5_13TeV-amcatnlo-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"),
  ("xsection",              0.04537),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 559.87MB; nevents: 250.00k; release: 10_2_18; last modified: 2019-11-09 10:35:55"),
])

meta_dictionary["/ttZJets_TuneCP5_13TeV_madgraphMLM_pythia8/RunIIAutumn18NanoAODv6-Nano25Oct2019_102X_upgrade2018_realistic_v20_ext1-v1/NANOAODSIM"] =  OD([
  ("crab_string",           ""),
  ("sample_category",       "TTZ"),
  ("process_name_specific", "TTZJets_LO_ext1"),
  ("nof_db_events",         22646257),
  ("nof_db_files",          27),
  ("fsize_db",              52121347463),
  ("parent_db",             "/ttZJets_TuneCP5_13TeV_madgraphMLM_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext1-v2/MINIAODSIM"),
  ("xsection",              0.8393),
  ("use_it",                False),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 52.12GB; nevents: 22.65M; release: 10_2_18; last modified: 2019-11-07 03:35:12"),
])

meta_dictionary["/TTWJetsToLNu_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/RunIIAutumn18NanoAODv6-Nano25Oct2019_102X_upgrade2018_realistic_v20_ext1-v1/NANOAODSIM"] =  OD([
  ("crab_string",           ""),
  ("sample_category",       "TTW"),
  ("process_name_specific", "TTWJetsToLNu_ext1"),
  ("nof_db_events",         4911941),
  ("nof_db_files",          7),
  ("fsize_db",              11588703643),
  ("parent_db",             "/TTWJetsToLNu_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext1-v2/MINIAODSIM"),
  ("xsection",              0.196),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 11.59GB; nevents: 4.91M; release: 10_2_18; last modified: 2019-11-07 20:41:48"),
])

meta_dictionary["/ttWJets_TuneCP5_13TeV_madgraphMLM_pythia8/RunIIAutumn18NanoAODv6-Nano25Oct2019_102X_upgrade2018_realistic_v20_ext1-v1/NANOAODSIM"] =  OD([
  ("crab_string",           ""),
  ("sample_category",       "TTW"),
  ("process_name_specific", "TTWJets_LO_ext1"),
  ("nof_db_events",         12816567),
  ("nof_db_files",          19),
  ("fsize_db",              29001769287),
  ("parent_db",             "/ttWJets_TuneCP5_13TeV_madgraphMLM_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext1-v2/MINIAODSIM"),
  ("xsection",              0.6008),
  ("use_it",                False),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 29.00GB; nevents: 12.82M; release: 10_2_18; last modified: 2019-11-07 10:37:53"),
])

meta_dictionary["/TTWW_TuneCP5_13TeV-madgraph-pythia8/RunIIAutumn18NanoAODv6-Nano25Oct2019_102X_upgrade2018_realistic_v20_ext1-v1/NANOAODSIM"] =  OD([
  ("crab_string",           ""),
  ("sample_category",       "TTWW"),
  ("process_name_specific", "TTWW_ext1"),
  ("nof_db_events",         185000),
  ("nof_db_files",          3),
  ("fsize_db",              483359044),
  ("parent_db",             "/TTWW_TuneCP5_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext1-v2/MINIAODSIM"),
  ("xsection",              0.006981),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 483.36MB; nevents: 185.00k; release: 10_2_18; last modified: 2019-11-03 10:35:28"),
])

meta_dictionary["/TTWW_TuneCP5_13TeV-madgraph-pythia8/RunIIAutumn18NanoAODv6-Nano25Oct2019_102X_upgrade2018_realistic_v20_ext2-v1/NANOAODSIM"] =  OD([
  ("crab_string",           ""),
  ("sample_category",       "TTWW"),
  ("process_name_specific", "TTWW_ext2"),
  ("nof_db_events",         800000),
  ("nof_db_files",          3),
  ("fsize_db",              2057295437),
  ("parent_db",             "/TTWW_TuneCP5_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext2-v1/MINIAODSIM"),
  ("xsection",              0.006981),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 2.06GB; nevents: 800.00k; release: 10_2_18; last modified: 2019-11-12 00:25:56"),
])

meta_dictionary["/ST_t-channel_antitop_4f_InclusiveDecays_TuneCP5_13TeV-powheg-madspin-pythia8/RunIIAutumn18NanoAODv6-Nano25Oct2019_102X_upgrade2018_realistic_v20-v1/NANOAODSIM"] =  OD([
  ("crab_string",           ""),
  ("sample_category",       "TT"),
  ("process_name_specific", "ST_t-channel_antitop_4f_inclusiveDecays"),
  ("nof_db_events",         79090800),
  ("nof_db_files",          66),
  ("fsize_db",              124339595930),
  ("parent_db",             "/ST_t-channel_antitop_4f_InclusiveDecays_TuneCP5_13TeV-powheg-madspin-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"),
  ("xsection",              80.95),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 124.34GB; nevents: 79.09M; release: 10_2_18; last modified: 2019-11-06 04:16:11"),
])

meta_dictionary["/ST_t-channel_top_4f_InclusiveDecays_TuneCP5_13TeV-powheg-madspin-pythia8/RunIIAutumn18NanoAODv6-Nano25Oct2019_102X_upgrade2018_realistic_v20-v1/NANOAODSIM"] =  OD([
  ("crab_string",           ""),
  ("sample_category",       "TT"),
  ("process_name_specific", "ST_t-channel_top_4f_inclusiveDecays"),
  ("nof_db_events",         154307600),
  ("nof_db_files",          110),
  ("fsize_db",              241609954046),
  ("parent_db",             "/ST_t-channel_top_4f_InclusiveDecays_TuneCP5_13TeV-powheg-madspin-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"),
  ("xsection",              136.02),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 241.61GB; nevents: 154.31M; release: 10_2_18; last modified: 2019-11-10 19:55:50"),
])

meta_dictionary["/ST_tW_antitop_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8/RunIIAutumn18NanoAODv6-Nano25Oct2019_102X_upgrade2018_realistic_v20_ext1-v1/NANOAODSIM"] =  OD([
  ("crab_string",           ""),
  ("sample_category",       "TT"),
  ("process_name_specific", "ST_tW_antitop_5f_inclusiveDecays_ext1"),
  ("nof_db_events",         7623000),
  ("nof_db_files",          11),
  ("fsize_db",              13248434505),
  ("parent_db",             "/ST_tW_antitop_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext1-v1/MINIAODSIM"),
  ("xsection",              35.85),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 13.25GB; nevents: 7.62M; release: 10_2_18; last modified: 2019-11-07 20:42:38"),
])

meta_dictionary["/ST_tW_top_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8/RunIIAutumn18NanoAODv6-Nano25Oct2019_102X_upgrade2018_realistic_v20_ext1-v1/NANOAODSIM"] =  OD([
  ("crab_string",           ""),
  ("sample_category",       "TT"),
  ("process_name_specific", "ST_tW_top_5f_inclusiveDecays_ext1"),
  ("nof_db_events",         9598000),
  ("nof_db_files",          12),
  ("fsize_db",              16665155045),
  ("parent_db",             "/ST_tW_top_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext1-v1/MINIAODSIM"),
  ("xsection",              35.85),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 16.67GB; nevents: 9.60M; release: 10_2_18; last modified: 2019-11-08 08:32:33"),
])

meta_dictionary["/ST_tWll_5f_LO_TuneCP5_PSweights_13TeV-madgraph-pythia8/RunIIAutumn18NanoAODv6-Nano25Oct2019_102X_upgrade2018_realistic_v20_ext1-v1/NANOAODSIM"] =  OD([
  ("crab_string",           ""),
  ("sample_category",       "TT"),
  ("process_name_specific", "ST_tWll_PSweights_ext1"),
  ("nof_db_events",         248600),
  ("nof_db_files",          1),
  ("fsize_db",              578996241),
  ("parent_db",             "/ST_tWll_5f_LO_TuneCP5_PSweights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext1-v1/MINIAODSIM"),
  ("xsection",              0.01096),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 579.00MB; nevents: 248.60k; release: 10_2_18; last modified: 2019-11-07 07:34:02"),
])

meta_dictionary["/TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/RunIIAutumn18NanoAODv6-Nano25Oct2019_102X_upgrade2018_realistic_v20-v1/NANOAODSIM"] =  OD([
  ("crab_string",           ""),
  ("sample_category",       "TT"),
  ("process_name_specific", "TTTo2L2Nu"),
  ("nof_db_events",         64120000),
  ("nof_db_files",          59),
  ("fsize_db",              121159494191),
  ("parent_db",             "/TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"),
  ("xsection",              88.4),
  ("use_it",                False),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 121.16GB; nevents: 64.12M; release: 10_2_18; last modified: 2019-11-06 08:52:27"),
])

meta_dictionary["/TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8/RunIIAutumn18NanoAODv6-Nano25Oct2019_102X_upgrade2018_realistic_v20-v1/NANOAODSIM"] =  OD([
  ("crab_string",           ""),
  ("sample_category",       "TT"),
  ("process_name_specific", "TTToSemiLeptonic"),
  ("nof_db_events",         101550000),
  ("nof_db_files",          84),
  ("fsize_db",              194416796320),
  ("parent_db",             "/TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"),
  ("xsection",              365.52),
  ("use_it",                False),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 194.42GB; nevents: 101.55M; release: 10_2_18; last modified: 2019-11-11 17:40:32"),
])

meta_dictionary["/TTToHadronic_TuneCP5_13TeV-powheg-pythia8/RunIIAutumn18NanoAODv6-Nano25Oct2019_102X_upgrade2018_realistic_v20-v3/NANOAODSIM"] =  OD([
  ("crab_string",           ""),
  ("sample_category",       "TT"),
  ("process_name_specific", "TTToHadronic"),
  ("nof_db_events",         131024000),
  ("nof_db_files",          118),
  ("fsize_db",              247880598846),
  ("parent_db",             "/TTToHadronic_TuneCP5_13TeV-powheg-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"),
  ("xsection",              377.85),
  ("use_it",                False),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 247.88GB; nevents: 131.02M; release: 10_2_18; last modified: 2019-10-30 12:02:13"),
])

meta_dictionary["/TTJets_DiLept_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18NanoAODv6-Nano25Oct2019_102X_upgrade2018_realistic_v20-v1/NANOAODSIM"] =  OD([
  ("crab_string",           ""),
  ("sample_category",       "TT"),
  ("process_name_specific", "TTJets_DiLept"),
  ("nof_db_events",         28701360),
  ("nof_db_files",          36),
  ("fsize_db",              52492171756),
  ("parent_db",             "/TTJets_DiLept_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"),
  ("xsection",              88.4),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 52.49GB; nevents: 28.70M; release: 10_2_18; last modified: 2019-11-10 00:46:53"),
])

meta_dictionary["/TTJets_SingleLeptFromT_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18NanoAODv6-Nano25Oct2019_102X_upgrade2018_realistic_v20-v1/NANOAODSIM"] =  OD([
  ("crab_string",           ""),
  ("sample_category",       "TT"),
  ("process_name_specific", "TTJets_SingleLeptFromT"),
  ("nof_db_events",         57259880),
  ("nof_db_files",          61),
  ("fsize_db",              106329224495),
  ("parent_db",             "/TTJets_SingleLeptFromT_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"),
  ("xsection",              182.76),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 106.33GB; nevents: 57.26M; release: 10_2_18; last modified: 2019-11-10 00:56:39"),
])

meta_dictionary["/TTJets_SingleLeptFromTbar_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18NanoAODv6-Nano25Oct2019_102X_upgrade2018_realistic_v20-v1/NANOAODSIM"] =  OD([
  ("crab_string",           ""),
  ("sample_category",       "TT"),
  ("process_name_specific", "TTJets_SingleLeptFromTbar"),
  ("nof_db_events",         59929205),
  ("nof_db_files",          61),
  ("fsize_db",              111291435445),
  ("parent_db",             "/TTJets_SingleLeptFromTbar_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"),
  ("xsection",              182.76),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 111.29GB; nevents: 59.93M; release: 10_2_18; last modified: 2019-11-10 18:03:34"),
])

meta_dictionary["/TTJets_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIIAutumn18NanoAODv6-Nano25Oct2019_102X_upgrade2018_realistic_v20_ext1-v1/NANOAODSIM"] =  OD([
  ("crab_string",           ""),
  ("sample_category",       "TT"),
  ("process_name_specific", "TTJets_amcatnloFXFX_ext1"),
  ("nof_db_events",         142155064),
  ("nof_db_files",          159),
  ("fsize_db",              287162158199),
  ("parent_db",             "/TTJets_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext1-v2/MINIAODSIM"),
  ("xsection",              831.76),
  ("use_it",                False),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 287.16GB; nevents: 142.16M; release: 10_2_18; last modified: 2019-11-10 00:44:23"),
])

meta_dictionary["/TTJets_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18NanoAODv6-Nano25Oct2019_102X_upgrade2018_realistic_v20-v1/NANOAODSIM"] =  OD([
  ("crab_string",           ""),
  ("sample_category",       "TT"),
  ("process_name_specific", "TTJets_madgraphMLM"),
  ("nof_db_events",         10244307),
  ("nof_db_files",          13),
  ("fsize_db",              19068580594),
  ("parent_db",             "/TTJets_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"),
  ("xsection",              831.76),
  ("use_it",                False),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 19.07GB; nevents: 10.24M; release: 10_2_18; last modified: 2019-11-10 09:28:43"),
])

meta_dictionary["/TTWH_TuneCP5_13TeV-madgraph-pythia8/RunIIAutumn18NanoAODv6-Nano25Oct2019_102X_upgrade2018_realistic_v20_ext1-v1/NANOAODSIM"] =  OD([
  ("crab_string",           ""),
  ("sample_category",       "TTWH"),
  ("process_name_specific", "TTWH_ext1"),
  ("nof_db_events",         200000),
  ("nof_db_files",          1),
  ("fsize_db",              529928089),
  ("parent_db",             "/TTWH_TuneCP5_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext1-v2/MINIAODSIM"),
  ("xsection",              0.001582),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 529.93MB; nevents: 200.00k; release: 10_2_18; last modified: 2019-11-07 19:57:45"),
])

meta_dictionary["/TTZH_TuneCP5_13TeV-madgraph-pythia8/RunIIAutumn18NanoAODv6-Nano25Oct2019_102X_upgrade2018_realistic_v20_ext1-v1/NANOAODSIM"] =  OD([
  ("crab_string",           ""),
  ("sample_category",       "TTZH"),
  ("process_name_specific", "TTZH_ext1"),
  ("nof_db_events",         200000),
  ("nof_db_files",          1),
  ("fsize_db",              547619037),
  ("parent_db",             "/TTZH_TuneCP5_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext1-v2/MINIAODSIM"),
  ("xsection",              0.001535),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 547.62MB; nevents: 200.00k; release: 10_2_18; last modified: 2019-11-06 04:42:09"),
])

meta_dictionary["/WWW_4F_TuneCP5_13TeV-amcatnlo-pythia8/RunIIAutumn18NanoAODv6-Nano25Oct2019_102X_upgrade2018_realistic_v20_ext1-v1/NANOAODSIM"] =  OD([
  ("crab_string",           ""),
  ("sample_category",       "Rares"),
  ("process_name_specific", "WWW_ext1"),
  ("nof_db_events",         240000),
  ("nof_db_files",          3),
  ("fsize_db",              447888297),
  ("parent_db",             "/WWW_4F_TuneCP5_13TeV-amcatnlo-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext1-v2/MINIAODSIM"),
  ("xsection",              0.2086),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 447.89MB; nevents: 240.00k; release: 10_2_18; last modified: 2019-11-11 20:51:09"),
])

meta_dictionary["/WWZ_TuneCP5_13TeV-amcatnlo-pythia8/RunIIAutumn18NanoAODv6-Nano25Oct2019_102X_upgrade2018_realistic_v20_ext1-v1/NANOAODSIM"] =  OD([
  ("crab_string",           ""),
  ("sample_category",       "Rares"),
  ("process_name_specific", "WWZ_ext1"),
  ("nof_db_events",         250000),
  ("nof_db_files",          1),
  ("fsize_db",              480611970),
  ("parent_db",             "/WWZ_TuneCP5_13TeV-amcatnlo-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext1-v2/MINIAODSIM"),
  ("xsection",              0.1676),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 480.61MB; nevents: 250.00k; release: 10_2_18; last modified: 2019-11-09 10:56:30"),
])

meta_dictionary["/WZZ_TuneCP5_13TeV-amcatnlo-pythia8/RunIIAutumn18NanoAODv6-Nano25Oct2019_102X_upgrade2018_realistic_v20_ext1-v1/NANOAODSIM"] =  OD([
  ("crab_string",           ""),
  ("sample_category",       "Rares"),
  ("process_name_specific", "WZZ_ext1"),
  ("nof_db_events",         250000),
  ("nof_db_files",          2),
  ("fsize_db",              459287006),
  ("parent_db",             "/WZZ_TuneCP5_13TeV-amcatnlo-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext1-v2/MINIAODSIM"),
  ("xsection",              0.05701),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 459.29MB; nevents: 250.00k; release: 10_2_18; last modified: 2019-11-09 21:33:47"),
])

meta_dictionary["/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/RunIIAutumn18NanoAODv6-Nano25Oct2019_102X_upgrade2018_realistic_v20_ext1-v1/NANOAODSIM"] =  OD([
  ("crab_string",           ""),
  ("sample_category",       "Rares"),
  ("process_name_specific", "ZZZ_ext1"),
  ("nof_db_events",         250000),
  ("nof_db_files",          1),
  ("fsize_db",              425512211),
  ("parent_db",             "/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext1-v2/MINIAODSIM"),
  ("xsection",              0.01473),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 425.51MB; nevents: 250.00k; release: 10_2_18; last modified: 2019-11-08 12:51:05"),
])

meta_dictionary["/WZG_TuneCP5_13TeV-amcatnlo-pythia8/RunIIAutumn18NanoAODv6-Nano25Oct2019_102X_upgrade2018_realistic_v20-v1/NANOAODSIM"] =  OD([
  ("crab_string",           ""),
  ("sample_category",       "Rares"),
  ("process_name_specific", "WZG"),
  ("nof_db_events",         1960000),
  ("nof_db_files",          5),
  ("fsize_db",              3461597146),
  ("parent_db",             "/WZG_TuneCP5_13TeV-amcatnlo-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"),
  ("xsection",              0.04345),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 3.46GB; nevents: 1.96M; release: 10_2_18; last modified: 2019-11-10 15:49:46"),
])

meta_dictionary["/WGToLNuG_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18NanoAODv6-Nano25Oct2019_102X_upgrade2018_realistic_v20-v1/NANOAODSIM"] =  OD([
  ("crab_string",           ""),
  ("sample_category",       "Rares"),
  ("process_name_specific", "WGToLNuG"),
  ("nof_db_events",         6012425),
  ("nof_db_files",          8),
  ("fsize_db",              6738227074),
  ("parent_db",             "/WGToLNuG_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"),
  ("xsection",              464.8),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 6.74GB; nevents: 6.01M; release: 10_2_18; last modified: 2019-11-09 18:15:16"),
])

meta_dictionary["/ZGToLLG_01J_5f_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIIAutumn18NanoAODv6-Nano25Oct2019_102X_upgrade2018_realistic_v20_ext1-v1/NANOAODSIM"] =  OD([
  ("crab_string",           ""),
  ("sample_category",       "Rares"),
  ("process_name_specific", "ZGTo2LG_01J_ext1"),
  ("nof_db_events",         13946364),
  ("nof_db_files",          18),
  ("fsize_db",              17852341385),
  ("parent_db",             "/ZGToLLG_01J_5f_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext1-v2/MINIAODSIM"),
  ("xsection",              55.59),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 17.85GB; nevents: 13.95M; release: 10_2_18; last modified: 2019-11-06 23:26:36"),
])

meta_dictionary["/TGJets_leptonDecays_TuneCP5_13TeV-madgraph-pythia8/RunIIAutumn18NanoAODv6-Nano25Oct2019_102X_upgrade2018_realistic_v20_ext1-v1/NANOAODSIM"] =  OD([
  ("crab_string",           ""),
  ("sample_category",       "Rares"),
  ("process_name_specific", "TGJets"),
  ("nof_db_events",         6520000),
  ("nof_db_files",          7),
  ("fsize_db",              11394708284),
  ("parent_db",             "/TGJets_leptonDecays_TuneCP5_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext1-v2/MINIAODSIM"),
  ("xsection",              1.018),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 11.39GB; nevents: 6.52M; release: 10_2_18; last modified: 2019-11-07 19:59:26"),
])

meta_dictionary["/TTGJets_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/RunIIAutumn18NanoAODv6-Nano25Oct2019_102X_upgrade2018_realistic_v20-v1/NANOAODSIM"] =  OD([
  ("crab_string",           ""),
  ("sample_category",       "Rares"),
  ("process_name_specific", "TTGJets"),
  ("nof_db_events",         4691915),
  ("nof_db_files",          8),
  ("fsize_db",              10387022864),
  ("parent_db",             "/TTGJets_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"),
  ("xsection",              4.215),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 10.39GB; nevents: 4.69M; release: 10_2_18; last modified: 2019-11-10 03:54:22"),
])

meta_dictionary["/tZq_ll_4f_ckm_NLO_TuneCP5_13TeV-madgraph-pythia8/RunIIAutumn18NanoAODv6-Nano25Oct2019_102X_upgrade2018_realistic_v20_ext1-v1/NANOAODSIM"] =  OD([
  ("crab_string",           ""),
  ("sample_category",       "Rares"),
  ("process_name_specific", "tZq_ll_4f_ext1"),
  ("nof_db_events",         13736000),
  ("nof_db_files",          17),
  ("fsize_db",              30164428683),
  ("parent_db",             "/tZq_ll_4f_ckm_NLO_TuneCP5_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext1-v2/MINIAODSIM"),
  ("xsection",              0.07358),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 30.16GB; nevents: 13.74M; release: 10_2_18; last modified: 2019-11-04 23:10:06"),
])

meta_dictionary["/WpWpJJ_EWK-QCD_TuneCP5_13TeV-madgraph-pythia8/RunIIAutumn18NanoAODv6-Nano25Oct2019_102X_upgrade2018_realistic_v20-v1/NANOAODSIM"] =  OD([
  ("crab_string",           ""),
  ("sample_category",       "Rares"),
  ("process_name_specific", "WpWpJJ_EWK_QCD"),
  ("nof_db_events",         150000),
  ("nof_db_files",          2),
  ("fsize_db",              282363142),
  ("parent_db",             "/WpWpJJ_EWK-QCD_TuneCP5_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"),
  ("xsection",              0.04926),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 282.36MB; nevents: 150.00k; release: 10_2_18; last modified: 2019-11-10 09:27:52"),
])

meta_dictionary["/WWTo2L2Nu_DoubleScattering_13TeV-pythia8/RunIIAutumn18NanoAODv6-Nano25Oct2019_102X_upgrade2018_realistic_v20-v1/NANOAODSIM"] =  OD([
  ("crab_string",           ""),
  ("sample_category",       "Rares"),
  ("process_name_specific", "WWTo2L2Nu_DoubleScattering"),
  ("nof_db_events",         871500),
  ("nof_db_files",          2),
  ("fsize_db",              979769578),
  ("parent_db",             "/WWTo2L2Nu_DoubleScattering_13TeV-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"),
  ("xsection",              0.2232),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 979.77MB; nevents: 871.50k; release: 10_2_18; last modified: 2019-11-05 21:54:33"),
])

meta_dictionary["/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/RunIIAutumn18NanoAODv6-Nano25Oct2019_102X_upgrade2018_realistic_v20_ext1-v1/NANOAODSIM"] =  OD([
  ("crab_string",           ""),
  ("sample_category",       "Rares"),
  ("process_name_specific", "TTTT_ext1"),
  ("nof_db_events",         2359420),
  ("nof_db_files",          6),
  ("fsize_db",              7881341141),
  ("parent_db",             "/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext1-v2/MINIAODSIM"),
  ("xsection",              0.008213),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 7.88GB; nevents: 2.36M; release: 10_2_18; last modified: 2019-11-07 03:48:58"),
])

meta_dictionary["/TTTW_TuneCP5_13TeV-madgraph-pythia8/RunIIAutumn18NanoAODv6-Nano25Oct2019_102X_upgrade2018_realistic_v20_ext1-v1/NANOAODSIM"] =  OD([
  ("crab_string",           ""),
  ("sample_category",       "Rares"),
  ("process_name_specific", "TTTW_ext1"),
  ("nof_db_events",         200000),
  ("nof_db_files",          1),
  ("fsize_db",              581401135),
  ("parent_db",             "/TTTW_TuneCP5_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext1-v2/MINIAODSIM"),
  ("xsection",              0.000732),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 581.40MB; nevents: 200.00k; release: 10_2_18; last modified: 2019-11-06 14:06:12"),
])

meta_dictionary["/TTTJ_TuneCP5_13TeV-madgraph-pythia8/RunIIAutumn18NanoAODv6-Nano25Oct2019_102X_upgrade2018_realistic_v20_ext1-v1/NANOAODSIM"] =  OD([
  ("crab_string",           ""),
  ("sample_category",       "Rares"),
  ("process_name_specific", "TTTJ_ext1"),
  ("nof_db_events",         184000),
  ("nof_db_files",          2),
  ("fsize_db",              500099389),
  ("parent_db",             "/TTTJ_TuneCP5_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext1-v2/MINIAODSIM"),
  ("xsection",              0.000397),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 500.10MB; nevents: 184.00k; release: 10_2_18; last modified: 2019-11-07 03:37:58"),
])

meta_dictionary["/TTWZ_TuneCP5_13TeV-madgraph-pythia8/RunIIAutumn18NanoAODv6-Nano25Oct2019_102X_upgrade2018_realistic_v20_ext1-v1/NANOAODSIM"] =  OD([
  ("crab_string",           ""),
  ("sample_category",       "Rares"),
  ("process_name_specific", "TTWZ_ext1"),
  ("nof_db_events",         200000),
  ("nof_db_files",          1),
  ("fsize_db",              503556019),
  ("parent_db",             "/TTWZ_TuneCP5_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext1-v2/MINIAODSIM"),
  ("xsection",              0.003884),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 503.56MB; nevents: 200.00k; release: 10_2_18; last modified: 2019-11-06 23:23:01"),
])

meta_dictionary["/TTZZ_TuneCP5_13TeV-madgraph-pythia8/RunIIAutumn18NanoAODv6-Nano25Oct2019_102X_upgrade2018_realistic_v20_ext1-v1/NANOAODSIM"] =  OD([
  ("crab_string",           ""),
  ("sample_category",       "Rares"),
  ("process_name_specific", "TTZZ_ext1"),
  ("nof_db_events",         200000),
  ("nof_db_files",          1),
  ("fsize_db",              510448757),
  ("parent_db",             "/TTZZ_TuneCP5_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext1-v2/MINIAODSIM"),
  ("xsection",              0.001982),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 510.45MB; nevents: 200.00k; release: 10_2_18; last modified: 2019-11-07 20:02:46"),
])

meta_dictionary["/VHToNonbb_M125_13TeV_amcatnloFXFX_madspin_pythia8/RunIIAutumn18NanoAODv6-Nano25Oct2019_102X_upgrade2018_realistic_v20-v1/NANOAODSIM"] =  OD([
  ("crab_string",           ""),
  ("sample_category",       "VH"),
  ("process_name_specific", "VHToNonbb_M125"),
  ("nof_db_events",         1102578),
  ("nof_db_files",          2),
  ("fsize_db",              1715464431),
  ("parent_db",             "/VHToNonbb_M125_13TeV_amcatnloFXFX_madspin_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"),
  ("xsection",              0.9425),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 1.72GB; nevents: 1.10M; release: 10_2_18; last modified: 2019-11-09 18:10:31"),
])

meta_dictionary["/ZH_HToBB_ZToLL_M125_13TeV_powheg_pythia8/RunIIAutumn18NanoAODv6-Nano25Oct2019_102X_upgrade2018_realistic_v20-v1/NANOAODSIM"] =  OD([
  ("crab_string",           ""),
  ("sample_category",       "VH"),
  ("process_name_specific", "ZH_HToBB_ZToLL"),
  ("nof_db_events",         4743200),
  ("nof_db_files",          7),
  ("fsize_db",              8273896273),
  ("parent_db",             "/ZH_HToBB_ZToLL_M125_13TeV_powheg_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"),
  ("xsection",              0.05198),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 8.27GB; nevents: 4.74M; release: 10_2_18; last modified: 2019-11-04 20:02:11"),
])

meta_dictionary["/ZH_HToBB_ZToLL_M125_13TeV_powheg_pythia8/RunIIAutumn18NanoAODv6-Nano25Oct2019_102X_upgrade2018_realistic_v20_ext1-v1/NANOAODSIM"] =  OD([
  ("crab_string",           ""),
  ("sample_category",       "VH"),
  ("process_name_specific", "ZH_HToBB_ZToLL_ext1"),
  ("nof_db_events",         2222100),
  ("nof_db_files",          5),
  ("fsize_db",              3881099997),
  ("parent_db",             "/ZH_HToBB_ZToLL_M125_13TeV_powheg_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext1-v1/MINIAODSIM"),
  ("xsection",              0.05198),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 3.88GB; nevents: 2.22M; release: 10_2_18; last modified: 2019-11-08 12:48:15"),
])

meta_dictionary["/DYJetsToLL_M-10to50_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18NanoAODv6-Nano25Oct2019_102X_upgrade2018_realistic_v20-v1/NANOAODSIM"] =  OD([
  ("crab_string",           ""),
  ("sample_category",       "EWK"),
  ("process_name_specific", "DYJetsToLL_M-10to50"),
  ("nof_db_events",         39392062),
  ("nof_db_files",          29),
  ("fsize_db",              27681286216),
  ("parent_db",             "/DYJetsToLL_M-10to50_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"),
  ("xsection",              18610.0),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 27.68GB; nevents: 39.39M; release: 10_2_18; last modified: 2019-11-06 14:08:28"),
])

meta_dictionary["/DYJetsToLL_M-4to50_HT-70to100_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/RunIIAutumn18NanoAODv6-Nano25Oct2019_102X_upgrade2018_realistic_v20-v1/NANOAODSIM"] =  OD([
  ("crab_string",           ""),
  ("sample_category",       "EWK"),
  ("process_name_specific", "DYJetsToLL_M-4to50_HT-70to100_PSweights"),
  ("nof_db_events",         8893094),
  ("nof_db_files",          16),
  ("fsize_db",              11875266675),
  ("parent_db",             "/DYJetsToLL_M-4to50_HT-70to100_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"),
  ("xsection",              172.34),
  ("use_it",                False),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 11.88GB; nevents: 8.89M; release: 10_2_18; last modified: 2019-11-06 08:51:17"),
])

meta_dictionary["/DYJetsToLL_M-4to50_HT-100to200_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/RunIIAutumn18NanoAODv6-Nano25Oct2019_102X_upgrade2018_realistic_v20-v1/NANOAODSIM"] =  OD([
  ("crab_string",           ""),
  ("sample_category",       "EWK"),
  ("process_name_specific", "DYJetsToLL_M-4to50_HT-100to200_PSweights"),
  ("nof_db_events",         6794838),
  ("nof_db_files",          11),
  ("fsize_db",              8272051509),
  ("parent_db",             "/DYJetsToLL_M-4to50_HT-100to200_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"),
  ("xsection",              239.04),
  ("use_it",                False),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 8.27GB; nevents: 6.79M; release: 10_2_18; last modified: 2019-11-04 10:06:19"),
])

meta_dictionary["/DYJetsToLL_M-4to50_HT-200to400_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/RunIIAutumn18NanoAODv6-Nano25Oct2019_102X_upgrade2018_realistic_v20-v1/NANOAODSIM"] =  OD([
  ("crab_string",           ""),
  ("sample_category",       "EWK"),
  ("process_name_specific", "DYJetsToLL_M-4to50_HT-200to400_PSweights"),
  ("nof_db_events",         1939010),
  ("nof_db_files",          2),
  ("fsize_db",              2854883515),
  ("parent_db",             "/DYJetsToLL_M-4to50_HT-200to400_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"),
  ("xsection",              63.72),
  ("use_it",                False),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 2.85GB; nevents: 1.94M; release: 10_2_18; last modified: 2019-11-08 12:50:20"),
])

meta_dictionary["/DYJetsToLL_M-4to50_HT-400to600_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/RunIIAutumn18NanoAODv6-Nano25Oct2019_102X_upgrade2018_realistic_v20-v1/NANOAODSIM"] =  OD([
  ("crab_string",           ""),
  ("sample_category",       "EWK"),
  ("process_name_specific", "DYJetsToLL_M-4to50_HT-400to600_PSweights"),
  ("nof_db_events",         2008779),
  ("nof_db_files",          3),
  ("fsize_db",              3728860887),
  ("parent_db",             "/DYJetsToLL_M-4to50_HT-400to600_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"),
  ("xsection",              6.729),
  ("use_it",                False),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 3.73GB; nevents: 2.01M; release: 10_2_18; last modified: 2019-11-09 00:32:16"),
])

meta_dictionary["/DYJetsToLL_M-4to50_HT-600toInf_TuneCP5_PSWeights_13TeV-madgraphMLM-pythia8/RunIIAutumn18NanoAODv6-Nano25Oct2019_102X_upgrade2018_realistic_v20-v1/NANOAODSIM"] =  OD([
  ("crab_string",           ""),
  ("sample_category",       "EWK"),
  ("process_name_specific", "DYJetsToLL_M-4to50_HT-600toInf_PSWeights"),
  ("nof_db_events",         1975490),
  ("nof_db_files",          5),
  ("fsize_db",              4135167536),
  ("parent_db",             "/DYJetsToLL_M-4to50_HT-600toInf_TuneCP5_PSWeights_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"),
  ("xsection",              2.1692),
  ("use_it",                False),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 4.14GB; nevents: 1.98M; release: 10_2_18; last modified: 2019-11-07 20:00:26"),
])

meta_dictionary["/DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18NanoAODv6-Nano25Oct2019_102X_upgrade2018_realistic_v20-v1/NANOAODSIM"] =  OD([
  ("crab_string",           ""),
  ("sample_category",       "EWK"),
  ("process_name_specific", "DYJetsToLL_M-50"),
  ("nof_db_events",         100194597),
  ("nof_db_files",          58),
  ("fsize_db",              106274878918),
  ("parent_db",             "/DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"),
  ("xsection",              6077.22),
  ("use_it",                False),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 106.27GB; nevents: 100.19M; release: 10_2_18; last modified: 2019-11-16 11:09:56"),
])

meta_dictionary["/DYJetsToLL_M-50_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIIAutumn18NanoAODv6-Nano25Oct2019_102X_upgrade2018_realistic_v20-v1/NANOAODSIM"] =  OD([
  ("crab_string",           ""),
  ("sample_category",       "EWK"),
  ("process_name_specific", "DYJetsToLL_M-50_amcatnloFXFX"),
  ("nof_db_events",         997561),
  ("nof_db_files",          1),
  ("fsize_db",              1131714528),
  ("parent_db",             "/DYJetsToLL_M-50_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"),
  ("xsection",              6077.22),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 1.13GB; nevents: 997.56k; release: 10_2_18; last modified: 2019-11-07 10:43:53"),
])

meta_dictionary["/DYJetsToLL_M-50_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIIAutumn18NanoAODv6-Nano25Oct2019_102X_upgrade2018_realistic_v20_ext2-v1/NANOAODSIM"] =  OD([
  ("crab_string",           ""),
  ("sample_category",       "EWK"),
  ("process_name_specific", "DYJetsToLL_M-50_amcatnloFXFX_ext2"),
  ("nof_db_events",         193215674),
  ("nof_db_files",          143),
  ("fsize_db",              218975451817),
  ("parent_db",             "/DYJetsToLL_M-50_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext2-v1/MINIAODSIM"),
  ("xsection",              6077.22),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 218.98GB; nevents: 193.22M; release: 10_2_18; last modified: 2019-11-12 22:29:08"),
])

meta_dictionary["/DY1JetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18NanoAODv6-Nano25Oct2019_102X_upgrade2018_realistic_v20-v1/NANOAODSIM"] =  OD([
  ("crab_string",           ""),
  ("sample_category",       "EWK"),
  ("process_name_specific", "DY1JetsToLL_M-50"),
  ("nof_db_events",         68898175),
  ("nof_db_files",          64),
  ("fsize_db",              80404146078),
  ("parent_db",             "/DY1JetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"),
  ("xsection",              998.61),
  ("use_it",                False),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 80.40GB; nevents: 68.90M; release: 10_2_18; last modified: 2019-11-06 08:56:47"),
])

meta_dictionary["/DY2JetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18NanoAODv6-Nano25Oct2019_102X_upgrade2018_realistic_v20-v1/NANOAODSIM"] =  OD([
  ("crab_string",           ""),
  ("sample_category",       "EWK"),
  ("process_name_specific", "DY2JetsToLL_M-50"),
  ("nof_db_events",         20456037),
  ("nof_db_files",          15),
  ("fsize_db",              27271340726),
  ("parent_db",             "/DY2JetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"),
  ("xsection",              349.25),
  ("use_it",                False),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 27.27GB; nevents: 20.46M; release: 10_2_18; last modified: 2019-11-07 20:08:16"),
])

meta_dictionary["/DY3JetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18NanoAODv6-Nano25Oct2019_102X_upgrade2018_realistic_v20-v1/NANOAODSIM"] =  OD([
  ("crab_string",           ""),
  ("sample_category",       "EWK"),
  ("process_name_specific", "DY3JetsToLL_M-50"),
  ("nof_db_events",         5652357),
  ("nof_db_files",          7),
  ("fsize_db",              8544670474),
  ("parent_db",             "/DY3JetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"),
  ("xsection",              127.52),
  ("use_it",                False),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 8.54GB; nevents: 5.65M; release: 10_2_18; last modified: 2019-11-07 10:38:43"),
])

meta_dictionary["/DY4JetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18NanoAODv6-Nano25Oct2019_102X_upgrade2018_realistic_v20-v1/NANOAODSIM"] =  OD([
  ("crab_string",           ""),
  ("sample_category",       "EWK"),
  ("process_name_specific", "DY4JetsToLL_M-50"),
  ("nof_db_events",         2817812),
  ("nof_db_files",          8),
  ("fsize_db",              5074844419),
  ("parent_db",             "/DY4JetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"),
  ("xsection",              50.039),
  ("use_it",                False),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 5.07GB; nevents: 2.82M; release: 10_2_18; last modified: 2019-11-10 00:57:33"),
])

meta_dictionary["/DYJetsToLL_M-50_HT-70to100_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/RunIIAutumn18NanoAODv6-Nano25Oct2019_102X_upgrade2018_realistic_v20-v1/NANOAODSIM"] =  OD([
  ("crab_string",           ""),
  ("sample_category",       "EWK"),
  ("process_name_specific", "DYJetsToLL_M50_HT70to100_PSweights"),
  ("nof_db_events",         10019684),
  ("nof_db_files",          16),
  ("fsize_db",              13375184360),
  ("parent_db",             "/DYJetsToLL_M-50_HT-70to100_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"),
  ("xsection",              167.33),
  ("use_it",                False),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 13.38GB; nevents: 10.02M; release: 10_2_18; last modified: 2019-11-11 05:01:51"),
])

meta_dictionary["/DYJetsToLL_M-50_HT-100to200_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/RunIIAutumn18NanoAODv6-Nano25Oct2019_102X_upgrade2018_realistic_v20-v1/NANOAODSIM"] =  OD([
  ("crab_string",           ""),
  ("sample_category",       "EWK"),
  ("process_name_specific", "DYJetsToLL_M50_HT100to200_PSweights"),
  ("nof_db_events",         11530510),
  ("nof_db_files",          12),
  ("fsize_db",              17125800611),
  ("parent_db",             "/DYJetsToLL_M-50_HT-100to200_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"),
  ("xsection",              183.53),
  ("use_it",                False),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 17.13GB; nevents: 11.53M; release: 10_2_18; last modified: 2019-11-10 00:15:51"),
])

meta_dictionary["/DYJetsToLL_M-50_HT-200to400_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/RunIIAutumn18NanoAODv6-Nano25Oct2019_102X_upgrade2018_realistic_v20-v1/NANOAODSIM"] =  OD([
  ("crab_string",           ""),
  ("sample_category",       "EWK"),
  ("process_name_specific", "DYJetsToLL_M50_HT200to400_PSweights"),
  ("nof_db_events",         11225887),
  ("nof_db_files",          12),
  ("fsize_db",              20079024079),
  ("parent_db",             "/DYJetsToLL_M-50_HT-200to400_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"),
  ("xsection",              55.411),
  ("use_it",                False),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 20.08GB; nevents: 11.23M; release: 10_2_18; last modified: 2019-11-05 21:58:08"),
])

meta_dictionary["/DYJetsToLL_M-50_HT-400to600_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/RunIIAutumn18NanoAODv6-Nano25Oct2019_102X_upgrade2018_realistic_v20_ext2-v1/NANOAODSIM"] =  OD([
  ("crab_string",           ""),
  ("sample_category",       "EWK"),
  ("process_name_specific", "DYJetsToLL_M50_HT400to600_PSweights_ext2"),
  ("nof_db_events",         9358053),
  ("nof_db_files",          15),
  ("fsize_db",              20019480804),
  ("parent_db",             "/DYJetsToLL_M-50_HT-400to600_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext2-v3/MINIAODSIM"),
  ("xsection",              7.9592),
  ("use_it",                False),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 20.02GB; nevents: 9.36M; release: 10_2_18; last modified: 2019-11-10 00:41:57"),
])

meta_dictionary["/DYJetsToLL_M-50_HT-600to800_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/RunIIAutumn18NanoAODv6-Nano25Oct2019_102X_upgrade2018_realistic_v20-v1/NANOAODSIM"] =  OD([
  ("crab_string",           ""),
  ("sample_category",       "EWK"),
  ("process_name_specific", "DYJetsToLL_M50_HT600to800_PSweights"),
  ("nof_db_events",         8862104),
  ("nof_db_files",          13),
  ("fsize_db",              20540347698),
  ("parent_db",             "/DYJetsToLL_M-50_HT-600to800_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"),
  ("xsection",              2.0041),
  ("use_it",                False),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 20.54GB; nevents: 8.86M; release: 10_2_18; last modified: 2019-11-13 00:55:31"),
])

meta_dictionary["/DYJetsToLL_M-50_HT-800to1200_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/RunIIAutumn18NanoAODv6-Nano25Oct2019_102X_upgrade2018_realistic_v20-v1/NANOAODSIM"] =  OD([
  ("crab_string",           ""),
  ("sample_category",       "EWK"),
  ("process_name_specific", "DYJetsToLL_M50_HT800to1200_PSweights"),
  ("nof_db_events",         3138129),
  ("nof_db_files",          6),
  ("fsize_db",              7641141120),
  ("parent_db",             "/DYJetsToLL_M-50_HT-800to1200_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"),
  ("xsection",              0.92367),
  ("use_it",                False),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 7.64GB; nevents: 3.14M; release: 10_2_18; last modified: 2019-11-06 04:12:38"),
])

meta_dictionary["/DYJetsToLL_M-50_HT-1200to2500_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/RunIIAutumn18NanoAODv6-Nano25Oct2019_102X_upgrade2018_realistic_v20-v1/NANOAODSIM"] =  OD([
  ("crab_string",           ""),
  ("sample_category",       "EWK"),
  ("process_name_specific", "DYJetsToLL_M50_HT1200to2500_PSweights"),
  ("nof_db_events",         536416),
  ("nof_db_files",          2),
  ("fsize_db",              1378999396),
  ("parent_db",             "/DYJetsToLL_M-50_HT-1200to2500_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"),
  ("xsection",              0.22025),
  ("use_it",                False),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 1.38GB; nevents: 536.42k; release: 10_2_18; last modified: 2019-11-09 21:39:57"),
])

meta_dictionary["/DYJetsToLL_M-50_HT-2500toInf_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/RunIIAutumn18NanoAODv6-Nano25Oct2019_102X_upgrade2018_realistic_v20-v1/NANOAODSIM"] =  OD([
  ("crab_string",           ""),
  ("sample_category",       "EWK"),
  ("process_name_specific", "DYJetsToLL_M50_HT2500toInf_PSweights"),
  ("nof_db_events",         427051),
  ("nof_db_files",          2),
  ("fsize_db",              1176868719),
  ("parent_db",             "/DYJetsToLL_M-50_HT-2500toInf_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"),
  ("xsection",              0.004007),
  ("use_it",                False),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 1.18GB; nevents: 427.05k; release: 10_2_18; last modified: 2019-11-06 04:20:34"),
])

meta_dictionary["/DYBBJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18NanoAODv6-Nano25Oct2019_102X_upgrade2018_realistic_v20-v1/NANOAODSIM"] =  OD([
  ("crab_string",           ""),
  ("sample_category",       "EWK"),
  ("process_name_specific", "DYBBJetsToLL_M-50"),
  ("nof_db_events",         5039926),
  ("nof_db_files",          11),
  ("fsize_db",              8049675729),
  ("parent_db",             "/DYBBJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"),
  ("xsection",              14.6),
  ("use_it",                False),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 8.05GB; nevents: 5.04M; release: 10_2_18; last modified: 2019-11-16 09:13:17"),
])

meta_dictionary["/WJetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18NanoAODv6-Nano25Oct2019_102X_upgrade2018_realistic_v20-v1/NANOAODSIM"] =  OD([
  ("crab_string",           ""),
  ("sample_category",       "EWK"),
  ("process_name_specific", "WJetsToLNu_madgraphMLM"),
  ("nof_db_events",         70454125),
  ("nof_db_files",          50),
  ("fsize_db",              62105117099),
  ("parent_db",             "/WJetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"),
  ("xsection",              61526.7),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 62.11GB; nevents: 70.45M; release: 10_2_18; last modified: 2019-11-06 04:29:39"),
])

meta_dictionary["/W1JetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18NanoAODv6-Nano25Oct2019_102X_upgrade2018_realistic_v20-v1/NANOAODSIM"] =  OD([
  ("crab_string",           ""),
  ("sample_category",       "EWK"),
  ("process_name_specific", "W1JetsToLNu"),
  ("nof_db_events",         51082776),
  ("nof_db_files",          39),
  ("fsize_db",              50083170755),
  ("parent_db",             "/W1JetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"),
  ("xsection",              9442.49),
  ("use_it",                False),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 50.08GB; nevents: 51.08M; release: 10_2_18; last modified: 2019-11-09 00:13:36"),
])

meta_dictionary["/W2JetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18NanoAODv6-Nano25Oct2019_102X_upgrade2018_realistic_v20-v1/NANOAODSIM"] =  OD([
  ("crab_string",           ""),
  ("sample_category",       "EWK"),
  ("process_name_specific", "W2JetsToLNu"),
  ("nof_db_events",         23290710),
  ("nof_db_files",          22),
  ("fsize_db",              26490489412),
  ("parent_db",             "/W2JetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"),
  ("xsection",              3252.49),
  ("use_it",                False),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 26.49GB; nevents: 23.29M; release: 10_2_18; last modified: 2019-11-12 00:26:16"),
])

meta_dictionary["/W3JetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18NanoAODv6-Nano25Oct2019_102X_upgrade2018_realistic_v20-v1/NANOAODSIM"] =  OD([
  ("crab_string",           ""),
  ("sample_category",       "EWK"),
  ("process_name_specific", "W3JetsToLNu"),
  ("nof_db_events",         14508481),
  ("nof_db_files",          17),
  ("fsize_db",              18997547578),
  ("parent_db",             "/W3JetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"),
  ("xsection",              1153.42),
  ("use_it",                False),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 19.00GB; nevents: 14.51M; release: 10_2_18; last modified: 2019-11-09 18:09:56"),
])

meta_dictionary["/W4JetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18NanoAODv6-Nano25Oct2019_102X_upgrade2018_realistic_v20-v1/NANOAODSIM"] =  OD([
  ("crab_string",           ""),
  ("sample_category",       "EWK"),
  ("process_name_specific", "W4JetsToLNu"),
  ("nof_db_events",         10082747),
  ("nof_db_files",          11),
  ("fsize_db",              15933008980),
  ("parent_db",             "/W4JetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"),
  ("xsection",              634.05),
  ("use_it",                False),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 15.93GB; nevents: 10.08M; release: 10_2_18; last modified: 2019-11-07 03:42:23"),
])

meta_dictionary["/WJetsToLNu_HT-70To100_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18NanoAODv6-Nano25Oct2019_102X_upgrade2018_realistic_v20-v1/NANOAODSIM"] =  OD([
  ("crab_string",           ""),
  ("sample_category",       "EWK"),
  ("process_name_specific", "WJetsToLNu_HT70To100"),
  ("nof_db_events",         28084244),
  ("nof_db_files",          27),
  ("fsize_db",              32004519653),
  ("parent_db",             "/WJetsToLNu_HT-70To100_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"),
  ("xsection",              1504.92),
  ("use_it",                False),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 32.00GB; nevents: 28.08M; release: 10_2_18; last modified: 2019-11-06 14:13:29"),
])

meta_dictionary["/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18NanoAODv6-Nano25Oct2019_102X_upgrade2018_realistic_v20-v1/NANOAODSIM"] =  OD([
  ("crab_string",           ""),
  ("sample_category",       "EWK"),
  ("process_name_specific", "WJetsToLNu_HT100To200"),
  ("nof_db_events",         28370527),
  ("nof_db_files",          27),
  ("fsize_db",              36410187592),
  ("parent_db",             "/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"),
  ("xsection",              1625.08),
  ("use_it",                False),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 36.41GB; nevents: 28.37M; release: 10_2_18; last modified: 2019-11-12 22:30:21"),
])

meta_dictionary["/WJetsToLNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18NanoAODv6-Nano25Oct2019_102X_upgrade2018_realistic_v20-v1/NANOAODSIM"] =  OD([
  ("crab_string",           ""),
  ("sample_category",       "EWK"),
  ("process_name_specific", "WJetsToLNu_HT200To400"),
  ("nof_db_events",         25468933),
  ("nof_db_files",          36),
  ("fsize_db",              40024429592),
  ("parent_db",             "/WJetsToLNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"),
  ("xsection",              477.96),
  ("use_it",                False),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 40.02GB; nevents: 25.47M; release: 10_2_18; last modified: 2019-11-06 23:14:32"),
])

meta_dictionary["/WJetsToLNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18NanoAODv6-Nano25Oct2019_102X_upgrade2018_realistic_v20-v1/NANOAODSIM"] =  OD([
  ("crab_string",           ""),
  ("sample_category",       "EWK"),
  ("process_name_specific", "WJetsToLNu_HT400To600"),
  ("nof_db_events",         5932701),
  ("nof_db_files",          13),
  ("fsize_db",              11376838068),
  ("parent_db",             "/WJetsToLNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"),
  ("xsection",              67.441),
  ("use_it",                False),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 11.38GB; nevents: 5.93M; release: 10_2_18; last modified: 2019-11-13 01:09:58"),
])

meta_dictionary["/WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18NanoAODv6-Nano25Oct2019_102X_upgrade2018_realistic_v20-v1/NANOAODSIM"] =  OD([
  ("crab_string",           ""),
  ("sample_category",       "EWK"),
  ("process_name_specific", "WJetsToLNu_HT600To800"),
  ("nof_db_events",         19771294),
  ("nof_db_files",          28),
  ("fsize_db",              41410674516),
  ("parent_db",             "/WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"),
  ("xsection",              15.096),
  ("use_it",                False),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 41.41GB; nevents: 19.77M; release: 10_2_18; last modified: 2019-11-10 23:48:10"),
])

meta_dictionary["/WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18NanoAODv6-Nano25Oct2019_102X_upgrade2018_realistic_v20-v1/NANOAODSIM"] =  OD([
  ("crab_string",           ""),
  ("sample_category",       "EWK"),
  ("process_name_specific", "WJetsToLNu_HT800To1200"),
  ("nof_db_events",         8402687),
  ("nof_db_files",          18),
  ("fsize_db",              18631306255),
  ("parent_db",             "/WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"),
  ("xsection",              6.3626),
  ("use_it",                False),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 18.63GB; nevents: 8.40M; release: 10_2_18; last modified: 2019-11-13 01:11:48"),
])

meta_dictionary["/WJetsToLNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18NanoAODv6-Nano25Oct2019_102X_upgrade2018_realistic_v20-v1/NANOAODSIM"] =  OD([
  ("crab_string",           ""),
  ("sample_category",       "EWK"),
  ("process_name_specific", "WJetsToLNu_HT1200To2500"),
  ("nof_db_events",         7633949),
  ("nof_db_files",          17),
  ("fsize_db",              17906435905),
  ("parent_db",             "/WJetsToLNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"),
  ("xsection",              1.2658),
  ("use_it",                False),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 17.91GB; nevents: 7.63M; release: 10_2_18; last modified: 2019-11-13 15:53:23"),
])

meta_dictionary["/WJetsToLNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18NanoAODv6-Nano25Oct2019_102X_upgrade2018_realistic_v20-v1/NANOAODSIM"] =  OD([
  ("crab_string",           ""),
  ("sample_category",       "EWK"),
  ("process_name_specific", "WJetsToLNu_HT2500ToInf"),
  ("nof_db_events",         3273980),
  ("nof_db_files",          9),
  ("fsize_db",              8398542295),
  ("parent_db",             "/WJetsToLNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"),
  ("xsection",              0.009405),
  ("use_it",                False),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 8.40GB; nevents: 3.27M; release: 10_2_18; last modified: 2019-11-10 13:49:16"),
])

meta_dictionary["/WWTo2L2Nu_NNPDF31_TuneCP5_13TeV-powheg-pythia8/RunIIAutumn18NanoAODv6-Nano25Oct2019_102X_upgrade2018_realistic_v20-v1/NANOAODSIM"] =  OD([
  ("crab_string",           ""),
  ("sample_category",       "WW"),
  ("process_name_specific", "WWTo2L2Nu"),
  ("nof_db_events",         7758900),
  ("nof_db_files",          11),
  ("fsize_db",              9931066867),
  ("parent_db",             "/WWTo2L2Nu_NNPDF31_TuneCP5_13TeV-powheg-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"),
  ("xsection",              12.2),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 9.93GB; nevents: 7.76M; release: 10_2_18; last modified: 2019-11-13 01:14:53"),
])

meta_dictionary["/WWToLNuQQ_NNPDF31_TuneCP5_13TeV-powheg-pythia8/RunIIAutumn18NanoAODv6-Nano25Oct2019_102X_upgrade2018_realistic_v20-v1/NANOAODSIM"] =  OD([
  ("crab_string",           ""),
  ("sample_category",       "WW"),
  ("process_name_specific", "WWToLNuQQ"),
  ("nof_db_events",         19199100),
  ("nof_db_files",          18),
  ("fsize_db",              24865402193),
  ("parent_db",             "/WWToLNuQQ_NNPDF31_TuneCP5_13TeV-powheg-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"),
  ("xsection",              50.45),
  ("use_it",                False),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 24.87GB; nevents: 19.20M; release: 10_2_18; last modified: 2019-11-06 08:52:42"),
])

meta_dictionary["/WWTo1L1Nu2Q_13TeV_amcatnloFXFX_madspin_pythia8/RunIIAutumn18NanoAODv6-Nano25Oct2019_102X_upgrade2018_realistic_v20-v1/NANOAODSIM"] =  OD([
  ("crab_string",           ""),
  ("sample_category",       "WW"),
  ("process_name_specific", "WWTo1L1Nu2Q"),
  ("nof_db_events",         4683136),
  ("nof_db_files",          8),
  ("fsize_db",              6654988423),
  ("parent_db",             "/WWTo1L1Nu2Q_13TeV_amcatnloFXFX_madspin_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"),
  ("xsection",              50.45),
  ("use_it",                False),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 6.65GB; nevents: 4.68M; release: 10_2_18; last modified: 2019-11-11 20:51:30"),
])

meta_dictionary["/WWTo4Q_NNPDF31_TuneCP5_13TeV-powheg-pythia8/RunIIAutumn18NanoAODv6-Nano25Oct2019_102X_upgrade2018_realistic_v20-v1/NANOAODSIM"] =  OD([
  ("crab_string",           ""),
  ("sample_category",       "WW"),
  ("process_name_specific", "WWTo4Q"),
  ("nof_db_events",         3808800),
  ("nof_db_files",          6),
  ("fsize_db",              4818034221),
  ("parent_db",             "/WWTo4Q_NNPDF31_TuneCP5_13TeV-powheg-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"),
  ("xsection",              52.15),
  ("use_it",                False),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 4.82GB; nevents: 3.81M; release: 10_2_18; last modified: 2019-11-09 21:46:38"),
])

meta_dictionary["/WZTo3LNu_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIIAutumn18NanoAODv6-Nano25Oct2019_102X_upgrade2018_realistic_v20-v1/NANOAODSIM"] =  OD([
  ("crab_string",           ""),
  ("sample_category",       "WZ"),
  ("process_name_specific", "WZTo3LNu"),
  ("nof_db_events",         10749269),
  ("nof_db_files",          16),
  ("fsize_db",              14181154222),
  ("parent_db",             "/WZTo3LNu_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"),
  ("xsection",              4.43),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 14.18GB; nevents: 10.75M; release: 10_2_18; last modified: 2019-11-10 00:32:32"),
])

meta_dictionary["/WZTo3LNu_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIIAutumn18NanoAODv6-Nano25Oct2019_102X_upgrade2018_realistic_v20_ext1-v1/NANOAODSIM"] =  OD([
  ("crab_string",           ""),
  ("sample_category",       "WZ"),
  ("process_name_specific", "WZTo3LNu_ext1"),
  ("nof_db_events",         11248318),
  ("nof_db_files",          11),
  ("fsize_db",              14827183817),
  ("parent_db",             "/WZTo3LNu_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext1-v2/MINIAODSIM"),
  ("xsection",              4.43),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 14.83GB; nevents: 11.25M; release: 10_2_18; last modified: 2019-11-10 09:45:20"),
])

meta_dictionary["/WZTo3LNu_TuneCP5_13TeV-powheg-pythia8/RunIIAutumn18NanoAODv6-Nano25Oct2019_102X_upgrade2018_realistic_v20_ext1-v1/NANOAODSIM"] =  OD([
  ("crab_string",           ""),
  ("sample_category",       "WZ"),
  ("process_name_specific", "WZTo3LNu_powheg_ext1"),
  ("nof_db_events",         1976600),
  ("nof_db_files",          6),
  ("fsize_db",              2481678247),
  ("parent_db",             "/WZTo3LNu_TuneCP5_13TeV-powheg-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext1-v2/MINIAODSIM"),
  ("xsection",              4.43),
  ("use_it",                False),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 2.48GB; nevents: 1.98M; release: 10_2_18; last modified: 2019-11-13 01:13:38"),
])

meta_dictionary["/WZTo3LNu_0Jets_MLL-4to50_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18NanoAODv6-Nano25Oct2019_102X_upgrade2018_realistic_v20-v1/NANOAODSIM"] =  OD([
  ("crab_string",           ""),
  ("sample_category",       "WZ"),
  ("process_name_specific", "WZTo3LNu_0Jets_MLL-4to50"),
  ("nof_db_events",         549864),
  ("nof_db_files",          3),
  ("fsize_db",              559187138),
  ("parent_db",             "/WZTo3LNu_0Jets_MLL-4to50_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"),
  ("xsection",              2.3986),
  ("use_it",                False),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 559.19MB; nevents: 549.86k; release: 10_2_18; last modified: 2019-11-10 09:28:53"),
])

meta_dictionary["/WZTo3LNu_0Jets_MLL-50_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18NanoAODv6-Nano25Oct2019_102X_upgrade2018_realistic_v20-v1/NANOAODSIM"] =  OD([
  ("crab_string",           ""),
  ("sample_category",       "WZ"),
  ("process_name_specific", "WZTo3LNu_0Jets_MLL-50"),
  ("nof_db_events",         496707),
  ("nof_db_files",          2),
  ("fsize_db",              663080415),
  ("parent_db",             "/WZTo3LNu_0Jets_MLL-50_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"),
  ("xsection",              0.6067),
  ("use_it",                False),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 663.08MB; nevents: 496.71k; release: 10_2_18; last modified: 2019-11-09 05:02:32"),
])

meta_dictionary["/WZTo3LNu_1Jets_MLL-4to50_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18NanoAODv6-Nano25Oct2019_102X_upgrade2018_realistic_v20-v1/NANOAODSIM"] =  OD([
  ("crab_string",           ""),
  ("sample_category",       "WZ"),
  ("process_name_specific", "WZTo3LNu_1Jets_MLL-4to50"),
  ("nof_db_events",         504010),
  ("nof_db_files",          4),
  ("fsize_db",              638458422),
  ("parent_db",             "/WZTo3LNu_1Jets_MLL-4to50_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"),
  ("xsection",              0.46107),
  ("use_it",                False),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 638.46MB; nevents: 504.01k; release: 10_2_18; last modified: 2019-11-13 00:46:50"),
])

meta_dictionary["/WZTo3LNu_1Jets_MLL-50_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18NanoAODv6-Nano25Oct2019_102X_upgrade2018_realistic_v20-v1/NANOAODSIM"] =  OD([
  ("crab_string",           ""),
  ("sample_category",       "WZ"),
  ("process_name_specific", "WZTo3LNu_1Jets_MLL-50"),
  ("nof_db_events",         497831),
  ("nof_db_files",          2),
  ("fsize_db",              798498568),
  ("parent_db",             "/WZTo3LNu_1Jets_MLL-50_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"),
  ("xsection",              0.3226),
  ("use_it",                False),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 798.50MB; nevents: 497.83k; release: 10_2_18; last modified: 2019-11-10 00:57:48"),
])

meta_dictionary["/WZTo3LNu_2Jets_MLL-4to50_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18NanoAODv6-Nano25Oct2019_102X_upgrade2018_realistic_v20-v1/NANOAODSIM"] =  OD([
  ("crab_string",           ""),
  ("sample_category",       "WZ"),
  ("process_name_specific", "WZTo3LNu_2Jets_MLL-4to50"),
  ("nof_db_events",         1409762),
  ("nof_db_files",          3),
  ("fsize_db",              2112601911),
  ("parent_db",             "/WZTo3LNu_2Jets_MLL-4to50_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"),
  ("xsection",              0.15607),
  ("use_it",                False),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 2.11GB; nevents: 1.41M; release: 10_2_18; last modified: 2019-11-11 15:52:01"),
])

meta_dictionary["/WZTo3LNu_2Jets_MLL-50_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18NanoAODv6-Nano25Oct2019_102X_upgrade2018_realistic_v20-v1/NANOAODSIM"] =  OD([
  ("crab_string",           ""),
  ("sample_category",       "WZ"),
  ("process_name_specific", "WZTo3LNu_2Jets_MLL-50"),
  ("nof_db_events",         1855668),
  ("nof_db_files",          5),
  ("fsize_db",              3543263933),
  ("parent_db",             "/WZTo3LNu_2Jets_MLL-50_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"),
  ("xsection",              0.06314),
  ("use_it",                False),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 3.54GB; nevents: 1.86M; release: 10_2_18; last modified: 2019-11-09 21:40:17"),
])

meta_dictionary["/WZTo3LNu_3Jets_MLL-4to50_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18NanoAODv6-Nano25Oct2019_102X_upgrade2018_realistic_v20-v1/NANOAODSIM"] =  OD([
  ("crab_string",           ""),
  ("sample_category",       "WZ"),
  ("process_name_specific", "WZTo3LNu_3Jets_MLL-4to50"),
  ("nof_db_events",         2160519),
  ("nof_db_files",          5),
  ("fsize_db",              3970156601),
  ("parent_db",             "/WZTo3LNu_3Jets_MLL-4to50_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"),
  ("xsection",              0.06769),
  ("use_it",                False),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 3.97GB; nevents: 2.16M; release: 10_2_18; last modified: 2019-11-10 00:50:58"),
])

meta_dictionary["/WZTo3LNu_3Jets_MLL-50_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18NanoAODv6-Nano25Oct2019_102X_upgrade2018_realistic_v20-v1/NANOAODSIM"] =  OD([
  ("crab_string",           ""),
  ("sample_category",       "WZ"),
  ("process_name_specific", "WZTo3LNu_3Jets_MLL-50"),
  ("nof_db_events",         1788755),
  ("nof_db_files",          5),
  ("fsize_db",              3992350176),
  ("parent_db",             "/WZTo3LNu_3Jets_MLL-50_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"),
  ("xsection",              0.090512),
  ("use_it",                False),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 3.99GB; nevents: 1.79M; release: 10_2_18; last modified: 2019-11-10 19:53:43"),
])

meta_dictionary["/WZTo2L2Q_13TeV_amcatnloFXFX_madspin_pythia8/RunIIAutumn18NanoAODv6-Nano25Oct2019_102X_upgrade2018_realistic_v20-v1/NANOAODSIM"] =  OD([
  ("crab_string",           ""),
  ("sample_category",       "WZ"),
  ("process_name_specific", "WZTo2L2Q"),
  ("nof_db_events",         28193648),
  ("nof_db_files",          25),
  ("fsize_db",              41008169433),
  ("parent_db",             "/WZTo2L2Q_13TeV_amcatnloFXFX_madspin_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"),
  ("xsection",              5.6),
  ("use_it",                False),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 41.01GB; nevents: 28.19M; release: 10_2_18; last modified: 2019-11-06 14:14:33"),
])

meta_dictionary["/WZTo1L1Nu2Q_13TeV_amcatnloFXFX_madspin_pythia8/RunIIAutumn18NanoAODv6-Nano25Oct2019_102X_upgrade2018_realistic_v20-v1/NANOAODSIM"] =  OD([
  ("crab_string",           ""),
  ("sample_category",       "WZ"),
  ("process_name_specific", "WZTo1L1Nu2Q"),
  ("nof_db_events",         18901469),
  ("nof_db_files",          22),
  ("fsize_db",              27193289426),
  ("parent_db",             "/WZTo1L1Nu2Q_13TeV_amcatnloFXFX_madspin_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"),
  ("xsection",              10.71),
  ("use_it",                False),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 27.19GB; nevents: 18.90M; release: 10_2_18; last modified: 2019-11-10 09:44:51"),
])

meta_dictionary["/ZZTo4L_TuneCP5_13TeV_powheg_pythia8/RunIIAutumn18NanoAODv6-Nano25Oct2019_102X_upgrade2018_realistic_v20_ext1-v1/NANOAODSIM"] =  OD([
  ("crab_string",           ""),
  ("sample_category",       "ZZ"),
  ("process_name_specific", "ZZTo4L_ext1"),
  ("nof_db_events",         6689900),
  ("nof_db_files",          8),
  ("fsize_db",              8214393939),
  ("parent_db",             "/ZZTo4L_TuneCP5_13TeV_powheg_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext1-v2/MINIAODSIM"),
  ("xsection",              1.256),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 8.21GB; nevents: 6.69M; release: 10_2_18; last modified: 2019-11-06 23:26:11"),
])

meta_dictionary["/ZZTo4L_TuneCP5_13TeV_powheg_pythia8/RunIIAutumn18NanoAODv6-Nano25Oct2019_102X_upgrade2018_realistic_v20_ext2-v1/NANOAODSIM"] =  OD([
  ("crab_string",           ""),
  ("sample_category",       "ZZ"),
  ("process_name_specific", "ZZTo4L_ext2"),
  ("nof_db_events",         98613000),
  ("nof_db_files",          71),
  ("fsize_db",              120899734618),
  ("parent_db",             "/ZZTo4L_TuneCP5_13TeV_powheg_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext2-v2/MINIAODSIM"),
  ("xsection",              1.256),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 120.90GB; nevents: 98.61M; release: 10_2_18; last modified: 2019-11-10 00:37:02"),
])

meta_dictionary["/ZZTo2L2Nu_TuneCP5_13TeV_powheg_pythia8/RunIIAutumn18NanoAODv6-Nano25Oct2019_102X_upgrade2018_realistic_v20_ext1-v1/NANOAODSIM"] =  OD([
  ("crab_string",           ""),
  ("sample_category",       "ZZ"),
  ("process_name_specific", "ZZTo2L2Nu_ext1"),
  ("nof_db_events",         8382600),
  ("nof_db_files",          11),
  ("fsize_db",              10740000144),
  ("parent_db",             "/ZZTo2L2Nu_TuneCP5_13TeV_powheg_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext1-v2/MINIAODSIM"),
  ("xsection",              0.564),
  ("use_it",                False),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 10.74GB; nevents: 8.38M; release: 10_2_18; last modified: 2019-11-09 14:31:19"),
])

meta_dictionary["/ZZTo2L2Nu_TuneCP5_13TeV_powheg_pythia8/RunIIAutumn18NanoAODv6-Nano25Oct2019_102X_upgrade2018_realistic_v20_ext2-v1/NANOAODSIM"] =  OD([
  ("crab_string",           ""),
  ("sample_category",       "ZZ"),
  ("process_name_specific", "ZZTo2L2Nu_ext2"),
  ("nof_db_events",         48046000),
  ("nof_db_files",          38),
  ("fsize_db",              61500928714),
  ("parent_db",             "/ZZTo2L2Nu_TuneCP5_13TeV_powheg_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext2-v2/MINIAODSIM"),
  ("xsection",              0.564),
  ("use_it",                False),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 61.50GB; nevents: 48.05M; release: 10_2_18; last modified: 2019-11-10 00:33:57"),
])

meta_dictionary["/ZZTo2L2Q_13TeV_amcatnloFXFX_madspin_pythia8/RunIIAutumn18NanoAODv6-Nano25Oct2019_102X_upgrade2018_realistic_v20-v1/NANOAODSIM"] =  OD([
  ("crab_string",           ""),
  ("sample_category",       "ZZ"),
  ("process_name_specific", "ZZTo2L2Q"),
  ("nof_db_events",         27900469),
  ("nof_db_files",          24),
  ("fsize_db",              40886905434),
  ("parent_db",             "/ZZTo2L2Q_13TeV_amcatnloFXFX_madspin_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"),
  ("xsection",              5.52),
  ("use_it",                False),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 40.89GB; nevents: 27.90M; release: 10_2_18; last modified: 2019-11-09 14:10:57"),
])

meta_dictionary["/QCD_Pt_15to20_bcToE_TuneCP5_13TeV_pythia8/RunIIAutumn18NanoAODv6-Nano25Oct2019_102X_upgrade2018_realistic_v20-v1/NANOAODSIM"] =  OD([
  ("crab_string",           ""),
  ("sample_category",       "QCD"),
  ("process_name_specific", "QCD_Pt15to20_bcToE"),
  ("nof_db_events",         4316068),
  ("nof_db_files",          4),
  ("fsize_db",              3667759751),
  ("parent_db",             "/QCD_Pt_15to20_bcToE_TuneCP5_13TeV_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"),
  ("xsection",              186900.0),
  ("use_it",                False),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 3.67GB; nevents: 4.32M; release: 10_2_18; last modified: 2019-11-10 09:43:35"),
])

meta_dictionary["/QCD_Pt_20to30_bcToE_TuneCP5_13TeV_pythia8/RunIIAutumn18NanoAODv6-Nano25Oct2019_102X_upgrade2018_realistic_v20-v1/NANOAODSIM"] =  OD([
  ("crab_string",           ""),
  ("sample_category",       "QCD"),
  ("process_name_specific", "QCD_Pt20to30_bcToE"),
  ("nof_db_events",         10561226),
  ("nof_db_files",          11),
  ("fsize_db",              9582231521),
  ("parent_db",             "/QCD_Pt_20to30_bcToE_TuneCP5_13TeV_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"),
  ("xsection",              305400.0),
  ("use_it",                False),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 9.58GB; nevents: 10.56M; release: 10_2_18; last modified: 2019-11-10 09:30:33"),
])

meta_dictionary["/QCD_Pt_30to80_bcToE_TuneCP5_13TeV_pythia8/RunIIAutumn18NanoAODv6-Nano25Oct2019_102X_upgrade2018_realistic_v20-v1/NANOAODSIM"] =  OD([
  ("crab_string",           ""),
  ("sample_category",       "QCD"),
  ("process_name_specific", "QCD_Pt30to80_bcToE"),
  ("nof_db_events",         15177630),
  ("nof_db_files",          19),
  ("fsize_db",              15565787544),
  ("parent_db",             "/QCD_Pt_30to80_bcToE_TuneCP5_13TeV_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"),
  ("xsection",              361100.0),
  ("use_it",                False),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 15.57GB; nevents: 15.18M; release: 10_2_18; last modified: 2019-11-11 04:59:54"),
])

meta_dictionary["/QCD_Pt_80to170_bcToE_TuneCP5_13TeV_pythia8/RunIIAutumn18NanoAODv6-Nano25Oct2019_102X_upgrade2018_realistic_v20-v1/NANOAODSIM"] =  OD([
  ("crab_string",           ""),
  ("sample_category",       "QCD"),
  ("process_name_specific", "QCD_Pt80to170_bcToE"),
  ("nof_db_events",         14934946),
  ("nof_db_files",          23),
  ("fsize_db",              18669335488),
  ("parent_db",             "/QCD_Pt_80to170_bcToE_TuneCP5_13TeV_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"),
  ("xsection",              33820.0),
  ("use_it",                False),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 18.67GB; nevents: 14.93M; release: 10_2_18; last modified: 2019-11-07 10:38:08"),
])

meta_dictionary["/QCD_Pt_170to250_bcToE_TuneCP5_13TeV_pythia8/RunIIAutumn18NanoAODv6-Nano25Oct2019_102X_upgrade2018_realistic_v20-v1/NANOAODSIM"] =  OD([
  ("crab_string",           ""),
  ("sample_category",       "QCD"),
  ("process_name_specific", "QCD_Pt170to250_bcToE"),
  ("nof_db_events",         9654492),
  ("nof_db_files",          17),
  ("fsize_db",              15279971417),
  ("parent_db",             "/QCD_Pt_170to250_bcToE_TuneCP5_13TeV_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"),
  ("xsection",              2130.0),
  ("use_it",                False),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 15.28GB; nevents: 9.65M; release: 10_2_18; last modified: 2019-11-06 23:19:36"),
])

meta_dictionary["/QCD_Pt_250toInf_bcToE_TuneCP5_13TeV_pythia8/RunIIAutumn18NanoAODv6-Nano25Oct2019_102X_upgrade2018_realistic_v20-v1/NANOAODSIM"] =  OD([
  ("crab_string",           ""),
  ("sample_category",       "QCD"),
  ("process_name_specific", "QCD_Pt250toInf_bcToE"),
  ("nof_db_events",         10191317),
  ("nof_db_files",          16),
  ("fsize_db",              18368443723),
  ("parent_db",             "/QCD_Pt_250toInf_bcToE_TuneCP5_13TeV_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"),
  ("xsection",              563.0),
  ("use_it",                False),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 18.37GB; nevents: 10.19M; release: 10_2_18; last modified: 2019-11-10 14:03:08"),
])

meta_dictionary["/QCD_Pt-15to20_EMEnriched_TuneCP5_13TeV_pythia8/RunIIAutumn18NanoAODv6-Nano25Oct2019_102X_upgrade2018_realistic_v20_ext1-v1/NANOAODSIM"] =  OD([
  ("crab_string",           ""),
  ("sample_category",       "QCD"),
  ("process_name_specific", "QCD_Pt15to20_EMEnriched_ext1"),
  ("nof_db_events",         14578212),
  ("nof_db_files",          11),
  ("fsize_db",              10981110481),
  ("parent_db",             "/QCD_Pt-15to20_EMEnriched_TuneCP5_13TeV_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext1-v2/MINIAODSIM"),
  ("xsection",              1324000.0),
  ("use_it",                False),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 10.98GB; nevents: 14.58M; release: 10_2_18; last modified: 2019-11-14 03:55:35"),
])

meta_dictionary["/QCD_Pt-20to30_EMEnriched_TuneCP5_13TeV_pythia8/RunIIAutumn18NanoAODv6-Nano25Oct2019_102X_upgrade2018_realistic_v20-v1/NANOAODSIM"] =  OD([
  ("crab_string",           ""),
  ("sample_category",       "QCD"),
  ("process_name_specific", "QCD_Pt20to30_EMEnriched"),
  ("nof_db_events",         14255377),
  ("nof_db_files",          9),
  ("fsize_db",              11272031564),
  ("parent_db",             "/QCD_Pt-20to30_EMEnriched_TuneCP5_13TeV_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"),
  ("xsection",              4912000.0),
  ("use_it",                False),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 11.27GB; nevents: 14.26M; release: 10_2_18; last modified: 2019-11-10 18:00:48"),
])

meta_dictionary["/QCD_Pt-30to50_EMEnriched_TuneCP5_13TeV_pythia8/RunIIAutumn18NanoAODv6-Nano25Oct2019_102X_upgrade2018_realistic_v20_ext1-v1/NANOAODSIM"] =  OD([
  ("crab_string",           ""),
  ("sample_category",       "QCD"),
  ("process_name_specific", "QCD_Pt30to50_EMEnriched_ext1"),
  ("nof_db_events",         15086084),
  ("nof_db_files",          11),
  ("fsize_db",              12750648076),
  ("parent_db",             "/QCD_Pt-30to50_EMEnriched_TuneCP5_13TeV_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext1-v2/MINIAODSIM"),
  ("xsection",              6420000.0),
  ("use_it",                False),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 12.75GB; nevents: 15.09M; release: 10_2_18; last modified: 2019-11-10 11:49:04"),
])

meta_dictionary["/QCD_Pt-50to80_EMEnriched_TuneCP5_13TeV_pythia8/RunIIAutumn18NanoAODv6-Nano25Oct2019_102X_upgrade2018_realistic_v20-v1/NANOAODSIM"] =  OD([
  ("crab_string",           ""),
  ("sample_category",       "QCD"),
  ("process_name_specific", "QCD_Pt50to80_EMEnriched"),
  ("nof_db_events",         10798233),
  ("nof_db_files",          8),
  ("fsize_db",              9995645743),
  ("parent_db",             "/QCD_Pt-50to80_EMEnriched_TuneCP5_13TeV_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"),
  ("xsection",              1988000.0),
  ("use_it",                False),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 10.00GB; nevents: 10.80M; release: 10_2_18; last modified: 2019-11-13 15:43:39"),
])

meta_dictionary["/QCD_Pt-80to120_EMEnriched_TuneCP5_13TeV_pythia8/RunIIAutumn18NanoAODv6-Nano25Oct2019_102X_upgrade2018_realistic_v20-v1/NANOAODSIM"] =  OD([
  ("crab_string",           ""),
  ("sample_category",       "QCD"),
  ("process_name_specific", "QCD_Pt80to120_EMEnriched"),
  ("nof_db_events",         9648791),
  ("nof_db_files",          9),
  ("fsize_db",              10061320063),
  ("parent_db",             "/QCD_Pt-80to120_EMEnriched_TuneCP5_13TeV_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"),
  ("xsection",              366500.0),
  ("use_it",                False),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 10.06GB; nevents: 9.65M; release: 10_2_18; last modified: 2019-11-10 18:04:18"),
])

meta_dictionary["/QCD_Pt-120to170_EMEnriched_TuneCP5_13TeV_pythia8/RunIIAutumn18NanoAODv6-Nano25Oct2019_102X_upgrade2018_realistic_v20-v1/NANOAODSIM"] =  OD([
  ("crab_string",           ""),
  ("sample_category",       "QCD"),
  ("process_name_specific", "QCD_Pt120to170_EMEnriched"),
  ("nof_db_events",         9964143),
  ("nof_db_files",          11),
  ("fsize_db",              11976961321),
  ("parent_db",             "/QCD_Pt-120to170_EMEnriched_TuneCP5_13TeV_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"),
  ("xsection",              66510.0),
  ("use_it",                False),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 11.98GB; nevents: 9.96M; release: 10_2_18; last modified: 2019-11-07 03:43:33"),
])

meta_dictionary["/QCD_Pt-170to300_EMEnriched_TuneCP5_13TeV_pythia8/RunIIAutumn18NanoAODv6-Nano25Oct2019_102X_upgrade2018_realistic_v20-v1/NANOAODSIM"] =  OD([
  ("crab_string",           ""),
  ("sample_category",       "QCD"),
  ("process_name_specific", "QCD_Pt170to300_EMEnriched"),
  ("nof_db_events",         3712174),
  ("nof_db_files",          4),
  ("fsize_db",              5379172635),
  ("parent_db",             "/QCD_Pt-170to300_EMEnriched_TuneCP5_13TeV_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"),
  ("xsection",              16560.0),
  ("use_it",                False),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 5.38GB; nevents: 3.71M; release: 10_2_18; last modified: 2019-11-10 15:55:47"),
])

meta_dictionary["/QCD_Pt-300toInf_EMEnriched_TuneCP5_13TeV_pythia8/RunIIAutumn18NanoAODv6-Nano25Oct2019_102X_upgrade2018_realistic_v20-v1/NANOAODSIM"] =  OD([
  ("crab_string",           ""),
  ("sample_category",       "QCD"),
  ("process_name_specific", "QCD_Pt300toInf_EMEnriched"),
  ("nof_db_events",         2901355),
  ("nof_db_files",          8),
  ("fsize_db",              4890669255),
  ("parent_db",             "/QCD_Pt-300toInf_EMEnriched_TuneCP5_13TeV_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"),
  ("xsection",              1100.0),
  ("use_it",                False),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 4.89GB; nevents: 2.90M; release: 10_2_18; last modified: 2019-11-13 01:24:13"),
])

meta_dictionary["/QCD_Pt-15to20_MuEnrichedPt5_TuneCP5_13TeV_pythia8/RunIIAutumn18NanoAODv6-Nano25Oct2019_102X_upgrade2018_realistic_v20-v1/NANOAODSIM"] =  OD([
  ("crab_string",           ""),
  ("sample_category",       "QCD"),
  ("process_name_specific", "QCD_Pt15to20_Mu5"),
  ("nof_db_events",         4576065),
  ("nof_db_files",          10),
  ("fsize_db",              4571527790),
  ("parent_db",             "/QCD_Pt-15to20_MuEnrichedPt5_TuneCP5_13TeV_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v3/MINIAODSIM"),
  ("xsection",              2811000.0),
  ("use_it",                False),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 4.57GB; nevents: 4.58M; release: 10_2_18; last modified: 2019-11-15 23:55:18"),
])

meta_dictionary["/QCD_Pt-20to30_MuEnrichedPt5_TuneCP5_13TeV_pythia8/RunIIAutumn18NanoAODv6-Nano25Oct2019_102X_upgrade2018_realistic_v20-v1/NANOAODSIM"] =  OD([
  ("crab_string",           ""),
  ("sample_category",       "QCD"),
  ("process_name_specific", "QCD_Pt20to30_Mu5"),
  ("nof_db_events",         30612338),
  ("nof_db_files",          24),
  ("fsize_db",              32332946870),
  ("parent_db",             "/QCD_Pt-20to30_MuEnrichedPt5_TuneCP5_13TeV_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v4/MINIAODSIM"),
  ("xsection",              2531000.0),
  ("use_it",                False),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 32.33GB; nevents: 30.61M; release: 10_2_18; last modified: 2019-11-13 19:50:36"),
])

meta_dictionary["/QCD_Pt-30to50_MuEnrichedPt5_TuneCP5_13TeV_pythia8/RunIIAutumn18NanoAODv6-Nano25Oct2019_102X_upgrade2018_realistic_v20-v1/NANOAODSIM"] =  OD([
  ("crab_string",           ""),
  ("sample_category",       "QCD"),
  ("process_name_specific", "QCD_Pt30to50_Mu5"),
  ("nof_db_events",         29884616),
  ("nof_db_files",          29),
  ("fsize_db",              34609208874),
  ("parent_db",             "/QCD_Pt-30to50_MuEnrichedPt5_TuneCP5_13TeV_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v3/MINIAODSIM"),
  ("xsection",              1367000.0),
  ("use_it",                False),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 34.61GB; nevents: 29.88M; release: 10_2_18; last modified: 2019-11-07 07:32:23"),
])

meta_dictionary["/QCD_Pt-50to80_MuEnrichedPt5_TuneCP5_13TeV_pythia8/RunIIAutumn18NanoAODv6-Nano25Oct2019_102X_upgrade2018_realistic_v20-v1/NANOAODSIM"] =  OD([
  ("crab_string",           ""),
  ("sample_category",       "QCD"),
  ("process_name_specific", "QCD_Pt50to80_Mu5"),
  ("nof_db_events",         20268872),
  ("nof_db_files",          26),
  ("fsize_db",              25976092360),
  ("parent_db",             "/QCD_Pt-50to80_MuEnrichedPt5_TuneCP5_13TeV_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v3/MINIAODSIM"),
  ("xsection",              377900.0),
  ("use_it",                False),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 25.98GB; nevents: 20.27M; release: 10_2_18; last modified: 2019-11-06 14:12:16"),
])

meta_dictionary["/QCD_Pt-80to120_MuEnrichedPt5_TuneCP5_13TeV_pythia8/RunIIAutumn18NanoAODv6-Nano25Oct2019_102X_upgrade2018_realistic_v20-v1/NANOAODSIM"] =  OD([
  ("crab_string",           ""),
  ("sample_category",       "QCD"),
  ("process_name_specific", "QCD_Pt80to120_Mu5"),
  ("nof_db_events",         612919),
  ("nof_db_files",          2),
  ("fsize_db",              873739459),
  ("parent_db",             "/QCD_Pt-80to120_MuEnrichedPt5_TuneCP5_13TeV_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"),
  ("xsection",              88620.0),
  ("use_it",                False),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 873.74MB; nevents: 612.92k; release: 10_2_18; last modified: 2019-11-10 19:52:28"),
])

meta_dictionary["/QCD_Pt-80to120_MuEnrichedPt5_TuneCP5_13TeV_pythia8/RunIIAutumn18NanoAODv6-Nano25Oct2019_102X_upgrade2018_realistic_v20_ext1-v1/NANOAODSIM"] =  OD([
  ("crab_string",           ""),
  ("sample_category",       "QCD"),
  ("process_name_specific", "QCD_Pt80to120_Mu5_ext1"),
  ("nof_db_events",         25039361),
  ("nof_db_files",          25),
  ("fsize_db",              35515548461),
  ("parent_db",             "/QCD_Pt-80to120_MuEnrichedPt5_TuneCP5_13TeV_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext1-v2/MINIAODSIM"),
  ("xsection",              88620.0),
  ("use_it",                False),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 35.52GB; nevents: 25.04M; release: 10_2_18; last modified: 2019-11-15 13:56:51"),
])

meta_dictionary["/QCD_Pt-120to170_MuEnrichedPt5_TuneCP5_13TeV_pythia8/RunIIAutumn18NanoAODv6-Nano25Oct2019_102X_upgrade2018_realistic_v20-v1/NANOAODSIM"] =  OD([
  ("crab_string",           ""),
  ("sample_category",       "QCD"),
  ("process_name_specific", "QCD_Pt120to170_Mu5"),
  ("nof_db_events",         633668),
  ("nof_db_files",          2),
  ("fsize_db",              1014460605),
  ("parent_db",             "/QCD_Pt-120to170_MuEnrichedPt5_TuneCP5_13TeV_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"),
  ("xsection",              21190.0),
  ("use_it",                False),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 1.01GB; nevents: 633.67k; release: 10_2_18; last modified: 2019-11-06 04:27:18"),
])

meta_dictionary["/QCD_Pt-120to170_MuEnrichedPt5_TuneCP5_13TeV_pythia8/RunIIAutumn18NanoAODv6-Nano25Oct2019_102X_upgrade2018_realistic_v20_ext1-v1/NANOAODSIM"] =  OD([
  ("crab_string",           ""),
  ("sample_category",       "QCD"),
  ("process_name_specific", "QCD_Pt120to170_Mu5_ext1"),
  ("nof_db_events",         20682254),
  ("nof_db_files",          22),
  ("fsize_db",              32977417373),
  ("parent_db",             "/QCD_Pt-120to170_MuEnrichedPt5_TuneCP5_13TeV_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext1-v2/MINIAODSIM"),
  ("xsection",              21190.0),
  ("use_it",                False),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 32.98GB; nevents: 20.68M; release: 10_2_18; last modified: 2019-11-10 23:48:05"),
])

meta_dictionary["/QCD_Pt-170to300_MuEnrichedPt5_TuneCP5_13TeV_pythia8/RunIIAutumn18NanoAODv6-Nano25Oct2019_102X_upgrade2018_realistic_v20-v1/NANOAODSIM"] =  OD([
  ("crab_string",           ""),
  ("sample_category",       "QCD"),
  ("process_name_specific", "QCD_Pt170to300_Mu5"),
  ("nof_db_events",         35978539),
  ("nof_db_files",          44),
  ("fsize_db",              67099061370),
  ("parent_db",             "/QCD_Pt-170to300_MuEnrichedPt5_TuneCP5_13TeV_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v3/MINIAODSIM"),
  ("xsection",              7020.0),
  ("use_it",                False),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 67.10GB; nevents: 35.98M; release: 10_2_18; last modified: 2019-11-13 00:54:58"),
])

meta_dictionary["/QCD_Pt-300to470_MuEnrichedPt5_TuneCP5_13TeV_pythia8/RunIIAutumn18NanoAODv6-Nano25Oct2019_102X_upgrade2018_realistic_v20-v1/NANOAODSIM"] =  OD([
  ("crab_string",           ""),
  ("sample_category",       "QCD"),
  ("process_name_specific", "QCD_Pt300to470_Mu5"),
  ("nof_db_events",         492418),
  ("nof_db_files",          3),
  ("fsize_db",              1050185376),
  ("parent_db",             "/QCD_Pt-300to470_MuEnrichedPt5_TuneCP5_13TeV_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v3/MINIAODSIM"),
  ("xsection",              620.2),
  ("use_it",                False),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 1.05GB; nevents: 492.42k; release: 10_2_18; last modified: 2019-11-06 04:27:34"),
])

meta_dictionary["/QCD_Pt-300to470_MuEnrichedPt5_TuneCP5_13TeV_pythia8/RunIIAutumn18NanoAODv6-Nano25Oct2019_102X_upgrade2018_realistic_v20_ext3-v1/NANOAODSIM"] =  OD([
  ("crab_string",           ""),
  ("sample_category",       "QCD"),
  ("process_name_specific", "QCD_Pt300to470_Mu5_ext3"),
  ("nof_db_events",         28805021),
  ("nof_db_files",          40),
  ("fsize_db",              61023319649),
  ("parent_db",             "/QCD_Pt-300to470_MuEnrichedPt5_TuneCP5_13TeV_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext3-v1/MINIAODSIM"),
  ("xsection",              620.2),
  ("use_it",                False),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 61.02GB; nevents: 28.81M; release: 10_2_18; last modified: 2019-11-08 12:52:11"),
])

meta_dictionary["/QCD_Pt-470to600_MuEnrichedPt5_TuneCP5_13TeV_pythia8/RunIIAutumn18NanoAODv6-Nano25Oct2019_102X_upgrade2018_realistic_v20-v1/NANOAODSIM"] =  OD([
  ("crab_string",           ""),
  ("sample_category",       "QCD"),
  ("process_name_specific", "QCD_Pt470to600_Mu5"),
  ("nof_db_events",         492716),
  ("nof_db_files",          1),
  ("fsize_db",              1103467775),
  ("parent_db",             "/QCD_Pt-470to600_MuEnrichedPt5_TuneCP5_13TeV_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"),
  ("xsection",              59.06),
  ("use_it",                False),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 1.10GB; nevents: 492.72k; release: 10_2_18; last modified: 2019-11-10 09:42:55"),
])

meta_dictionary["/QCD_Pt-470to600_MuEnrichedPt5_TuneCP5_13TeV_pythia8/RunIIAutumn18NanoAODv6-Nano25Oct2019_102X_upgrade2018_realistic_v20_ext1-v1/NANOAODSIM"] =  OD([
  ("crab_string",           ""),
  ("sample_category",       "QCD"),
  ("process_name_specific", "QCD_Pt470to600_Mu5_ext1"),
  ("nof_db_events",         20003034),
  ("nof_db_files",          25),
  ("fsize_db",              44752322467),
  ("parent_db",             "/QCD_Pt-470to600_MuEnrichedPt5_TuneCP5_13TeV_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext1-v2/MINIAODSIM"),
  ("xsection",              59.06),
  ("use_it",                False),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 44.75GB; nevents: 20.00M; release: 10_2_18; last modified: 2019-11-15 13:38:06"),
])

meta_dictionary["/QCD_Pt-600to800_MuEnrichedPt5_TuneCP5_13TeV_pythia8/RunIIAutumn18NanoAODv6-Nano25Oct2019_102X_upgrade2018_realistic_v20-v1/NANOAODSIM"] =  OD([
  ("crab_string",           ""),
  ("sample_category",       "QCD"),
  ("process_name_specific", "QCD_Pt600to800_Mu5"),
  ("nof_db_events",         16523299),
  ("nof_db_files",          20),
  ("fsize_db",              38093160759),
  ("parent_db",             "/QCD_Pt-600to800_MuEnrichedPt5_TuneCP5_13TeV_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"),
  ("xsection",              18.2),
  ("use_it",                False),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 38.09GB; nevents: 16.52M; release: 10_2_18; last modified: 2019-11-07 13:50:52"),
])

meta_dictionary["/QCD_Pt-800to1000_MuEnrichedPt5_TuneCP5_13TeV_pythia8/RunIIAutumn18NanoAODv6-Nano25Oct2019_102X_upgrade2018_realistic_v20_ext3-v1/NANOAODSIM"] =  OD([
  ("crab_string",           ""),
  ("sample_category",       "QCD"),
  ("process_name_specific", "QCD_Pt800to1000_Mu5_ext3"),
  ("nof_db_events",         16749914),
  ("nof_db_files",          32),
  ("fsize_db",              39953437088),
  ("parent_db",             "/QCD_Pt-800to1000_MuEnrichedPt5_TuneCP5_13TeV_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext3-v2/MINIAODSIM"),
  ("xsection",              3.276),
  ("use_it",                False),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 39.95GB; nevents: 16.75M; release: 10_2_18; last modified: 2019-11-09 21:42:53"),
])

meta_dictionary["/QCD_Pt-1000toInf_MuEnrichedPt5_TuneCP5_13TeV_pythia8/RunIIAutumn18NanoAODv6-Nano25Oct2019_102X_upgrade2018_realistic_v20-v1/NANOAODSIM"] =  OD([
  ("crab_string",           ""),
  ("sample_category",       "QCD"),
  ("process_name_specific", "QCD_Pt1000toInf_Mu5"),
  ("nof_db_events",         10625137),
  ("nof_db_files",          25),
  ("fsize_db",              26045993908),
  ("parent_db",             "/QCD_Pt-1000toInf_MuEnrichedPt5_TuneCP5_13TeV_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"),
  ("xsection",              1.079),
  ("use_it",                False),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 26.05GB; nevents: 10.63M; release: 10_2_18; last modified: 2019-11-13 00:52:51"),
])


# event statistics by sample category:
# ttH:        17.12M
# ttH_ctcvcp: 29.09M
# tHq:        29.59M
# tHW:        15.00M
# ggH:        22.82M
# qqH:        13.01M
# TTZ:        36.18M
# TTW:        17.73M
# TTWW:       985.00k
# TT:         845.85M
# TTWH:       200.00k
# TTZH:       200.00k
# Rares:      52.02M
# VH:         8.07M
# EWK:        809.73M
# WW:         35.45M
# WZ:         80.33M
# ZZ:         189.63M
# QCD:        407.76M

