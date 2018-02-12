#include "tthAnalysis/HiggsToTauTau/interface/RecoJetReaderHTTv2.h" // RecoJetReaderHTTv2

#include "tthAnalysis/HiggsToTauTau/interface/RecoSubjetReaderHTTv2.h" // RecoSubjetReaderHTTv2

#include "tthAnalysis/HiggsToTauTau/interface/cmsException.h" // cmsException()
#include "tthAnalysis/HiggsToTauTau/interface/analysisAuxFunctions.h" // kBtag_*
#include "tthAnalysis/HiggsToTauTau/interface/BranchAddressInitializer.h" // BranchAddressInitializer, TTree, Form()

std::map<std::string, int> RecoJetReaderHTTv2::numInstances_;
std::map<std::string, RecoJetReaderHTTv2 *> RecoJetReaderHTTv2::instances_;

RecoJetReaderHTTv2::RecoJetReaderHTTv2(int era)
  : RecoJetReaderHTTv2(era, "HTTV2")
{}

RecoJetReaderHTTv2::RecoJetReaderHTTv2(int era,
				       const std::string & branchName_obj)
  : era_(era)
  , max_nJets_(32)
  , branchName_num_(Form("n%s", branchName_obj.data()))
  , branchName_obj_(branchName_obj)
  , subjetReader_(nullptr)
  , jet_pt_(nullptr)
  , jet_eta_(nullptr)
  , jet_phi_(nullptr)
  , jet_mass_(nullptr)
  , jet_area_(nullptr)
  , subjet_idx1_(nullptr)
  , subjet_idx2_(nullptr)
  , subjet_idx3_(nullptr)
  , jet_fRec_(nullptr)
  , jet_Ropt_(nullptr)
  , jet_RoptCalc_(nullptr)
  , jet_ptForRoptCalc_(nullptr)
{
  setBranchNames();
}

RecoJetReaderHTTv2::~RecoJetReaderHTTv2()
{
  --numInstances_[branchName_obj_];
  assert(numInstances_[branchName_obj_] >= 0);
  if(numInstances_[branchName_obj_] == 0)
  {
    RecoJetReaderHTTv2 * const gInstance = instances_[branchName_obj_];
    assert(gInstance);
    delete[] gInstance->jet_pt_;
    delete[] gInstance->jet_eta_;
    delete[] gInstance->jet_phi_;
    delete[] gInstance->jet_mass_;
    delete[] gInstance->jet_area_;
    delete[] gInstance->subjet_idx1_;
    delete[] gInstance->subjet_idx2_;
    delete[] gInstance->subjet_idx3_;
    delete[] gInstance->jet_fRec_;
    delete[] gInstance->jet_Ropt_;
    delete[] gInstance->jet_RoptCalc_;
    delete[] gInstance->jet_ptForRoptCalc_;
    instances_[branchName_obj_] = nullptr;
  }
}

void
RecoJetReaderHTTv2::setBranchNames()
{
  if(numInstances_[branchName_obj_] == 0)
  {
    branchName_pt_ = Form("%s_%s", branchName_obj_.data(), "pt");
    branchName_eta_ = Form("%s_%s", branchName_obj_.data(), "eta");
    branchName_phi_ = Form("%s_%s", branchName_obj_.data(), "phi");
    branchName_mass_ = Form("%s_%s", branchName_obj_.data(), "mass");
    branchName_area_ = Form("%s_%s", branchName_obj_.data(), "area");
    branchName_subjetIdx1_ = Form("%s_%s", branchName_obj_.data(), "subjetIdx1");
    branchName_subjetIdx2_ = Form("%s_%s", branchName_obj_.data(), "subjetIdx2");
    branchName_subjetIdx3_ = Form("%s_%s", branchName_obj_.data(), "subjetIdx3");
    branchName_fRec_ = Form("%s_%s", branchName_obj_.data(), "fRec");
    branchName_Ropt_ = Form("%s_%s", branchName_obj_.data(), "Ropt");
    branchName_RoptCalc_ = Form("%s_%s", branchName_obj_.data(), "RoptCalc");
    branchName_ptForRoptCalc_ = Form("%s_%s", branchName_obj_.data(), "ptForRoptCalc");
    instances_[branchName_obj_] = this;
  }
  else
  {
    if(branchName_num_ != instances_[branchName_obj_]->branchName_num_)
    {
      throw cmsException(this)
        << "Association between configuration parameters 'branchName_num' and 'branchName_obj' must be unique:"
        << " present association 'branchName_num' = " << branchName_num_ << " with 'branchName_obj' = " << branchName_obj_
        << " does not match previous association 'branchName_num' = " << instances_[branchName_obj_]->branchName_num_
        << " with 'branchName_obj' = " << instances_[branchName_obj_]->branchName_obj_ << " !!\n";
    }
  }
  ++numInstances_[branchName_obj_];
}

