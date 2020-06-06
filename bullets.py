import secrets

#Class we are using to determine information about a bullet
class bullets():

    def __init__(self,xPos, yPos,rect):
        self.onScreen = True
        self.blocked = False
        self.shouldBlock = 10 
        self.xPos = xPos
        self.yPos = yPos
        self.yChange = -3
        self.xChange = 0
        self.rect = rect


    def checkCollisionHelper(self,otherPos,otherSize):

        otherXPos = otherPos[0]
        otherYPos = otherPos[1]
        
        otherXSize = otherSize[2]
        otherYSize = otherSize[3]
        #+ (otherXSize/2)
        if otherXPos + (otherXSize/2)  > self.xPos and otherXPos-(otherXSize/2) <self.xPos:
            if otherYPos + (otherYSize/3) > self.yPos and otherYPos-(otherYSize/3) <self.yPos:
                
                #Right here we should be adding something to x coordinate depending on which sid e
                #you hit the opposing ball in
                
                if self.xPos < (otherXPos + 40 ):
                    self.xChange = (self.xChange *-1) + int(secrets.randbelow(6))
                elif self.xPos <  (otherXPos +70):
                    self.xChange = (self.xChange *-1) - int(secrets.randbelow(6))
                return True
        return False

    def checkCollisionBoundary(self,xMax):
        if self.xPos >= xMax:
            self.xChange *= -1
        elif self.xPos <= 0:
            self.xChange *= -1


    def checkCollision(self,otherObjectPosition,otherObjectSize):
        if self.shouldBlock > 0 :
            self.shouldBlock = self.shouldBlock -1
            return False
        
        if self.checkCollisionHelper(otherObjectPosition,otherObjectSize):            
            self.yChange *= -1
            self.blocked = True
            self.shouldBlock = 10
        
        
        print (otherObjectPosition)
        #I will check if my x position and y position are in the same space as other thing
        #And if it is I will change yCHange to positive 3
        #return self.rect.collide

    def doneBullet(self):
        self.onScreen = False

    def moveBullet(self):
        self.yPos += self.yChange
        self.xPos += self.xChange
