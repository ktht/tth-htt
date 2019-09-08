#include "tthAnalysis/HiggsToTauTau/interface/EvtWeightRecorder.h" // EvtWeightRecorder

#include "tthAnalysis/HiggsToTauTau/interface/L1PreFiringWeightReader.h"
#include "tthAnalysis/HiggsToTauTau/interface/LHEInfoReader.h"
#include "tthAnalysis/HiggsToTauTau/interface/EventInfo.h"
#include "tthAnalysis/HiggsToTauTau/interface/Data_to_MC_CorrectionInterface_Base.h"
#include "tthAnalysis/HiggsToTauTau/interface/JetToTauFakeRateInterface.h"
#include "tthAnalysis/HiggsToTauTau/interface/LeptonFakeRateInterface.h"
#include "tthAnalysis/HiggsToTauTau/interface/analysisAuxFunctions.h"
#include "tthAnalysis/HiggsToTauTau/interface/sysUncertOptions.h"

#include <cassert> // assert()

EvtWeightRecorder::EvtWeightRecorder()
  : central_(1.)
  , leptonSF_(1.)
{}

EvtWeightRecorder::EvtWeightRecorder(const std::vector<std::string> & central_or_shifts,
                                     bool isMC)
  : central_(1.)
  , leptonSF_(1.)
  , central_or_shifts_(central_or_shifts)
{
  for(const std::string & central_or_shift: central_or_shifts_)
  {
    checkOptionValidity(central_or_shift, isMC);
  }
}

double
EvtWeightRecorder::get(const std::string & central_or_shift) const
{
  if(! weights_.count(central_or_shift))
  {
    throw cmsException(this, __func__, __LINE__) << "Invalid option: " << central_or_shift;
  }
  return weights_.at(central_or_shift);
}

double
EvtWeightRecorder::get_inclusive() const
{
  double inclusive = central_;
  if(weights_l1PreFiring_.count(L1PreFiringWeightSys::nominal))
  {
    inclusive *= weights_l1PreFiring_.at(L1PreFiringWeightSys::nominal);
  }
  if(weights_lheScale_.count(kLHE_scale_central))
  {
    inclusive *= weights_lheScale_.at(kLHE_scale_central);
  }
  if(weights_pu_.count(PUsys::central))
  {
    inclusive *= weights_pu_.at(PUsys::central);
  }
  return inclusive;
}

double
EvtWeightRecorder::get_btag() const
{
  if(weights_btag_.count(kBtag_central))
  {
    return weights_btag_.at(kBtag_central);
  }
  return 1.;
}

double
EvtWeightRecorder::get_sf_triggerEff() const
{
  if(weights_leptonTriggerEff_.count(TriggerSFsys::central))
  {
    return weights_leptonTriggerEff_.at(TriggerSFsys::central);
  }
  return 1.;
}

double
EvtWeightRecorder::get_leptonSF() const
{
  return leptonSF_;
}

double
EvtWeightRecorder::get_tauSF() const
{
  double tauSF_weight = 1.;
  if(weights_hadTauID_and_Iso_.count(TauIDSFsys::central))
  {
    tauSF_weight *= weights_hadTauID_and_Iso_.count(TauIDSFsys::central);
  }
  if(weights_eToTauFakeRate_.count(FRet::central))
  {
    tauSF_weight *= weights_eToTauFakeRate_.count(FRet::central);
  }
  if(weights_muToTauFakeRate_.count(FRmt::central))
  {
    tauSF_weight *= weights_muToTauFakeRate_.count(FRmt::central);
  }
  return tauSF_weight;
}

EvtWeightRecorder &
EvtWeightRecorder::operator*=(double weight)
{
  central_ *= weight;
  return *this;
}

void
EvtWeightRecorder::record_leptonSF(double weight)
{
  leptonSF_ *= weight;
  central_ *= weight;
}

void
EvtWeightRecorder::record_l1PrefireWeight(const L1PreFiringWeightReader * const l1PreFiringWeightReader)
{
  weights_l1PreFiring_.clear();
  for(const std::string & central_or_shift: central_or_shifts_)
  {
    const L1PreFiringWeightSys l1PreFire_option = getL1PreFiringWeightSys_option(central_or_shift);
    if(weights_l1PreFiring_.count(l1PreFire_option))
    {
      continue;
    }
    weights_l1PreFiring_[l1PreFire_option] = l1PreFiringWeightReader->getWeight(l1PreFire_option);
  }
}

