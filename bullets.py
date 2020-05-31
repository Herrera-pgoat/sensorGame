#Class we are using to determine information about a bullet
class bullets():

    def __init__(self,xPos, yPos,rect):
        self.onScreen = True
        self.xPos = xPos
        self.yPos = yPos
        self.yChange = -3
        self.rect = rect

    def checkCollision(self,otherObject):
        
        print (otherObject)
        #I will check if my x position and y position are in the same space as other thing
        #And if it is I will change yCHange to positive 3
        #return self.rect.collide

    def doneBullet(self):
        self.onScreen = False

    def moveBullet(self):
        self.yPos += self.yChange
