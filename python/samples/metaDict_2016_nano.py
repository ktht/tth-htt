from tthAnalysis.HiggsToTauTau.samples.metaDict_2016_data_nano import meta_dictionary as meta_dictionary_data
# from tthAnalysis.HiggsToTauTau.samples.metaDict_2016_mc_nano import meta_dictionary as meta_dictionary_mc
# from tthAnalysis.HiggsToTauTau.samples.metaDict_2016_mc_nano import sum_events
sum_events = {}

import itertools, collections

# meta_dictionary = collections.OrderedDict(itertools.chain(
#   meta_dictionary_data.items(), meta_dictionary_mc.items()
# ))
meta_dictionary = meta_dictionary_data