void
EvtWeightRecorder::record_lheScaleWeight(const LHEInfoReader * const lheInfoReader)
{
  weights_lheScale_.clear();
  for(const std::string & central_or_shift: central_or_shifts_)
  {
    const int lheScale_option = getLHEscale_option(central_or_shift);
    if(weights_lheScale_.count(lheScale_option))
    {
      continue;
    }
    weights_lheScale_[lheScale_option] = lheInfoReader->getWeight_scale(lheScale_option);
  }
}

void
EvtWeightRecorder::record_puWeight(const EventInfo * const eventInfo)
{
  weights_pu_.clear();
  for(const std::string & central_or_shift: central_or_shifts_)
  {
    const PUsys puSys_option = getPUsys_option(central_or_shift);
    if(weights_pu_.count(puSys_option))
    {
      continue;
    }
    switch(puSys_option)
    {
      case PUsys::central: weights_pu_[puSys_option] = eventInfo->pileupWeight;     break;
      case PUsys::up:      weights_pu_[puSys_option] = eventInfo->pileupWeightUp;   break;
      case PUsys::down:    weights_pu_[puSys_option] = eventInfo->pileupWeightDown; break;
      default: assert(0);
    }
  }
}

void
EvtWeightRecorder::record_btagWeight(const std::vector<const RecoJet *> & jets)
{
  weights_btag_.clear();
  for(const std::string & central_or_shift: central_or_shifts_)
  {
    const int jetBtagSF_option = getBTagWeight_option(central_or_shift);
    if(weights_btag_.count(jetBtagSF_option))
    {
      continue;
    }
    weights_btag_[jetBtagSF_option] = get_BtagWeight(jets, jetBtagSF_option);
  }
}

void
EvtWeightRecorder::record_leptonTriggerEff(const Data_to_MC_CorrectionInterface_Base * const dataToMCcorrectionInterface)
{
  weights_leptonTriggerEff_.clear();
  for(const std::string & central_or_shift: central_or_shifts_)
  {
    const TriggerSFsys triggerSF_option = getTriggerSF_option(central_or_shift);
    if(weights_leptonTriggerEff_.count(triggerSF_option))
    {
      continue;
    }
    weights_leptonTriggerEff_[triggerSF_option] = dataToMCcorrectionInterface->getSF_leptonTriggerEff(triggerSF_option);
  }
}

void
EvtWeightRecorder::record_hadTauID_and_Iso(const Data_to_MC_CorrectionInterface_Base * const dataToMCcorrectionInterface)
{
  weights_hadTauID_and_Iso_.clear();
  for(const std::string & central_or_shift: central_or_shifts_)
  {
    const TauIDSFsys tauIDSF_option = getTauIDSFsys_option(central_or_shift);
    if(weights_hadTauID_and_Iso_.count(tauIDSF_option))
    {
      continue;
    }
    weights_hadTauID_and_Iso_[tauIDSF_option] = dataToMCcorrectionInterface->getSF_hadTauID_and_Iso(tauIDSF_option);
  }
}

void
EvtWeightRecorder::record_eToTauFakeRate(const Data_to_MC_CorrectionInterface_Base * const dataToMCcorrectionInterface)
{
  weights_eToTauFakeRate_.clear();
  for(const std::string & central_or_shift: central_or_shifts_)
  {
    const FRet eToTauFakeRate_option = getEToTauFR_option(central_or_shift);
    if(weights_eToTauFakeRate_.count(eToTauFakeRate_option))
    {
      continue;
    }
    weights_eToTauFakeRate_[eToTauFakeRate_option] = dataToMCcorrectionInterface->getSF_eToTauFakeRate(eToTauFakeRate_option);
  }
}

void
EvtWeightRecorder::record_muToTauFakeRate(const Data_to_MC_CorrectionInterface_Base * const dataToMCcorrectionInterface)
{
  weights_muToTauFakeRate_.clear();
  for(const std::string & central_or_shift: central_or_shifts_)
  {
    const FRmt muToTauFakeRate_option = getMuToTauFR_option(central_or_shift);
    if(weights_muToTauFakeRate_.count(muToTauFakeRate_option))
    {
      continue;
    }
    weights_muToTauFakeRate_[muToTauFakeRate_option] = dataToMCcorrectionInterface->getSF_muToTauFakeRate(muToTauFakeRate_option);
  }
}

