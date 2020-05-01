
def deSelectFirstOptionFromDesires (desires):
    def deSelect(dist):
        for i in range(40):
            if dist.cmLevels[i]>desires[i]:
                return i
        return -1
    return deSelect

def deSelectHighestOptionFromDesires (desires):
    def deSelect(dist):
        maxD=0
        maxI=-1
        for i in range(40):
            if dist.cmLevels[i]>desires[i] and dist.cmLevels[i]>maxD :
               maxD=dist.cmLevels[i]
               maxI=i
        return maxI
    return deSelect
 
def deSelectLowestOptionFromDesires (desires):
    def deSelect(dist):
        minD=100
        minI=-1
        for i in range(40):
            if dist.cmLevels[i]>desires[i] and dist.cmLevels[i]<minD :
               minD=dist.cmLevels[i]
               minI=i
        return minI
    return deSelect
 
    
def addSelectFirstDesiredOptionFromDesires (desires):    
    def addSelect(dist):
        options = dist.getOptions()
        for option in options:
            if dist.cmLevels[option] < desires[option]:
                return option
        return -1
    return addSelect
    
def addSelectFirstDesiresFromDesiresLoose (desires):
    def addSelect(dist):
        options = dist.getOptions()
        for option in options:
            if dist.cmLevels[option] < desires[option]:
                return option
        return options[0]
    return addSelect