void
RecoJetReaderHTTv2::setBranchAddresses(TTree * tree)
{
  if(instances_[branchName_obj_] == this)
  {
    BranchAddressInitializer bai(tree, max_nJets_);
    subjetReader_->setBranchAddresses(tree);
    bai.setBranchAddress(nJets_, branchName_num_);
    bai.setBranchAddress(jet_pt_, branchName_pt_);
    bai.setBranchAddress(jet_eta_, branchName_eta_);
    bai.setBranchAddress(jet_phi_, branchName_phi_);
    bai.setBranchAddress(jet_mass_, branchName_mass_);
    bai.setBranchAddress(jet_area_, branchName_area_);
    bai.setBranchAddress(subjet_idx1_, branchName_subjetIdx1_);
    bai.setBranchAddress(subjet_idx2_, branchName_subjetIdx2_);
    bai.setBranchAddress(subjet_idx3_, branchName_subjetIdx3_);
    bai.setBranchAddress(jet_fRec_, branchName_fRec_);
    bai.setBranchAddress(jet_Ropt_, branchName_Ropt_);
    bai.setBranchAddress(jet_RoptCalc_, branchName_RoptCalc_);
    bai.setBranchAddress(jet_ptForRoptCalc_, branchName_ptForRoptCalc_);
  }
}

namespace
{
  const RecoSubjetHTTv2* getSubjet(const std::vector<RecoSubjetHTTv2>& subjets, int idx)
  {
    if ( idx == -1 ) return 0;
    else if (idx >= 0 && idx < (int)subjets.size() ) return &subjets[idx];
    else throw cmsException("<getSubjet>:")
      << "Invalid subjet index = " << idx << ", given number of subjets = " << subjets.size() << " !!\n";
  }
}

std::vector<RecoJetHTTv2>
RecoJetReaderHTTv2::read() const
{
  const RecoJetReaderHTTv2 * const gInstance = instances_[branchName_obj_];
  assert(gInstance);

  std::vector<RecoJetHTTv2> jets;
  const UInt_t nJets = gInstance->nJets_;
  if(nJets > max_nJets_)
  {
    throw cmsException(this)
      << "Number of jets stored in Ntuple = " << nJets << ", exceeds max_nJets = " << max_nJets_ << " !!\n";
  }

  if(nJets > 0)
  {
    jets.reserve(nJets);
    std::vector<RecoSubjetHTTv2> subjets = subjetReader_->read();
    for(UInt_t idxJet = 0; idxJet < nJets; ++idxJet)
    {
      const RecoSubjetHTTv2* subJet1 = getSubjet(subjets, gInstance->subjet_idx1_[idxJet]);
      const RecoSubjetHTTv2* subJet2 = getSubjet(subjets, gInstance->subjet_idx2_[idxJet]);
      const RecoSubjetHTTv2* subJet3 = getSubjet(subjets, gInstance->subjet_idx3_[idxJet]);
      jets.push_back({
        {
          gInstance->jet_pt_[idxJet],
          gInstance->jet_eta_[idxJet],
          gInstance->jet_phi_[idxJet],
          gInstance->jet_mass_[idxJet]
        },
	gInstance->jet_area_[idxJet],
	subJet1,
	subJet2,
	subJet3,
	gInstance->jet_fRec_[idxJet],
        gInstance->jet_Ropt_[idxJet],
        gInstance->jet_RoptCalc_[idxJet],
	gInstance->jet_ptForRoptCalc_[idxJet],
        static_cast<Int_t>(idxJet)
      });
    } // idxJet
  } // nJets > 0
  return jets;
}