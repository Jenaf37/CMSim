from sim import *
from selectors import *

desires = [100]*16
desires.append(80)
desires.append(80)
for i in range(22):
    desires.append(0)
print(desires)

def startDist():
    x = cmDistribution()
    x.setUpRandom(1760)
    return x
    



remiga = SimReMig(addSelectFirstDesiresFromDesiresLoose(desires)
                   ,deSelectFirstOptionFromDesires(desires)
                   ,addSelectFirstDesiredOptionFromDesires(desires)
                   ,1760)
remigb = SimReMig(addSelectFirstDesiresFromDesiresLoose(desires)
                   ,deSelectHighestOptionFromDesires(desires)
                   ,addSelectFirstDesiredOptionFromDesires(desires)
                   ,1760)
remigc = SimReMig(addSelectFirstDesiresFromDesiresLoose(desires)
                   ,deSelectLowestOptionFromDesires(desires)
                   ,addSelectFirstDesiredOptionFromDesires(desires)
                   ,1760)                   
#mig  = SimMigrate (addSelectFirstDesiredOptionFromDesires(desires)
#                    ,deSelectFirstOptionFromDesires(desires)
#                    ,startDist)
#res  = SimRespec (addSelectFirstDesiredOptionFromDesires(desires),1760)                 
                   
sims = []
sims.append([remiga,'delevel in order'])
sims.append([remigb,'delevel highest'])
sims.append([remigc,'delevel lowest'])


def runner(sims,time):#sims: [[SIM,name]] atm jsut for a yolo run
    shortRes = []
    for sim in sims:
        results = sim[0].run(time/len(sims))
        shortRes.append([sim[1],len(results),sum(results)/len(results)])
    for stuff in shortRes:
        print(stuff)

runner(sims,60*60*17)