import sys

#Do some cleanup of sys for CDSW
import importlib
import buildStage0
importlib.reload(buildStage0)
import buildStage1
importlib.reload(buildStage1)
import buildStage2
importlib.reload(buildStage2)
import buildStage3
importlib.reload(buildStage3)
import buildStage4
importlib.reload(buildStage4)



def geoBoundaries_build(buildID):
  
  #In some cases, we may not be able to programmatically ping websites to confirm they exist.
  #In these cases, a manual exception can be defined if we can see the website ourselves.
  #These are included at the very beginning of the 'main', and are release-dependent.
  #I.e., any exceptions must be explicitly defined as belonging to a buildID.
  exceptions = {}
  exceptions[buildID] = {}
  exceptions[buildID]["URL"] = []
  exceptions["gbReleaseCandidate_2_0_0"]["URL"].append("http://ec.europa.eu/eurostat/web/gisco/geodata/reference-data/administrative-units-statistical-units/communes ")
  exceptions["gbReleaseCandidate_2_0_0"]["URL"].append("http://www.istat.it/it/archivio/124086")
  exceptions["gbReleaseCandidate_2_0_0"]["URL"].append("https://wambachers-osm.website/boundaries/")
  exceptions["gbReleaseCandidate_2_0_0"]["URL"].append("https://snig.dgterritorio.gov.pt/rndg/srv/por/catalog.search#/metadata/5e3debf1-6cde-4ff2-8301-a86799231907")
  exceptions["gbReleaseCandidate_2_0_0"]["URL"].append("http://geo.stp.gov.py/user/dgeec/tables/paraguay_2012_departamentos/public")
  exceptions["gbReleaseCandidate_2_0_0"]["URL"].append("https://www.pdok.nl/nl/producten/pdok-downloads/basis-registratie-kadaster/bestuurlijke-grenzen-actueel")
  exceptions["gbReleaseCandidate_2_0_0"]["URL"].append("https://www.statcan.gc.ca/eng/reference/licence")
  
  
  buildStage0.retrieveZip(buildID)
  buildStage0.metaDataChecks(buildID, exceptions)
  
  buildStage1.shapeChecks(buildID)

  if(buildID == "current"):
    print("Because this is being executed against the 'current' folder")
    print("Only the QA/QC procedures will be implemented.  No full build will be")
    print("produced.")
    return(0)

  buildStage2.metaStandardization(buildID)
  
  buildStage3.buildFiles(buildID)
  
  buildStage4.uploadGB(buildID)




if __name__ == "__main__": 
    import buildMain
    importlib.reload(buildMain)
    buildMain.geoBoundaries_build("gbReleaseCandidate_2_0_0")