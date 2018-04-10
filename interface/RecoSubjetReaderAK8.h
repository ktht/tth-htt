#ifndef tthAnalysis_HiggsToTauTau_RecoSubjetReaderAK8_h
#define tthAnalysis_HiggsToTauTau_RecoSubjetReaderAK8_h

#include "tthAnalysis/HiggsToTauTau/interface/ReaderBase.h" // ReaderBase
#include "tthAnalysis/HiggsToTauTau/interface/RecoSubjetAK8.h" // RecoSubjetAK8

#include <map> // std::map<,>

// forward declarations
class TTree;

class RecoSubjetReaderAK8
  : public ReaderBase
{
public:
  RecoSubjetReaderAK8(int era);
  RecoSubjetReaderAK8(int era,
		       const std::string & branchName_obj);
  ~RecoSubjetReaderAK8();

  /**
   * @brief Call tree->SetBranchAddress for all RecoSubjetHTTv2 branches
   */
  void
  setBranchAddresses(TTree * tree) override;

  /**
   * @brief Read branches from tree and use information to fill collection of RecoSubjetAK8 objects
   * @return Collection of RecoSubjetAK8 objects
   */
  std::vector<RecoSubjetAK8>
  read() const;

protected:
 /**
   * @brief Initialize names of branches to be read from tree
   */
  void
  setBranchNames();

  int era_;
  const unsigned int max_nJets_;
  std::string branchName_num_;
  std::string branchName_obj_;

  std::string branchName_pt_;
  std::string branchName_eta_;
  std::string branchName_phi_;
  std::string branchName_mass_;

  UInt_t nJets_;
  Float_t * jet_pt_;
  Float_t * jet_eta_;
  Float_t * jet_phi_;
  Float_t * jet_mass_;

  // CV: make sure that only one RecoSubjetReaderAK8 instance exists for a given branchName,
  //     as ROOT cannot handle multiple TTree::SetBranchAddress calls for the same branch.
  static std::map<std::string, int> numInstances_;
  static std::map<std::string, RecoSubjetReaderAK8 *> instances_;
};

#endif // tthAnalysis_HiggsToTauTau_RecoSubjetReaderAK8_h
