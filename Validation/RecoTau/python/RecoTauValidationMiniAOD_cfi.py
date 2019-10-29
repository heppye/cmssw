import FWCore.ParameterSet.Config as cms
from DQMServices.Core.DQMEDAnalyzer import DQMEDAnalyzer

tauValidationMiniAOD = DQMEDAnalyzer("TauValidationMiniAOD",
  tauCollection = cms.InputTag("slimmedTaus"),
  RefCollection = cms.InputTag("kinematicSelectedTauValDenominatorZTT"),
  ExtensionName = cms.string('ZTT'),
  discriminators = cms.VPSet(
    cms.PSet(discriminator = cms.string("decayModeFinding"),selectionCut = cms.double(0.5)),
    cms.PSet(discriminator = cms.string("decayModeFindingNewDMs"),selectionCut = cms.double(0.5)),
    cms.PSet(discriminator = cms.string("byLooseCombinedIsolationDeltaBetaCorr3Hits"),selectionCut = cms.double(0.5)),
    cms.PSet(discriminator = cms.string("byMediumCombinedIsolationDeltaBetaCorr3Hits"),selectionCut = cms.double(0.5)),
    cms.PSet(discriminator = cms.string("byTightCombinedIsolationDeltaBetaCorr3Hits"),selectionCut = cms.double(0.5)),
    cms.PSet(discriminator = cms.string("againstMuonLoose3"),selectionCut = cms.double(0.5)),
    cms.PSet(discriminator = cms.string("againstMuonTight3"),selectionCut = cms.double(0.5)),
    cms.PSet(discriminator = cms.string("againstElectronVLooseMVA6"),selectionCut = cms.double(0.5)),
    cms.PSet(discriminator = cms.string("againstElectronLooseMVA6"),selectionCut = cms.double(0.5)),
    cms.PSet(discriminator = cms.string("againstElectronMediumMVA6"),selectionCut = cms.double(0.5)),
    cms.PSet(discriminator = cms.string("againstElectronTightMVA6"),selectionCut = cms.double(0.5)),
    cms.PSet(discriminator = cms.string("againstElectronVTightMVA6"),selectionCut = cms.double(0.5)),
    cms.PSet(discriminator = cms.string("byVLooseIsolationMVArun2v1DBoldDMwLT"),selectionCut = cms.double(0.5)),
    cms.PSet(discriminator = cms.string("byLooseIsolationMVArun2v1DBoldDMwLT"),selectionCut = cms.double(0.5)),
    cms.PSet(discriminator = cms.string("byMediumIsolationMVArun2v1DBoldDMwLT"),selectionCut = cms.double(0.5)),
    cms.PSet(discriminator = cms.string("byTightIsolationMVArun2v1DBoldDMwLT"),selectionCut = cms.double(0.5)),
    cms.PSet(discriminator = cms.string("byVTightIsolationMVArun2v1DBoldDMwLT"),selectionCut = cms.double(0.5)),
    cms.PSet(discriminator = cms.string("byVVTightIsolationMVArun2v1DBoldDMwLT"),selectionCut = cms.double(0.5)),
    cms.PSet(discriminator = cms.string("byVLooseIsolationMVArun2v1DBnewDMwLT"),selectionCut = cms.double(0.5)),
    cms.PSet(discriminator = cms.string("byLooseIsolationMVArun2v1DBnewDMwLT"),selectionCut = cms.double(0.5)),
    cms.PSet(discriminator = cms.string("byMediumIsolationMVArun2v1DBnewDMwLT"),selectionCut = cms.double(0.5)),
    cms.PSet(discriminator = cms.string("byTightIsolationMVArun2v1DBnewDMwLT"),selectionCut = cms.double(0.5)),
    cms.PSet(discriminator = cms.string("byVTightIsolationMVArun2v1DBnewDMwLT"),selectionCut = cms.double(0.5)),
    cms.PSet(discriminator = cms.string("byVVTightIsolationMVArun2v1DBnewDMwLT"),selectionCut = cms.double(0.5)),
    cms.PSet(discriminator = cms.string("byVLooseIsolationMVArun2v1PWoldDMwLT"),selectionCut = cms.double(0.5)),
    cms.PSet(discriminator = cms.string("byLooseIsolationMVArun2v1PWoldDMwLT"),selectionCut = cms.double(0.5)),
    cms.PSet(discriminator = cms.string("byMediumIsolationMVArun2v1PWoldDMwLT"),selectionCut = cms.double(0.5)),
    cms.PSet(discriminator = cms.string("byTightIsolationMVArun2v1PWoldDMwLT"),selectionCut = cms.double(0.5)),
    cms.PSet(discriminator = cms.string("byVTightIsolationMVArun2v1PWoldDMwLT"),selectionCut = cms.double(0.5)),
    cms.PSet(discriminator = cms.string("byVVTightIsolationMVArun2v1PWoldDMwLT"),selectionCut = cms.double(0.5)),
    cms.PSet(discriminator = cms.string("byVLooseIsolationMVArun2v1PWnewDMwLT"),selectionCut = cms.double(0.5)),
    cms.PSet(discriminator = cms.string("byLooseIsolationMVArun2v1PWnewDMwLT"),selectionCut = cms.double(0.5)),
    cms.PSet(discriminator = cms.string("byMediumIsolationMVArun2v1PWnewDMwLT"),selectionCut = cms.double(0.5)),
    cms.PSet(discriminator = cms.string("byTightIsolationMVArun2v1PWnewDMwLT"),selectionCut = cms.double(0.5)),
    cms.PSet(discriminator = cms.string("byVTightIsolationMVArun2v1PWnewDMwLT"),selectionCut = cms.double(0.5)),
    cms.PSet(discriminator = cms.string("byVVTightIsolationMVArun2v1PWnewDMwLT"),selectionCut = cms.double(0.5)),
    cms.PSet(discriminator = cms.string("byVLooseIsolationMVArun2v1DBdR03oldDMwLT"),selectionCut = cms.double(0.5)),
    cms.PSet(discriminator = cms.string("byLooseIsolationMVArun2v1DBdR03oldDMwLT"),selectionCut = cms.double(0.5)),
    cms.PSet(discriminator = cms.string("byMediumIsolationMVArun2v1DBdR03oldDMwLT"),selectionCut = cms.double(0.5)),
    cms.PSet(discriminator = cms.string("byTightIsolationMVArun2v1DBdR03oldDMwLT"),selectionCut = cms.double(0.5)),
    cms.PSet(discriminator = cms.string("byVTightIsolationMVArun2v1DBdR03oldDMwLT"),selectionCut = cms.double(0.5)),
    cms.PSet(discriminator = cms.string("byVVTightIsolationMVArun2v1DBdR03oldDMwLT"),selectionCut = cms.double(0.5)),
    cms.PSet(discriminator = cms.string("byVLooseIsolationMVArun2v1PWdR03oldDMwLT"),selectionCut = cms.double(0.5)),
    cms.PSet(discriminator = cms.string("byLooseIsolationMVArun2v1PWdR03oldDMwLT"),selectionCut = cms.double(0.5)),
    cms.PSet(discriminator = cms.string("byMediumIsolationMVArun2v1PWdR03oldDMwLT"),selectionCut = cms.double(0.5)),
    cms.PSet(discriminator = cms.string("byTightIsolationMVArun2v1PWdR03oldDMwLT"),selectionCut = cms.double(0.5)),
    cms.PSet(discriminator = cms.string("byVTightIsolationMVArun2v1PWdR03oldDMwLT"),selectionCut = cms.double(0.5)),
    cms.PSet(discriminator = cms.string("byVVTightIsolationMVArun2v1PWdR03oldDMwLT"),selectionCut = cms.double(0.5))
  ),
)