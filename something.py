import sys
import pygame
import time
from bullets import bullets
from sensorClass import sensorThread
from playerControls import playerInfo

import time


#Sending the pin numbers when I create the thread
player1Readings = sensorThread(32,18)
player2Readings = sensorThread(8,10)

#Tennis ball from
#Icons made by <a href="https://www.flaticon.com/authors/those-icons" title="Those Icons">Those Icons</a> from <a href="https://www.flaticon.com/" title="Flaticon"> www.flaticon.com</a>

#barrier icon from
#Icons made by <a href="https://www.flaticon.com/authors/freepik" title="Freepik">Freepik</a> from <a href="https://www.flaticon.com/" title="Flaticon"> www.flaticon.com</a>
pygame.init()

size = width, height = 800, 600
speed = [2, 2]
black = 0, 0, 0

projectileList = list()

screen = pygame.display.set_mode(size)

ball = pygame.image.load("intro_ball.gif")
ballrect = ball.get_rect()

player1 = playerInfo(100,500)
player2 = playerInfo(100,100)

#Image of the projectile
projectilePicture = pygame.image.load("tennis.png")
projectileRect = projectilePicture.get_rect()

#I think what I should do is have a thread  class that
#Takes in the measurement independently 

background = pygame.image.load('naoto.png')

xPos = 0
xNeg = 0
yPos = 0
yNeg = 0

def showScore(player1Score,player2Score,x=300,y=0):
    myfont = pygame.font.SysFont('Comic Sans MS', 30)
    textsurface = myfont.render('P1 Score:'+ str(player1Score) + "\nP2 Score:"  + str(player2Score), False, (0, 0, 0))
    screen.blit(textsurface,(x,y))

def fromSensorTo(sensorData,width):
    #We are getting a distance from the sensor and then I wwant to translate it to some width thing
    maxDistRead = 45.0
    minDistRead = 3.5
    if sensorData < minDistRead:
        return (0)
    elif sensorData > (maxDistRead +minDistRead):
        return width
    else:
        #When we are within the sensor range we move to some position in the board
        return  ( (sensorData*1.0 - minDistRead)/(maxDistRead*1.0 ) ) * (width*1.0)


#Function to update bullets
def ballUpdate(x, y):
    screen.blit(ball,(x,y))



player1Readings.start()
player2Readings.start()

#In here forever until we quit
while 1:
    #First thing we are doing is filling the background of the screen
    screen.fill(black)
    screen.blit(background,(0,0))


    #Every event enters this for loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
            #When you push space we shoot a tennis ball
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                #shoot projectile
                #We are creating a bullet here with these specifications
                bullet = bullets(player1.returnXPos()+55,player1.returnYPos()-25,projectileRect)
                #We are adding the bullet to the projectile list
                projectileList.append(bullet)

            #If you push q the game quits
            if  event.key == pygame.K_q:
                print("WE ARE SUPPOSED TO BE QUITTING")
                #When we flip out on player2 we die 
                player1Readings.stopRunning()
                player2Readings.stopRunning()
                player1Readings.join()
                player2Readings.join()
                sys.exit()
                


    #the distance is in cm
    player1X = fromSensorTo(player1Readings.returnDistance(), width - 110)
    player2X = fromSensorTo(player2Readings.returnDistance(),width-110)
    
    player1.updateXPos(player1X)
    player2.updateXPos(player2X)
    #moving the ball
    ballUpdate(player1.returnXPos(),player1.returnYPos())
    #moving the second ball 
    ballUpdate(player2.returnXPos(),player2.returnYPos())
    
    #I think we should move barrier first then ball
    #Then during ball check we see if we should reflect
        
    #We loop through each projectile in our projectile list
    #THings get added to the list based on how many times you pushed space
    for projectile in projectileList:
        #We are showing the projectile on the screen
        screen.blit(projectilePicture,(projectile.xPos,projectile.yPos))
        #Call function that checks if there is collision
        
        #get both players position
        player1Pos = ( player1.returnXPos(),player1.returnYPos() )
        player2Pos = ( player2.returnXPos(),player2.returnYPos() + 80 )
        

        projectile.checkCollision(player1Pos,ballrect)
        projectile.checkCollision(player2Pos,ballrect)
        projectile.checkCollisionBoundary(width)

        #We are calling the moveBulletFunction in the bullets class which moves the y position
        projectile.moveBullet()
        #If the yPosition is <0 then we call the doneBullet() method which says that the bullet should no longer be on screen
        if projectile.yPos < -15 :
            projectile.doneBullet()
            #The top player has been scored on
            player1.increaseScore()
        elif projectile.yPos > height - 15:
            projectile.doneBullet()
            player2.increaseScore()
            #the bottom player has been scored on
            
        #if we encounter the barrier then we should reflect ball yChange 

    projectileListSize = len(projectileList)
    #We are removing any bullets from the list that are no longer on screen
    #We are looping through the list backwards so that we don't have to worry about removing something then being in the wrong index
    #IF we loop from the start then when we remove something we technically shouldn't move our index. But if we do it from the back then we continue going backwards
    for i in range(projectileListSize):
        if not(projectileList[(projectileListSize-1)-i].onScreen):
            #Removing the projectile with the pop method
            projectileList.pop((projectileListSize-1)-i)

    showScore(player1.returnScore(),player2.returnScore())

    #updating the display
    pygame.display.update()
