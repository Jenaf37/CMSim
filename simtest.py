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
    



remig = SimReMig(addSelectFirstDesiresFromDesiresLoose(desires)
                   ,deSelectFirstOptionFromDesires(desires)
                   ,addSelectFirstDesiredOptionFromDesires(desires)
                   ,1760)
mig  = SimMigrate (addSelectFirstDesiredOptionFromDesires(desires)
                    ,deSelectFirstOptionFromDesires(desires)
                    ,startDist)
res  = SimRespec (addSelectFirstDesiredOptionFromDesires(desires),1760)                 
                   
sims = []
sims.append([remig,'remig'])
#sims.append([mig,'mig'])
sims.append([res,'resp'])


def runner(sims,time):#sims: [[SIM,name]] atm jsut for a yolo run
    shortRes = []
    for sim in sims:
        results = sim[0].run(time/len(sims))
        shortRes.append([sim[1],len(results),sum(results)/len(results)])
    print(shortRes)

runner(sims,60*60*6)