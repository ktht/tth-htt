#ifndef tthAnalysis_HiggsToTauTau_RecoJet_h
#define tthAnalysis_HiggsToTauTau_RecoJet_h

/** \class RecoJet
 *
 * Class to access information for "resolved" jets, 
 * reconstructed by anti-kT algorithm with dR=0.4
 *
 * \author Christian Veelken, Tallinn
 *
 */

#include "tthAnalysis/HiggsToTauTau/interface/RecoJetBase.h" // RecoJetBase

#include <map> // std::map<,>

enum class Btag;

class RecoJet
  : public RecoJetBase
{
public:
  RecoJet() = default;
  RecoJet(const GenJet & particle,
          Double_t BtagCSV,
          Double_t BtagWeight,
          Double_t QGDiscr,
          Int_t jetId,
          Int_t puId,
          Int_t genMatchIdx,
          Int_t idx,
          Btag btag);

  virtual ~RecoJet();

  /**
   * @brief Funtions to access data-members
   * @return Values of data-members
   */
  Double_t BtagCSV() const;
  Double_t BtagCSV(Btag btag) const;
  Double_t BtagWeight() const;
  Double_t BtagWeight(int central_or_shift) const;
  Double_t BtagWeight(Btag btag, int central_or_shift) const;
  Double_t QGDiscr() const;
  Int_t jetId() const;
  Int_t puId() const;
  Int_t genMatchIdx() const;

  Double_t maxPt() const;

  bool hasBtag(Btag btag) const;

  friend class RecoJetReader;
  friend class RecoJetWriter;

protected:
  Double_t BtagCSV_;    ///< CSV b-tagging discriminator value
  Double_t BtagWeight_; ///< weight for data/MC correction of b-tagging efficiency and mistag rate
  Double_t QGDiscr_;    ///< quark/gluon discriminator
  Int_t jetId_;         ///< jet ID, as explained in https://twiki.cern.ch/twiki/bin/view/CMS/JetID
  Int_t puId_;          ///< pileup jet ID, as explained in https://twiki.cern.ch/twiki/bin/viewauth/CMS/PileupJetID
  Int_t genMatchIdx_;   ///< index to gen jet
  Btag btag_;           ///< default b-tagging discriminant

  //---------------------------------------------------------
  // CV: needed by RecoJetWriter
  std::map<Btag, std::map<int, Double_t>> BtagWeight_systematics_;
  std::map<Btag, Double_t> BtagCSVs_;
  std::map<int, Double_t> pt_systematics_;
  std::map<int, Double_t> mass_systematics_;
  //---------------------------------------------------------
};

std::ostream &
operator<<(std::ostream & stream,
           const RecoJet & jet);

#endif // tthAnalysis_HiggsToTauTau_RecoJet_h

