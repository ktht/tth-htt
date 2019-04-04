#include "FWCore/ParameterSet/interface/ParameterSet.h" // edm::ParameterSet
#include "FWCore/PythonParameterSet/interface/MakeParameterSets.h" // edm::readPSetsFrom()
#include "FWCore/Utilities/interface/Exception.h" // cms::Exception
#include "PhysicsTools/FWLite/interface/TFileService.h" // fwlite::TFileService
#include "DataFormats/FWLite/interface/InputSource.h" // fwlite::InputSource
#include "DataFormats/FWLite/interface/OutputFiles.h" // fwlite::OutputFiles
#include "DataFormats/Math/interface/LorentzVector.h" // math::PtEtaPhiMLorentzVector
#include "DataFormats/Math/interface/deltaR.h" // deltaR

#include <TBenchmark.h> // TBenchmark
#include <TString.h> // TString, Form
#include <TMatrixD.h> // TMatrixD
#include <TError.h> // gErrorAbortLevel, kError
#include <TMath.h> // TMath::
#include <TH2.h> // TH2

#include "tthAnalysis/HiggsToTauTau/interface/RecoLepton.h" // RecoLepton
#include "tthAnalysis/HiggsToTauTau/interface/RecoJet.h" // RecoJet
#include "tthAnalysis/HiggsToTauTau/interface/RecoHadTau.h" // RecoHadTau
#include "tthAnalysis/HiggsToTauTau/interface/GenLepton.h" // GenLepton
#include "tthAnalysis/HiggsToTauTau/interface/GenJet.h" // GenJet
#include "tthAnalysis/HiggsToTauTau/interface/GenHadTau.h" // GenHadTau
#include "tthAnalysis/HiggsToTauTau/interface/RecoMEt.h" // RecoMEt
#include "tthAnalysis/HiggsToTauTau/interface/EventInfo.h" // EventInfo
#include "tthAnalysis/HiggsToTauTau/interface/MEMOutput_2lss_1tau.h" // MEMOutput_2lss_1tau
#include "tthAnalysis/HiggsToTauTau/interface/TMVAInterface.h" // TMVAInterface
#include "tthAnalysis/HiggsToTauTau/interface/mvaAuxFunctions.h" // check_mvaInputs, get_mvaInputVariables
#include "tthAnalysis/HiggsToTauTau/interface/mvaAuxFunctions_Hj_and_Hjj_taggers.h" // comp_mvaOutput_Hj_tagger, comp_mvaOutput_Hjj_tagger
#include "tthAnalysis/HiggsToTauTau/interface/mvaInputVariables.h" // auxiliary functions for computing input variables of the MVA used for signal extraction in the 2lss_1tau category
#include "tthAnalysis/HiggsToTauTau/interface/LeptonFakeRateInterface.h" // LeptonFakeRateInterface
#include "tthAnalysis/HiggsToTauTau/interface/JetToTauFakeRateInterface.h" // JetToTauFakeRateInterface
#include "tthAnalysis/HiggsToTauTau/interface/RecoElectronReader.h" // RecoElectronReader
#include "tthAnalysis/HiggsToTauTau/interface/RecoMuonReader.h" // RecoMuonReader
#include "tthAnalysis/HiggsToTauTau/interface/RecoHadTauReader.h" // RecoHadTauReader
#include "tthAnalysis/HiggsToTauTau/interface/RecoJetReader.h" // RecoJetReader
#include "tthAnalysis/HiggsToTauTau/interface/RecoMEtReader.h" // RecoMEtReader
#include "tthAnalysis/HiggsToTauTau/interface/MEtFilterReader.h" // MEtFilterReader
#include "tthAnalysis/HiggsToTauTau/interface/MEMOutputReader_2lss_1tau.h" // MEMOutputReader_2lss_1tau
#include "tthAnalysis/HiggsToTauTau/interface/GenLeptonReader.h" // GenLeptonReader
#include "tthAnalysis/HiggsToTauTau/interface/GenHadTauReader.h" // GenHadTauReader
#include "tthAnalysis/HiggsToTauTau/interface/GenPhotonReader.h" // GenPhotonReader
#include "tthAnalysis/HiggsToTauTau/interface/GenJetReader.h" // GenJetReader
#include "tthAnalysis/HiggsToTauTau/interface/GenParticleReader.h" // GenParticleReader
#include "tthAnalysis/HiggsToTauTau/interface/LHEInfoReader.h" // LHEInfoReader
#include "tthAnalysis/HiggsToTauTau/interface/EventInfoReader.h" // EventInfoReader
#include "tthAnalysis/HiggsToTauTau/interface/convert_to_ptrs.h" // convert_to_ptrs
#include "tthAnalysis/HiggsToTauTau/interface/ParticleCollectionCleaner.h" // RecoElectronCollectionCleaner, RecoMuonCollectionCleaner, RecoHadTauCollectionCleaner, RecoJetCollectionCleaner
#include "tthAnalysis/HiggsToTauTau/interface/ParticleCollectionGenMatcher.h" // RecoElectronCollectionGenMatcher, RecoMuonCollectionGenMatcher, RecoHadTauCollectionGenMatcher, RecoJetCollectionGenMatcher
#include "tthAnalysis/HiggsToTauTau/interface/RecoElectronCollectionSelectorLoose.h" // RecoElectronCollectionSelectorLoose
#include "tthAnalysis/HiggsToTauTau/interface/RecoElectronCollectionSelectorFakeable.h" // RecoElectronCollectionSelectorFakeable
#include "tthAnalysis/HiggsToTauTau/interface/RecoElectronCollectionSelectorTight.h" // RecoElectronCollectionSelectorTight
#include "tthAnalysis/HiggsToTauTau/interface/RecoMuonCollectionSelectorLoose.h" // RecoMuonCollectionSelectorLoose
#include "tthAnalysis/HiggsToTauTau/interface/RecoMuonCollectionSelectorFakeable.h" // RecoMuonCollectionSelectorFakeable
#include "tthAnalysis/HiggsToTauTau/interface/RecoMuonCollectionSelectorTight.h" // RecoMuonCollectionSelectorTight
#include "tthAnalysis/HiggsToTauTau/interface/RecoHadTauCollectionSelectorLoose.h" // RecoHadTauCollectionSelectorLoose
#include "tthAnalysis/HiggsToTauTau/interface/RecoHadTauCollectionSelectorFakeable.h" // RecoHadTauCollectionSelectorFakeable
#include "tthAnalysis/HiggsToTauTau/interface/RecoHadTauCollectionSelectorTight.h" // RecoHadTauCollectionSelectorTight
#include "tthAnalysis/HiggsToTauTau/interface/RecoJetCollectionSelector.h" // RecoJetCollectionSelector
#include "tthAnalysis/HiggsToTauTau/interface/RecoJetCollectionSelectorBtag.h" // RecoJetCollectionSelectorBtagLoose, RecoJetCollectionSelectorBtagMedium
#include "tthAnalysis/HiggsToTauTau/interface/RecoJetCollectionSelectorForward.h" // RecoJetSelectorForward
#include "tthAnalysis/HiggsToTauTau/interface/RunLumiEventSelector.h" // RunLumiEventSelector
#include "tthAnalysis/HiggsToTauTau/interface/MEtFilterSelector.h" // MEtFilterSelector
#include "tthAnalysis/HiggsToTauTau/interface/ElectronHistManager.h" // ElectronHistManager
#include "tthAnalysis/HiggsToTauTau/interface/MuonHistManager.h" // MuonHistManager
#include "tthAnalysis/HiggsToTauTau/interface/HadTauHistManager.h" // HadTauHistManager
#include "tthAnalysis/HiggsToTauTau/interface/JetHistManager.h" // JetHistManager
#include "tthAnalysis/HiggsToTauTau/interface/MEtHistManager.h" // MEtHistManager
#include "tthAnalysis/HiggsToTauTau/interface/MEtFilterHistManager.h" // MEtFilterHistManager
#include "tthAnalysis/HiggsToTauTau/interface/MVAInputVarHistManager.h" // MVAInputVarHistManager
#include "tthAnalysis/HiggsToTauTau/interface/EvtHistManager_2lss_1tau.h" // EvtHistManager_2lss_1tau
#include "tthAnalysis/HiggsToTauTau/interface/EvtYieldHistManager.h" // EvtYieldHistManager
#include "tthAnalysis/HiggsToTauTau/interface/CutFlowTableHistManager.h" // CutFlowTableHistManager
#include "tthAnalysis/HiggsToTauTau/interface/WeightHistManager.h" // WeightHistManager
#include "tthAnalysis/HiggsToTauTau/interface/GenEvtHistManager.h" // GenEvtHistManager
#include "tthAnalysis/HiggsToTauTau/interface/LHEInfoHistManager.h" // LHEInfoHistManager
#include "tthAnalysis/HiggsToTauTau/interface/leptonTypes.h" // getLeptonType, kElectron, kMuon
#include "tthAnalysis/HiggsToTauTau/interface/analysisAuxFunctions.h" // getBTagWeight_option, getHadTau_genPdgId, isHigherPt, isMatched
#include "tthAnalysis/HiggsToTauTau/interface/HistManagerBase.h" // HistManagerBase
#include "tthAnalysis/HiggsToTauTau/interface/histogramAuxFunctions.h" // fillWithOverFlow2d
#include "tthAnalysis/HiggsToTauTau/interface/HadTopTagger.h" // HadTopTagger
#include "tthAnalysis/HiggsToTauTau/interface/HadTopTagger_boosted.h" // HadTopTagger_boosted
#include "tthAnalysis/HiggsToTauTau/interface/HadTopTagger_semi_boosted.h" // HadTopTagger_semi_boosted
#include "tthAnalysis/HiggsToTauTau/interface/HadTopTagger_semi_boosted_AK8.h" // HadTopTagger_semi_boosted
#include "tthAnalysis/HiggsToTauTau/interface/leptonGenMatchingAuxFunctions.h" // getLeptonGenMatch_definitions_1lepton, getLeptonGenMatch_string, getLeptonGenMatch_int
#include "tthAnalysis/HiggsToTauTau/interface/hadTauGenMatchingAuxFunctions.h" // getHadTauGenMatch_definitions_1tau, getHadTauGenMatch_string, getHadTauGenMatch_int
#include "tthAnalysis/HiggsToTauTau/interface/fakeBackgroundAuxFunctions.h" // getWeight_2L, getWeight_3L
#include "tthAnalysis/HiggsToTauTau/interface/backgroundEstimation.h" // prob_chargeMisId
#include "tthAnalysis/HiggsToTauTau/interface/hltPath.h" // hltPath, create_hltPaths, hltPaths_isTriggered, hltPaths_delete
#include "tthAnalysis/HiggsToTauTau/interface/hltPathReader.h" // hltPathReader
#include "tthAnalysis/HiggsToTauTau/interface/Data_to_MC_CorrectionInterface_2016.h"
#include "tthAnalysis/HiggsToTauTau/interface/Data_to_MC_CorrectionInterface_2017.h"
#include "tthAnalysis/HiggsToTauTau/interface/Data_to_MC_CorrectionInterface_2018.h"
#include "tthAnalysis/HiggsToTauTau/interface/lutAuxFunctions.h" // loadTH2, getSF_from_TH2
#include "tthAnalysis/HiggsToTauTau/interface/cutFlowTable.h" // cutFlowTableType
#include "tthAnalysis/HiggsToTauTau/interface/NtupleFillerBDT.h" // NtupleFillerBDT
#include "tthAnalysis/HiggsToTauTau/interface/hadTopTaggerAuxFunctions.h" // isGenMatchedJetTriplet
#include "tthAnalysis/HiggsToTauTau/interface/hadTopTaggerAuxFunctions_geral.h" // isGenMatchedJetTriplet tags
#include "tthAnalysis/HiggsToTauTau/interface/XGBInterface.h" // XGBInterface
#include "tthAnalysis/HiggsToTauTau/interface/HadTopKinFit.h" // HadTopKinFit
#include "tthAnalysis/HiggsToTauTau/interface/TTreeWrapper.h" // TTreeWrapper
#include "tthAnalysis/HiggsToTauTau/interface/SyncNtupleManager.h" // SyncNtupleManager
#include "tthAnalysis/HiggsToTauTau/interface/hltFilter.h" // hltFilter()
#include "tthAnalysis/HiggsToTauTau/interface/EvtWeightManager.h" // EvtWeightManager

#include "tthAnalysis/HiggsToTauTau/interface/RecoJetCollectionSelectorHTTv2.h" // RecoJetSelectorHTTv2
#include "tthAnalysis/HiggsToTauTau/interface/RecoJetHTTv2.h"
#include "tthAnalysis/HiggsToTauTau/interface/RecoJetReaderHTTv2.h" // RecoJetReaderHTTv2
#include "tthAnalysis/HiggsToTauTau/interface/RecoJetReaderAK8.h" // RecoJetReaderAK8
#include "tthAnalysis/HiggsToTauTau/interface/ParticleCollectionCleanerSubJets.h" // RecoJetCollectionCleanerAK8SubJets
#include "tthAnalysis/HiggsToTauTau/interface/JetHistManagerHTTv2.h" // JetHistManagerHTTv2

#include "tthAnalysis/HiggsToTauTau/interface/RecoJetCollectionSelectorAK8.h" // RecoJetSelectorAK8

#include <boost/math/special_functions/sign.hpp> // boost::math::sign()
#include "tthAnalysis/HiggsToTauTau/interface/TensorFlowInterface.h"

#include <iostream> // std::cerr, std::fixed
#include <iomanip> // std::setprecision(), std::setw()
#include <string> // std::string
#include <vector> // std::vector<>
#include <cstdlib> // EXIT_SUCCESS, EXIT_FAILURE
#include <fstream> // std::ofstream
#include <assert.h> // assert

typedef math::PtEtaPhiMLorentzVector LV;
typedef std::vector<std::string> vstring;

enum { kFR_disabled, kFR_2lepton, kFR_3L, kFR_1tau };

//const int hadTauSelection_antiElectron = 1; // vLoose
//const int hadTauSelection_antiMuon = 1; // Loose
const int hadTauSelection_antiElectron = -1; // not applied
const int hadTauSelection_antiMuon = -1; // not applied
const int hadTauSelection_veto_antiElectron = -1; // CV: needs to match anti-electron discriminator applied in 2l+2tau category
const int hadTauSelection_veto_antiMuon = -1; // CV: needs to match anti-muon discriminator applied in 2l+2tau category

/**
 * @brief Produce datacard and control plots for 2lss_1tau categories.
 */