void
EvtWeightRecorder::record_jetToTau_FR_lead(const JetToTauFakeRateInterface * const jetToTauFakeRateInterface,
                                           double hadTauPt_lead,
                                           double hadTauAbsEta_lead)
{
  weights_FR_hadTau_lead_.clear();
  for(const std::string & central_or_shift: central_or_shifts_)
  {
    const int jetToTauFakeRate_option = getJetToTauFR_option(central_or_shift);
    if(weights_FR_hadTau_lead_.count(jetToTauFakeRate_option))
    {
      continue;
    }
    weights_FR_hadTau_lead_[jetToTauFakeRate_option] = jetToTauFakeRateInterface->getWeight_lead(
      hadTauPt_lead, hadTauAbsEta_lead, jetToTauFakeRate_option
    );
  }
}

void
EvtWeightRecorder::record_jetToTau_SF_lead(const JetToTauFakeRateInterface * const jetToTauFakeRateInterface,
                                           double hadTauPt_lead,
                                           double hadTauAbsEta_lead)
{
  weights_SF_hadTau_lead_.clear();
  for(const std::string & central_or_shift: central_or_shifts_)
  {
    const int jetToTauFakeRate_option = getJetToTauFR_option(central_or_shift);
    if(weights_SF_hadTau_lead_.count(jetToTauFakeRate_option))
    {
      continue;
    }
    weights_SF_hadTau_lead_[jetToTauFakeRate_option] = jetToTauFakeRateInterface->getSF_lead(
      hadTauPt_lead, hadTauAbsEta_lead, jetToTauFakeRate_option
    );
  }
}

void
EvtWeightRecorder::record_jetToLepton_FR(const LeptonFakeRateInterface * const leptonFakeRateInterface,
                                         double leptonPt,
                                         double leptonAbsEta,
                                         int leptonPdgId,
                                         std::map<int, double> & weights_FR_lepton)
{
  assert(leptonPdgId == 11 || leptonPdgId == 13);
  weights_FR_lepton.clear();
  for(const std::string & central_or_shift: central_or_shifts_)
  {
    const int jetToLeptonFakeRate_option = getJetToLeptonFR_option(central_or_shift);
    if(weights_FR_lepton.count(jetToLeptonFakeRate_option))
    {
      continue;
    }
    if(leptonPdgId == 11 &&
       (jetToLeptonFakeRate_option == kFRl_central ||
        (jetToLeptonFakeRate_option >= kFRe_shape_ptUp && jetToLeptonFakeRate_option <= kFRe_shape_eta_barrelDown)))
    {
      weights_FR_lepton[jetToLeptonFakeRate_option] = leptonFakeRateInterface->getWeight_e(
        leptonPt, leptonAbsEta, jetToLeptonFakeRate_option
      );
    }
    else if(leptonPdgId == 13 &&
            (jetToLeptonFakeRate_option == kFRl_central ||
            (jetToLeptonFakeRate_option >= kFRm_shape_ptUp && jetToLeptonFakeRate_option <= kFRm_shape_eta_barrelDown)))
    {
      weights_FR_lepton[jetToLeptonFakeRate_option] = leptonFakeRateInterface->getWeight_mu(
        leptonPt, leptonAbsEta, jetToLeptonFakeRate_option
      );
    }
  }
}

void
EvtWeightRecorder::record_jetToLepton_FR_lead(const LeptonFakeRateInterface * const leptonFakeRateInterface,
                                              double leptonPt_lead,
                                              double leptonAbsEta_lead,
                                              int leptonPdgId_lead)
{
  record_jetToLepton_FR(leptonFakeRateInterface, leptonPt_lead, leptonAbsEta_lead, leptonPdgId_lead, weights_FR_lepton_lead_);
}

void
EvtWeightRecorder::record_jetToLepton_FR_sublead(const LeptonFakeRateInterface * const leptonFakeRateInterface,
                                                 double leptonPt_sublead,
                                                 double leptonAbsEta_sublead,
                                                 int leptonPdgId_sublead)
{
  record_jetToLepton_FR(leptonFakeRateInterface, leptonPt_sublead, leptonAbsEta_sublead, leptonPdgId_sublead, weights_FR_lepton_sublead_);
}

void
EvtWeightRecorder::reset()
{
  weights_.clear();
}

