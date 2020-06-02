class playerPosition():
    
    def __init__(self,xPos,yPos):
        self._xPos = xPos
        self._yPos = yPos
        
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
        
        