int main(int argc, char* argv[])
{
//--- throw an exception in case ROOT encounters an error
  gErrorAbortLevel = kError;

//--- parse command-line arguments
  if ( argc < 2 ) {
    std::cout << "Usage: " << argv[0] << " [parameters.py]" << std::endl;
    return EXIT_FAILURE;
  }

  std::cout << "<analyze_2lss_1tau>:" << std::endl;

//--- keep track of time it takes the macro to execute
  TBenchmark clock;
  clock.Start("analyze_2lss_1tau");

//--- read python configuration parameters
  if ( !edm::readPSetsFrom(argv[1])->existsAs<edm::ParameterSet>("process") )
    throw cms::Exception("analyze_2lss_1tau")
      << "No ParameterSet 'process' found in configuration file = " << argv[1] << " !!\n";

  edm::ParameterSet cfg = edm::readPSetsFrom(argv[1])->getParameter<edm::ParameterSet>("process");

  edm::ParameterSet cfg_analyze = cfg.getParameter<edm::ParameterSet>("analyze_2lss_1tau");

  std::string treeName = cfg_analyze.getParameter<std::string>("treeName");

  std::string process_string = cfg_analyze.getParameter<std::string>("process");
  bool isSignal = ( process_string == "signal" ) ? true : false;

  std::string histogramDir = cfg_analyze.getParameter<std::string>("histogramDir");
  bool isMCClosure_e = histogramDir.find("mcClosure_e") != std::string::npos;
  bool isMCClosure_m = histogramDir.find("mcClosure_m") != std::string::npos;
  bool isMCClosure_t = histogramDir.find("mcClosure_t") != std::string::npos;

  std::string era_string = cfg_analyze.getParameter<std::string>("era");
  const int era = get_era(era_string);

  vstring triggerNames_1e = cfg_analyze.getParameter<vstring>("triggers_1e");
  std::vector<hltPath*> triggers_1e = create_hltPaths(triggerNames_1e, "triggers_1e");
  bool use_triggers_1e = cfg_analyze.getParameter<bool>("use_triggers_1e");
  vstring triggerNames_2e = cfg_analyze.getParameter<vstring>("triggers_2e");
  std::vector<hltPath*> triggers_2e = create_hltPaths(triggerNames_2e, "triggers_2e");
  bool use_triggers_2e = cfg_analyze.getParameter<bool>("use_triggers_2e");
  vstring triggerNames_1mu = cfg_analyze.getParameter<vstring>("triggers_1mu");
  std::vector<hltPath*> triggers_1mu = create_hltPaths(triggerNames_1mu, "triggers_1mu");
  bool use_triggers_1mu = cfg_analyze.getParameter<bool>("use_triggers_1mu");
  vstring triggerNames_2mu = cfg_analyze.getParameter<vstring>("triggers_2mu");
  std::vector<hltPath*> triggers_2mu = create_hltPaths(triggerNames_2mu, "triggers_2mu");
  bool use_triggers_2mu = cfg_analyze.getParameter<bool>("use_triggers_2mu");
  vstring triggerNames_1e1mu = cfg_analyze.getParameter<vstring>("triggers_1e1mu");
  std::vector<hltPath*> triggers_1e1mu = create_hltPaths(triggerNames_1e1mu, "triggers_1e1mu");
  bool use_triggers_1e1mu = cfg_analyze.getParameter<bool>("use_triggers_1e1mu");

  bool apply_offline_e_trigger_cuts_1e = cfg_analyze.getParameter<bool>("apply_offline_e_trigger_cuts_1e");
  bool apply_offline_e_trigger_cuts_2e = cfg_analyze.getParameter<bool>("apply_offline_e_trigger_cuts_2e");
  bool apply_offline_e_trigger_cuts_1mu = cfg_analyze.getParameter<bool>("apply_offline_e_trigger_cuts_1mu");
  bool apply_offline_e_trigger_cuts_2mu = cfg_analyze.getParameter<bool>("apply_offline_e_trigger_cuts_2mu");
  bool apply_offline_e_trigger_cuts_1e1mu = cfg_analyze.getParameter<bool>("apply_offline_e_trigger_cuts_1e1mu");

  enum { kOS, kSS };
  std::string leptonChargeSelection_string = cfg_analyze.getParameter<std::string>("leptonChargeSelection");
  int leptonChargeSelection = -1;
  if      ( leptonChargeSelection_string == "OS" ) leptonChargeSelection = kOS;
  else if ( leptonChargeSelection_string == "SS" ) leptonChargeSelection = kSS;
  else throw cms::Exception("analyze_2lss_1tau")
    << "Invalid Configuration parameter 'leptonChargeSelection' = " << leptonChargeSelection_string << " !!\n";

  const std::string electronSelection_string = cfg_analyze.getParameter<std::string>("electronSelection");
  const std::string muonSelection_string     = cfg_analyze.getParameter<std::string>("muonSelection");
  std::cout << "electronSelection_string = " << electronSelection_string << "\n"
               "muonSelection_string     = " << muonSelection_string     << '\n'
  ;
  const int electronSelection = get_selection(electronSelection_string);
  const int muonSelection     = get_selection(muonSelection_string);
  double lep_mva_cut = cfg_analyze.getParameter<double>("lep_mva_cut"); // CV: used for tight lepton selection only

  bool apply_leptonGenMatching = cfg_analyze.getParameter<bool>("apply_leptonGenMatching");
  std::vector<leptonGenMatchEntry> leptonGenMatch_definitions = getLeptonGenMatch_definitions_2lepton(apply_leptonGenMatching);
  std::cout << "leptonGenMatch_definitions:" << std::endl;
  std::cout << leptonGenMatch_definitions;

  TString hadTauSelection_string = cfg_analyze.getParameter<std::string>("hadTauSelection").data();
  TObjArray* hadTauSelection_parts = hadTauSelection_string.Tokenize("|");
  assert(hadTauSelection_parts->GetEntries() >= 1);
  const std::string hadTauSelection_part1 = (dynamic_cast<TObjString*>(hadTauSelection_parts->At(0)))->GetString().Data();
  const int hadTauSelection = get_selection(hadTauSelection_part1);
  std::string hadTauSelection_part2 = ( hadTauSelection_parts->GetEntries() == 2 ) ? (dynamic_cast<TObjString*>(hadTauSelection_parts->At(1)))->GetString().Data() : "";
  delete hadTauSelection_parts;
  std::string hadTauSelection_veto = cfg_analyze.getParameter<std::string>("hadTauSelection_veto");

  bool apply_hadTauGenMatching = cfg_analyze.getParameter<bool>("apply_hadTauGenMatching");
  std::vector<hadTauGenMatchEntry> hadTauGenMatch_definitions = getHadTauGenMatch_definitions_1tau(apply_hadTauGenMatching);
  std::cout << "hadTauGenMatch_definitions:" << std::endl;
  std::cout << hadTauGenMatch_definitions;

  std::string chargeSumSelection_string = cfg_analyze.getParameter<std::string>("chargeSumSelection");
  int chargeSumSelection = -1;
  if      ( chargeSumSelection_string == "OS" ) chargeSumSelection = kOS;
  else if ( chargeSumSelection_string == "SS" ) chargeSumSelection = kSS;
  else throw cms::Exception("analyze_2lss_1tau")
    << "Invalid Configuration parameter 'chargeSumSelection' = " << chargeSumSelection_string << " !!\n";

  bool apply_lepton_and_hadTauCharge_cut = cfg_analyze.getParameter<bool>("apply_lepton_and_hadTauCharge_cut");
  std::cout << "apply_lepton_and_hadTauCharge_cut = " << apply_lepton_and_hadTauCharge_cut << std::endl;

  bool isMC = cfg_analyze.getParameter<bool>("isMC");
  bool isMC_tH = ( process_string == "tHq" || process_string == "tHW" ) ? true : false;
  bool hasLHE = cfg_analyze.getParameter<bool>("hasLHE");
  std::string central_or_shift = cfg_analyze.getParameter<std::string>("central_or_shift");
  double lumiScale = ( process_string != "data_obs" ) ? cfg_analyze.getParameter<double>("lumiScale") : 1.;
  bool apply_genWeight = cfg_analyze.getParameter<bool>("apply_genWeight");
  bool apply_hlt_filter = cfg_analyze.getParameter<bool>("apply_hlt_filter");
  bool apply_met_filters = cfg_analyze.getParameter<bool>("apply_met_filters");
  edm::ParameterSet cfgMEtFilter = cfg_analyze.getParameter<edm::ParameterSet>("cfgMEtFilter");
  MEtFilterSelector metFilterSelector(cfgMEtFilter, isMC);
  bool apply_hadTauFakeRateSF = cfg_analyze.getParameter<bool>("apply_hadTauFakeRateSF");
  const bool useNonNominal = cfg_analyze.getParameter<bool>("useNonNominal");
  const bool useNonNominal_jetmet = useNonNominal || ! isMC;

  const edm::ParameterSet syncNtuple_cfg = cfg_analyze.getParameter<edm::ParameterSet>("syncNtuple");
  const std::string syncNtuple_tree = syncNtuple_cfg.getParameter<std::string>("tree");
  const std::string syncNtuple_output = syncNtuple_cfg.getParameter<std::string>("output");
  const bool sync_requireGenMatching = syncNtuple_cfg.getParameter<bool>("requireGenMatching");
  const bool do_sync = ! syncNtuple_tree.empty() && ! syncNtuple_output.empty();

  const edm::ParameterSet additionalEvtWeight = cfg_analyze.getParameter<edm::ParameterSet>("evtWeight");
  const bool applyAdditionalEvtWeight = additionalEvtWeight.getParameter<bool>("apply");
  EvtWeightManager * eventWeightManager = nullptr;
  if(applyAdditionalEvtWeight)
  {
    eventWeightManager = new EvtWeightManager(additionalEvtWeight);
  }

  bool isDEBUG = cfg_analyze.getParameter<bool>("isDEBUG");
  if ( isDEBUG ) std::cout << "Warning: DEBUG mode enabled -> trigger selection will not be applied for data !!" << std::endl;

  checkOptionValidity(central_or_shift, isMC);
  const int jetToLeptonFakeRate_option = getJetToLeptonFR_option(central_or_shift);
  const int hadTauPt_option            = getHadTauPt_option     (central_or_shift);
  const int jetToTauFakeRate_option    = getJetToTauFR_option   (central_or_shift);
  const int lheScale_option            = getLHEscale_option     (central_or_shift);
  const int jetBtagSF_option           = getBTagWeight_option   (central_or_shift);
  const PUsys puSys_option             = getPUsys_option        (central_or_shift);

  const int met_option   = useNonNominal_jetmet ? kMEt_central_nonNominal : getMET_option(central_or_shift, isMC);
  const int jetPt_option = useNonNominal_jetmet ? kJet_central_nonNominal : getJet_option(central_or_shift, isMC);

  std::cout
    << "central_or_shift = "               << central_or_shift           << "\n"
       " -> jetToLeptonFakeRate_option = " << jetToLeptonFakeRate_option << "\n"
       " -> hadTauPt_option            = " << hadTauPt_option            << "\n"
       " -> jetToTauFakeRate_option    = " << jetToTauFakeRate_option    << "\n"
       " -> lheScale_option            = " << lheScale_option            << "\n"
       " -> jetBtagSF_option           = " << jetBtagSF_option           << "\n"
       " -> met_option                 = " << met_option                 << "\n"
       " -> jetPt_option               = " << jetPt_option               << '\n'
  ;

  edm::ParameterSet cfg_dataToMCcorrectionInterface;
  cfg_dataToMCcorrectionInterface.addParameter<std::string>("era", era_string);
  cfg_dataToMCcorrectionInterface.addParameter<std::string>("hadTauSelection", hadTauSelection_part2);
  cfg_dataToMCcorrectionInterface.addParameter<int>("hadTauSelection_antiElectron", hadTauSelection_antiElectron);
  cfg_dataToMCcorrectionInterface.addParameter<int>("hadTauSelection_antiMuon", hadTauSelection_antiMuon);
  cfg_dataToMCcorrectionInterface.addParameter<std::string>("central_or_shift", central_or_shift);
  Data_to_MC_CorrectionInterface_Base * dataToMCcorrectionInterface = nullptr;
  switch(era)
  {
    case kEra_2016: dataToMCcorrectionInterface = new Data_to_MC_CorrectionInterface_2016(cfg_dataToMCcorrectionInterface); break;
    case kEra_2017: dataToMCcorrectionInterface = new Data_to_MC_CorrectionInterface_2017(cfg_dataToMCcorrectionInterface); break;
    case kEra_2018: dataToMCcorrectionInterface = new Data_to_MC_CorrectionInterface_2018(cfg_dataToMCcorrectionInterface); break;
    default: throw cmsException("analyze_2lss_1tau", __LINE__) << "Invalid era = " << era;
  }

  std::string applyFakeRateWeights_string = cfg_analyze.getParameter<std::string>("applyFakeRateWeights");
  int applyFakeRateWeights = -1;
  if      ( applyFakeRateWeights_string == "disabled" ) applyFakeRateWeights = kFR_disabled;
  else if ( applyFakeRateWeights_string == "2lepton"  ) applyFakeRateWeights = kFR_2lepton;
  else if ( applyFakeRateWeights_string == "3L"       ) applyFakeRateWeights = kFR_3L;
  else if ( applyFakeRateWeights_string == "1tau"     ) applyFakeRateWeights = kFR_1tau;
  else throw cms::Exception("analyze_2lss_1tau")
    << "Invalid Configuration parameter 'applyFakeRateWeights' = " << applyFakeRateWeights_string << " !!\n";
  std::cout << "Applying fake rate weights = " << applyFakeRateWeights_string << " (" << applyFakeRateWeights << ")\n";

  LeptonFakeRateInterface* leptonFakeRateInterface = 0;
  if ( applyFakeRateWeights == kFR_2lepton || applyFakeRateWeights == kFR_3L ) {
    edm::ParameterSet cfg_leptonFakeRateWeight = cfg_analyze.getParameter<edm::ParameterSet>("leptonFakeRateWeight");
    leptonFakeRateInterface = new LeptonFakeRateInterface(cfg_leptonFakeRateWeight, jetToLeptonFakeRate_option);
  }

  JetToTauFakeRateInterface* jetToTauFakeRateInterface = 0;
  if ( applyFakeRateWeights == kFR_3L || applyFakeRateWeights == kFR_1tau || apply_hadTauFakeRateSF ) {
    edm::ParameterSet cfg_hadTauFakeRateWeight = cfg_analyze.getParameter<edm::ParameterSet>("hadTauFakeRateWeight");
    cfg_hadTauFakeRateWeight.addParameter<std::string>("hadTauSelection", hadTauSelection_part2);
    jetToTauFakeRateInterface = new JetToTauFakeRateInterface(cfg_hadTauFakeRateWeight, jetToTauFakeRate_option);
  }
  std::cout << "Applying jetToTauFakeRate fake rate weights = " << applyFakeRateWeights_string << " (" << applyFakeRateWeights << ")\n";

  bool fillGenEvtHistograms = cfg_analyze.getParameter<bool>("fillGenEvtHistograms");
  edm::ParameterSet cfg_EvtYieldHistManager = cfg_analyze.getParameter<edm::ParameterSet>("cfgEvtYieldHistManager");

  std::string branchName_electrons = cfg_analyze.getParameter<std::string>("branchName_electrons");
  std::string branchName_muons = cfg_analyze.getParameter<std::string>("branchName_muons");
  std::string branchName_hadTaus = cfg_analyze.getParameter<std::string>("branchName_hadTaus");
  std::string branchName_jets = cfg_analyze.getParameter<std::string>("branchName_jets");
  std::string branchName_jetsHTTv2 = cfg_analyze.getParameter<std::string>("branchName_jetsHTTv2");
  std::string branchName_subjetsHTTv2 = cfg_analyze.getParameter<std::string>("branchName_subjetsHTTv2");
  std::string branchName_jetsAK8 = cfg_analyze.getParameter<std::string>("branchName_jetsAK8");
  std::string branchName_subjetsAK8 = cfg_analyze.getParameter<std::string>("branchName_subjetsAK8");
  std::string branchName_met = cfg_analyze.getParameter<std::string>("branchName_met");
  std::string branchName_memOutput = cfg_analyze.getParameter<std::string>("branchName_memOutput");

  std::string branchName_genLeptons = cfg_analyze.getParameter<std::string>("branchName_genLeptons");
  std::string branchName_genHadTaus = cfg_analyze.getParameter<std::string>("branchName_genHadTaus");
  std::string branchName_genPhotons = cfg_analyze.getParameter<std::string>("branchName_genPhotons");
  std::string branchName_genJets = cfg_analyze.getParameter<std::string>("branchName_genJets");

  bool redoGenMatching = cfg_analyze.getParameter<bool>("redoGenMatching");

  std::string branchName_genTopQuarks = cfg_analyze.getParameter<std::string>("branchName_genTopQuarks");
  std::string branchName_genBJets = cfg_analyze.getParameter<std::string>("branchName_genBJets");
  std::string branchName_genWBosons = cfg_analyze.getParameter<std::string>("branchName_genWBosons");
  std::string branchName_genWJets = cfg_analyze.getParameter<std::string>("branchName_genWJets");
  std::string branchName_genQuarkFromTop = cfg_analyze.getParameter<std::string>("branchName_genQuarkFromTop");

  bool selectBDT = ( cfg_analyze.exists("selectBDT") ) ? cfg_analyze.getParameter<bool>("selectBDT") : false;

  std::string selEventsFileName_input = cfg_analyze.getParameter<std::string>("selEventsFileName_input");
  std::cout << "selEventsFileName_input = " << selEventsFileName_input << std::endl;
  RunLumiEventSelector* run_lumi_eventSelector = 0;
  if ( selEventsFileName_input != "" ) {
    edm::ParameterSet cfgRunLumiEventSelector;
    cfgRunLumiEventSelector.addParameter<std::string>("inputFileName", selEventsFileName_input);
    cfgRunLumiEventSelector.addParameter<std::string>("separator", ":");
    run_lumi_eventSelector = new RunLumiEventSelector(cfgRunLumiEventSelector);
  }

  std::string selEventsFileName_output = cfg_analyze.getParameter<std::string>("selEventsFileName_output");

  fwlite::InputSource inputFiles(cfg);
  int maxEvents = inputFiles.maxEvents();
  std::cout << " maxEvents = " << maxEvents << std::endl;
  unsigned reportEvery = inputFiles.reportAfter();

  fwlite::OutputFiles outputFile(cfg);
  fwlite::TFileService fs = fwlite::TFileService(outputFile.file().data());

  TTreeWrapper * inputTree = new TTreeWrapper(treeName.data(), inputFiles.files(), maxEvents);

  std::cout << "Loaded " << inputTree -> getFileCount() << " file(s).\n";

//--- prepare sync Ntuple
  SyncNtupleManager * snm = nullptr;
  if(do_sync)
  {
    snm = new SyncNtupleManager(syncNtuple_output, syncNtuple_tree);
    snm->initializeBranches();
    snm->initializeHLTBranches({ triggers_1e, triggers_2e, triggers_1mu, triggers_2mu, triggers_1e1mu });
  }

//--- declare event-level variables
  EventInfo eventInfo(isSignal, isMC, isMC_tH);
  EventInfoReader eventInfoReader(&eventInfo, puSys_option);
  inputTree -> registerReader(&eventInfoReader);

  hltPathReader hltPathReader_instance({ triggers_1e, triggers_2e, triggers_1mu, triggers_2mu, triggers_1e1mu });
  inputTree -> registerReader(&hltPathReader_instance);

  if(eventWeightManager)
  {
    inputTree->registerReader(eventWeightManager);
  }

//--- declare particle collections
  const bool readGenObjects = isMC && !redoGenMatching;
  RecoMuonReader* muonReader = new RecoMuonReader(era, branchName_muons, readGenObjects);
  inputTree -> registerReader(muonReader);
  RecoMuonCollectionGenMatcher muonGenMatcher;
  RecoMuonCollectionSelectorLoose preselMuonSelector(era, -1, isDEBUG);
  RecoMuonCollectionSelectorFakeable fakeableMuonSelector(era, -1, isDEBUG);
  RecoMuonCollectionSelectorTight tightMuonSelector(era, -1, isDEBUG);
  tightMuonSelector.getSelector().set_min_mvaTTH(lep_mva_cut);

  RecoElectronReader* electronReader = new RecoElectronReader(era, branchName_electrons, readGenObjects);
  electronReader->readUncorrected(useNonNominal);
  inputTree -> registerReader(electronReader);
  RecoElectronCollectionGenMatcher electronGenMatcher;
  RecoElectronCollectionCleaner electronCleaner(0.3, isDEBUG);
  RecoElectronCollectionSelectorLoose preselElectronSelector(era, -1, isDEBUG);
  RecoElectronCollectionSelectorFakeable fakeableElectronSelector(era, -1, isDEBUG);
  RecoElectronCollectionSelectorTight tightElectronSelector(era, -1, isDEBUG);
  tightElectronSelector.getSelector().set_min_mvaTTH(lep_mva_cut);

  RecoHadTauReader* hadTauReader = new RecoHadTauReader(era, branchName_hadTaus, readGenObjects);
  hadTauReader->setHadTauPt_central_or_shift(hadTauPt_option);
  inputTree -> registerReader(hadTauReader);
  RecoHadTauCollectionGenMatcher hadTauGenMatcher;
  RecoHadTauCollectionCleaner hadTauCleaner(0.3, isDEBUG);
  RecoHadTauCollectionSelectorLoose preselHadTauSelector(era, -1, isDEBUG);
  preselHadTauSelector.set_if_looser(hadTauSelection_part2);
  preselHadTauSelector.set_min_antiElectron(hadTauSelection_antiElectron);
  preselHadTauSelector.set_min_antiMuon(hadTauSelection_antiMuon);
  RecoHadTauCollectionSelectorFakeable fakeableHadTauSelector(era, -1, isDEBUG);
  fakeableHadTauSelector.set_if_looser(hadTauSelection_part2);
  fakeableHadTauSelector.set_min_antiElectron(hadTauSelection_antiElectron);
  fakeableHadTauSelector.set_min_antiMuon(hadTauSelection_antiMuon);
  RecoHadTauCollectionSelectorTight tightHadTauSelector(era, -1, isDEBUG);
  tightHadTauSelector.set(hadTauSelection_part2);
  tightHadTauSelector.set_min_antiElectron(hadTauSelection_antiElectron);
  tightHadTauSelector.set_min_antiMuon(hadTauSelection_antiMuon);
  RecoHadTauSelectorTight tightHadTauFilter(era, -1, isDEBUG);
  tightHadTauFilter.set("dR03mvaMedium");
  tightHadTauFilter.set_min_antiElectron(hadTauSelection_antiElectron);
  tightHadTauFilter.set_min_antiMuon(hadTauSelection_antiMuon);

  RecoJetReaderHTTv2* jetReaderHTTv2 = new RecoJetReaderHTTv2(era, branchName_jetsHTTv2, branchName_subjetsHTTv2);
  inputTree -> registerReader(jetReaderHTTv2);
  RecoJetCollectionSelectorHTTv2 jetSelectorHTTv2(era);
  RecoJetCollectionCleanerHTTv2 jetCleanerHTTv2(0.01, isDEBUG); //to clean against leptons and hadronic taus
  RecoJetCollectionCleanerHTTv2SubJets jetCleanerHTTv2SubJets(0.4, isDEBUG); //to clean against leptons and hadronic taus

  RecoJetReaderAK8* jetReaderAK8 = new RecoJetReaderAK8(era, branchName_jetsAK8, branchName_subjetsAK8);
  inputTree -> registerReader(jetReaderAK8);
  RecoJetCollectionSelectorAK8 jetSelectorAK8(era);
  RecoJetCollectionCleanerAK8 jetCleanerAK8(0.01, isDEBUG); //to clean against leptons and hadronic taus
  RecoJetCollectionCleanerAK8SubJets jetCleanerAK8SubJets(0.4, isDEBUG); //to clean against leptons and hadronic taus

  // CV: veto events containing more than one tau passing the VTight WP, to avoid overlap with the 2l+2tau category
  RecoHadTauCollectionSelectorTight vetoHadTauSelector(era, -1, isDEBUG);
  vetoHadTauSelector.set(hadTauSelection_veto);
  vetoHadTauSelector.set_min_antiElectron(hadTauSelection_veto_antiElectron);
  vetoHadTauSelector.set_min_antiMuon(hadTauSelection_veto_antiMuon);

  RecoJetReader* jetReader = new RecoJetReader(era, isMC, branchName_jets, readGenObjects);
  jetReader->setPtMass_central_or_shift(jetPt_option);
  jetReader->setBranchName_BtagWeight(jetBtagSF_option);
  inputTree -> registerReader(jetReader);
  RecoJetCollectionGenMatcher jetGenMatcher;
  RecoJetCollectionCleaner jetCleaner(0.4, isDEBUG);
  RecoJetCollectionSelector jetSelector(era, -1, isDEBUG);
  RecoJetCollectionSelectorForward jetSelectorForward(era, -1, isDEBUG);
  RecoJetCollectionSelectorBtagLoose jetSelectorBtagLoose(era, -1, isDEBUG);
  RecoJetCollectionSelectorBtagMedium jetSelectorBtagMedium(era, -1, isDEBUG);

//--- declare missing transverse energy
  RecoMEtReader* metReader = new RecoMEtReader(era, isMC, branchName_met);
  metReader->setMEt_central_or_shift(met_option);
  inputTree -> registerReader(metReader);

  MEtFilter metFilters;
  MEtFilterReader* metFilterReader = new MEtFilterReader(&metFilters, era);
  inputTree -> registerReader(metFilterReader);

//--- declare likelihoods for signal/background hypotheses, obtained by matrix element method
  MEMOutputReader_2lss_1tau* memReader = 0;
  if ( branchName_memOutput != "" ) {
    memReader = new MEMOutputReader_2lss_1tau(Form("n%s", branchName_memOutput.data()), branchName_memOutput);
    inputTree -> registerReader(memReader);
  }

//--- declare generator level information
  GenLeptonReader* genLeptonReader = 0;
  GenHadTauReader* genHadTauReader = 0;
  GenPhotonReader* genPhotonReader = 0;
  GenJetReader* genJetReader = 0;
  LHEInfoReader* lheInfoReader = 0;
  if ( isMC ) {
    if ( !readGenObjects ) {
      if ( branchName_genLeptons != "" ) {
        genLeptonReader = new GenLeptonReader(branchName_genLeptons);
        inputTree -> registerReader(genLeptonReader);
      }
      if ( branchName_genHadTaus != "" ) {
        genHadTauReader = new GenHadTauReader(branchName_genHadTaus);
        inputTree -> registerReader(genHadTauReader);
      }
      if ( branchName_genPhotons != "" ) {
        genPhotonReader = new GenPhotonReader(branchName_genPhotons);
        inputTree -> registerReader(genPhotonReader);
      }
      if ( branchName_genJets != "" ) {
        genJetReader = new GenJetReader(branchName_genJets);
        inputTree -> registerReader(genJetReader);
      }
    }
    lheInfoReader = new LHEInfoReader(hasLHE);
    inputTree -> registerReader(lheInfoReader);
  }

  GenParticleReader* genTopQuarkReader = new GenParticleReader(branchName_genTopQuarks);
  GenParticleReader* genBJetReader = new GenParticleReader(branchName_genBJets);
  GenParticleReader* genWBosonReader = new GenParticleReader(branchName_genWBosons);
  GenParticleReader* genWJetReader = new GenParticleReader(branchName_genWJets);
  GenParticleReader* genQuarkFromTopReader = new GenParticleReader(branchName_genQuarkFromTop);

  if ( isMC ) {
          inputTree -> registerReader(genTopQuarkReader);
          inputTree -> registerReader(genBJetReader);
          inputTree -> registerReader(genWBosonReader);
          inputTree -> registerReader(genWJetReader);
          inputTree -> registerReader(genQuarkFromTopReader);
  }

  //--- initialize hadronic top tagger BDT
  HadTopTagger* hadTopTagger = new HadTopTagger();
  HadTopTagger_boosted* hadTopTagger_boosted = new HadTopTagger_boosted();
  HadTopTagger_semi_boosted_AK8*  hadTopTagger_semi_boosted = new HadTopTagger_semi_boosted_AK8();

  // Hj-tagger
  std::string mvaFileName_Hj_tagger = "tthAnalysis/HiggsToTauTau/data/Hj_deepcsv_BDTG_2017.weights.xml";
  std::vector<std::string> mvaInputVariables_Hj_tagger = {
    "Jet25_lepdrmin", "max(Jet25_bDiscriminator,0.)",
    "max(Jet25_qg,0.)", "Jet25_lepdrmax", "Jet25_pt" };
  TMVAInterface mva_Hj_tagger(mvaFileName_Hj_tagger, mvaInputVariables_Hj_tagger);

  std::string mvaFileName_Hjj_tagger = "tthAnalysis/HiggsToTauTau/data/Hjj_csv_BDTG.weights.xml";
  std::vector<std::string> mvaInputVariables_Hjj_tagger = {
    "bdtJetPair_minlepmass", "bdtJetPair_sumbdt", "bdtJetPair_dr",
    "bdtJetPair_minjdr", "bdtJetPair_mass", "bdtJetPair_minjOvermaxjdr"};
TMVAInterface mva_Hjj_tagger(mvaFileName_Hjj_tagger, mvaInputVariables_Hjj_tagger);

//--- initialize BDTs used to discriminate ttH vs. ttV and tt
//    in 2lss_1tau category of ttH multilepton analysis
  std::string mvaFileName_2lss_ttV = "tthAnalysis/HiggsToTauTau/data/2lss_ttV_BDTG.weights.xml";
  std::vector<std::string> mvaInputVariables_2lss_ttV = {
    "max(abs(LepGood_eta[iF_Recl[0]]),abs(LepGood_eta[iF_Recl[1]]))",
    "MT_met_lep1", "nJet25_Recl", "mindr_lep1_jet", "mindr_lep2_jet",
    "LepGood_conePt[iF_Recl[0]]", "LepGood_conePt[iF_Recl[1]]"
  };
  TMVAInterface mva_2lss_ttV(mvaFileName_2lss_ttV, mvaInputVariables_2lss_ttV,
    { "iF_Recl[0]", "iF_Recl[1]", "iF_Recl[2]" });

  std::string mvaFileName_2lss_tt = "tthAnalysis/HiggsToTauTau/data/2lss_ttbar_BDTG.weights.xml";
  std::vector<std::string> mvaInputVariables_2lss_tt = {
    "max(abs(LepGood_eta[iF_Recl[0]]),abs(LepGood_eta[iF_Recl[1]]))",
    "nJet25_Recl", "mindr_lep1_jet", "mindr_lep2_jet", "min(met_pt,400)",
    "avg_dr_jet", "MT_met_lep1"};
  TMVAInterface mva_2lss_tt(mvaFileName_2lss_tt, mvaInputVariables_2lss_tt,
    { "iF_Recl[0]", "iF_Recl[1]", "iF_Recl[2]" });

  // trained with XGB (March 2018)
  std::string mvaFileName_plainKin_tt = "tthAnalysis/HiggsToTauTau/data/evtLevel_2018March/2lss_1tau_XGB_plainKin_evtLevelTT_TTH_16Var.xml";
  std::vector<std::string> mvaInputVariables_plainKin_ttSort = {
    "avg_dr_jet", "dr_lep1_tau", "dr_lep2_tau", "dr_leps", "lep1_conePt", "lep2_conePt",
    "mT_lep2", "mTauTauVis1", "mTauTauVis2", "mbb", "mindr_lep1_jet",
    "mindr_lep2_jet", "mindr_tau_jet", "nJet", "ptmiss", "tau_pt"
  };
  TMVAInterface mva_2lss_1tau_plainKin_tt(mvaFileName_plainKin_tt, mvaInputVariables_plainKin_ttSort);
  mva_2lss_1tau_plainKin_tt.enableBDTTransform();

  std::string mvaFileName_plainKin_ttV ="tthAnalysis/HiggsToTauTau/data/evtLevel_2018March/2lss_1tau_XGB_plainKin_evtLevelTTV_TTH_15Var.xml";
  std::vector<std::string> mvaInputVariables_plainKin_ttVSort = {
    "avg_dr_jet", "dr_lep1_tau", "dr_leps", "lep1_conePt", "lep2_conePt",
    "mT_lep1", "mT_lep2", "mTauTauVis1", "mTauTauVis2","mindr_lep1_jet",
    "mindr_lep2_jet", "mindr_tau_jet", "ptmiss", "max_lep_eta", "tau_pt"
  };
  TMVAInterface mva_2lss_1tau_plainKin_ttV(mvaFileName_plainKin_ttV, mvaInputVariables_plainKin_ttVSort);
  mva_2lss_1tau_plainKin_ttV.enableBDTTransform();

  // Joint 1B
  std::vector<std::string> mvaInputVariables_1BSort = {"BDTtt", "BDTttV"};
  std::string mvaFileName_plainKin_1B_M ="tthAnalysis/HiggsToTauTau/data/evtLevel_2018March/2lss_1tau_XGB_JointBDT_plainKin_1B_M.xml";
  TMVAInterface mva_2lss_1tau_plainKin_1B_M(mvaFileName_plainKin_1B_M, mvaInputVariables_1BSort);
  mva_2lss_1tau_plainKin_1B_M.enableBDTTransform();

  // SUM BDTs - to all layers of variables (including HTT , and including HTT+MEM)
  std::string mvaFileName_plainKin_SUM_M ="tthAnalysis/HiggsToTauTau/data/evtLevel_2018March/2lss_1tau_XGB_plainKin_evtLevelSUM_TTH_M_18Var.xml";
  std::vector<std::string> mvaInputVariables_plainKin_SUMSort = {
    "avg_dr_jet", "dr_lep1_tau", "dr_lep2_tau", "dr_leps",
    "lep1_conePt", "lep2_conePt", "mT_lep1", "mT_lep2",
    "mTauTauVis1", "mTauTauVis2", "max_lep_eta", "mbb",
    "mindr_lep1_jet", "mindr_lep2_jet", "mindr_tau_jet",
    "nJet", "ptmiss", "tau_pt"
  };
  TMVAInterface mva_2lss_1tau_plainKin_SUM_M(mvaFileName_plainKin_SUM_M, mvaInputVariables_plainKin_SUMSort);
  mva_2lss_1tau_plainKin_SUM_M.enableBDTTransform();

  std::string mvaFileName_HTT_SUM_M ="tthAnalysis/HiggsToTauTau/data/evtLevel_2018March/2lss_1tau_XGB_HTT_evtLevelSUM_TTH_M_18Var.xml";
  std::vector<std::string> mvaInputVariables_HTT_SUMSort = {
    "avg_dr_jet", "dr_lep1_tau", "dr_lep2_tau", "dr_leps", "lep2_conePt",
    "mT_lep1", "mT_lep2", "mTauTauVis2", "max_lep_eta",
    "mbb", "mindr_lep1_jet", "mindr_lep2_jet", "mindr_tau_jet",
    "nJet", "ptmiss", "tau_pt",
    "HTT", "HadTop_pt"
  };
  TMVAInterface mva_2lss_1tau_HTT_SUM_M(mvaFileName_HTT_SUM_M, mvaInputVariables_HTT_SUMSort);
  mva_2lss_1tau_HTT_SUM_M.enableBDTTransform();
  std::vector<std::string> mvaInputVariables_2lss = get_mvaInputVariables(mvaInputVariables_HTT_SUMSort, mvaInputVariables_plainKin_SUMSort);

  std::string mvaFileName_HTTMEM_SUM_M ="tthAnalysis/HiggsToTauTau/data/evtLevel_2018March/2lss_1tau_XGB_HTTMEM_evtLevelSUM_TTH_M_20Var.xml";
  std::vector<std::string> mvaInputVariables_HTTMEM_SUMSort = {
    "avg_dr_jet", "dr_lep1_tau", "dr_lep2_tau", "dr_leps", "lep2_conePt", "mT_lep1", "mT_lep2", "mTauTauVis2", "max_lep_eta",
    "mbb", "mindr_lep1_jet", "mindr_lep2_jet", "mindr_tau_jet", "nJet", "ptmiss", "tau_pt", "memOutput_LR",
    "HTT", "Hj_tagger", "HadTop_pt"
  };
  TMVAInterface mva_2lss_1tau_HTTMEM_SUM_M(mvaFileName_HTTMEM_SUM_M, mvaInputVariables_HTTMEM_SUMSort);
  mva_2lss_1tau_HTTMEM_SUM_M.enableBDTTransform();

  // enter the pb
  std::string mvaFileName_TensorFlow_4classes = "tthAnalysis/HiggsToTauTau/data/NN/test_model_kerasPlain_2lss_0tau.pb";
  // the order of input variables should be the same as during the training - saved on model_kerasPlain_2lss_0tau_variables.log
  std::vector<std::string> mvaInputVariables_TensorFlow_4classes = {
    "lep1_conePt", "lep2_conePt",
    "mindr_lep1_jet", "mindr_lep2_jet",
    "mT_lep1", "mT_lep2", "max_lep_eta",
    "nJet", "res-HTT_CSVsort4rd",
    "HadTop_pt_CSVsort4rd",
    "Hj_tagger", "nElectron", "mbb", "ptmiss",
    "LeptonCharge", "resolved_and_semi_AK8", "minDR_AK8_lep", "HTT_boosted"
  };
  // the order also matters
  std::vector<std::string> classes_TensorFlow_4classes = {"predictions_ttH", "predictions_ttZ", "predictions_ttW", "predictions_ttJ"};
  TensorFlowInterface mva_2lss_TF(mvaFileName_TensorFlow_4classes, mvaInputVariables_TensorFlow_4classes, classes_TensorFlow_4classes);
  std::map<std::string, double> mvaInputs_2lss_TF;
  std::cout << "read NN 1" << std::endl;
  //std::map<std::string, double> mvaInputs_2lss_TF_output;


//--- open output file containing run:lumi:event numbers of events passing final event selection criteria
  std::ostream* selEventsFile = ( selEventsFileName_output != "" ) ? new std::ofstream(selEventsFileName_output.data(), std::ios::out) : 0;
  std::cout << "selEventsFileName_output = " << selEventsFileName_output << std::endl;

//--- declare histograms
  struct preselHistManagerType
  {
    ElectronHistManager* electrons_;
    MuonHistManager* muons_;
    HadTauHistManager* hadTaus_;
    JetHistManager* jets_;
    JetHistManager* BJets_loose_;
    JetHistManager* BJets_medium_;
    MEtHistManager* met_;
    MEtFilterHistManager* metFilters_;
    EvtHistManager_2lss_1tau* evt_;
    EvtYieldHistManager* evtYield_;
  };
  typedef std::map<int, preselHistManagerType*> int_to_preselHistManagerMap;
  std::map<int, int_to_preselHistManagerMap> preselHistManagers;
  struct selHistManagerType
  {
    ElectronHistManager* electrons_;
    std::map<std::string, ElectronHistManager*> electrons_in_categories_;
    ElectronHistManager* leadElectron_;
    std::map<std::string, ElectronHistManager*> leadElectron_in_categories_;
    ElectronHistManager* subleadElectron_;
    std::map<std::string, ElectronHistManager*> subleadElectron_in_categories_;
    MuonHistManager* muons_;
    std::map<std::string, MuonHistManager*> muons_in_categories_;
    MuonHistManager* leadMuon_;
    std::map<std::string, MuonHistManager*> leadMuon_in_categories_;
    MuonHistManager* subleadMuon_;
    std::map<std::string, MuonHistManager*> subleadMuon_in_categories_;
    HadTauHistManager* hadTaus_;
    JetHistManager* jets_;
    JetHistManager* leadJet_;
    JetHistManager* subleadJet_;
    JetHistManager* BJets_loose_;
    JetHistManager* leadBJet_loose_;
    JetHistManager* subleadBJet_loose_;
    JetHistManager* BJets_medium_;
    MEtHistManager* met_;
    MEtFilterHistManager* metFilters_;
    MVAInputVarHistManager* mvaInputVariables_2lss_;
    MVAInputVarHistManager* mvaInputVariables_2lss_1tau_;
    EvtHistManager_2lss_1tau* evt_;
    std::map<std::string, EvtHistManager_2lss_1tau*> evt_in_decayModes_;
    std::map<std::string, EvtHistManager_2lss_1tau*> evt_in_categories_;
    std::map<std::string, EvtHistManager_2lss_1tau*> evt_in_categories_2lss_ttH_3cat_TF_;
    std::map<std::string, EvtHistManager_2lss_1tau*> evt_in_categories_in_decayModes_;
    std::map<std::string, EvtHistManager_2lss_1tau*> evt_in_categories_2lss_ttH_3cat_TF_and_decayModes_;
    EvtYieldHistManager* evtYield_;
    WeightHistManager* weights_;
  };
  typedef std::map<int, selHistManagerType*> int_to_selHistManagerMap;
  std::map<int, int_to_selHistManagerMap> selHistManagers;

  for ( std::vector<leptonGenMatchEntry>::const_iterator leptonGenMatch_definition = leptonGenMatch_definitions.begin();
        leptonGenMatch_definition != leptonGenMatch_definitions.end(); ++leptonGenMatch_definition ) {
    for ( std::vector<hadTauGenMatchEntry>::const_iterator hadTauGenMatch_definition = hadTauGenMatch_definitions.begin();
          hadTauGenMatch_definition != hadTauGenMatch_definitions.end(); ++hadTauGenMatch_definition ) {

      std::string process_and_genMatch = process_string;
      if ( apply_leptonGenMatching ) process_and_genMatch += leptonGenMatch_definition->name_;
      if ( apply_leptonGenMatching && apply_hadTauGenMatching ) process_and_genMatch += "&";
      if ( apply_hadTauGenMatching ) process_and_genMatch += hadTauGenMatch_definition->name_;

      int idxLepton = leptonGenMatch_definition->idx_;
      int idxHadTau = hadTauGenMatch_definition->idx_;

      preselHistManagerType* preselHistManager = new preselHistManagerType();
      preselHistManager->electrons_ = new ElectronHistManager(makeHistManager_cfg(process_and_genMatch,
        Form("%s/presel/electrons", histogramDir.data()), central_or_shift));
      preselHistManager->electrons_->bookHistograms(fs);
      preselHistManager->muons_ = new MuonHistManager(makeHistManager_cfg(process_and_genMatch,
        Form("%s/presel/muons", histogramDir.data()), central_or_shift));
      preselHistManager->muons_->bookHistograms(fs);
      preselHistManager->hadTaus_ = new HadTauHistManager(makeHistManager_cfg(process_and_genMatch,
        Form("%s/presel/hadTaus", histogramDir.data()), central_or_shift));
      preselHistManager->hadTaus_->bookHistograms(fs);
      preselHistManager->jets_ = new JetHistManager(makeHistManager_cfg(process_and_genMatch,
        Form("%s/presel/jets", histogramDir.data()), central_or_shift));
      preselHistManager->jets_->bookHistograms(fs);
      preselHistManager->BJets_loose_ = new JetHistManager(makeHistManager_cfg(process_and_genMatch,
        Form("%s/presel/BJets_loose", histogramDir.data()), central_or_shift));
      preselHistManager->BJets_loose_->bookHistograms(fs);
      preselHistManager->BJets_medium_ = new JetHistManager(makeHistManager_cfg(process_and_genMatch,
        Form("%s/presel/BJets_medium", histogramDir.data()), central_or_shift));
      preselHistManager->BJets_medium_->bookHistograms(fs);
      preselHistManager->met_ = new MEtHistManager(makeHistManager_cfg(process_and_genMatch,
        Form("%s/presel/met", histogramDir.data()), central_or_shift));
      preselHistManager->met_->bookHistograms(fs);
      preselHistManager->metFilters_ = new MEtFilterHistManager(makeHistManager_cfg(process_and_genMatch,
        Form("%s/presel/metFilters", histogramDir.data()), central_or_shift));
      preselHistManager->metFilters_->bookHistograms(fs);
      preselHistManager->evt_ = new EvtHistManager_2lss_1tau(makeHistManager_cfg(process_and_genMatch,
        Form("%s/presel/evt", histogramDir.data()), era_string, central_or_shift));
      preselHistManager->evt_->bookHistograms(fs);
      edm::ParameterSet cfg_EvtYieldHistManager_presel = makeHistManager_cfg(process_and_genMatch,
        Form("%s/presel/evtYield", histogramDir.data()), central_or_shift);
      cfg_EvtYieldHistManager_presel.addParameter<edm::ParameterSet>("runPeriods", cfg_EvtYieldHistManager);
      cfg_EvtYieldHistManager_presel.addParameter<bool>("isMC", isMC);
      preselHistManager->evtYield_ = new EvtYieldHistManager(cfg_EvtYieldHistManager_presel);
      preselHistManager->evtYield_->bookHistograms(fs);
      preselHistManagers[idxLepton][idxHadTau] = preselHistManager;

      selHistManagerType* selHistManager = new selHistManagerType();
      //selHistManager->evt_->LoadMaps(nstart, ntarget);
      selHistManager->electrons_ = new ElectronHistManager(makeHistManager_cfg(process_and_genMatch,
        Form("%s/sel/electrons", histogramDir.data()), central_or_shift));
      selHistManager->electrons_->bookHistograms(fs);
      selHistManager->leadElectron_ = new ElectronHistManager(makeHistManager_cfg(process_and_genMatch,
        Form("%s/sel/leadElectron", histogramDir.data()), central_or_shift, 0));
      selHistManager->leadElectron_->bookHistograms(fs);
      selHistManager->subleadElectron_ = new ElectronHistManager(makeHistManager_cfg(process_and_genMatch,
        Form("%s/sel/subleadElectron", histogramDir.data()), central_or_shift, 1));
      selHistManager->subleadElectron_->bookHistograms(fs);
      selHistManager->muons_ = new MuonHistManager(makeHistManager_cfg(process_and_genMatch,
        Form("%s/sel/muons", histogramDir.data()), central_or_shift));
      selHistManager->muons_->bookHistograms(fs);
      selHistManager->leadMuon_ = new MuonHistManager(makeHistManager_cfg(process_and_genMatch,
        Form("%s/sel/leadMuon", histogramDir.data()), central_or_shift, 0));
      selHistManager->leadMuon_->bookHistograms(fs);
      selHistManager->subleadMuon_ = new MuonHistManager(makeHistManager_cfg(process_and_genMatch,
        Form("%s/sel/subleadMuon", histogramDir.data()), central_or_shift, 1));
      selHistManager->subleadMuon_->bookHistograms(fs);
      selHistManager->hadTaus_ = new HadTauHistManager(makeHistManager_cfg(process_and_genMatch,
        Form("%s/sel/hadTaus", histogramDir.data()), central_or_shift));
      selHistManager->hadTaus_->bookHistograms(fs);
      selHistManager->jets_ = new JetHistManager(makeHistManager_cfg(process_and_genMatch,
        Form("%s/sel/jets", histogramDir.data()), central_or_shift));
      selHistManager->jets_->bookHistograms(fs);
      selHistManager->leadJet_ = new JetHistManager(makeHistManager_cfg(process_and_genMatch,
        Form("%s/sel/leadJet", histogramDir.data()), central_or_shift, 0));
      selHistManager->leadJet_->bookHistograms(fs);
      selHistManager->subleadJet_ = new JetHistManager(makeHistManager_cfg(process_and_genMatch,
        Form("%s/sel/subleadJet", histogramDir.data()), central_or_shift, 1));
      selHistManager->subleadJet_->bookHistograms(fs);
      selHistManager->BJets_loose_ = new JetHistManager(makeHistManager_cfg(process_and_genMatch,
        Form("%s/sel/BJets_loose", histogramDir.data()), central_or_shift));
      selHistManager->BJets_loose_->bookHistograms(fs);
      selHistManager->leadBJet_loose_ = new JetHistManager(makeHistManager_cfg(process_and_genMatch,
        Form("%s/sel/leadBJet_loose", histogramDir.data()), central_or_shift, 0));
      selHistManager->leadBJet_loose_->bookHistograms(fs);
      selHistManager->subleadBJet_loose_ = new JetHistManager(makeHistManager_cfg(process_and_genMatch,
        Form("%s/sel/subleadBJet_loose", histogramDir.data()), central_or_shift, 1));
      selHistManager->subleadBJet_loose_->bookHistograms(fs);
      selHistManager->BJets_medium_ = new JetHistManager(makeHistManager_cfg(process_and_genMatch,
        Form("%s/sel/BJets_medium", histogramDir.data()), central_or_shift));
      selHistManager->BJets_medium_->bookHistograms(fs);
      selHistManager->met_ = new MEtHistManager(makeHistManager_cfg(process_and_genMatch,
        Form("%s/sel/met", histogramDir.data()), central_or_shift));
      selHistManager->met_->bookHistograms(fs);
      selHistManager->metFilters_ = new MEtFilterHistManager(makeHistManager_cfg(process_and_genMatch,
        Form("%s/sel/metFilters", histogramDir.data()), central_or_shift));
      selHistManager->metFilters_->bookHistograms(fs);
      selHistManager->mvaInputVariables_2lss_ = new MVAInputVarHistManager(makeHistManager_cfg(process_and_genMatch,
        Form("%s/sel/mvaInputs_2lss", histogramDir.data()), central_or_shift));
      selHistManager->mvaInputVariables_2lss_->bookHistograms(fs, mvaInputVariables_2lss);
      selHistManager->mvaInputVariables_2lss_1tau_ = new MVAInputVarHistManager(makeHistManager_cfg(process_and_genMatch,
        Form("%s/sel/mvaInputs_2lss_1tau", histogramDir.data()), central_or_shift));
      selHistManager->evt_ = new EvtHistManager_2lss_1tau(makeHistManager_cfg(process_and_genMatch,
        Form("%s/sel/evt", histogramDir.data()), era_string, central_or_shift));
      selHistManager->evt_->bookHistograms(fs);

      vstring categories_evt = {
        "2ess_1tau_btight_0J", "2ess_1tau_bloose_0J",
        "2muss_1tau_btight_0J", "2muss_1tau_bloose_0J",
        "1mu1ess_1tau_btight_0J", "1mu1ess_1tau_bloose_0J",
        "2lss_1tau_1Jp"
      };

      vstring categories_TensorFlow_2lss_ttH_3cat = {
        "output_NN_2lss_ttH_3cat_ttH", "output_NN_2lss_ttH_3cat_ttW", "output_NN_2lss_ttH_3cat_rest",
        "output_NN_2lss_ttH_3cat_tH", "output_NN_2lss_ttH_3cat_tH_1jet"
      };

      const vstring decayModes_evt = eventInfo.getDecayModes();
      if(isSignal)
      {
        for(const std::string & decayMode_evt: decayModes_evt)
        {
          std::string decayMode_and_genMatch = decayMode_evt;
          if(apply_leptonGenMatching)                            decayMode_and_genMatch += leptonGenMatch_definition -> name_;
          if(apply_leptonGenMatching && apply_hadTauGenMatching) decayMode_and_genMatch += "&";
          if(apply_hadTauGenMatching)                            decayMode_and_genMatch += hadTauGenMatch_definition -> name_;

          selHistManager -> evt_in_decayModes_[decayMode_evt] = new EvtHistManager_2lss_1tau(makeHistManager_cfg(
            decayMode_and_genMatch,
            Form("%s/sel/evt", histogramDir.data()),
            era_string,
            central_or_shift
          ));
          selHistManager -> evt_in_decayModes_[decayMode_evt] -> bookHistograms(fs);
          for ( vstring::const_iterator category = categories_evt.begin();
                category != categories_evt.end(); ++category ) {
            TString histogramDir_category = histogramDir.data();
            histogramDir_category.ReplaceAll("2lss_1tau", category->data());
            selHistManager->evt_in_categories_in_decayModes_[category->data()+decayMode_evt] = new EvtHistManager_2lss_1tau(makeHistManager_cfg(
              decayMode_and_genMatch,
              Form("%s/sel/evt", histogramDir_category.Data()),
              era_string,
              central_or_shift));
            selHistManager->evt_in_categories_in_decayModes_[category->data()+decayMode_evt]->bookHistograms(fs);
          }
          for ( vstring::const_iterator category = categories_TensorFlow_2lss_ttH_3cat.begin();
          category != categories_TensorFlow_2lss_ttH_3cat.end(); ++category ) {
            TString histogramDir_category = histogramDir.data();
            histogramDir_category.ReplaceAll("2lss",  category->data());
            selHistManager -> evt_in_categories_2lss_ttH_3cat_TF_and_decayModes_[category->data()+decayMode_evt] = new EvtHistManager_2lss_1tau(makeHistManager_cfg(
              decayMode_and_genMatch,
              Form("%s/sel/evt", histogramDir_category.Data()),
              era_string,
              central_or_shift
            ));
            selHistManager -> evt_in_categories_2lss_ttH_3cat_TF_and_decayModes_[category->data()+decayMode_evt] -> bookHistograms(fs);
          }
        }
      }

      for ( vstring::const_iterator category = categories_evt.begin();
            category != categories_evt.end(); ++category ) {
        TString histogramDir_category = histogramDir.data();
        histogramDir_category.ReplaceAll("2lss_1tau", category->data());
        selHistManager->evt_in_categories_[*category] = new EvtHistManager_2lss_1tau(makeHistManager_cfg(process_and_genMatch,
          Form("%s/sel/evt", histogramDir_category.Data()), era_string, central_or_shift));
        selHistManager->evt_in_categories_[*category]->bookHistograms(fs);
      }

      for ( vstring::const_iterator category = categories_TensorFlow_2lss_ttH_3cat.begin();
        category != categories_TensorFlow_2lss_ttH_3cat.end(); ++category ) {
        TString histogramDir_category = histogramDir.data();
        histogramDir_category.ReplaceAll("2lss",  category->data());
        selHistManager->evt_in_categories_2lss_ttH_3cat_TF_[*category] = new EvtHistManager_2lss_1tau(makeHistManager_cfg(process_and_genMatch,
          Form("%s/sel/evt", histogramDir_category.Data()), era_string, central_or_shift));
        selHistManager->evt_in_categories_2lss_ttH_3cat_TF_[*category]->bookHistograms(fs);
      }

      edm::ParameterSet cfg_EvtYieldHistManager_sel = makeHistManager_cfg(process_and_genMatch,
        Form("%s/sel/evtYield", histogramDir.data()), central_or_shift);
      cfg_EvtYieldHistManager_sel.addParameter<edm::ParameterSet>("runPeriods", cfg_EvtYieldHistManager);
      cfg_EvtYieldHistManager_sel.addParameter<bool>("isMC", isMC);
      selHistManager->evtYield_ = new EvtYieldHistManager(cfg_EvtYieldHistManager_sel);
      selHistManager->evtYield_->bookHistograms(fs);
      selHistManager->weights_ = new WeightHistManager(makeHistManager_cfg(process_and_genMatch,
        Form("%s/sel/weights", histogramDir.data()), central_or_shift));
      selHistManager->weights_->bookHistograms(fs, { "genWeight", "pileupWeight", "triggerWeight", "data_to_MC_correction", "fakeRate" });
      selHistManagers[idxLepton][idxHadTau] = selHistManager;

    }
  }

  GenEvtHistManager* genEvtHistManager_beforeCuts = 0;
  GenEvtHistManager* genEvtHistManager_afterCuts = 0;
  LHEInfoHistManager* lheInfoHistManager = 0;
  if ( isMC ) {
    genEvtHistManager_beforeCuts = new GenEvtHistManager(makeHistManager_cfg(process_string,
      Form("%s/unbiased/genEvt", histogramDir.data()), central_or_shift));
    genEvtHistManager_beforeCuts->bookHistograms(fs);
    genEvtHistManager_afterCuts = new GenEvtHistManager(makeHistManager_cfg(process_string,
      Form("%s/sel/genEvt", histogramDir.data()), central_or_shift));
    genEvtHistManager_afterCuts->bookHistograms(fs);
    lheInfoHistManager = new LHEInfoHistManager(makeHistManager_cfg(process_string,
      Form("%s/sel/lheInfo", histogramDir.data()), central_or_shift));
    lheInfoHistManager->bookHistograms(fs);

    if(eventWeightManager)
    {
      genEvtHistManager_beforeCuts->bookHistograms(fs, eventWeightManager);
      genEvtHistManager_afterCuts->bookHistograms(fs, eventWeightManager);
    }
  }

  NtupleFillerBDT<float, int>* bdt_filler = nullptr;
  typedef std::remove_pointer<decltype(bdt_filler)>::type::float_type float_type;
  typedef std::remove_pointer<decltype(bdt_filler)>::type::int_type int_type;

  if ( selectBDT ) {
    bdt_filler = new std::remove_pointer<decltype(bdt_filler)>::type(
      makeHistManager_cfg(process_string, Form("%s/sel/evtntuple", histogramDir.data()), central_or_shift)
    );
    bdt_filler->register_variable<float_type>(
      "lep1_pt", "lep1_conePt", "lep1_eta", "lep1_tth_mva", "mindr_lep1_jet",
      "mindr_lep2_jet", "mT_lep1",  "MT_met_lep1", "dr_lep1_tau",
      "lep2_pt", "lep2_conePt", "lep2_eta", "max_lep_eta", "avg_dr_lep",
      "lep2_tth_mva", "mT_lep2", "dr_lep2_tau",
      "mindr_tau_jet", "avg_dr_jet",  "nJet25_Recl", "ptmiss", "htmiss",
      "tau_mva", "tau_pt", "tau_eta", "dr_leps",
      "mTauTauVis1", "mTauTauVis2",
      "memOutput_isValid",   "memOutput_errorFlag",  "memOutput_LR",
      //"memOutput_tt_LR", "memOutput_ttZ_LR",
      //"memOutput_tt_LR",  "memOutput_ttZ_LR", "memOutput_ttZ_Zll_LR",
      //"log_memOutput_ttH",  "log_memOutput_ttZ",  "log_memOutput_ttZ_Zll", "log_memOutput_tt",
      "lep1_genLepPt", "lep2_genLepPt",
      "tau_genTauPt",
      "lep1_fake_prob", "lep2_fake_prob",  "tau_fake_prob", "tau_fake_test",
      "Hj_tagger",
      "genWeight", "evtWeight",
      "HadTop_pt", "HadTop_eta", "genTopPt","min(met_pt,400)",
      "mbb","ptbb", "mbb_loose","ptbb_loose",
      "res-HTT", "res-HTT_IHEP",
      "res-HTT_CSVsort4rd", "res-HTT_highestCSV",
      "res-HTT_CSVsort4rd_WithKinFit", "res-HTT_highestCSV_WithKinFit",
      "minDR_HTTv2_lep", "minDR_HTTv2_tau", "minDR_HTTv2_L",
      "minDR_AK8_lep", "DR_AK8_tau", "minDR_AK8_L",
      "HTTv2_lead_pt",
      "HTTv2_lead_mass",
      "HadTop_pt_multilep",
      "HadTop_pt_CSVsort4rd", "HadTop_pt_highestCSV",
      "HadTop_pt_CSVsort4rd_WithKinFit", "HadTop_pt_highestCSV_WithKinFit",
      "genTopPt_multilep",
      "genTopPt_CSVsort4rd", "genTopPt_highestCSV",
      "genTopPt_CSVsort4rd_WithKinFit", "genTopPt_highestCSV_WithKinFit",
      "HTT_boosted", "genTopPt_boosted", "HadTop_pt_HTT_boosted",
      "HTT_boosted_WithKinFit", "genTopPt_boosted_WithKinFit", "HadTop_pt_HTT_boosted_WithKinFit",
      "HTT_semi_boosted_AK8", "genTopPt_semi_boosted", "HadTop_pt_HTT_semi_boosted_AK8",
      "HTT_semi_boosted_AK8_WithKinFit", "genTopPt_semi_boosted_WithKinFit", "HadTop_pt_HTT_semi_boosted_AK8_WithKinFit",
      "mvaOutput_2lss_1tau_HTTMEM_SUM_M"
    );
    bdt_filler->register_variable<int_type>(
      "nJet", "nBJetLoose", "nBJetMedium", "nLep","nTau",
      "lep1_isTight", "lep2_isTight", "tau_isTight","failsTightChargeCut", "nHTTv2", "nElectron", "nMuon",
      "N_jetAK8",
      "hadtruth", "hadtruth_boosted", "hadtruth_semi_boosted_AK8",
      "bWj1Wj2_isGenMatchedWithKinFit", "bWj1Wj2_isGenMatched_IHEP",
      "bWj1Wj2_isGenMatched_CSVsort4rd", "bWj1Wj2_isGenMatched_highestCSV",
      "bWj1Wj2_isGenMatched_CSVsort4rd_WithKinFit", "bWj1Wj2_isGenMatched_highestCSV_WithKinFit",
      "bWj1Wj2_isGenMatched_boosted", "bWj1Wj2_isGenMatched_boosted_WithKinFit",
      "bWj1Wj2_isGenMatched_semi_boosted_AK8", "bWj1Wj2_isGenMatched_semi_boosted_AK8_WithKinFit"
    );
    bdt_filler->bookTree(fs);
  }

  int analyzedEntries = 0;
  int selectedEntries = 0;
  double selectedEntries_weighted = 0.;
  TH1* histogram_analyzedEntries = fs.make<TH1D>("analyzedEntries", "analyzedEntries", 1, -0.5, +0.5);
  TH1* histogram_selectedEntries = fs.make<TH1D>("selectedEntries", "selectedEntries", 1, -0.5, +0.5);
  cutFlowTableType cutFlowTable;
  const edm::ParameterSet cutFlowTableCfg = makeHistManager_cfg(
    process_string, Form("%s/sel/cutFlow", histogramDir.data()), central_or_shift
  );
  const std::vector<std::string> cuts = {
    "run:ls:event selection",
    "trigger",
    ">= 2 presel leptons",
    "presel lepton trigger match",
    ">= 2 jets",
    ">= 2 loose b-jets || 1 medium b-jet (1)",
    ">= 1 sel tau (1)",
    ">= 2 sel leptons",
    "<= 2 tight leptons",
    "fakeable lepton trigger match",
    "HLT filter matching",
    ">= 3 jets",
    ">= 2 loose b-jets || 1 medium b-jet (2)",
    ">= 1 sel tau (2)",
    "<= 1 veto taus",
    "m(ll) > 12 GeV",
    "lead lepton pT > 25 GeV && sublead lepton pT > 15(e)/10(mu) GeV",
    "tight lepton charge",
    "sel lepton-pair OS/SS charge",
    "sel lepton+tau charge",
    "Z-boson mass veto",
    "met LD > 30 GeV",
    "MEt filters",
    "sel lepton-pair gen=rec charge match",
    "signal region veto",
  };
  CutFlowTableHistManager * cutFlowHistManager = new CutFlowTableHistManager(cutFlowTableCfg, cuts);
  cutFlowHistManager->bookHistograms(fs);

  int contHTTv2_noclean = 0;
  int contHTTv2_clean = 0;
  double count_ttH_like = 0;
  double count_tH_like = 0;
  while(inputTree -> hasNextEvent() && (! run_lumi_eventSelector || (run_lumi_eventSelector && ! run_lumi_eventSelector -> areWeDone())))
  {
    if(inputTree -> canReport(reportEvery))
    {
      std::cout << "processing Entry " << inputTree -> getCurrentMaxEventIdx()
                << " or " << inputTree -> getCurrentEventIdx() << " entry in #"
                << (inputTree -> getProcessedFileCount() - 1)
                << " (" << eventInfo
                << ") file (" << selectedEntries << " Entries selected)\n";
    }
    ++analyzedEntries;
    //if (analyzedEntries > 10000) break;
    histogram_analyzedEntries->Fill(0.);

    if (run_lumi_eventSelector && !(*run_lumi_eventSelector)(eventInfo))
    {
      continue;
    }

    cutFlowTable.update("run:ls:event selection");
    cutFlowHistManager->fillHistograms("run:ls:event selection", lumiScale);

    if ( isDEBUG ) {
      std::cout << "event #" << inputTree -> getCurrentMaxEventIdx() << ' ' << eventInfo << '\n';
    }

    if(run_lumi_eventSelector)
    {
      std::cout << "processing Entry " << inputTree -> getCurrentMaxEventIdx() << ": " << eventInfo << '\n';
      if(inputTree -> isOpen())
      {
        std::cout << "input File = " << inputTree -> getCurrentFileName() << '\n';
      }
    }

//--- build collections of generator level particles (before any cuts are applied, to check distributions in unbiased event samples)
    std::vector<GenLepton> genLeptons;
    std::vector<GenLepton> genElectrons;
    std::vector<GenLepton> genMuons;
    std::vector<GenHadTau> genHadTaus;
    std::vector<GenPhoton> genPhotons;
    std::vector<GenJet> genJets;
    if ( isMC && fillGenEvtHistograms ) {
      if ( genLeptonReader ) {
        genLeptons = genLeptonReader->read();
        for ( std::vector<GenLepton>::const_iterator genLepton = genLeptons.begin();
              genLepton != genLeptons.end(); ++genLepton ) {
          int abs_pdgId = std::abs(genLepton->pdgId());
          if      ( abs_pdgId == 11 ) genElectrons.push_back(*genLepton);
          else if ( abs_pdgId == 13 ) genMuons.push_back(*genLepton);
        }
      }
      if ( genHadTauReader ) {
        genHadTaus = genHadTauReader->read();
      }
      if ( genPhotonReader ) {
        genPhotons = genPhotonReader->read();
      }
      if ( genJetReader ) {
        genJets = genJetReader->read();
      }
    }

    double evtWeight_inclusive = 1.;
    if(isMC)
    {
      if(apply_genWeight)    evtWeight_inclusive *= boost::math::sign(eventInfo.genWeight);
      if(isMC_tH)            evtWeight_inclusive *= eventInfo.genWeight_tH;
      if(eventWeightManager) evtWeight_inclusive *= eventWeightManager->getWeight();
      lheInfoReader->read();
      evtWeight_inclusive *= lheInfoReader->getWeight_scale(lheScale_option);
      evtWeight_inclusive *= eventInfo.pileupWeight;
      evtWeight_inclusive *= lumiScale;
      genEvtHistManager_beforeCuts->fillHistograms(genElectrons, genMuons, genHadTaus, genPhotons, genJets, evtWeight_inclusive);
      if(eventWeightManager)
      {
        genEvtHistManager_beforeCuts->fillHistograms(eventWeightManager, evtWeight_inclusive);
      }
    }

    bool isTriggered_1e = hltPaths_isTriggered(triggers_1e, isDEBUG);
    bool isTriggered_2e = hltPaths_isTriggered(triggers_2e, isDEBUG);
    bool isTriggered_1mu = hltPaths_isTriggered(triggers_1mu, isDEBUG);
    bool isTriggered_2mu = hltPaths_isTriggered(triggers_2mu, isDEBUG);
    bool isTriggered_1e1mu = hltPaths_isTriggered(triggers_1e1mu, isDEBUG);

    bool selTrigger_1e = use_triggers_1e && isTriggered_1e;
    bool selTrigger_2e = use_triggers_2e && isTriggered_2e;
    bool selTrigger_1mu = use_triggers_1mu && isTriggered_1mu;
    bool selTrigger_2mu = use_triggers_2mu && isTriggered_2mu;
    bool selTrigger_1e1mu = use_triggers_1e1mu && isTriggered_1e1mu;

    //--- build collections of generator level particles
    //std::cout << "built gen variable" << std::endl;
    std::vector<GenParticle> genTopQuarks;
    std::vector<GenParticle> genBJets;
    std::vector<GenParticle> genWBosons;
    std::vector<GenParticle> genWJets;
    std::vector<GenParticle> genQuarkFromTop;
    if ( isMC ) {
      genTopQuarks = genTopQuarkReader->read();
      genBJets = genBJetReader->read();
      genWBosons = genWBosonReader->read();
      genWJets = genWJetReader->read();
      genQuarkFromTop = genQuarkFromTopReader->read();
    }

    if ( !(selTrigger_1e || selTrigger_2e || selTrigger_1mu || selTrigger_2mu || selTrigger_1e1mu) ) {
      if ( run_lumi_eventSelector ) {
        std::cout << "event " << eventInfo.str() << " FAILS trigger selection." << std::endl;
        std::cout << " (selTrigger_1e = " << selTrigger_1e
                  << ", selTrigger_2e = " << selTrigger_2e
                  << ", selTrigger_1mu = " << selTrigger_1mu
                  << ", selTrigger_2mu = " << selTrigger_2mu
                  << ", selTrigger_1e1mu = " << selTrigger_1e1mu << ")" << std::endl;
      }
      continue;
    }

//--- rank triggers by priority and ignore triggers of lower priority if a trigger of higher priority has fired for given event;
//    the ranking of the triggers is as follows: 2mu, 1e1mu, 2e, 1mu, 1e
// CV: this logic is necessary to avoid that the same event is selected multiple times when processing different primary datasets
    if ( !isMC && !isDEBUG ) {
      if ( selTrigger_1e && (isTriggered_2e || isTriggered_1mu || isTriggered_2mu || isTriggered_1e1mu) ) {
        if ( run_lumi_eventSelector ) {
          std::cout << "event " << eventInfo.str() << " FAILS trigger selection." << std::endl;
          std::cout << " (selTrigger_1e = " << selTrigger_1e
                    << ", isTriggered_2e = " << isTriggered_2e
                    << ", isTriggered_1mu = " << isTriggered_1mu
                    << ", isTriggered_2mu = " << isTriggered_2mu
                    << ", isTriggered_1e1mu = " << isTriggered_1e1mu << ")" << std::endl;
        }
        continue;
      }
      if ( selTrigger_2e && (isTriggered_2mu || isTriggered_1e1mu) ) {
        if ( run_lumi_eventSelector ) {
          std::cout << "event " << eventInfo.str() << " FAILS trigger selection." << std::endl;
          std::cout << " (selTrigger_2e = " << selTrigger_2e
                    << ", isTriggered_2mu = " << isTriggered_2mu
                    << ", isTriggered_1e1mu = " << isTriggered_1e1mu << ")" << std::endl;
        }
        continue;
      }
      if ( selTrigger_1mu && (isTriggered_2e || isTriggered_2mu || isTriggered_1e1mu) ) {
        if ( run_lumi_eventSelector ) {
          std::cout << "event " << eventInfo.str() << " FAILS trigger selection." << std::endl;
          std::cout << " (selTrigger_1mu = " << selTrigger_1mu
                    << ", isTriggered_2e = " << isTriggered_2e
                    << ", isTriggered_2mu = " << isTriggered_2mu
                    << ", isTriggered_1e1mu = " << isTriggered_1e1mu << ")" << std::endl;
        }
        continue;
      }
      if ( selTrigger_1e1mu && isTriggered_2mu ) {
        if ( run_lumi_eventSelector ) {
          std::cout << "event " << eventInfo.str() << " FAILS trigger selection." << std::endl;
          std::cout << " (selTrigger_1e1mu = " << selTrigger_1e1mu
                    << ", isTriggered_2mu = " << isTriggered_2mu << ")" << std::endl;
        }
        continue;
      }
    }
    cutFlowTable.update("trigger");
    cutFlowHistManager->fillHistograms("trigger", lumiScale);

    if ( (selTrigger_2mu   && !apply_offline_e_trigger_cuts_2mu)   ||
         (selTrigger_1mu   && !apply_offline_e_trigger_cuts_1mu)   ||
         (selTrigger_2e    && !apply_offline_e_trigger_cuts_2e)    ||
         (selTrigger_1e1mu && !apply_offline_e_trigger_cuts_1e1mu) ||
         (selTrigger_1e    && !apply_offline_e_trigger_cuts_1e)    ) {
      fakeableElectronSelector.disable_offline_e_trigger_cuts();
      tightElectronSelector.disable_offline_e_trigger_cuts();
    } else {
      fakeableElectronSelector.enable_offline_e_trigger_cuts();
      tightElectronSelector.enable_offline_e_trigger_cuts();
    }

//--- build collections of electrons, muons and hadronic taus;
//    resolve overlaps in order of priority: muon, electron,
    std::vector<RecoMuon> muons = muonReader->read();
    std::vector<const RecoMuon*> muon_ptrs = convert_to_ptrs(muons);
    std::vector<const RecoMuon*> cleanedMuons = muon_ptrs; // CV: no cleaning needed for muons, as they have the highest priority in the overlap removal
    std::vector<const RecoMuon*> preselMuons = preselMuonSelector(cleanedMuons, isHigherConePt);
    std::vector<const RecoMuon*> fakeableMuons = fakeableMuonSelector(preselMuons, isHigherConePt);
    std::vector<const RecoMuon*> tightMuons = tightMuonSelector(fakeableMuons, isHigherConePt);
    if(isDEBUG || run_lumi_eventSelector)
    {
      printCollection("preselMuons",   preselMuons);
      printCollection("fakeableMuons", fakeableMuons);
      printCollection("tightMuons",    tightMuons);
    }

    std::vector<RecoElectron> electrons = electronReader->read();
    std::vector<const RecoElectron*> electron_ptrs = convert_to_ptrs(electrons);
    std::vector<const RecoElectron*> cleanedElectrons = electronCleaner(electron_ptrs, preselMuons);
    std::vector<const RecoElectron*> preselElectrons = preselElectronSelector(cleanedElectrons, isHigherConePt);
    std::vector<const RecoElectron*> fakeableElectrons = fakeableElectronSelector(preselElectrons, isHigherConePt);
    std::vector<const RecoElectron*> tightElectrons = tightElectronSelector(fakeableElectrons, isHigherConePt);
    if(isDEBUG || run_lumi_eventSelector)
    {
      printCollection("preselElectrons",   preselElectrons);
      printCollection("fakeableElectrons", fakeableElectrons);
      printCollection("tightElectrons",    tightElectrons);
    }

    std::vector<const RecoLepton*> preselLeptonsFull = mergeLeptonCollections(preselElectrons, preselMuons, isHigherConePt);
    std::vector<const RecoLepton*> fakeableLeptonsFull = mergeLeptonCollections(fakeableElectrons, fakeableMuons, isHigherConePt);
    std::vector<const RecoLepton*> tightLeptonsFull = mergeLeptonCollections(tightElectrons, tightMuons, isHigherConePt);

    std::vector<const RecoLepton*> preselLeptons = pickFirstNobjects(preselLeptonsFull, 2);
    std::vector<const RecoLepton*> fakeableLeptons = pickFirstNobjects(fakeableLeptonsFull, 2);
    std::vector<const RecoLepton*> tightLeptons = getIntersection(fakeableLeptons, tightLeptonsFull, isHigherConePt);

    std::vector<const RecoLepton*> selLeptons;
    std::vector<const RecoMuon*> selMuons;
    std::vector<const RecoElectron*> selElectrons;
    if(electronSelection == muonSelection)
    {
      // for SR, flip region and fake CR
      // doesn't matter if we supply electronSelection or muonSelection here
      selLeptons = selectObjects(muonSelection, preselLeptons, fakeableLeptons, tightLeptons);
      selMuons = getIntersection(preselMuons, selLeptons, isHigherConePt);
      selElectrons = getIntersection(preselElectrons, selLeptons, isHigherConePt);
    }
    else
    {
      // for MC closure
      // make sure that neither electron nor muon selections are loose
      assert(electronSelection != kLoose && muonSelection != kLoose);
      selMuons = selectObjects(muonSelection, preselMuons, fakeableMuons, tightMuons);
      selElectrons = selectObjects(electronSelection, preselElectrons, fakeableElectrons, tightElectrons);
      std::vector<const RecoLepton*> selLeptons_full = mergeLeptonCollections(selElectrons, selMuons, isHigherConePt);
      selLeptons = getIntersection(fakeableLeptons, selLeptons_full, isHigherConePt);
    }

    std::vector<RecoHadTau> hadTaus = hadTauReader->read();
    std::vector<const RecoHadTau*> hadTau_ptrs = convert_to_ptrs(hadTaus);
    std::vector<const RecoHadTau*> cleanedHadTaus = hadTauCleaner(hadTau_ptrs, preselMuons, preselElectrons);
    std::vector<const RecoHadTau*> preselHadTausFull = preselHadTauSelector(cleanedHadTaus, isHigherPt);
    std::vector<const RecoHadTau*> fakeableHadTausFull = fakeableHadTauSelector(preselHadTausFull, isHigherPt);
    std::vector<const RecoHadTau*> tightHadTausFull = tightHadTauSelector(fakeableHadTausFull, isHigherPt);

    std::vector<const RecoHadTau*> preselHadTaus = pickFirstNobjects(preselHadTausFull, 1);
    std::vector<const RecoHadTau*> fakeableHadTaus = pickFirstNobjects(fakeableHadTausFull, 1);
    std::vector<const RecoHadTau*> tightHadTaus = getIntersection(fakeableHadTaus, tightHadTausFull, isHigherPt);
    std::vector<const RecoHadTau*> selHadTaus = selectObjects(hadTauSelection, preselHadTaus, fakeableHadTaus, tightHadTaus);
    if(isDEBUG || run_lumi_eventSelector)
    {
      printCollection("preselHadTaus",   preselHadTaus);
      printCollection("fakeableHadTaus", fakeableHadTaus);
      printCollection("tightHadTaus",    tightHadTaus);
    }

    if(isDEBUG || run_lumi_eventSelector)
    {
      printCollection("selMuons", selMuons);
      printCollection("selElectrons", selElectrons);
      printCollection("selLeptons", selLeptons);
      printCollection("selHadTaus", selHadTaus);
    }

    // CV: veto events containing more than one tau passing the VTight WP, to avoid overlap with the 2l+2tau category
    std::vector<const RecoHadTau*> vetoHadTaus = vetoHadTauSelector(cleanedHadTaus, isHigherPt);

  //--- build collections of jets reconstructed by hep-top-tagger (HTTv2) algorithm
  std::vector<RecoJetHTTv2> jetsHTTv2 = jetReaderHTTv2->read();
  std::vector<const RecoJetHTTv2*> jet_ptrsHTTv2raw = convert_to_ptrs(jetsHTTv2);
  std::vector<const RecoJetHTTv2*> cleanedJetsHTTv2 = jetCleanerHTTv2SubJets(jet_ptrsHTTv2raw, selMuons, selElectrons, selHadTaus);
  std::vector<const RecoJetHTTv2*> sel_HTTv2 =  jetSelectorHTTv2(cleanedJetsHTTv2, isHigherPt);

//--- build collections of jets reconstructed by anti-kT algorithm with dR=0.8 (AK8)
    std::vector<RecoJetAK8> jetsAK8 = jetReaderAK8->read();
    std::vector<const RecoJetAK8*> jet_ptrsAK8raw = convert_to_ptrs(jetsAK8);
    std::vector<const RecoJetAK8*> jet_ptrsAK8;
    std::vector<const RecoJetAK8*> cleanedJetsAK8 = jetCleanerAK8SubJets(jet_ptrsAK8raw, selMuons, selElectrons, selHadTaus);
    jet_ptrsAK8 = jetSelectorAK8(cleanedJetsAK8, isHigherPt);
    //std::cout << "after load ak8"  << std::endl;

//--- build collections of jets and select subset of jets passing b-tagging criteria
    std::vector<RecoJet> jets = jetReader->read();
    std::vector<const RecoJet*> jet_ptrs = convert_to_ptrs(jets);
    std::vector<const RecoJet*> cleanedJets = jetCleaner(jet_ptrs, fakeableLeptons, fakeableHadTaus);
    std::vector<const RecoJet*> selJets = jetSelector(cleanedJets, isHigherPt);
    std::vector<const RecoJet*> selBJets_loose = jetSelectorBtagLoose(cleanedJets, isHigherPt);
    std::vector<const RecoJet*> selBJets_medium = jetSelectorBtagMedium(cleanedJets, isHigherPt);
    std::vector<const RecoJet*> selJetsForward = jetSelectorForward(jet_ptrs, isHigherPt);
    if(isDEBUG || run_lumi_eventSelector)
    {
      printCollection("uncleanedJets", jet_ptrs);
      printCollection("selJets",       selJets);
    }

//--- cleaned RecoJet collection from AK8 as well
    // -- to make the semi-boosted tagger but keep b-tag ordering consistent in cat2
    std::vector<const RecoJet*> cleanedJets_fromAK8;
    cleanedJets_fromAK8 = jetCleaner(selJets, jet_ptrsAK8);

//--- build collections of generator level particles (after some cuts are applied, to safe computing time)
    if ( isMC && redoGenMatching && !fillGenEvtHistograms ) {
      if ( genLeptonReader ) {
        genLeptons = genLeptonReader->read();
        for ( std::vector<GenLepton>::const_iterator genLepton = genLeptons.begin();
              genLepton != genLeptons.end(); ++genLepton ) {
          int abs_pdgId = std::abs(genLepton->pdgId());
          if      ( abs_pdgId == 11 ) genElectrons.push_back(*genLepton);
          else if ( abs_pdgId == 13 ) genMuons.push_back(*genLepton);
        }
      }
      if ( genHadTauReader ) {
        genHadTaus = genHadTauReader->read();
      }
      if ( genPhotonReader ) {
        genPhotons = genPhotonReader->read();
      }
      if ( genJetReader ) {
        genJets = genJetReader->read();
      }
    }

//--- match reconstructed to generator level particles
    if ( isMC && redoGenMatching ) {
      muonGenMatcher.addGenLeptonMatch(preselMuons, genLeptons, 0.2);
      muonGenMatcher.addGenHadTauMatch(preselMuons, genHadTaus, 0.2);
      muonGenMatcher.addGenJetMatch(preselMuons, genJets, 0.2);

      electronGenMatcher.addGenLeptonMatch(preselElectrons, genLeptons, 0.2);
      electronGenMatcher.addGenHadTauMatch(preselElectrons, genHadTaus, 0.2);
      electronGenMatcher.addGenPhotonMatch(preselElectrons, genPhotons, 0.2);
      electronGenMatcher.addGenJetMatch(preselElectrons, genJets, 0.2);

      hadTauGenMatcher.addGenLeptonMatch(selHadTaus, genLeptons, 0.2);
      hadTauGenMatcher.addGenHadTauMatch(selHadTaus, genHadTaus, 0.2);
      hadTauGenMatcher.addGenJetMatch(selHadTaus, genJets, 0.2);

      jetGenMatcher.addGenLeptonMatch(selJets, genLeptons, 0.2);
      jetGenMatcher.addGenHadTauMatch(selJets, genHadTaus, 0.2);
      jetGenMatcher.addGenJetMatch(selJets, genJets, 0.2);
    }

//--- apply preselection
    // require at least two leptons passing loose preselection criteria
    if ( !(preselLeptonsFull.size() >= 2) ) {
      if ( run_lumi_eventSelector ) {
        std::cout << "event " << eventInfo.str() << " FAILS preselLeptons selection." << std::endl;
        printCollection("preselLeptons", preselLeptonsFull);
      }
      continue;
    }
    cutFlowTable.update(">= 2 presel leptons");
    cutFlowHistManager->fillHistograms(">= 2 presel leptons", lumiScale);
    const RecoLepton* preselLepton_lead = preselLeptonsFull[0];
    const RecoLepton* preselLepton_sublead = preselLeptonsFull[1];
    const leptonGenMatchEntry& preselLepton_genMatch = getLeptonGenMatch(leptonGenMatch_definitions, preselLepton_lead, preselLepton_sublead);
    int idxPreselLepton_genMatch = preselLepton_genMatch.idx_;
    assert(idxPreselLepton_genMatch != kGen_LeptonUndefined2);

    // require that trigger paths match event category (with event category based on preselLeptons)
    if ( !((preselElectrons.size() >= 2 &&                            (selTrigger_2e    || selTrigger_1e                  )) ||
           (preselElectrons.size() >= 1 && preselMuons.size() >= 1 && (selTrigger_1e1mu || selTrigger_1mu || selTrigger_1e)) ||
           (                               preselMuons.size() >= 2 && (selTrigger_2mu   || selTrigger_1mu                 ))) ) {
      if ( run_lumi_eventSelector ) {
        std::cout << "event " << eventInfo.str() << " FAILS trigger selection for given preselLepton multiplicity." << std::endl;
        std::cout << " (#preselElectrons = " << preselElectrons.size()
                  << ", #preselMuons = " << preselMuons.size()
                  << ", selTrigger_2mu = " << selTrigger_2mu
                  << ", selTrigger_1e1mu = " << selTrigger_1e1mu
                  << ", selTrigger_2e = " << selTrigger_2e
                  << ", selTrigger_1mu = " << selTrigger_1mu
                  << ", selTrigger_1e = " << selTrigger_1e << ")" << std::endl;
      }
      continue;
    }
    cutFlowTable.update("presel lepton trigger match");
    cutFlowHistManager->fillHistograms("presel lepton trigger match", lumiScale);

    /*
    // apply requirement on jets (incl. b-tagged jets) and hadronic taus on preselection level
    if ( !(selJets.size() >= 2) ) {
      if ( run_lumi_eventSelector ) {
        std::cout << "event " << eventInfo.str() << " FAILS selJets selection (1)." << std::endl;
        printCollection("selJets", selJets);
      }
      continue;
    }
    cutFlowTable.update(">= 2 jets");
    cutFlowHistManager->fillHistograms(">= 2 jets", lumiScale);
    if ( !(selBJets_loose.size() >= 2 || selBJets_medium.size() >= 1) ) {
      if ( run_lumi_eventSelector ) {
        std::cout << "event " << eventInfo.str() << " FAILS selBJets selection (1)." << std::endl;
        printCollection("selJets", selJets);
        printCollection("selBJets_loose", selBJets_loose);
        printCollection("selBJets_medium", selBJets_medium);
      }
      continue;
    }
    cutFlowTable.update(">= 2 loose b-jets || 1 medium b-jet (1)");
    cutFlowHistManager->fillHistograms(">= 2 loose b-jets || 1 medium b-jet (1)", lumiScale);
    */
    bool tH_like = false;
    bool tH_like_1jet = false;
    bool ttH_like = false;

    if ((selBJets_loose.size() >= 2 || selBJets_medium.size() >= 1) && ((int)selJets.size() >= 3)) {
      ttH_like = true;
    }
    if ((selBJets_medium.size() >= 1 && ((selJets.size() - selBJets_medium.size()) + selJetsForward.size()) >= 1) && (selJets.size() >= 2)) {tH_like = true;} // Xanda -- adapted logic
    if ((selBJets_medium.size() >= 1 && ((selJets.size() - selBJets_medium.size()) + selJetsForward.size()) >= 1) && (selJets.size() >= 1))  tH_like_1jet =true;
    if ( tH_like && 0 > 1 ) std::cout <<
    "selBJets_medium.size() = "<< selBJets_medium.size() << "\n" <<
    "selBJets_loose.size() = "<< selBJets_loose.size() << "\n" <<
    "selJets.size() = " << selJets.size() << "\n" <<
    "selJetsForward.size()" << selJetsForward.size() << "\n ================ \n";
    if (!(tH_like || ttH_like || tH_like_1jet))
    {
      if ( run_lumi_eventSelector ) {
    std::cout << "event " << eventInfo.str() << " FAILS selBJets selection adding tH-like and ttW-like (2)." << std::endl;
  printCollection("selJets", selJets);
  printCollection("selBJets_loose", selBJets_loose);
  printCollection("selBJets_medium", selBJets_medium);
      }
      continue;
    }


    if ( !(selHadTaus.size() >= 1) ) {
      if ( run_lumi_eventSelector ) {
        std::cout << "event " << eventInfo.str() << " FAILS selHadTaus selection." << std::endl;
        printCollection("selHadTaus", selHadTaus);
      }
      continue;
    }
    cutFlowTable.update(">= 1 sel tau (1)");
    cutFlowHistManager->fillHistograms(">= 1 sel tau (1)", lumiScale);
    const RecoHadTau* selHadTau = selHadTaus[0];
    const hadTauGenMatchEntry& selHadTau_genMatch = getHadTauGenMatch(hadTauGenMatch_definitions, selHadTau);
    int idxSelHadTau_genMatch = selHadTau_genMatch.idx_;
    assert(idxSelHadTau_genMatch != kGen_HadTauUndefined1);

//--- compute MHT and linear MET discriminant (met_LD)
    RecoMEt met = metReader->read();
    Particle::LorentzVector mht_p4 = compMHT(fakeableLeptons, fakeableHadTaus, selJets);
    double met_LD = compMEt_LD(met.p4(), mht_p4);

    double mTauTauVis1_presel = (preselLepton_lead->p4() + selHadTau->p4()).mass();
    double mTauTauVis2_presel = (preselLepton_sublead->p4() + selHadTau->p4()).mass();

//--- fill histograms with events passing preselection
    preselHistManagerType* preselHistManager = preselHistManagers[idxPreselLepton_genMatch][idxSelHadTau_genMatch];
    assert(preselHistManager != 0);

    preselHistManager->electrons_->fillHistograms(preselElectrons, 1.);
    preselHistManager->muons_->fillHistograms(preselMuons, 1.);
    preselHistManager->hadTaus_->fillHistograms(selHadTaus, 1.);
    preselHistManager->jets_->fillHistograms(selJets, 1.);
    preselHistManager->BJets_loose_->fillHistograms(selBJets_loose, 1.);
    preselHistManager->BJets_medium_->fillHistograms(selBJets_medium, 1.);
    preselHistManager->met_->fillHistograms(met, mht_p4, met_LD, 1.);
    preselHistManager->metFilters_->fillHistograms(metFilters, 1.);
    preselHistManager->evt_->fillHistograms(
      preselElectrons.size(), preselMuons.size(), selHadTaus.size(),
      selJets.size(), selBJets_loose.size(), selBJets_medium.size(),
      1.0, // evtWeight is first to be sure of not being loosing counting
      -1., -1., -1., -1., -1., -1., -1., -1.,
      mTauTauVis1_presel, mTauTauVis2_presel,
      -1.
    );
    preselHistManager->evtYield_->fillHistograms(eventInfo, 1.);

//--- apply final event selection
    if ( !(selLeptons.size() >= 2) ) {
      if ( run_lumi_eventSelector ) {
        std::cout << "event " << eventInfo.str() << " FAILS selLeptons selection." << std::endl;
        printCollection("selLeptons", selLeptons);
      }
      continue;
    }
    cutFlowTable.update(">= 2 sel leptons", 1.);
    cutFlowHistManager->fillHistograms(">= 2 sel leptons", 1.);
    const RecoLepton* selLepton_lead = selLeptons[0];
    int selLepton_lead_type = getLeptonType(selLepton_lead->pdgId());
    const RecoLepton* selLepton_sublead = selLeptons[1];
    int selLepton_sublead_type = getLeptonType(selLepton_sublead->pdgId());
    const leptonGenMatchEntry& selLepton_genMatch = getLeptonGenMatch(leptonGenMatch_definitions, selLepton_lead, selLepton_sublead);
    int idxSelLepton_genMatch = selLepton_genMatch.idx_;
    assert(idxSelLepton_genMatch != kGen_LeptonUndefined2);

//--- compute event-level weight for data/MC correction of b-tagging efficiency and mistag rate
//   (using the method "Event reweighting using scale factors calculated with a tag and probe method",
//    described on the BTV POG twiki https://twiki.cern.ch/twiki/bin/view/CMS/BTagShapeCalibration )
    double evtWeight = 1.;
    double btagWeight = 1.;
    if ( isMC ) {
      evtWeight *= evtWeight_inclusive;
      btagWeight = get_BtagWeight(selJets);
      evtWeight *= btagWeight;
      if ( isDEBUG ) {
        std::cout << "lumiScale = " << lumiScale << std::endl;
        if ( apply_genWeight ) std::cout << "genWeight = " << boost::math::sign(eventInfo.genWeight) << std::endl;
        std::cout << "pileupWeight = " << eventInfo.pileupWeight << std::endl;
        std::cout << "btagWeight = " << btagWeight << std::endl;
      }
    }

    double weight_data_to_MC_correction = 1.;
    double triggerWeight = 1.;
    double leptonSF_weight = 1.;
    double tauSF_weight = 1.;
    if ( isMC ) {
      dataToMCcorrectionInterface->setLeptons(
        selLepton_lead_type, selLepton_lead->pt(), selLepton_lead->eta(),
        selLepton_sublead_type, selLepton_sublead->pt(), selLepton_sublead->eta());

//--- apply data/MC corrections for trigger efficiency
      double sf_triggerEff = dataToMCcorrectionInterface->getSF_leptonTriggerEff();
      if ( isDEBUG ) {
        std::cout << "sf_triggerEff = " << sf_triggerEff << std::endl;
      }
      triggerWeight *= sf_triggerEff;
      weight_data_to_MC_correction *= sf_triggerEff;

//--- apply data/MC corrections for efficiencies for lepton to pass loose identification and isolation criteria
      leptonSF_weight *= dataToMCcorrectionInterface->getSF_leptonID_and_Iso_loose();

//--- apply data/MC corrections for efficiencies of leptons passing the loose identification and isolation criteria
//    to also pass the tight identification and isolation criteria
      if ( electronSelection == kFakeable && muonSelection == kFakeable ) {
        leptonSF_weight *= dataToMCcorrectionInterface->getSF_leptonID_and_Iso_fakeable_to_loose();
      } else if ( electronSelection >= kFakeable && muonSelection >= kFakeable ) {
        // apply loose-to-tight lepton ID SFs if either of the following is true:
        // 1) both electron and muon selections are tight -> corresponds to SR
        // 2) electron selection is relaxed to fakeable and muon selection is kept as tight -> corresponds to MC closure w/ relaxed e selection
        // 3) muon selection is relaxed to fakeable and electron selection is kept as tight -> corresponds to MC closure w/ relaxed mu selection
        // we allow (2) and (3) so that the MC closure regions would more compatible w/ the SR (1) in comparison
        leptonSF_weight *= dataToMCcorrectionInterface->getSF_leptonID_and_Iso_tight_to_loose_wTightCharge();
      }
      weight_data_to_MC_correction *= leptonSF_weight;

//--- apply data/MC corrections for hadronic tau identification efficiency
//    and for e->tau and mu->tau misidentification rates
      int selHadTau_genPdgId = getHadTau_genPdgId(selHadTau);
      dataToMCcorrectionInterface->setHadTaus(selHadTau_genPdgId, selHadTau->pt(), selHadTau->eta());
      tauSF_weight *= dataToMCcorrectionInterface->getSF_hadTauID_and_Iso();
      tauSF_weight *= dataToMCcorrectionInterface->getSF_eToTauFakeRate();
      tauSF_weight *= dataToMCcorrectionInterface->getSF_muToTauFakeRate();
      weight_data_to_MC_correction *= tauSF_weight;
      if ( isDEBUG ) {
        std::cout << "weight_data_to_MC_correction = " << weight_data_to_MC_correction << std::endl;
      }

      evtWeight *= weight_data_to_MC_correction;
    }

    bool passesTight_lepton_lead = isMatched(*selLepton_lead, tightElectrons) || isMatched(*selLepton_lead, tightMuons);
    bool passesTight_lepton_sublead = isMatched(*selLepton_sublead, tightElectrons) || isMatched(*selLepton_sublead, tightMuons);
    bool passesTight_hadTau = isMatched(*selHadTau, tightHadTausFull);

    double weight_fakeRate = 1.;
    double prob_fake_lepton_lead = 1.;
    double prob_fake_lepton_sublead = 1.;
    double prob_fake_hadTau = 1.;
    if ( leptonFakeRateInterface ) {
      if      ( std::abs(selLepton_lead->pdgId()) == 11 ) prob_fake_lepton_lead = leptonFakeRateInterface->getWeight_e(selLepton_lead->cone_pt(), selLepton_lead->absEta());
      else if ( std::abs(selLepton_lead->pdgId()) == 13 ) prob_fake_lepton_lead = leptonFakeRateInterface->getWeight_mu(selLepton_lead->cone_pt(), selLepton_lead->absEta());
      else assert(0);
      if      ( std::abs(selLepton_sublead->pdgId()) == 11 ) prob_fake_lepton_sublead = leptonFakeRateInterface->getWeight_e(selLepton_sublead->cone_pt(), selLepton_sublead->absEta());
      else if ( std::abs(selLepton_sublead->pdgId()) == 13 ) prob_fake_lepton_sublead = leptonFakeRateInterface->getWeight_mu(selLepton_sublead->cone_pt(), selLepton_sublead->absEta());
      else assert(0);
    }
    if ( jetToTauFakeRateInterface ) {
      prob_fake_hadTau = jetToTauFakeRateInterface->getWeight_lead(selHadTau->pt(), selHadTau->absEta());
    }

    if ( !selectBDT ) {
      if ( applyFakeRateWeights == kFR_3L ) {
        weight_fakeRate = getWeight_3L(
          prob_fake_lepton_lead, passesTight_lepton_lead,
          prob_fake_lepton_sublead, passesTight_lepton_sublead,
          prob_fake_hadTau, passesTight_hadTau);
      } else if ( applyFakeRateWeights == kFR_2lepton) {
        weight_fakeRate = getWeight_2L(
          prob_fake_lepton_lead, passesTight_lepton_lead,
          prob_fake_lepton_sublead, passesTight_lepton_sublead);
      } else if ( applyFakeRateWeights == kFR_1tau ){
        weight_fakeRate = prob_fake_hadTau;
      }
      evtWeight *= weight_fakeRate;
      // CV: apply data/MC ratio for jet->tau fake-rates in case data-driven "fake" background estimation is applied to leptons only
      if ( isMC && apply_hadTauFakeRateSF && hadTauSelection == kTight && !(selHadTau->genHadTau() || selHadTau->genLepton())) {
        double weight_data_to_MC_correction_hadTau = jetToTauFakeRateInterface->getSF_lead(selHadTau->pt(), selHadTau->absEta());
        if ( isDEBUG ) {
          std::cout << "weight_data_to_MC_correction_hadTau = " << weight_data_to_MC_correction_hadTau << std::endl;
        }
        tauSF_weight *= weight_data_to_MC_correction_hadTau;
        evtWeight *= weight_data_to_MC_correction_hadTau;
      }
    } // end if !selectBDT

    // require exactly two leptons passing tight selection criteria, to avoid overlap with other channels
    if ( !(tightLeptonsFull.size() <= 2) ) {
      if ( run_lumi_eventSelector ) {
        std::cout << "event " << eventInfo.str() << " FAILS tightLeptons selection.\n";
        printCollection("tightLeptonsFull", tightLeptonsFull);
      }
      continue;
    }
    cutFlowTable.update("<= 2 tight leptons", evtWeight);
    cutFlowHistManager->fillHistograms("<= 2 tight leptons", evtWeight);
    // require that trigger paths match event category (with event category based on fakeableLeptons)
    if ( !((fakeableElectrons.size() >= 2 &&                              (selTrigger_2e    || selTrigger_1e                  )) ||
           (fakeableElectrons.size() >= 1 && fakeableMuons.size() >= 1 && (selTrigger_1e1mu || selTrigger_1mu || selTrigger_1e)) ||
           (                                 fakeableMuons.size() >= 2 && (selTrigger_2mu   || selTrigger_1mu                 ))) ) {
      if ( run_lumi_eventSelector ) {
        std::cout << "event " << eventInfo.str() << " FAILS trigger selection for given fakeableLepton multiplicity." << std::endl;
        std::cout << " (#fakeableElectrons = " << fakeableElectrons.size()
                  << ", #fakeableMuons = " << fakeableMuons.size()
                  << ", selTrigger_2mu = " << selTrigger_2mu
                  << ", selTrigger_1e1mu = " << selTrigger_1e1mu
                  << ", selTrigger_2e = " << selTrigger_2e
                  << ", selTrigger_1mu = " << selTrigger_1mu
                  << ", selTrigger_1e = " << selTrigger_1e << ")" << std::endl;
      }
      continue;
    }
    cutFlowTable.update("fakeable lepton trigger match", evtWeight);
    cutFlowHistManager->fillHistograms("fakeable lepton trigger match", evtWeight);

//--- apply HLT filter
    if(apply_hlt_filter)
    {
      const std::map<hltPathsE, bool> trigger_bits = {
        { hltPathsE::trigger_1e,    selTrigger_1e    },
        { hltPathsE::trigger_1mu,   selTrigger_1mu   },
        { hltPathsE::trigger_2e,    selTrigger_2e    },
        { hltPathsE::trigger_2mu,   selTrigger_2mu   },
        { hltPathsE::trigger_1e1mu, selTrigger_1e1mu },
      };
      if(! hltFilter(trigger_bits, fakeableLeptons, fakeableHadTaus))
      {
        if(run_lumi_eventSelector || isDEBUG)
        {
          std::cout << "event " << eventInfo.str() << " FAILS HLT filter matching\n";
        }
        continue;
      }
    }
    cutFlowTable.update("HLT filter matching", evtWeight);
    cutFlowHistManager->fillHistograms("HLT filter matching", evtWeight);

    // apply requirement on jets (incl. b-tagged jets) and hadronic taus on level of final event selection
    /*
    if ( !(selJets.size() >= 3) ) {
      if ( run_lumi_eventSelector ) {
        std::cout << "event " << eventInfo.str() << " FAILS selJets selection (2)." << std::endl;
        printCollection("selJets", selJets);
      }
      continue;
    }
    */
    cutFlowTable.update(">= 3 jets", evtWeight);
    cutFlowHistManager->fillHistograms(">= 3 jets", evtWeight);
    if ( !(selBJets_loose.size() >= 2 || selBJets_medium.size() >= 1) ) {
      if ( run_lumi_eventSelector ) {
        std::cout << "event " << eventInfo.str() << " FAILS selBJets selection (2)." << std::endl;
        printCollection("selJets", selJets);
        printCollection("selBJets_loose", selBJets_loose);
        printCollection("selBJets_medium", selBJets_medium);
      }
      continue;
    }
    cutFlowTable.update(">= 2 loose b-jets || 1 medium b-jet (2)", evtWeight);
    cutFlowHistManager->fillHistograms(">= 2 loose b-jets || 1 medium b-jet (2)", evtWeight);

    if ( !(selHadTaus.size() >= 1) ) {
      if ( run_lumi_eventSelector ) {
        std::cout << "event " << eventInfo.str() << " FAILS selHadTaus selection." << std::endl;
        printCollection("selHadTaus", selHadTaus);
      }
      continue;
    }
    cutFlowTable.update(">= 1 sel tau (2)", evtWeight);
    cutFlowHistManager->fillHistograms(">= 1 sel tau (2)", evtWeight);

    // veto events containing more than one tau passing the Medium WP, to avoid overlap with the 2l+2tau category
    // we want to keep all cuts consistent in SR and fake CR, to obtain a consistent estimate of the fake background
    if ( !(vetoHadTaus.size() <= 1) ) {
      if ( run_lumi_eventSelector ) {
        std::cout << "event " << eventInfo.str() << " FAILS vetoHadTaus selection." << std::endl;
        printCollection("vetoHadTaus", vetoHadTaus);
      }
      continue;
    }
    cutFlowTable.update("<= 1 veto taus", evtWeight);
    cutFlowHistManager->fillHistograms("<= 1 veto taus", evtWeight);

    bool failsLowMassVeto = false;
    for ( std::vector<const RecoLepton*>::const_iterator lepton1 = preselLeptonsFull.begin();
          lepton1 != preselLeptonsFull.end(); ++lepton1 ) {
      for ( std::vector<const RecoLepton*>::const_iterator lepton2 = lepton1 + 1;
            lepton2 != preselLeptonsFull.end(); ++lepton2 ) {
        double mass = ((*lepton1)->p4() + (*lepton2)->p4()).mass();
        if ( mass < 12. ) {
          failsLowMassVeto = true;
        }
      }
    }
    if ( failsLowMassVeto ) {
      if ( run_lumi_eventSelector ) {
        std::cout << "event " << eventInfo.str() << " FAILS low mass lepton pair veto." << std::endl;
      }
      continue;
    }
    cutFlowTable.update("m(ll) > 12 GeV", evtWeight);
    cutFlowHistManager->fillHistograms("m(ll) > 12 GeV", evtWeight);

    const double minPt_lead = 25.;
    const double minPt_sublead = selLepton_sublead->is_electron() ? 15. : 10.;
    if ( !(selLepton_lead->cone_pt() > minPt_lead && selLepton_sublead->cone_pt() > minPt_sublead) ) {
      if ( run_lumi_eventSelector ) {
        std::cout << "event " << eventInfo.str() << " FAILS lepton pT selection." << std::endl;
        std::cout << " (leading selLepton pT = " << selLepton_lead->pt() << ", minPt_lead = " << minPt_lead
                  << ", subleading selLepton pT = " << selLepton_sublead->pt() << ", minPt_sublead = " << minPt_sublead << ")" << std::endl;
      }
      continue;
    }
    cutFlowTable.update("lead lepton pT > 25 GeV && sublead lepton pT > 15(e)/10(mu) GeV", evtWeight);
    cutFlowHistManager->fillHistograms("lead lepton pT > 25 GeV && sublead lepton pT > 15(e)/10(mu) GeV", evtWeight);

    bool failsTightChargeCut = false;
    for ( std::vector<const RecoLepton*>::const_iterator lepton = fakeableLeptons.begin();
          lepton != fakeableLeptons.end(); ++lepton ) {
      if ( (*lepton)->is_electron() ) {
        const RecoElectron* electron = dynamic_cast<const RecoElectron*>(*lepton);
        assert(electron);
        if ( electron->tightCharge() < 2 )
        {
          failsTightChargeCut = true;
          break;
        }
      }
      else if ( (*lepton)->is_muon() ) {
        const RecoMuon* muon = dynamic_cast<const RecoMuon*>(*lepton);
        assert(muon);
        if ( muon->tightCharge() < 2 )
        {
          failsTightChargeCut = true;
          break;
        }
      }
    }
    if ( failsTightChargeCut ) {
      if ( run_lumi_eventSelector ) {
        std::cout << "event " << eventInfo.str() << " FAILS tight lepton charge requirement." << std::endl;
      }
      //if (!selectBDT)
      continue;
    }
    cutFlowTable.update("tight lepton charge", evtWeight);
    cutFlowHistManager->fillHistograms("tight lepton charge", evtWeight);

    bool isLeptonCharge_SS = selLepton_lead->charge()*selLepton_sublead->charge() > 0;
    bool isLeptonCharge_OS = selLepton_lead->charge()*selLepton_sublead->charge() < 0;
    if ( leptonChargeSelection == kOS && isLeptonCharge_SS ) {
      if ( run_lumi_eventSelector ) {
        std::cout << "event " << eventInfo.str() << " FAILS lepton charge selection." << std::endl;
        std::cout << " (leading selLepton charge = " << selLepton_lead->charge()
                  << ", subleading selLepton charge = " << selLepton_sublead->charge() << ", leptonChargeSelection = OS)" << std::endl;
      }
      continue;
    }
    if ( leptonChargeSelection == kSS && isLeptonCharge_OS ) {
      if ( run_lumi_eventSelector ) {
        std::cout << "event " << eventInfo.str() << " FAILS lepton charge selection." << std::endl;
        std::cout << " (leading selLepton charge = " << selLepton_lead->charge()
                  << ", subleading selLepton charge = " << selLepton_sublead->charge() << ", leptonChargeSelection = SS)" << std::endl;
      }
      continue;
    }
    if ( leptonChargeSelection == kOS ) {
      double prob_chargeMisId_lead = prob_chargeMisId(getLeptonType(selLepton_lead->pdgId()), selLepton_lead->pt(), selLepton_lead->eta());
      double prob_chargeMisId_sublead = prob_chargeMisId(getLeptonType(selLepton_sublead->pdgId()), selLepton_sublead->pt(), selLepton_sublead->eta());

      if ( apply_lepton_and_hadTauCharge_cut ) {
        if ( chargeSumSelection == kOS ) {
          // CV: apply charge misidentification probability to lepton of same charge as hadronic tau
          //    (if the lepton of charge opposite to the charge of the hadronic tau "flips",
          //     the event has sum of charges equal to three and fails "lepton+tau charge" cut)
          if ( selLepton_lead->charge()*selHadTau->charge()    > 0 ) evtWeight *= prob_chargeMisId_lead;
          if ( selLepton_sublead->charge()*selHadTau->charge() > 0 ) evtWeight *= prob_chargeMisId_sublead;
        } else if ( chargeSumSelection == kSS ) {
          // CV: apply charge misidentification probability to lepton of opposite charge as hadronic tau
          //    (if the lepton of same charge as the hadronic tau "flips",
          //     the event has sum of charges equal to one and fails "lepton+tau charge" cut)
          if ( selLepton_lead->charge()*selHadTau->charge()    < 0 ) evtWeight *= prob_chargeMisId_lead;
          if ( selLepton_sublead->charge()*selHadTau->charge() < 0 ) evtWeight *= prob_chargeMisId_sublead;
        } else assert(0);
      } else {
        evtWeight *= (prob_chargeMisId_lead + prob_chargeMisId_sublead);
      }
      // Karl: reject the event, if the applied probability of charge misidentification is 0;
      //       we assume that the event weight was not 0 before including the charge flip weights.
      //       This can happen only if
      //       1) both selected leptons are muons (their misId prob is 0).
      //       2) one lepton is a muon and the other is an electron, and the muon has the same sign as the selected tau.
      if(evtWeight == 0.)
      {
        if(run_lumi_eventSelector)
        {
          std::cout << "event " << eventInfo.str() << " FAILS charge flip selection\n"
                       "(leading lepton charge (pdgId) = " << selLepton_lead->charge() << " (" << selLepton_lead->pdgId()
                    << ") => misId prob = " << prob_chargeMisId_lead << "; "
                       "subleading lepton charge (pdgId) = " << selLepton_sublead->charge() << " (" << selLepton_sublead->pdgId()
                    << ") => misId prob = " << prob_chargeMisId_sublead << "); "
                       "tau charge = " << selHadTau->charge() << ")\n"
          ;
        }
        continue;
      }
    }
    cutFlowTable.update(Form("sel lepton-pair %s charge", leptonChargeSelection_string.data()), evtWeight);
    cutFlowHistManager->fillHistograms("sel lepton-pair OS/SS charge", evtWeight);

    if ( apply_lepton_and_hadTauCharge_cut ) {
      if ( !((chargeSumSelection == kOS && std::abs(selLepton_lead->charge() + selLepton_sublead->charge() + selHadTau->charge()) == 1) ||
             (chargeSumSelection == kSS && std::abs(selLepton_lead->charge() + selLepton_sublead->charge() + selHadTau->charge()) != 1)) ) {
        if ( run_lumi_eventSelector ) {
          std::cout << "event " << eventInfo.str() << " FAILS lepton+tau charge selection." << std::endl;
          std::cout << " (leading selLepton charge = " << selLepton_lead->charge()
                    << ", subleading selLepton charge = " << selLepton_sublead->charge()
                    << ", selHadTau charge = " << selHadTau->charge() << ")" << std::endl;
        }
        continue;
      }
      cutFlowTable.update(Form("sel lepton+tau %s charge", chargeSumSelection_string.data()), evtWeight);
      cutFlowHistManager->fillHistograms("sel lepton+tau charge", evtWeight);
    }

    bool failsZbosonMassVeto = false;
    /*
    for ( std::vector<const RecoLepton*>::const_iterator lepton1 = preselLeptonsFull.begin();
          lepton1 != preselLeptonsFull.end(); ++lepton1 ) {
      for ( std::vector<const RecoLepton*>::const_iterator lepton2 = lepton1 + 1;
            lepton2 != preselLeptonsFull.end(); ++lepton2 ) {
        double mass = ((*lepton1)->p4() + (*lepton2)->p4()).mass();
        if ( (*lepton1)->is_electron() && (*lepton2)->is_electron() && std::fabs(mass - z_mass) < z_window ) {
          failsZbosonMassVeto = true;
        }
      }
    }*/
    // Sergio and Marco way
    // Zee veto in 2lss categories <=> veto event if the two tight leptons are electrons with mZ-mee < 10
    double mass = (selLepton_lead->p4() + selLepton_sublead->p4()).mass();
    if ( selLepton_lead->is_electron() && selLepton_sublead->is_electron() && std::fabs(mass - z_mass) < z_window ) failsZbosonMassVeto = true;
    if ( failsZbosonMassVeto ) {
      if ( run_lumi_eventSelector ) {
        std::cout << "event " << eventInfo.str() << " FAILS Z-boson veto." << std::endl;
      }
      continue;
    }
    cutFlowTable.update("Z-boson mass veto", evtWeight);
    cutFlowHistManager->fillHistograms("Z-boson mass veto", evtWeight);
    if ( !(selLepton_lead->is_muon() || selLepton_sublead->is_muon() || met_LD >= 30.) ) {
      if ( run_lumi_eventSelector ) {
          std::cout << "event " << eventInfo.str() << " FAILS MET LD selection." << std::endl;
          std::cout << " (LD = " << met_LD << ")\n"
        ;
      }
      continue;
    }
    cutFlowTable.update("met LD > 30 GeV", evtWeight);
    cutFlowHistManager->fillHistograms("met LD > 30 GeV", evtWeight);

    if ( apply_met_filters ) {
      if ( !metFilterSelector(metFilters) ) {
	if ( run_lumi_eventSelector ) {
      std::cout << "event " << eventInfo.str() << " FAILS MEt filters." << std::endl;
	}
	continue;
      }
    }
    cutFlowTable.update("MEt filters", evtWeight);
    cutFlowHistManager->fillHistograms("MEt filters", evtWeight);

    if (isMC) {
      if((selLepton_lead->genLepton() && selLepton_lead->charge() != selLepton_lead->genLepton()->charge()) ||
         (selLepton_sublead->genLepton() && selLepton_sublead->charge() != selLepton_sublead->genLepton()->charge())){
        if(run_lumi_eventSelector)
          {
	    std::cout << "event " << eventInfo.str() << " FAILS lepton-par gen=rec charge matching\n"
              "(leading lepton charge = " << selLepton_lead->charge() << " genlepton charge = " << selLepton_lead->genLepton()->charge()<< "; "
              "subleading lepton charge = " << selLepton_sublead->charge() << " genlepton charge = " << selLepton_sublead->genLepton()->charge()<< "\n"
              ;
          }
        continue;
      }
    }
    cutFlowTable.update("sel lepton-pair gen=rec charge match", evtWeight);
    cutFlowHistManager->fillHistograms("sel lepton-pair gen=rec charge match", evtWeight);


    bool failsSignalRegionVeto = false;
    if ( isMCClosure_e || isMCClosure_m || isMCClosure_t ) {
      bool applySignalRegionVeto_lepton = (isMCClosure_e && countFakeElectrons(selLeptons) >= 1) || (isMCClosure_m && countFakeMuons(selLeptons) >= 1);
      bool applySignalRegionVeto_hadTau = isMCClosure_t && countFakeHadTaus(selHadTaus) >= 1;
      if ( applySignalRegionVeto_lepton && tightLeptons.size() >= 2 ) failsSignalRegionVeto = true;
      if ( applySignalRegionVeto_hadTau && tightHadTaus.size() >= 1 ) failsSignalRegionVeto = true;
    } else if ( electronSelection == kFakeable || muonSelection == kFakeable || hadTauSelection == kFakeable ) {
      if ( tightLeptons.size() >= 2 && tightHadTaus.size() >= 1 ) failsSignalRegionVeto = true;
    }
    if ( failsSignalRegionVeto ) {
      if ( run_lumi_eventSelector ) {
	std::cout << "event " << eventInfo.str() << " FAILS overlap w/ the SR: "
	             "# tight leptons = " << tightLeptons.size() << " >= 2 and "
                     "# tight taus = " << tightHadTaus.size() << " >= 1\n"
        ;
	printCollection("tightLeptons", tightLeptons);
	printCollection("tightHadTaus", tightHadTaus);
      }
      continue; // CV: avoid overlap with signal region
    }
    cutFlowTable.update("signal region veto", evtWeight);
    cutFlowHistManager->fillHistograms("signal region veto", evtWeight);

    MEMOutput_2lss_1tau memOutput_2lss_1tau_matched;
    if ( memReader ) {
      std::vector<MEMOutput_2lss_1tau> memOutputs_2lss_1tau = memReader->read();
      for ( std::vector<MEMOutput_2lss_1tau>::const_iterator memOutput_2lss_1tau = memOutputs_2lss_1tau.begin();
            memOutput_2lss_1tau != memOutputs_2lss_1tau.end(); ++memOutput_2lss_1tau ) {
        const double selLepton_lead_dR = deltaR(
          selLepton_lead->eta(), selLepton_lead->phi(),
          memOutput_2lss_1tau->leadLepton_eta_, memOutput_2lss_1tau->leadLepton_phi_);
        if ( selLepton_lead_dR > 1.e-2 ) continue;
        const double selLepton_sublead_dR = deltaR(
          selLepton_sublead->eta(), selLepton_sublead->phi(),
          memOutput_2lss_1tau->subleadLepton_eta_, memOutput_2lss_1tau->subleadLepton_phi_);
        if ( selLepton_sublead_dR > 1.e-2 ) continue;
        const double selHadTau_dR = deltaR(
          selHadTau->eta(), selHadTau->phi(),
          memOutput_2lss_1tau->hadTau_eta_, memOutput_2lss_1tau->hadTau_phi_);
        if ( selHadTau_dR > 1.e-2 ) continue;
        memOutput_2lss_1tau_matched = (*memOutput_2lss_1tau);
        break;
      }
      if ( !memOutput_2lss_1tau_matched.is_initialized() ) {
        std::cout << "Warning in " << eventInfo << '\n'
                  << "No MEMOutput_2lss_1tau object found for:\n"
                  << "\tselLepton_lead: pT = " << selLepton_lead->pt()
                  << ", eta = "                << selLepton_lead->eta()
                  << ", phi = "                << selLepton_lead->phi()
                  << ", pdgId = "              << selLepton_lead->pdgId() << '\n'
                  << "\tselLepton_sublead: pT = " << selLepton_sublead->pt()
                  << ", eta = "                   << selLepton_sublead->eta()
                  << ", phi = "                   << selLepton_sublead->phi()
                  << ", pdgId = "                 << selLepton_sublead->pdgId() << '\n'
                  << "\tselHadTau: pT = " << selHadTau->pt()
                  << ", eta = "           << selHadTau->eta()
                  << ", phi = "           << selHadTau->phi() << '\n'
                  << "Number of MEM objects read: " << memOutputs_2lss_1tau.size() << '\n';
        if ( memOutputs_2lss_1tau.size() ) {
          for ( unsigned mem_idx = 0; mem_idx < memOutputs_2lss_1tau.size(); ++mem_idx ) {
            std::cout << "\t#" << mem_idx << " mem object;\n"
                      << "\t\tlead lepton eta = " << memOutputs_2lss_1tau[mem_idx].leadLepton_eta_
                      << "; phi = "               << memOutputs_2lss_1tau[mem_idx].leadLepton_phi_ << '\n'
                      << "\t\tsublead lepton eta = " << memOutputs_2lss_1tau[mem_idx].subleadLepton_eta_
                      << "; phi = "                  << memOutputs_2lss_1tau[mem_idx].subleadLepton_phi_ << '\n'
                      << "\t\thadronic tau eta = " << memOutputs_2lss_1tau[mem_idx].hadTau_eta_
                      << "; phi = "                << memOutputs_2lss_1tau[mem_idx].hadTau_phi_ << '\n';
          }
        } else {
          std::cout << "Event contains no MEM objects whatsoever !!\n";
        }
      }
    }
    double memOutput_LR = ( memOutput_2lss_1tau_matched.isValid() ) ? memOutput_2lss_1tau_matched.LR() : -1.;

    //--- compute output of hadronic top tagger BDT
    // it returns the gen-triplets organized in top/anti-top
    bool calculate_matching = isMC && selectBDT && !applyAdditionalEvtWeight; // DY has not matching info
    std::map<int, Particle::LorentzVector> genVar;
    std::map<int, Particle::LorentzVector> genVarAnti;
    if (calculate_matching) {
      genVar = isGenMatchedJetTripletVar(genTopQuarks, genBJets, genWBosons, genQuarkFromTop, kGenTop);
      genVarAnti = isGenMatchedJetTripletVar(genTopQuarks, genBJets, genWBosons, genQuarkFromTop, kGenAntiTop);
    }

    // resolved HTT
    double max_mvaOutput_HTT_2016 = 0.;
    bool max_truth_HTT_2016 = false;
    double genTopPt = 0.;

    double max_mvaOutput_HTT_multilep = -1.;
    bool max_truth_multilep = false;
    double HadTop_pt_multilep = 0.;
    double genTopPt_multilep = 0.;

    double max_mvaOutput_HTT_CSVsort4rd = 0.;
    bool max_truth_HTT_CSVsort4rd = false;
    double HadTop_pt_CSVsort4rd = 0.;
    double genTopPt_CSVsort4rd = 0.;
    double b_pt_CSVsort4rd_1 = 0.1;
    double Wj1_pt_CSVsort4rd_1 = 0.1;
    double Wj2_pt_CSVsort4rd_1 = 0.1;

    double max_mvaOutput_HTT_highestCSV = 0.;
    bool max_truth_HTT_highestCSV = false;
    double HadTop_pt_highestCSV = 0.;
    double genTopPt_highestCSV = 0.;

    double max_mvaOutput_HTT_CSVsort4rd_WithKinFit = 0.;
    bool max_truth_HTT_CSVsort4rd_WithKinFit = false;
    double HadTop_pt_CSVsort4rd_WithKinFit = 0.;
    double genTopPt_CSVsort4rd_WithKinFit = 0.;

    double max_mvaOutput_HTT_highestCSV_WithKinFit = 0.;
    bool max_truth_HTT_highestCSV_WithKinFit = false;
    double HadTop_pt_highestCSV_WithKinFit = 0.;
    double genTopPt_highestCSV_WithKinFit = 0.;

    bool hadtruth = false;
    Particle::LorentzVector unfittedHadTopP4, fittedHadTopP4;
    bool massCut = true; // wheather apply calculating the HTT

    for ( std::vector<const RecoJet*>::const_iterator selBJet = selJets.begin(); selBJet != selJets.end(); ++selBJet ) {
      //btag_iterator++;
      for ( std::vector<const RecoJet*>::const_iterator selWJet1 = selJets.begin(); selWJet1 != selJets.end(); ++selWJet1 ) {
       if ( &(*selWJet1) == &(*selBJet) ) continue;
       for ( std::vector<const RecoJet*>::const_iterator selWJet2 = selWJet1 + 1; selWJet2 != selJets.end(); ++selWJet2 ) {
	  if ( &(*selWJet2) == &(*selBJet) ) continue;
	  if ( &(*selWJet2) == &(*selWJet1) ) continue;
    bool isGenMatched = false;
    double genTopPt_teste = 0.;
    const std::map<int, double> bdtResult = (*hadTopTagger)(**selBJet, **selWJet1, **selWJet2, calculate_matching, isGenMatched, genTopPt_teste, genVar, genVarAnti, massCut );
    if ( isGenMatched ) hadtruth = true;
    // save genpt of all options

    //if (!(btag_order_selJets[btag_iterator] > cutJetCombo)) {
    if (1 > 0) {
      if ( bdtResult.at(kXGB_with_kinFit) > max_mvaOutput_HTT_2016 ) { // HTT_2016
        max_truth_HTT_2016 = isGenMatched;
        max_mvaOutput_HTT_2016 = bdtResult.at(kXGB_with_kinFit);
        fittedHadTopP4 = (*selBJet)->p4() + (*selWJet1)->p4() + (*selWJet2)->p4();
        unfittedHadTopP4 = (*selBJet)->p4() + (*selWJet1)->p4() + (*selWJet2)->p4();
        genTopPt = genTopPt_teste;
      }

      if ( bdtResult.at(kXGB_CSVsort4rd) > max_mvaOutput_HTT_CSVsort4rd ) {
        max_truth_HTT_CSVsort4rd = isGenMatched;
        max_mvaOutput_HTT_CSVsort4rd = bdtResult.at(kXGB_CSVsort4rd);
        HadTop_pt_CSVsort4rd = ((*selBJet)->p4() + (*selWJet1)->p4() + (*selWJet2)->p4()).pt();
        genTopPt_CSVsort4rd = genTopPt_teste;
        Wj1_pt_CSVsort4rd_1 = (*selWJet1)->pt();
        Wj2_pt_CSVsort4rd_1 = (*selWJet2)->pt();
        b_pt_CSVsort4rd_1   = (*selBJet)->pt();
      }

      if ( bdtResult.at(kXGB_CSVsort4rd_withKinFit) > max_mvaOutput_HTT_highestCSV_WithKinFit ) {
        max_truth_HTT_CSVsort4rd_WithKinFit = isGenMatched;
        max_mvaOutput_HTT_CSVsort4rd_WithKinFit = bdtResult.at(kXGB_CSVsort4rd_withKinFit);
        HadTop_pt_CSVsort4rd_WithKinFit = ((*selBJet)->p4() + (*selWJet1)->p4() + (*selWJet2)->p4()).pt();
        genTopPt_CSVsort4rd_WithKinFit = genTopPt_teste;
      }
    } // close if passed b-jet combinatorics

    if ((*selBJet)->BtagCSV() > (*selWJet1)->BtagCSV() && (*selBJet)->BtagCSV() > (*selWJet2)->BtagCSV() ) {

      if ( bdtResult.at(kXGB_highestCSV) > max_mvaOutput_HTT_highestCSV ) {
        max_truth_HTT_highestCSV = isGenMatched;
        max_mvaOutput_HTT_highestCSV = bdtResult.at(kXGB_highestCSV);
        HadTop_pt_highestCSV = ((*selBJet)->p4() + (*selWJet1)->p4() + (*selWJet2)->p4()).pt();
        genTopPt_highestCSV = genTopPt_teste;
      }

      if ( bdtResult.at(kXGB_highestCSV_withKinFit) > max_mvaOutput_HTT_highestCSV_WithKinFit ) {
        max_truth_HTT_highestCSV_WithKinFit = isGenMatched;
        max_mvaOutput_HTT_highestCSV_WithKinFit = bdtResult.at(kXGB_highestCSV_withKinFit);
        HadTop_pt_highestCSV_WithKinFit = ((*selBJet)->p4() + (*selWJet1)->p4() + (*selWJet2)->p4()).pt();
        genTopPt_highestCSV_WithKinFit = genTopPt_teste;
      }

      if ( bdtResult.at(kXGB_multilep) > max_mvaOutput_HTT_multilep ) {
        max_truth_multilep = isGenMatched;
        max_mvaOutput_HTT_multilep = bdtResult.at(kXGB_multilep);
        HadTop_pt_multilep = ((*selBJet)->p4() + (*selWJet1)->p4() + (*selWJet2)->p4()).pt();
        genTopPt_multilep = genTopPt_teste;
      }

      //std::cout << "resolved HTT " << max_truth_HTT_2016 << " "
      //<< max_mvaOutput_HTT_CSVsort4rd  << " "
      //<< max_mvaOutput_HTT_CSVsort4rd_WithKinFit << " "
      //<< max_mvaOutput_HTT_multilep << " "
      //<< max_mvaOutput_HTT_highestCSV << " "
      //<< max_mvaOutput_HTT_highestCSV_WithKinFit << " "
      //<< std::endl;
  } // close if b candidate is the highest btagged one

	}
      }
    }

//--- boosted hTT
double HTT_boosted = 0.;
bool bWj1Wj2_isGenMatched_boosted = false;
double genTopPt_boosted = 0.;
double HadTop_pt_HTT_boosted = 0.;

double HTT_boosted_WithKinFit = 0.;
bool bWj1Wj2_isGenMatched_boosted_WithKinFit = false;
double genTopPt_boosted_WithKinFit = 0.;
double HadTop_pt_HTT_boosted_WithKinFit = 0.;

bool hadtruth_boosted = false;
double minDR_HTTv2_lep = -1.;
double minDR_HTTv2_L = -1.;
double minDR_HTTv2_tau = -1.;
for ( std::vector<const RecoJetHTTv2*>::const_iterator jetIter = sel_HTTv2.begin();
  jetIter != sel_HTTv2.end(); ++jetIter ) {
    bool isGenMatched = false;
    double genTopPt_boosted_test = 0.;
    //bool fatjet_isGenMatched = false;
    const std::map<int, double> bdtResult = (*hadTopTagger_boosted)(**jetIter, calculate_matching, isGenMatched, genTopPt_boosted_test, genVar, genVarAnti);
	  if (isGenMatched) {hadtruth_boosted = true;}

    if ( bdtResult.at(kXGB_boosted_no_kinFit) > HTT_boosted ) {
      bWj1Wj2_isGenMatched_boosted = isGenMatched;
      HTT_boosted = bdtResult.at(kXGB_boosted_no_kinFit);
      HadTop_pt_HTT_boosted = (*jetIter)->pt();
      genTopPt_boosted = genTopPt_boosted_test;

      minDR_HTTv2_lep = std::min(
        deltaR(selLepton_lead->p4(), (*jetIter)->p4()),
        deltaR(selLepton_sublead->p4(), (*jetIter)->p4())
      );
      // do the DR qith the selected sel_HTTv2
      minDR_HTTv2_L = std::min(
        std::min(
          deltaR(selHadTau->p4(), (*jetIter)->p4()),
          deltaR(selLepton_lead->p4(), (*jetIter)->p4())
        ),
        deltaR(selLepton_sublead->p4(), (*jetIter)->p4())
      );
      minDR_HTTv2_tau = deltaR(selHadTau->p4(), (*jetIter)->p4());
    }

    if ( bdtResult.at(kXGB_boosted_with_kinFit) > HTT_boosted_WithKinFit ) {
      bWj1Wj2_isGenMatched_boosted_WithKinFit = isGenMatched;
      HTT_boosted_WithKinFit = bdtResult.at(kXGB_boosted_with_kinFit);
      HadTop_pt_HTT_boosted_WithKinFit = (*jetIter)->pt();
      genTopPt_boosted_WithKinFit = genTopPt_boosted_test;
    }

    //std::cout << "boosted HTT " << HTT_boosted << " "
    //<< HTT_boosted_WithKinFit  << " "
    //<< minDR_HTTv2_L << " "
    //<< minDR_HTTv2_lep << " "
    //<< minDR_HTTv2_tau << " "
    //<< std::endl;

  }

  // -- semi-boosted hTT
  double HTT_semi_boosted_AK8 = 0.;
  bool bWj1Wj2_isGenMatched_semi_boosted_AK8 = false;
  double genTopPt_semi_boosted = 0.;
  double HadTop_pt_HTT_semi_boosted_AK8 = 0.;

  double HTT_semi_boosted_AK8_WithKinFit = 0.;
  bool bWj1Wj2_isGenMatched_semi_boosted_AK8_WithKinFit = false;
  double genTopPt_semi_boosted_WithKinFit = 0.;
  double HadTop_pt_HTT_semi_boosted_AK8_WithKinFit = 0.;

  bool hadtruth_semi_boosted_AK8 = false;
  //double genTopPt_boosted = 0.;
  double minDR_AK8_lep = -1.;
  double minDR_AK8_L = -1.;
  double DR_AK8_tau = -1.;
  //for (auto i: btag_order) std::cout << i << " ";
  for ( std::vector<const RecoJet*>::const_iterator selBJet = cleanedJets_fromAK8.begin(); selBJet != cleanedJets_fromAK8.end(); ++selBJet )  { // cleanedJets.size()
    for ( std::vector<const RecoJetAK8*>::const_iterator jetIter = jet_ptrsAK8.begin();
          jetIter != jet_ptrsAK8.end(); ++jetIter ) {
        bool isGenMatched = false;
        double genTopPt_boosted_test = 0.;
        //bool fatjet_isGenMatched = false;
        const std::map<int, double> bdtResult = (*hadTopTagger_semi_boosted)(**jetIter, **selBJet, calculate_matching, isGenMatched, genTopPt_boosted_test, genVar, genVarAnti);
        if (isGenMatched) {hadtruth_semi_boosted_AK8 = true;}

        if ( bdtResult.at(kXGB_semi_boosted_no_kinFit) > HTT_semi_boosted_AK8 ) {
          bWj1Wj2_isGenMatched_semi_boosted_AK8 = isGenMatched;
          HTT_semi_boosted_AK8 = bdtResult.at(kXGB_semi_boosted_no_kinFit);
          HadTop_pt_HTT_semi_boosted_AK8 = (*jetIter)->pt();
          genTopPt_semi_boosted = genTopPt_boosted_test;

          minDR_AK8_lep = std::min(
            deltaR(selLepton_lead->p4(), (*jetIter)->p4()),
            deltaR(selLepton_sublead->p4(), (*jetIter)->p4())
          );
          // do the DR qith the selected AK8
          minDR_AK8_L = std::min(
            std::min(
              deltaR(selHadTau->p4(), (*jetIter)->p4()),
              deltaR(selLepton_lead->p4(), (*jetIter)->p4())
            ),
            deltaR(selLepton_sublead->p4(), (*jetIter)->p4())
          );
          DR_AK8_tau = deltaR(selHadTau->p4(), (*jetIter)->p4());

        }

        if ( bdtResult.at(kXGB_semi_boosted_with_kinFit) > HTT_semi_boosted_AK8_WithKinFit ) {
          bWj1Wj2_isGenMatched_semi_boosted_AK8_WithKinFit = isGenMatched;
          HTT_semi_boosted_AK8_WithKinFit = bdtResult.at(kXGB_semi_boosted_with_kinFit);
          HadTop_pt_HTT_semi_boosted_AK8_WithKinFit = (*jetIter)->pt();
          genTopPt_semi_boosted_WithKinFit = genTopPt_boosted_test;
        }
      }
    }
    //std::cout << "semi-boosted HTT " << HTT_semi_boosted_AK8 << " "
    //<< HTT_semi_boosted_AK8_WithKinFit  << " "
    //<< minDR_AK8_L << " "
    //<< minDR_AK8_lep << " "
    //<< DR_AK8_tau << " "
    //<< std::endl;

    //std::map<std::string, double> mvaOutput_Hj_tagger;
    std::map<std::string, double> mvaInputs_Hj_tagger;
    double mvaOutput_Hj_tagger = 0.;
    for ( std::vector<const RecoJet*>::const_iterator selJet = selJets.begin();
	  selJet != selJets.end(); ++selJet ) {
      if ((*selJet)->pt()==Wj1_pt_CSVsort4rd_1 || (*selJet)->pt()==Wj2_pt_CSVsort4rd_1 || (*selJet)->pt()==b_pt_CSVsort4rd_1) continue;
      double mvaOutput = comp_mvaOutput_Hj_tagger(
        *selJet, fakeableLeptons, mvaInputs_Hj_tagger, mva_Hj_tagger,
        eventInfo);
      if ( mvaOutput > mvaOutput_Hj_tagger ) mvaOutput_Hj_tagger = mvaOutput;
    }

//--- compute variables BDTs used to discriminate ttH vs. ttV and ttH vs. ttba -- they will be used more than once -- Xanda
    const int nJet25_Recl = comp_n_jet25_recl(selJets);

    const double mindr_lep1_jet  = comp_mindr_lep1_jet(*selLepton_lead, selJets);
    const double mindr_lep2_jet  = comp_mindr_lep2_jet(*selLepton_sublead, selJets);
    const double max_lep_eta     = std::max(selLepton_lead->absEta(), selLepton_sublead->absEta());
    const double tau_pt          = selHadTau->pt();
    const double ptmiss          = met.pt();
    const double dr_leps         = deltaR(selLepton_lead->p4(), selLepton_sublead->p4());
    const double mT_lep1         = comp_MT_met_lep1(*selLepton_lead,    met.pt(), met.phi());
    const double mT_lep2         = comp_MT_met_lep2(*selLepton_sublead, met.pt(), met.phi());
    const double dr_lep1_tau     = deltaR(selLepton_lead->p4(),    selHadTau->p4());
    const double dr_lep2_tau     = deltaR(selLepton_sublead->p4(), selHadTau->p4());
    const double avg_dr_jet      = comp_avg_dr_jet(selJets);
    const double lep1_conePt     = comp_lep1_conePt(*selLepton_lead);
    const double lep2_conePt     = comp_lep2_conePt(*selLepton_sublead);
    const double minMET400       = std::min(met.pt(), 400.);
    const double mindr_tau_jet   = comp_mindr_hadTau1_jet(*selHadTau, selJets);
    const double mbb             = selBJets_medium.size() > 1 ?  (selBJets_medium[0]->p4() + selBJets_medium[1]->p4()).mass() : -1000;
    const double mTauTauVis1_sel = (selLepton_lead->p4() + selHadTau->p4()).mass();
    const double mTauTauVis2_sel = (selLepton_sublead->p4() + selHadTau->p4()).mass();
    const double HTT             = max_mvaOutput_HTT_2016;
    const double HadTop_pt       = unfittedHadTopP4.pt();

//--- compute output of BDTs used to discriminate ttH vs. ttV and ttH vs. tt
//    in 2lss_1tau category of ttH multilepton analysis
    std::map<std::string, double> mvaInputs_2lss = {
      { "max(abs(LepGood_eta[iF_Recl[0]]),abs(LepGood_eta[iF_Recl[1]]))", max_lep_eta                   },
      { "MT_met_lep1",                                                    mT_lep1                       },
      { "nJet25_Recl",                                                    nJet25_Recl                   },
      { "mindr_lep1_jet",                                                 std::min(10., mindr_lep1_jet) },
      { "mindr_lep2_jet",                                                 std::min(10., mindr_lep2_jet) },
      { "LepGood_conePt[iF_Recl[0]]",                                     lep1_conePt                   },
      { "LepGood_conePt[iF_Recl[1]]",                                     lep2_conePt                   },
      { "min(met_pt,400)",                                                minMET400                     },
      { "avg_dr_jet",                                                     avg_dr_jet                    },
    };
    check_mvaInputs(mvaInputs_2lss, eventInfo);
    const double mvaOutput_2lss_ttV = mva_2lss_ttV(mvaInputs_2lss);
    const double mvaOutput_2lss_tt = mva_2lss_tt(mvaInputs_2lss);

//--- compute output of BDTs used to discriminate ttH vs. ttV and  tt trained with XGB
    const std::map<std::string, double> mvaInputVariables_plainKin_tt = {
      { "avg_dr_jet",     avg_dr_jet      },
      { "dr_lep1_tau",    dr_lep1_tau     },
      { "dr_lep2_tau",    dr_lep2_tau     },
      { "dr_leps",        dr_leps         },
      { "lep1_conePt",    lep1_conePt     },
      { "lep2_conePt",    lep2_conePt     },
      { "mT_lep2",        mT_lep2         },
      { "mTauTauVis1",    mTauTauVis1_sel },
      { "mTauTauVis2",    mTauTauVis2_sel },
      { "mbb",            mbb             },
      { "mindr_lep1_jet", mindr_lep1_jet  },
      { "mindr_lep2_jet", mindr_lep2_jet  },
      { "mindr_tau_jet",  mindr_tau_jet   },
      { "nJet",           nJet25_Recl     },
      { "ptmiss",         ptmiss          },
      { "tau_pt",         tau_pt          },
    };
    const double mvaOutput_2lss_1tau_plainKin_tt = mva_2lss_1tau_plainKin_tt(mvaInputVariables_plainKin_tt);

    const std::map<std::string, double>  mvaInputVariables_plainKin_ttV = {
      { "avg_dr_jet",     avg_dr_jet      },
      { "dr_lep1_tau",    dr_lep1_tau     },
      { "dr_leps",        dr_leps         },
      { "lep1_conePt",    lep1_conePt     },
      { "lep2_conePt",    lep2_conePt     },
      { "mT_lep1",        mT_lep1         },
      { "mT_lep2",        mT_lep2         },
      { "mTauTauVis1",    mTauTauVis1_sel },
      { "mTauTauVis2",    mTauTauVis2_sel },
      { "mindr_lep1_jet", mindr_lep1_jet  },
      { "mindr_lep2_jet", mindr_lep2_jet  },
      { "mindr_tau_jet",  mindr_tau_jet   },
      { "ptmiss",         ptmiss          },
      { "max_lep_eta",    max_lep_eta     },
      { "tau_pt",         tau_pt          },
    };
    const double mvaOutput_2lss_1tau_plainKin_ttV = mva_2lss_1tau_plainKin_ttV(mvaInputVariables_plainKin_ttV);

    const std::map<std::string, double> mvaInputVariables_plainKin_1B = {
      { "BDTtt",  mvaOutput_2lss_1tau_plainKin_tt  },
      { "BDTttV", mvaOutput_2lss_1tau_plainKin_ttV },
    };
    const double mvaOutput_2lss_1tau_plainKin_1B_M = mva_2lss_1tau_plainKin_1B_M(mvaInputVariables_plainKin_1B);

    const std::map<std::string, double>  mvaInputVariables_plainKin_SUM = {
      { "avg_dr_jet",     avg_dr_jet      },
      { "dr_lep1_tau",    dr_lep1_tau     },
      { "dr_lep2_tau",    dr_lep2_tau     },
      { "dr_leps",        dr_leps         },
      { "lep1_conePt",    lep1_conePt     },
      { "lep2_conePt",    lep2_conePt     },
      { "mT_lep1",        mT_lep1         },
      { "mT_lep2",        mT_lep2         },
      { "mTauTauVis1",    mTauTauVis1_sel },
      { "mTauTauVis2",    mTauTauVis2_sel },
      { "max_lep_eta",    max_lep_eta     },
      { "mbb",            mbb             },
      { "mindr_lep1_jet", mindr_lep1_jet  },
      { "mindr_lep2_jet", mindr_lep2_jet  },
      { "mindr_tau_jet",  mindr_tau_jet   },
      { "nJet",           nJet25_Recl     },
      { "ptmiss",         ptmiss          },
      { "tau_pt",         tau_pt          },
    };
    const double mvaOutput_2lss_1tau_plainKin_SUM_M = mva_2lss_1tau_plainKin_SUM_M(mvaInputVariables_plainKin_SUM);

    const std::map<std::string, double> mvaInputVariables_HTT_SUM = {
      { "avg_dr_jet",     avg_dr_jet          },
      { "dr_lep1_tau",    dr_lep1_tau         },
      { "dr_lep2_tau",    dr_lep2_tau         },
      { "dr_leps",        dr_leps             },
      { "lep2_conePt",    lep2_conePt         },
      { "mT_lep1",        mT_lep1             },
      { "mT_lep2",        mT_lep2             },
      { "mTauTauVis2",    mTauTauVis2_sel     },
      { "max_lep_eta",    max_lep_eta         },
      { "mbb",            mbb                 },
      { "mindr_lep1_jet", mindr_lep1_jet      },
      { "mindr_lep2_jet", mindr_lep2_jet      },
      { "mindr_tau_jet",  mindr_tau_jet       },
      { "nJet",           nJet25_Recl         },
      { "ptmiss",         ptmiss              },
      { "tau_pt",         tau_pt              },
      { "HTT",            HTT                 },
      //{ "Hj_tagger",      mvaOutput_Hj_tagger },
      { "HadTop_pt",      HadTop_pt           },
    };
    const double mvaOutput_2lss_1tau_HTT_SUM_M = mva_2lss_1tau_HTT_SUM_M(mvaInputVariables_HTT_SUM);

    const std::map<std::string, double> mvaInputVariables_HTTMEM_SUM = {
      { "avg_dr_jet",     avg_dr_jet          },
      { "dr_lep1_tau",    dr_lep1_tau         },
      { "dr_lep2_tau",    dr_lep2_tau         },
      { "dr_leps",        dr_leps             },
      { "lep2_conePt",    lep2_conePt         },
      { "mT_lep1",        mT_lep1             },
      { "mT_lep2",        mT_lep2             },
      { "mTauTauVis2",    mTauTauVis2_sel     },
      { "max_lep_eta",    max_lep_eta         },
      { "mbb",            mbb                 },
      { "mindr_lep1_jet", mindr_lep1_jet      },
      { "mindr_lep2_jet", mindr_lep2_jet      },
      { "mindr_tau_jet",  mindr_tau_jet       },
      { "nJet",           nJet25_Recl         },
      { "ptmiss",         ptmiss              },
      { "tau_pt",         tau_pt              },
      { "memOutput_LR",   memOutput_LR        },
      { "HTT",            HTT                 },
      { "Hj_tagger",      mvaOutput_Hj_tagger },
      { "HadTop_pt",      HadTop_pt           },
    };
    const double mvaOutput_2lss_1tau_HTTMEM_SUM_M = mva_2lss_1tau_HTTMEM_SUM_M(mvaInputVariables_HTTMEM_SUM);

    if ( jet_ptrsHTTv2raw.size() > 0 ) contHTTv2_noclean++;
    if ( sel_HTTv2.size() > 0 ) contHTTv2_clean++;
    std::string category;
     if ( sel_HTTv2.size() > 0 ) category = "2lss_1tau_1Jp";
     else if ( selElectrons.size() >= 2 && selMuons.size() ==0 && selBJets_medium.size() >= 1  ) category = "2ess_1tau_btight_0J";
     else if ( selElectrons.size() >= 2 && selMuons.size() ==0  ) category = "2ess_1tau_bloose_0J";
     else if ( selMuons.size()     >= 2 && selElectrons.size() == 0 && selBJets_medium.size() >= 1  ) category = "2muss_1tau_btight_0J";
     else if ( selMuons.size()     >= 2 && selElectrons.size() == 0                               ) category = "2muss_1tau_bloose_0J";
     else if ( selMuons.size()     >= 1 && selElectrons.size() >= 1 && selBJets_medium.size() >= 1  ) category = "1mu1ess_1tau_btight_0J";
     else if ( selMuons.size()     >= 1 && selElectrons.size() >= 1                               ) category = "1mu1ess_1tau_bloose_0J";
     else {
       std::cout<< " A category deffinition is missing! "<<std::endl;
       std::cout<<selMuons.size()<<" "<< selElectrons.size() <<" "<< selBJets_medium.size() <<" "<<std::endl;
       assert(0);
     }

     //"lep1_conePt", "lep2_conePt",
     //"mindr_lep1_jet", "mindr_lep2_jet",
     //"mT_lep1", "mT_lep2", "max_lep_eta",
     //"nJet", "res-HTT_CSVsort4rd",
     //"HadTop_pt_CSVsort4rd",
     //"Hj_tagger", "nElectron", "mbb", "ptmiss",
     //"LeptonCharge", "resolved_and_semi_AK8", "minDR_AK8_lep", "HTT_boosted
     mvaInputs_2lss_TF["lep1_conePt"] = lep1_conePt;
     mvaInputs_2lss_TF["lep2_conePt"] = lep2_conePt;
     mvaInputs_2lss_TF["mindr_lep1_jet"] = TMath::Min(10., mindr_lep1_jet);
     mvaInputs_2lss_TF["mindr_lep2_jet"] = TMath::Min(10., mindr_lep2_jet);
     mvaInputs_2lss_TF["mT_lep1"] = comp_MT_met_lep1(*selLepton_lead, met.pt(), met.phi());
     mvaInputs_2lss_TF["mT_lep2"] = comp_MT_met_lep1(*selLepton_sublead, met.pt(), met.phi());
     mvaInputs_2lss_TF["max_lep_eta"] = TMath::Max(std::abs(selLepton_lead -> eta()), std::abs(selLepton_sublead -> eta()));
     mvaInputs_2lss_TF["nJet"] = selJets.size();
     mvaInputs_2lss_TF["res-HTT_CSVsort4rd"] = max_mvaOutput_HTT_CSVsort4rd;
     mvaInputs_2lss_TF["HadTop_pt_CSVsort4rd"] = HadTop_pt_CSVsort4rd;
     mvaInputs_2lss_TF["Hj_tagger"] = mvaOutput_Hj_tagger;
     mvaInputs_2lss_TF["nElectron"] = selElectrons.size();
     mvaInputs_2lss_TF["mbb"] = selBJets_medium.size()>1 ?  (selBJets_medium[0]->p4()+selBJets_medium[1]->p4()).mass() : -1000;
     mvaInputs_2lss_TF["ptmiss"] = met.pt();
     mvaInputs_2lss_TF["LeptonCharge"] = selLepton_lead->charge();
     mvaInputs_2lss_TF["resolved_and_semi_AK8"] = 1.0;
     mvaInputs_2lss_TF["minDR_AK8_lep"] = minDR_AK8_lep;
     mvaInputs_2lss_TF["HTT_boosted"] = HTT_boosted;
     std::map<std::string, double> mvaOutput_2lss_TF = mva_2lss_TF(mvaInputs_2lss_TF);
     if (isDEBUG) {
       for(auto elem : mvaOutput_2lss_TF) std::cout << elem.first << " " << elem.second << "\n";
     }

     std::string category_2lss_ttH_3cat_TF = "output_NN_2lss_ttH_3cat_";
     double output_NN_2lss_ttH_3cat = -10;
     if (ttH_like) {

       if (
         mvaOutput_2lss_TF["predictions_ttH"] >= mvaOutput_2lss_TF["predictions_ttW"] &&\
         mvaOutput_2lss_TF["predictions_ttH"] >= mvaOutput_2lss_TF["predictions_rest"]
       ) {category_2lss_ttH_3cat_TF += "ttH"; output_NN_2lss_ttH_3cat = mvaOutput_2lss_TF["predictions_ttH"];}
       if (
         mvaOutput_2lss_TF["predictions_ttW"] > mvaOutput_2lss_TF["predictions_ttH"] &&\
         mvaOutput_2lss_TF["predictions_ttW"] >= mvaOutput_2lss_TF["predictions_rest"]
       ) {category_2lss_ttH_3cat_TF += "ttW"; output_NN_2lss_ttH_3cat = mvaOutput_2lss_TF["predictions_ttW"];}
       if (
         mvaOutput_2lss_TF["predictions_rest"] > mvaOutput_2lss_TF["predictions_ttH"] &&\
         mvaOutput_2lss_TF["predictions_rest"] > mvaOutput_2lss_TF["predictions_ttW"]
       ) {category_2lss_ttH_3cat_TF += "rest"; output_NN_2lss_ttH_3cat = mvaOutput_2lss_TF["predictions_rest"];}

     } else if (tH_like) {
       category_2lss_ttH_3cat_TF += "tH"; output_NN_2lss_ttH_3cat = mvaOutput_2lss_TF["predictions_ttH"];
     }  else if (tH_like_1jet) {
       category_2lss_ttH_3cat_TF += "tH_1jet"; output_NN_2lss_ttH_3cat = mvaOutput_2lss_TF["predictions_ttH"];
     }

     if (ttH_like) count_ttH_like += evtWeight;
     if (tH_like && !ttH_like) count_tH_like += evtWeight;

//--- fill histograms with events passing final selection
    selHistManagerType* selHistManager = selHistManagers[idxSelLepton_genMatch][idxSelHadTau_genMatch];
    assert(selHistManager != 0);
    selHistManager->electrons_->fillHistograms(selElectrons, evtWeight);
    selHistManager->muons_->fillHistograms(selMuons, evtWeight);
    selHistManager->hadTaus_->fillHistograms(selHadTaus, evtWeight);
    selHistManager->jets_->fillHistograms(selJets, evtWeight);
    selHistManager->leadJet_->fillHistograms(selJets, evtWeight);
    selHistManager->subleadJet_->fillHistograms(selJets, evtWeight);
    selHistManager->BJets_loose_->fillHistograms(selBJets_loose, evtWeight);
    selHistManager->leadBJet_loose_->fillHistograms(selBJets_loose, evtWeight);
    selHistManager->subleadBJet_loose_->fillHistograms(selBJets_loose, evtWeight);
    selHistManager->BJets_medium_->fillHistograms(selBJets_medium, evtWeight);
    selHistManager->met_->fillHistograms(met, mht_p4, met_LD, evtWeight);
    selHistManager->metFilters_->fillHistograms(metFilters, evtWeight);
    selHistManager->mvaInputVariables_2lss_->fillHistograms(mvaInputVariables_HTT_SUM, evtWeight);
    selHistManager->evt_->fillHistograms(
      selElectrons.size(),
      selMuons.size(),
      selHadTaus.size(),
      selJets.size(),
      selBJets_loose.size(),
      selBJets_medium.size(),
      evtWeight,
      //
      mvaOutput_2lss_ttV,
      mvaOutput_2lss_tt,
      mvaOutput_2lss_1tau_plainKin_tt,
      mvaOutput_2lss_1tau_plainKin_ttV,
      mvaOutput_2lss_1tau_plainKin_1B_M,
      mvaOutput_2lss_1tau_plainKin_SUM_M,
      mvaOutput_2lss_1tau_HTT_SUM_M,
      output_NN_2lss_ttH_3cat,
      mTauTauVis1_sel,
      mTauTauVis2_sel,
      memOutput_LR
    );
    if ( isSignal ) {
      const std::string decayModeStr = eventInfo.getDecayModeString();
      if(! decayModeStr.empty())
      {
        selHistManager->evt_in_decayModes_[decayModeStr]->fillHistograms(
          selElectrons.size(),
          selMuons.size(),
          selHadTaus.size(),
          selJets.size(),
          selBJets_loose.size(),
          selBJets_medium.size(),
          evtWeight,
          mvaOutput_2lss_ttV,
          mvaOutput_2lss_tt,
          mvaOutput_2lss_1tau_plainKin_tt,
          mvaOutput_2lss_1tau_plainKin_ttV,
          mvaOutput_2lss_1tau_plainKin_1B_M,
          mvaOutput_2lss_1tau_plainKin_SUM_M,
          mvaOutput_2lss_1tau_HTT_SUM_M,
          output_NN_2lss_ttH_3cat,
          mTauTauVis1_sel,
          mTauTauVis2_sel,
          memOutput_LR
        );
        selHistManager->evt_in_categories_in_decayModes_[category+decayModeStr]->fillHistograms(
          selElectrons.size(),
          selMuons.size(),
          selHadTaus.size(),
          selJets.size(),
          selBJets_loose.size(),
          selBJets_medium.size(),
          evtWeight,
          mvaOutput_2lss_ttV,
          mvaOutput_2lss_tt,
          mvaOutput_2lss_1tau_plainKin_tt,
          mvaOutput_2lss_1tau_plainKin_ttV,
          mvaOutput_2lss_1tau_plainKin_1B_M,
          mvaOutput_2lss_1tau_plainKin_SUM_M,
          mvaOutput_2lss_1tau_HTT_SUM_M,
          output_NN_2lss_ttH_3cat,
          mTauTauVis1_sel,
          mTauTauVis2_sel,
          memOutput_LR);
      }
      EvtHistManager_2lss_1tau* selHistManager_evt_category2lss_ttH_3cat_and_decayModes = selHistManager->evt_in_categories_2lss_ttH_3cat_TF_and_decayModes_[category_2lss_ttH_3cat_TF+decayModeStr];
      if ( selHistManager_evt_category2lss_ttH_3cat_and_decayModes ) { // CV: pointer is zero when running on OS control region to estimate "charge_flip" background
      selHistManager_evt_category2lss_ttH_3cat_and_decayModes->fillHistograms(
          selElectrons.size(),
          selMuons.size(),
          selHadTaus.size(),
          selJets.size(),
          selBJets_loose.size(),
          selBJets_medium.size(),
          evtWeight,
          mvaOutput_2lss_ttV,
          mvaOutput_2lss_tt,
          mvaOutput_2lss_1tau_plainKin_tt,
          mvaOutput_2lss_1tau_plainKin_ttV,
          mvaOutput_2lss_1tau_plainKin_1B_M,
          mvaOutput_2lss_1tau_plainKin_SUM_M,
          mvaOutput_2lss_1tau_HTT_SUM_M,
          output_NN_2lss_ttH_3cat,
          mTauTauVis1_sel,
          mTauTauVis2_sel,
          memOutput_LR
          );
        }

    }
    selHistManager->evt_in_categories_[category]->fillHistograms(
      selElectrons.size(),
      selMuons.size(),
      selHadTaus.size(),
      selJets.size(),
      selBJets_loose.size(),
      selBJets_medium.size(),
      evtWeight,
      mvaOutput_2lss_ttV,
      mvaOutput_2lss_tt,
      mvaOutput_2lss_1tau_plainKin_tt,
      mvaOutput_2lss_1tau_plainKin_ttV,
      mvaOutput_2lss_1tau_plainKin_1B_M,
      mvaOutput_2lss_1tau_plainKin_SUM_M,
      mvaOutput_2lss_1tau_HTT_SUM_M,
      output_NN_2lss_ttH_3cat,
      mTauTauVis1_sel,
      mTauTauVis2_sel,
      memOutput_LR);
    EvtHistManager_2lss_1tau* selHistManager_evt_category2lss_ttH_3cat = selHistManager->evt_in_categories_2lss_ttH_3cat_TF_[category_2lss_ttH_3cat_TF];
    if ( selHistManager_evt_category2lss_ttH_3cat ) { // CV: pointer is zero when running on OS control region to estimate "charge_flip" background
      selHistManager_evt_category2lss_ttH_3cat->fillHistograms(
        selElectrons.size(),
        selMuons.size(),
        selHadTaus.size(),
        selJets.size(),
        selBJets_loose.size(),
        selBJets_medium.size(),
        evtWeight,
        mvaOutput_2lss_ttV,
        mvaOutput_2lss_tt,
        mvaOutput_2lss_1tau_plainKin_tt,
        mvaOutput_2lss_1tau_plainKin_ttV,
        mvaOutput_2lss_1tau_plainKin_1B_M,
        mvaOutput_2lss_1tau_plainKin_SUM_M,
        mvaOutput_2lss_1tau_HTT_SUM_M,
        output_NN_2lss_ttH_3cat,
        mTauTauVis1_sel,
        mTauTauVis2_sel,
        memOutput_LR
      );
    }


    selHistManager->evtYield_->fillHistograms(eventInfo, evtWeight);
    selHistManager->weights_->fillHistograms("genWeight", eventInfo.genWeight);
    selHistManager->weights_->fillHistograms("pileupWeight", eventInfo.pileupWeight);
    selHistManager->weights_->fillHistograms("triggerWeight", triggerWeight);
    selHistManager->weights_->fillHistograms("data_to_MC_correction", weight_data_to_MC_correction);
    selHistManager->weights_->fillHistograms("fakeRate", weight_fakeRate);

    if ( isMC ) {
      genEvtHistManager_afterCuts->fillHistograms(genElectrons, genMuons, genHadTaus, genPhotons, genJets, evtWeight_inclusive);
      lheInfoHistManager->fillHistograms(*lheInfoReader, evtWeight);
      if(eventWeightManager)
      {
        genEvtHistManager_afterCuts->fillHistograms(eventWeightManager, evtWeight_inclusive);
      }
    }

    if ( selEventsFile ) {
      //(*selEventsFile) << eventInfo.run << ':' << eventInfo.lumi << ':' << eventInfo.event << '\n';
      (*selEventsFile) << "(" << eventInfo.run << ", " << eventInfo.lumi << ", " << eventInfo.event << "L, " << weight_fakeRate
		       << ", " << prob_fake_lepton_lead << ", " << passesTight_lepton_lead << ", " << prob_fake_lepton_sublead << ", " << passesTight_lepton_sublead
		       << ")" << '\n';
    }

    double memOutput_type=memOutput_2lss_1tau_matched.is_initialized() ? memOutput_2lss_1tau_matched.type() : -100.;
    double memOutput_ttH=memOutput_2lss_1tau_matched.is_initialized() ? memOutput_2lss_1tau_matched.weight_ttH()     : -100.;
    double memOutput_tt=memOutput_2lss_1tau_matched.is_initialized() ? memOutput_2lss_1tau_matched.weight_tt()      : -100.;
    double memOutput_ttZ=memOutput_2lss_1tau_matched.is_initialized() ? memOutput_2lss_1tau_matched.weight_ttZ()     : -100.;
    double memOutput_ttZ_Zll=memOutput_2lss_1tau_matched.is_initialized() ? memOutput_2lss_1tau_matched.weight_ttZ_Zll() : -100.;

    const bool isGenMatched = isMC &&
      ((apply_leptonGenMatching && selLepton_genMatch.numGenMatchedJets_ == 0) || ! apply_leptonGenMatching)
    ;

    if ( bdt_filler ) {

      std::map<std::string, double> mvaInputs_Hjj_tagger;
      double mvaOutput_Hjj_tagger = -1.;
      for ( std::vector<const RecoJet*>::const_iterator selJet1 = selJets.begin();
        selJet1 != selJets.end(); ++selJet1 ) {
          if ((*selJet1)->pt()==Wj1_pt_CSVsort4rd_1 || (*selJet1)->pt()==Wj2_pt_CSVsort4rd_1 || (*selJet1)->pt()==b_pt_CSVsort4rd_1) continue;
          for ( std::vector<const RecoJet*>::const_iterator selJet2 = selJet1 + 1;
            selJet2 != selJets.end(); ++selJet2 ) {
              if ((*selJet2)->pt()==Wj1_pt_CSVsort4rd_1 || (*selJet2)->pt()==Wj2_pt_CSVsort4rd_1 || (*selJet2)->pt()==b_pt_CSVsort4rd_1) continue;
              double mvaOutput = comp_mvaOutput_Hjj_tagger(
              *selJet1, *selJet2, selJets, fakeableLeptons,
              mvaInputs_Hjj_tagger, mva_Hjj_tagger,
              mvaInputs_Hj_tagger, mva_Hj_tagger, eventInfo);
              if ( mvaOutput > mvaOutput_Hjj_tagger ) mvaOutput_Hjj_tagger = mvaOutput;
        }
      }
      double lep1_genLepPt=( selLepton_lead->genLepton() != 0 ) ? selLepton_lead->genLepton()->pt() : 0.;
      double lep2_genLepPt=( selLepton_sublead->genLepton() != 0 ) ? selLepton_sublead->genLepton()->pt() : 0.;
      double tau_genTauPt=( selHadTau->genHadTau() != 0 ) ? selHadTau->genHadTau()->pt() : 0.;

      bdt_filler -> operator()({ eventInfo.run, eventInfo.lumi, eventInfo.event })
          ("nElectron",                      selElectrons.size())
          ("nMuon",                          selMuons.size())
          ("lep1_pt",                        selLepton_lead->pt())
          ("lep1_conePt",                    lep1_conePt)
          ("lep1_eta",                       selLepton_lead->absEta())
          ("lep1_tth_mva",                   selLepton_lead->mvaRawTTH())
          ("mindr_lep1_jet",                 std::min(10., mindr_lep1_jet) )
          ("mindr_lep2_jet",                 std::min(10., mindr_lep2_jet) )
          ("mT_lep1",                        mT_lep1)
          ("MT_met_lep1",                    comp_MT_met_lep1(selLepton_lead->cone_p4(), met.pt(), met.phi()))
          ("dr_lep1_tau",                    dr_lep1_tau)
          ("lep2_pt",                        selLepton_sublead->pt())
          ("lep2_conePt",                    lep2_conePt)
          ("lep2_eta",                       selLepton_sublead->absEta())
          ("max_lep_eta",                    max_lep_eta)
          ("avg_dr_lep",                     1.0) // dr_leps??
          ("lep2_tth_mva",                   selLepton_sublead->mvaRawTTH())
          ("mT_lep2",                        mT_lep2)
          ("dr_lep2_tau",                    dr_lep2_tau)
          ("mindr_tau_jet",                  std::min(10., mindr_tau_jet))
          ("avg_dr_jet",                     avg_dr_jet)
          ("nJet25_Recl",                    nJet25_Recl)
          ("ptmiss",                         ptmiss)
          ("htmiss",                         mht_p4.pt())
          ("tau_mva",                        selHadTau->raw_mva_dR03())
          ("tau_pt",                         selHadTau->pt())
          ("tau_eta",                        selHadTau->absEta())
          ("dr_leps",                        dr_leps)
          ("mTauTauVis1",                    mTauTauVis1_sel)
          ("mTauTauVis2",                    mTauTauVis2_sel)
          ("memOutput_isValid",              memOutput_2lss_1tau_matched.is_initialized() ? memOutput_2lss_1tau_matched.isValid()   : -100.)
          ("memOutput_errorFlag",            memOutput_2lss_1tau_matched.is_initialized() ? memOutput_2lss_1tau_matched.errorFlag() : -100.)
          ("memOutput_LR",                   memOutput_LR)
          ("lep1_genLepPt",                  lep1_genLepPt)
          ("lep2_genLepPt",                  lep2_genLepPt)
          ("tau_genTauPt",                   tau_genTauPt)
          ("lep1_fake_prob",                 selLepton_lead->genLepton() ? 1.0 : prob_fake_lepton_lead)
          ("lep2_fake_prob",                 selLepton_sublead->genLepton()? 1.0 : prob_fake_lepton_sublead)
          ("tau_fake_prob",                  selHadTau->genHadTau() || selHadTau->genLepton() ? 1.0 : prob_fake_hadTau)
          ("tau_fake_test",                  selHadTau->genHadTau() ? 1.0 : prob_fake_hadTau)
          ("Hj_tagger",                      mvaOutput_Hj_tagger)

          ("hadtruth",               hadtruth)
          ("bWj1Wj2_isGenMatched_CSVsort4rd",              max_truth_HTT_CSVsort4rd)
          ("res-HTT_CSVsort4rd",                 max_mvaOutput_HTT_CSVsort4rd)
          ("HadTop_pt_CSVsort4rd",            HadTop_pt_CSVsort4rd)
          ("genTopPt_CSVsort4rd",             genTopPt_CSVsort4rd)

          ("genWeight",                      eventInfo.genWeight)
          ("evtWeight",                      evtWeight)
          ("nJet",                           nJet25_Recl)
          ("nLep",                           selLeptons.size())
          ("nTau",                           selHadTaus.size())
          ("nBJetLoose",                     selBJets_loose.size())
          ("nBJetMedium",                    selBJets_medium.size())
          ("lep1_isTight",                   static_cast<int>(selLepton_lead->isTight()))
          ("lep2_isTight",                   static_cast<int>(selLepton_sublead->isTight()))
          ("tau_isTight",                    static_cast<int>(tightHadTauFilter(*selHadTau)))
          ("min(met_pt,400)",                minMET400)
          ("mbb",                            selBJets_medium.size() > 1 ? (selBJets_medium[0]->p4() + selBJets_medium[1]->p4()).mass() : -1000)
          ("ptbb",                           selBJets_medium.size() > 1 ? (selBJets_medium[0]->p4() + selBJets_medium[1]->p4()).pt() : -1000)
          ("mbb_loose",                      selBJets_loose.size()  > 1 ? (selBJets_loose[0]->p4() + selBJets_loose[1]->p4()).mass() : -1000)
          ("ptbb_loose",                     selBJets_loose.size()  > 1 ? (selBJets_loose[0]->p4() + selBJets_loose[1]->p4()).pt() : -1000)
          ("failsTightChargeCut",            failsTightChargeCut)

          ("res-HTT",                        max_mvaOutput_HTT_2016)
          ("HadTop_pt",                      fittedHadTopP4.pt())
          ("HadTop_eta",                     std::fabs(fittedHadTopP4.eta()))
          ("hadtruth",                       hadtruth)
          ("bWj1Wj2_isGenMatchedWithKinFit", max_truth_HTT_2016)
          ("bWj1Wj2_isGenMatched_IHEP",                    max_truth_multilep)
          ("bWj1Wj2_isGenMatched_CSVsort4rd",              max_truth_HTT_CSVsort4rd)
          ("bWj1Wj2_isGenMatched_highestCSV",              max_truth_HTT_highestCSV)
          ("bWj1Wj2_isGenMatched_CSVsort4rd_WithKinFit",   max_truth_HTT_CSVsort4rd_WithKinFit)
          ("bWj1Wj2_isGenMatched_highestCSV_WithKinFit",   max_truth_HTT_highestCSV_WithKinFit)

          ("res-HTT_CSVsort4rd",                 max_mvaOutput_HTT_CSVsort4rd)
          ("res-HTT_highestCSV",                 max_mvaOutput_HTT_highestCSV)
          ("res-HTT_CSVsort4rd_WithKinFit",      max_mvaOutput_HTT_CSVsort4rd_WithKinFit)
          ("res-HTT_highestCSV_WithKinFit",      max_mvaOutput_HTT_highestCSV_WithKinFit)
          ("res-HTT_IHEP",                       max_mvaOutput_HTT_multilep)

          ("HadTop_pt_multilep",              HadTop_pt_multilep)
          ("HadTop_pt_CSVsort4rd",            HadTop_pt_CSVsort4rd)
          ("HadTop_pt_highestCSV",            HadTop_pt_highestCSV)
          ("HadTop_pt_CSVsort4rd_WithKinFit", HadTop_pt_CSVsort4rd_WithKinFit)
          ("HadTop_pt_highestCSV_WithKinFit", HadTop_pt_highestCSV_WithKinFit)

          ("genTopPt_multilep",               genTopPt_multilep)
          ("genTopPt_CSVsort4rd",             genTopPt_CSVsort4rd)
          ("genTopPt_highestCSV",             genTopPt_highestCSV)
          ("genTopPt_CSVsort4rd_WithKinFit",  genTopPt_CSVsort4rd_WithKinFit)
          ("genTopPt_highestCSV_WithKinFit",  genTopPt_highestCSV_WithKinFit)

          ("hadtruth_boosted",               hadtruth_boosted)
          ("hadtruth_semi_boosted_AK8",               hadtruth_semi_boosted_AK8)

          ("genTopPt",                       genTopPt)
          //("prob_fake_lepton",               lep_genLepPt > 0 ? 1.0 : prob_fake_lepton)
          //("tau_fake_prob_lead",             tau1_genTauPt > 0 ? 1.0 : prob_fake_hadTau_lead)
          //("tau_fake_prob_sublead",          tau2_genTauPt > 0 ? 1.0 : prob_fake_hadTau_sublead)

          ("nHTTv2",                         sel_HTTv2.size())
          ("HTTv2_lead_pt",                  sel_HTTv2.size() > 0 ? sel_HTTv2[0]->pt() : -1 )
          ("HTTv2_lead_mass",                sel_HTTv2.size() > 0 ? sel_HTTv2[0]->p4().mass() : -1 )
          ("minDR_HTTv2_L",                  minDR_HTTv2_L)
          ("minDR_HTTv2_lep",                minDR_HTTv2_lep)
          ("minDR_HTTv2_tau",                   minDR_HTTv2_tau )

          ("HTT_boosted",                     HTT_boosted)
          ("bWj1Wj2_isGenMatched_boosted",    bWj1Wj2_isGenMatched_boosted)
          ("genTopPt_boosted",            genTopPt_boosted)
          ("HadTop_pt_HTT_boosted",           HadTop_pt_HTT_boosted)
          ("HTT_boosted_WithKinFit",                  HTT_boosted_WithKinFit)
          ("bWj1Wj2_isGenMatched_boosted_WithKinFit", bWj1Wj2_isGenMatched_boosted_WithKinFit)
          ("genTopPt_boosted_WithKinFit",         genTopPt_boosted_WithKinFit)
          ("HadTop_pt_HTT_boosted_WithKinFit",        HadTop_pt_HTT_boosted_WithKinFit)

          ("HTT_semi_boosted_AK8",                     HTT_semi_boosted_AK8)
          ("bWj1Wj2_isGenMatched_semi_boosted_AK8",    bWj1Wj2_isGenMatched_semi_boosted_AK8)
          ("genTopPt_semi_boosted",            genTopPt_semi_boosted)
          ("HadTop_pt_HTT_semi_boosted_AK8",           HadTop_pt_HTT_semi_boosted_AK8)
          ("HTT_semi_boosted_AK8_WithKinFit",                  HTT_semi_boosted_AK8_WithKinFit)
          ("bWj1Wj2_isGenMatched_semi_boosted_AK8_WithKinFit", bWj1Wj2_isGenMatched_semi_boosted_AK8_WithKinFit)
          ("genTopPt_semi_boosted_WithKinFit",         genTopPt_semi_boosted_WithKinFit)
          ("HadTop_pt_HTT_semi_boosted_AK8_WithKinFit",        HadTop_pt_HTT_semi_boosted_AK8_WithKinFit)

          ("minDR_AK8_L",                  minDR_AK8_L)
          ("minDR_AK8_lep",                minDR_AK8_lep)
          ("DR_AK8_tau",                   DR_AK8_tau )

          ("nJetForward",                  selJetsForward.size())

          ("N_jetAK8",     jet_ptrsAK8.size())
          ("mvaOutput_2lss_1tau_HTTMEM_SUM_M", mvaOutput_2lss_1tau_HTTMEM_SUM_M)
        .fill()
      ;
    }

    if(snm)
    {
      const double dr_lep1_tau1   = deltaR(selLepton_lead->p4(), selHadTau->p4());
      const double dr_lep2_tau1   = deltaR(selLepton_sublead->p4(), selHadTau->p4());
      const double max_dr_jet     = comp_max_dr_jet(selJets);
      const double mbb_loose      = selBJets_loose.size() > 1 ? (selBJets_loose[0]->p4() + selBJets_loose[1]->p4()).mass() : -1.;
      const double avr_dr_lep_tau = (dr_lep1_tau1 + dr_lep2_tau1) / 2;
      const double max_dr_lep_tau = std::max(dr_lep2_tau1, dr_lep1_tau1);
      const double min_dr_lep_tau = std::min(dr_lep2_tau1, dr_lep1_tau1);
      const double min_dr_lep_jet = std::min(mindr_lep1_jet, mindr_lep2_jet);

      snm->read(eventInfo);
      snm->read(selLeptons);
      snm->read(preselMuons,     fakeableMuons,     tightMuons);
      snm->read(preselElectrons, fakeableElectrons, tightElectrons);
      snm->read(preselHadTaus);
      snm->read(selJets);

      snm->read({ triggers_1e, triggers_2e, triggers_1mu, triggers_2mu, triggers_1e1mu });
      snm->read(isGenMatched, selBJets_medium.size(), selBJets_loose.size());

      snm->read(met.pt(),                               FloatVariableType::PFMET);
      snm->read(met.phi(),                              FloatVariableType::PFMETphi);
      snm->read(mht_p4.pt(),                            FloatVariableType::MHT);
      snm->read(met_LD,                                 FloatVariableType::metLD);

      snm->read(mindr_lep1_jet,                         FloatVariableType::mindr_lep1_jet);
      snm->read(mindr_lep2_jet,                         FloatVariableType::mindr_lep2_jet);
      // mindr_lep3_jet not filled
      // mindr_lep4_jet not filled

      snm->read(mindr_tau_jet,                          FloatVariableType::mindr_tau1_jet);
      // mindr_tau2_jet not filled

      snm->read(avg_dr_jet,                             FloatVariableType::avg_dr_jet);
      snm->read(avr_dr_lep_tau,                         FloatVariableType::avr_dr_lep_tau);
      snm->read(max_dr_jet,                             FloatVariableType::max_dr_jet);
      snm->read(max_dr_lep_tau,                         FloatVariableType::max_dr_lep_tau);
      snm->read(mindr_tau_jet,                          FloatVariableType::min_dr_tau_jet); // 1 tau
      snm->read(min_dr_lep_tau,                         FloatVariableType::min_dr_lep_tau);
      snm->read(min_dr_lep_jet,                         FloatVariableType::min_dr_lep_jet);

      snm->read(dr_leps,                                FloatVariableType::dr_leps);
      // dr_taus not filled

      // dr_lep_tau_ss not filled
      snm->read(dr_lep1_tau1,                           FloatVariableType::dr_lep1_tau1);
      // dr_lep1_tau2 not filled
      snm->read(dr_lep2_tau1,                           FloatVariableType::dr_lep2_tau1);
      // dr_lep3_tau1 not filled
      // dr_lep2_tau2 not filled

      snm->read(max_lep_eta,                            FloatVariableType::max_lep_eta);

      snm->read(mT_lep1,                                FloatVariableType::mT_met_lep1);
      snm->read(mT_lep2,                                FloatVariableType::mT_met_lep2);
      // mT_met_lep3 not filled
      // mT_met_lep4 not filled

      // mTauTauVis not filled
      snm->read(mTauTauVis1_sel,                        FloatVariableType::mvis_l1tau);
      snm->read(mTauTauVis2_sel,                        FloatVariableType::mvis_l2tau);

      snm->read(mbb,                                    FloatVariableType::mbb);
      snm->read(mbb_loose,                              FloatVariableType::mbb_loose);

      // cosThetaS_hadTau not filled
      snm->read(HTT,                                    FloatVariableType::HTT);
      snm->read(HadTop_pt,                              FloatVariableType::HadTop_pt);
      snm->read(mvaOutput_Hj_tagger,                    FloatVariableType::Hj_tagger);

      // mvaOutput_plainKin_ttV not filled
      // mvaOutput_plainKin_tt not filled
      // mvaOutput_plainKin_1B_VT not filled
      // mvaOutput_HTT_SUM_VT not filled

      // mvaOutput_plainKin_SUM_VT not filled

      snm->read(mvaOutput_2lss_ttV,                     FloatVariableType::mvaOutput_2lss_ttV);
      snm->read(mvaOutput_2lss_tt,                      FloatVariableType::mvaOutput_2lss_tt);
      snm->read(mvaOutput_2lss_1tau_plainKin_tt,        FloatVariableType::mvaOutput_2lss_1tau_plainKin_tt);
      snm->read(mvaOutput_2lss_1tau_plainKin_ttV,       FloatVariableType::mvaOutput_2lss_1tau_plainKin_ttV);
      snm->read(mvaOutput_2lss_1tau_plainKin_1B_M,      FloatVariableType::mvaOutput_2lss_1tau_plainKin_1B_M);
      snm->read(mvaOutput_2lss_1tau_plainKin_SUM_M,     FloatVariableType::mvaOutput_2lss_1tau_plainKin_SUM_M);
      snm->read(mvaOutput_2lss_1tau_HTT_SUM_M,          FloatVariableType::mvaOutput_2lss_1tau_HTT_SUM_M);
      snm->read(mvaOutput_2lss_1tau_HTTMEM_SUM_M,       FloatVariableType::mvaOutput_2lss_1tau_HTTMEM_SUM_M);

      // mvaOutput_3l_ttV not filled
      // mvaOutput_3l_ttbar not filled
      // mvaOutput_plainKin_SUM_M not filled
      // mvaOutput_plainKin_1B_M not filled

      snm->read(weight_fakeRate,                        FloatVariableType::FR_weight);
      snm->read(triggerWeight,                          FloatVariableType::triggerSF_weight);
      snm->read(leptonSF_weight,                        FloatVariableType::leptonSF_weight);
      snm->read(tauSF_weight,                           FloatVariableType::tauSF_weight);
      snm->read(btagWeight,                             FloatVariableType::bTagSF_weight);
      snm->read(eventInfo.pileupWeight,                 FloatVariableType::PU_weight);
      snm->read(boost::math::sign(eventInfo.genWeight), FloatVariableType::MC_weight);

      snm->read(memOutput_ttH,                          FloatVariableType::Integral_ttH);
      snm->read(memOutput_ttZ,                          FloatVariableType::Integral_ttZ);
      snm->read(memOutput_ttZ_Zll,                      FloatVariableType::Integral_ttZ_Zll);
      snm->read(memOutput_tt,                           FloatVariableType::Integral_ttbar);
      snm->read(memOutput_type,                         FloatVariableType::integration_type);
      snm->read(memOutput_LR,                           FloatVariableType::MEM_LR);

      snm->read(eventInfo.genWeight,                    FloatVariableType::genWeight);

      if((sync_requireGenMatching && isGenMatched) || ! sync_requireGenMatching)
      {
        snm->fill();
      }
      else
      {
        snm->reset();
      }
    }

    ++selectedEntries;
    selectedEntries_weighted += evtWeight;
    histogram_selectedEntries->Fill(0.);
  }

  if(snm)
  {
    snm->write();
  }

  std::cout << "max num. Entries = " << inputTree -> getCumulativeMaxEventCount()
            << " (limited by " << maxEvents << ") processed in "
            << inputTree -> getProcessedFileCount() << " file(s) (out of "
            << inputTree -> getFileCount() << ")\n"
            << " analyzed = " << analyzedEntries << '\n'
            << " selected = " << selectedEntries << " (weighted = " << selectedEntries_weighted << ")\n\n"
            << "cut-flow table" << std::endl;
  cutFlowTable.print(std::cout);
  std::cout << std::endl;

  std::cout << "count_ttH_like = " << count_ttH_like << "\n"
  <<  "count_tH_like =" << count_tH_like << "\n\n";

  std::cout << "sel. Entries by gen. matching:" << std::endl;
  for ( std::vector<leptonGenMatchEntry>::const_iterator leptonGenMatch_definition = leptonGenMatch_definitions.begin();
        leptonGenMatch_definition != leptonGenMatch_definitions.end(); ++leptonGenMatch_definition ) {
    for ( std::vector<hadTauGenMatchEntry>::const_iterator hadTauGenMatch_definition = hadTauGenMatch_definitions.begin();
          hadTauGenMatch_definition != hadTauGenMatch_definitions.end(); ++hadTauGenMatch_definition ) {

      std::string process_and_genMatch = process_string;
      if ( apply_leptonGenMatching ) process_and_genMatch += leptonGenMatch_definition->name_;
      if ( apply_leptonGenMatching && apply_hadTauGenMatching ) process_and_genMatch += "&";
      if ( apply_hadTauGenMatching ) process_and_genMatch += hadTauGenMatch_definition->name_;

      int idxLepton = leptonGenMatch_definition->idx_;
      int idxHadTau = hadTauGenMatch_definition->idx_;

      const TH1* histogram_EventCounter = selHistManagers[idxLepton][idxHadTau]->evt_->getHistogram_EventCounter();
      std::cout << " " << process_and_genMatch << " = " << histogram_EventCounter->GetEntries() << " (weighted = " << histogram_EventCounter->Integral() << ")" << std::endl;
    }
  }
  std::cout << std::endl;
  std::cout << "count HTTv2 selected with/without cleaning " << contHTTv2_clean << " " << contHTTv2_noclean  << std::endl;

  delete dataToMCcorrectionInterface;

  delete leptonFakeRateInterface;
  delete jetToTauFakeRateInterface;

  delete run_lumi_eventSelector;

  delete selEventsFile;

  delete muonReader;
  delete electronReader;
  delete hadTauReader;
  delete jetReader;
  delete metReader;
  delete metFilterReader;
  delete memReader;
  delete genLeptonReader;
  delete genHadTauReader;
  delete genPhotonReader;
  delete genJetReader;
  delete lheInfoReader;

  //delete hadTopTagger;

  delete genEvtHistManager_beforeCuts;
  delete genEvtHistManager_afterCuts;
  delete lheInfoHistManager;
  delete cutFlowHistManager;
  delete eventWeightManager;

  delete inputTree;
  delete snm;

  clock.Show("analyze_2lss_1tau");

  return EXIT_SUCCESS;
}
