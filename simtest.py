from sim import *
from selectors import *

desires = [99]*16
desires.append(88)
desires.append(88)
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

def tester(sims,timeout):
    for sim in sims:
        try:
            print(sim[1])
            result = sim[0].test(timeout)
            print(result[0])
            print(result[1].cmLevels)
        except TestTimeout as m:
            print(m)
            
tester(sims,-1)       
#runner(sims,5*60)