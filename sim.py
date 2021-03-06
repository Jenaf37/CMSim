from cmDistribution import *
from timeit import default_timer as timer

class TestTimeout(Exception):
    pass

class SimMigrate:
    
    def __init__(self,addSelect,deSelect,startDist):
        self.addSelect = addSelect
        self.deSelect = deSelect
        self.startDist = startDist
        
    def run(self,time):#returns when nothing to delevel
        startTime = timer()
        results=[]
        while (timer() - startTime < time):
            x=self.startDist()
            costs = 0
            while True :
                if not x.delevelWithSelector(self.deSelect):
                    break
                costs +=1
                while not x.addCMwithSelector(self.addSelect):
                    costs +=1
            results.append(costs)
        return results

    def test(self,timeout):
        startTime = timer()
        x=self.startDist()
        costs = 0
        while True :
            if timer()-startTime > timeout:
                raise TestTimeout("Timeout in outer loop")
            if not x.delevelWithSelector(self.deSelect):
                break
            costs +=1
            while not x.addCMwithSelector(self.addSelect):
                if timer()-startTime > timeout:
                    raise TestTimeout("timeout in inner loop")
                costs +=1
        return [costs,x]
        
        
class SimRespec:

    def __init__(self,addSelect,totalCM):
        self.addSelect = addSelect
        self.totalCM = totalCM
    
    def run(self,time):#returns when totalCM have been spent
        startTime=timer()
        results=[]
        while(timer()-startTime < time):
            x= cmDistribution()
            costs = 5
            CMspent = 0
            while (CMspent < self.totalCM):
                if x.addCMwithSelector(self.addSelect):
                    CMspent +=1
                else :
                    costs +=1
            results.append(costs)
        return results
        
    def test(self,timeout):
        startTime = timer()
        x= cmDistribution()
        costs = 5
        CMspent = 0
        while (CMspent < self.totalCM):
            if timer()-startTime > timeout:
                raise TestTimeout("timeout")
            if x.addCMwithSelector(self.addSelect):
                CMspent +=1
            else :
                costs +=1
        return [costs,x]
     
        
class SimReMig:
    
    def __init__(self,addSelectLoose,deSelect,addSelectStrict,totalCM):
        self.addSelectLoose = addSelectLoose
        self.deSelect = deSelect
        self.addSelectStrict = addSelectStrict
        self.totalCM = totalCM
        
    def run (self,time):
        startTime=timer()
        results=[]
        while(timer()-startTime < time):
            x= cmDistribution()
            costs = 5
            # respec without reroll
            CMspent=0
            while (CMspent < self.totalCM):
                if not x.addCMwithSelector(self.addSelectLoose):
                    raise RuntimeError('Loose selector must always choose an option')
                CMspent += 1
            
            #migrate the result to the desired ouput
            while True :
                if not x.delevelWithSelector(self.deSelect):
                    break
                costs +=1
                while not x.addCMwithSelector(self.addSelectStrict):
                    costs +=1
                    
            results.append(costs)
        return results
    
    def test(self,timeout):
        startTime=timer()
        x= cmDistribution()
        costs = 5
        # respec without reroll
        CMspent=0
        while (CMspent < self.totalCM):
            if timer()-startTime > timeout:
                raise TestTimeout("timeout in respec phase")
            if not x.addCMwithSelector(self.addSelectLoose):
                raise RuntimeError('Loose selector must always choose an option')
            CMspent += 1
            
        #migrate the result to the desired ouput
        while True :
            if timer()-startTime > timeout:
                raise TestTimeout("timeout in outer loop of migrate")
            if not x.delevelWithSelector(self.deSelect):
                break
            costs +=1
            while not x.addCMwithSelector(self.addSelectStrict):
                if timer()-startTime > timeout:
                    raise TestTimeout("timeout in inner loop of migrate")
                costs +=1
        return [costs,x]