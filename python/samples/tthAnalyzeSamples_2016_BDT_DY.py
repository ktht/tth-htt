from tthAnalysis.HiggsToTauTau.samples.tthAnalyzeSamples_2016 import samples_2016
from tthAnalysis.HiggsToTauTau.samples.tthAnalyzeSamples_2016_BDT import bdt_samples as bdt_samples_common
from tthAnalysis.HiggsToTauTau.samples.stitch import samples_to_stitch_2016
from tthAnalysis.HiggsToTauTau.analysisTools import split_stitched

dy_samples_inclusive, dy_samples_binned = split_stitched(samples_to_stitch_2016, 'DY')
bdt_samples = bdt_samples_common + dy_samples_inclusive + dy_samples_binned

for sample_name, sample_info in samples_2016.items():
  if sample_name == 'sum_events': continue
  sample_info["use_it"] = sample_info["process_name_specific"] in bdt_samples
  if sample_info["process_name_specific"] in [
      "TTJets_DiLept", "TTJets_DiLept_ext1", "TTJets_SingleLeptFromT", "TTJets_SingleLeptFromT_ext1",
      "TTJets_SingleLeptFromTbar", "TTJets_SingleLeptFromTbar_ext1",
    ]:
    sample_info["use_it"] = True
  if sample_info["process_name_specific"].startswith("TTTo"):
    sample_info["use_it"] = False
