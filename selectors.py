
def deSelectFirstOptionFromDesires (desires):
    def deSelect(dist):
        for i in range(40):
            if dist.cmLevels[i]>desires[i]:
                return i
        return -1
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