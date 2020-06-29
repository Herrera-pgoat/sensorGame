class playerInfo():
    
    def __init__(self,xPos,yPos):
        self._xPos = xPos
        self._yPos = yPos
        self._playerScore = 0
        
    def increaseScore(self):
        self._playerScore +=1
    
    def returnScore(self):
        return self._playerScore
        
    def updateXPos(self,xPos):
        self._xPos = xPos
    
    def updateYPos(self,yPos):
        self._yPos = yPos
        
    def returnCoordinates(self):
        return (self._xPos,self._yPos)
    
    def returnXPos(self):
        return self._xPos
    
    def returnYPos(self):
        return self._yPos
        
        