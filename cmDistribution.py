import random

class cmDistribution:
    
    def __init__(self):
        self.cmLevels = [0]*40

    def getOptions(self):#breaks when there are less than 6 cm options left.
        urn = [] #contains possible draws
        for i in range(40):
            urn.extend([i]*(100-self.cmLevels[i]))#set up the posibilities
        options=[]
        optcount=0
        while optcount < 6:
            newOption=random.choice(urn)
            if newOption in options:
                continue
            options.append(newOption)
            optcount +=1
            #options.append(random.choice(urn))#choose one
            #urn = list(filter(lambda x: x!= options[-1],urn))#remove similar options
        return options
        
    def addCM(self,number):
        if(number >= 40 or number <0):
            raise IndexError("CM number out of bounds")
        if(self.cmLevels[number]>=100):
            raise ValueError("CM is full")
        self.cmLevels[number]+=1
        
    def subCM(self,number):
        self.cmLevels[number]-=1 #not bothering for exceptions here I'm inconsistent sorry
    
    def setCM(self,number,value):
        if(number >= 40 or number <0):
            raise IndexError("CM number out of bounds")
        if(value < 0 or value >100):
            raise ValueError("CM Value incorrect")
        self.cmLevels[number]=value

    def addRandom(self):#selects a random cm from offered posibilties
        self.addCM(random.choice(self.getOptions()))

    def getTotalCMs(self):
        return sum(self.cmLevels)
    
    def addCMwithSelection(self,selection):
        #returns true if added succsessfull
        #returns false if no option is in selection
        options=self.getOptions()
        for option in options: #option is guaranteed to have free space because how getOptions() works
            if option in selection:
                self.addCM(option)
                return True
        return False

    def getSelectionFromDesires(self,desires):
        options = []
        for i in range(40):
            if self.cmLevels[i]<desires[i]:
                options.append(i)
        return options
    
    def getSingleDelevel(self,desires):
        #returns -1 of no delevel exists
        for i in range(40):
            if self.cmLevels[i]>desires[i]:
                return i
        return -1
      
    def getTotalCM(self):
        return sum(self.cmLevels)
      
    def setLevels(self,levels):
        self.cmLevels = levels
      
    def addCMwithSelector(self,selector):
        option = selector(self)
        if option == -1 :
            return False
        self.addCM(option)
        return True
    
    def delevelWithSelector(self,selector):
        delevel = selector(self)
        if delevel == -1:
            return False
        self.subCM(delevel)
        return True
    
    def setUpRandom(self,number):
        self.setLevels([0]*40)
        for i in range(number):
            self.addRandom()
        
    
    #Addselector: dist -> option / -1
    #delvelselector: dist ->option / -1
    #use delevelselector for terminating can give more flexible targets