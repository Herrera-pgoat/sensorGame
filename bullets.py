#Class we are using to determine information about a bullet
class bullets():

    def __init__(self,xPos, yPos,rect):
        self.onScreen = True
        self.blocked = False
        self.shouldBlock = 5 
        self.xPos = xPos
        self.yPos = yPos
        self.yChange = -3
        self.rect = rect


    def checkCollisionHelper(self,otherPos,otherSize):

        otherXPos = otherPos[0]
        otherYPos = otherPos[1]
        
        otherXSize = otherSize[2]
        otherYSize = otherSize[3]
        if otherXPos + (otherXSize/2) > self.xPos and otherXPos-(otherXSize/2) <self.xPos:
            if otherYPos + (otherYSize/6) > self.yPos and otherYPos-(otherYSize/5) <self.yPos:
                return True
        return False


    def checkCollision(self,otherObjectPosition,otherObjectSize):
        if self.shouldBlock > 0 :
            self.shouldBlock = self.shouldBlock -1
            return False
        
        if self.checkCollisionHelper(otherObjectPosition,otherObjectSize):            
            self.yChange *= -1
            self.blocked = True
            self.shouldBlock = 5
        
        
        print (otherObjectPosition)
        #I will check if my x position and y position are in the same space as other thing
        #And if it is I will change yCHange to positive 3
        #return self.rect.collide

    def doneBullet(self):
        self.onScreen = False

    def moveBullet(self):
        self.yPos += self.yChange
