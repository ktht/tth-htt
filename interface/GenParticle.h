#ifndef tthAnalysis_HiggsToTauTau_GenParticle_h
#define tthAnalysis_HiggsToTauTau_GenParticle_h

#include "tthAnalysis/HiggsToTauTau/interface/Particle.h" // Particle

class GenParticle
  : public Particle
{
public:
  GenParticle();
  GenParticle(Double_t pt,
              Double_t eta,
              Double_t phi,
              Double_t mass,
              Int_t pdgId,
              Int_t charge);
  GenParticle(const math::PtEtaPhiMLorentzVector & p4,
              Int_t pdgId,
              Int_t charge);
  virtual ~GenParticle() {}

  /**
   * @brief Funtions to access data-members
   * @return Values of data-members
   */
  Int_t pdgId() const;
  Int_t charge() const;

protected:
  Int_t pdgId_;  ///< PDG id of the particle (signed)
  Int_t charge_; ///< charge of particle
};

std::ostream &
operator<<(std::ostream & stream,
           const GenParticle & particle);

#endif // tthAnalysis_HiggsToTauTau_GenParticle_h
