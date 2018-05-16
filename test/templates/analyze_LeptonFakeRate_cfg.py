import FWCore.ParameterSet.Config as cms
import os

from tthAnalysis.HiggsToTauTau.recommendedMEtFilters_cfi import recommendedMEtFilters

process = cms.PSet()

process.fwliteInput = cms.PSet(
    fileNames = cms.vstring(
    ),
    maxEvents = cms.int32(-1),
    outputEvery = cms.uint32(100000)
)

process.fwliteOutput = cms.PSet(
    fileName = cms.string('analyze_LeptonFakeRate.root')
)

process.analyze_LeptonFakeRate = cms.PSet(
    treeName = cms.string('Events'),

    process = cms.string('ttH'),

    era = cms.string('2017'),

    use_triggers_1e = cms.bool(True),
    use_triggers_2e = cms.bool(True),
    use_triggers_1mu = cms.bool(True),
    use_triggers_2mu = cms.bool(True),

    triggers_mu = cms.VPSet(
        cms.PSet(
            path = cms.vstring("HLT_Mu27"),
            cone_minPt = cms.double(45.),
            cone_maxPt = cms.double(100.),
            minRecoPt = cms.double(27.), # NEWLY ADDED AFTER GIOVANNI SYNC
            jet_minPt = cms.double(30.),
#            pufile    = cms.FileInPath(""), ## PU file to be implemented later
            average_prescale = cms.double(225), ## 2016 VALUE: 143
            prescale_rand_mc = cms.double(5.),
            is_trigger_1mu = cms.bool(True),
            is_trigger_2mu = cms.bool(False),
            is_trigger_1e = cms.bool(False),
            is_trigger_2e = cms.bool(False)
        ),
        cms.PSet(
            path = cms.vstring("HLT_Mu20"),
            cone_minPt = cms.double(32.),
            cone_maxPt = cms.double(100.),
            minRecoPt = cms.double(20.), # NEWLY ADDED AFTER GIOVANNI SYNC
            jet_minPt = cms.double(30.),
#            pufile    = cms.FileInPath(""), ## PU file to be implemented later
            average_prescale = cms.double(225), ## 2016 VALUE: 143
            prescale_rand_mc = cms.double(5.),
            is_trigger_1mu = cms.bool(True),
            is_trigger_2mu = cms.bool(False),
            is_trigger_1e = cms.bool(False),
            is_trigger_2e = cms.bool(False)
        ),
        cms.PSet(
            path = cms.vstring("HLT_Mu17"),
            cone_minPt = cms.double(32.),
            cone_maxPt = cms.double(100.),
            minRecoPt = cms.double(17.), # NEWLY ADDED AFTER GIOVANNI SYNC
            jet_minPt = cms.double(30.),
#            pufile    = cms.FileInPath(""), ## PU file to be implemented later
            average_prescale = cms.double(594), ## 2016 VALUE: 126
            prescale_rand_mc = cms.double(5.),
            is_trigger_1mu = cms.bool(False),
            is_trigger_2mu = cms.bool(True),
            is_trigger_1e = cms.bool(False),
            is_trigger_2e = cms.bool(False)
         ),
        cms.PSet(
            path = cms.vstring("HLT_Mu8"),
            cone_minPt = cms.double(15.),
            cone_maxPt = cms.double(45.),
            minRecoPt = cms.double(8.), # NEWLY ADDED AFTER GIOVANNI SYNC
            jet_minPt = cms.double(30.),
#            pufile    = cms.FileInPath(""), ## PU file to be implemented later
            average_prescale = cms.double(15948), ## 2016 VALUE: 9072
            prescale_rand_mc = cms.double(100.),
            is_trigger_1mu = cms.bool(False),
            is_trigger_2mu = cms.bool(True),
            is_trigger_1e = cms.bool(False),
            is_trigger_2e = cms.bool(False)
        ),
        cms.PSet(
            path = cms.vstring("HLT_Mu3_PFJet40"),
            cone_minPt = cms.double(10.),
            cone_maxPt = cms.double(32.),
            minRecoPt = cms.double(-1.), # NEWLY ADDED AFTER GIOVANNI SYNC
            jet_minPt = cms.double(45.), # UPDATED FROM 2016 VALUE (40 GeV) FOR 2017 DATA
#            pufile    = cms.FileInPath(""), ## PU file to be implemented later
            average_prescale = cms.double(8992), ## 2016 VALUE: 4841
            prescale_rand_mc = cms.double(50.),
            is_trigger_1mu = cms.bool(True),
            is_trigger_2mu = cms.bool(False),
            is_trigger_1e = cms.bool(False),
            is_trigger_2e = cms.bool(False)
         )
    ),
    triggers_e = cms.VPSet(
        cms.PSet(
            path = cms.vstring("HLT_Ele8_CaloIdM_TrackIdM_PFJet30"),
            cone_minPt = cms.double(15.),
            cone_maxPt = cms.double(45.),
            minRecoPt = cms.double(8.), # NEWLY ADDED AFTER GIOVANNI SYNC
            jet_minPt = cms.double(30.),
#            pufile    = cms.FileInPath(""), ## PU file to be implemented later
            average_prescale = cms.double(11365),
            prescale_rand_mc = cms.double(10.),
            is_trigger_1mu = cms.bool(False),
            is_trigger_2mu = cms.bool(False),
            is_trigger_1e = cms.bool(True),
            is_trigger_2e = cms.bool(False)
        ),
#        cms.PSet(
#            path = cms.vstring("HLT_Ele12_CaloIdL_TrackIdL_IsoVL_PFJet30"), ## DOESN'T EXIST IN 2017 DATA
#            cone_minPt = cms.double(20.),
#            cone_maxPt = cms.double(30.),
#            minRecoPt = cms.double(12.), # NEWLY ADDED AFTER GIOVANNI SYNC
#            jet_minPt = cms.double(30.),
##            pufile    = cms.FileInPath(""), ## PU file to be implemented later
#            average_prescale = cms.double(1086), #TODO: update
#            prescale_rand_mc = cms.double(25.),
#            is_trigger_1mu = cms.bool(False),
#            is_trigger_2mu = cms.bool(False),
#            is_trigger_1e = cms.bool(True),
#            is_trigger_2e = cms.bool(False)
#        ),
        cms.PSet(
            path = cms.vstring("HLT_Ele17_CaloIdM_TrackIdM_PFJet30"),
            cone_minPt = cms.double(25.),
            cone_maxPt = cms.double(100.),
            minRecoPt = cms.double(17.), # NEWLY ADDED AFTER GIOVANNI SYNC
            jet_minPt = cms.double(30.),
#            pufile    = cms.FileInPath(""), ## PU file to be implemented later
            average_prescale = cms.double(1167), ## 2016 VALUE: 569
            prescale_rand_mc = cms.double(10.),
            is_trigger_1mu = cms.bool(False),
            is_trigger_2mu = cms.bool(False),
            is_trigger_1e = cms.bool(True),
            is_trigger_2e = cms.bool(False)
        ),
        cms.PSet(
            path = cms.vstring("HLT_Ele23_CaloIdM_TrackIdM_PFJet30"),
            cone_minPt = cms.double(32.),
            cone_maxPt = cms.double(100.),
            minRecoPt = cms.double(23.), # NEWLY ADDED AFTER GIOVANNI SYNC
            jet_minPt = cms.double(30.),
#            pufile    = cms.FileInPath(""), ## PU file to be implemented later
            average_prescale = cms.double(1069), ## suggested by christian to be checked with Giovanni !!!
            prescale_rand_mc = cms.double(10.),  ## suggested by christian to be checked with Giovanni !!!
            is_trigger_1mu = cms.bool(False),
            is_trigger_2mu = cms.bool(False),
            is_trigger_1e = cms.bool(True),
            is_trigger_2e = cms.bool(False)
        )
    ),

    absEtaBins_e = cms.vdouble(0., 1.479, 9.9),
    ptBins_e = cms.vdouble(15., 20., 30., 45., 65., 100000.),
    absEtaBins_mu = cms.vdouble(0., 1.479, 9.9),
    ptBins_mu = cms.vdouble(10., 15., 20., 30., 45., 65., 100000.),

    minConePt_global_e = cms.double(10),
    minRecoPt_global_e = cms.double(7),
    minConePt_global_mu = cms.double(10),
    minRecoPt_global_mu = cms.double(5),

    isMC = cms.bool(True),
    central_or_shift = cms.string('central'),
    lumiScale = cms.double(1.),
    apply_genWeight = cms.bool(True),
    apply_trigger_bits = cms.bool(False), # ignored
    fillGenEvtHistograms = cms.bool(True),

    branchName_electrons = cms.string('Electron'),
    branchName_muons = cms.string('Muon'),
    branchName_hadTaus = cms.string('Tau'),
    branchName_jets = cms.string('Jet'),
    branchName_met = cms.string('MET'),

    branchName_genLeptons = cms.string('GenLep'),
    branchName_genHadTaus = cms.string('GenVisTau'),
    branchName_genJets = cms.string('GenJet'),
    redoGenMatching = cms.bool(True),

    selEventsFileName_input = cms.string(''),
    selEventsFileName_output = cms.string(''),
    cfgMEtFilter = recommendedMEtFilters,
    isDEBUG = cms.bool(False),
    applyMETFilters = cms.bool(True),
    hasLHE = cms.bool(True),
)





