import sys
import pygame
import time
from bullets import bullets

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
ballx , bally = 100,100
ballXChange = 1
ballYChange = 1

print(ballrect)


#Image of the projectile
projectilePicture = pygame.image.load("tennis.png")
projectileRect = projectilePicture.get_rect()

#Image of barrier
barrierPicture = pygame.image.load("fence.png")
#Some features of the barrier
barrierXPos = 100
barrierYPos = 100
barrierXChange = .8
barrierYChange = 0



background = pygame.image.load('naoto.png')

xPos = 0
xNeg = 0
yPos = 0
yNeg = 0

#Function to update barrier
def barrierUpdate(x,y):
    screen.blit(barrierPicture,(barrierXPos,barrierYPos))

def fromSensorTo(sensorData,width):
    #We are getting a distance from the sensor and then I wwant to translate it to some width thing
    maxDistRead = 30
    if sensorData < 3:
        return (0)
    elif sensorData > maxDistRead:
        return width
    else:
        #When we are within the sensor range we move to some position in the board
        return  ( (sensorData*1.0)/(maxDistRead*1.0) ) * width


#Function to update bullets
def ballUpdate(x, y):
    screen.blit(ball,(x,y))

#In here forever until we quit
while 1:
    #First thing we are doing is filling the background of the screen
    screen.fill(black)
    screen.blit(background,(0,0))


    #Every event enters this for loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

        #When you do a keyDown then you enter here
        if event.type == pygame.KEYDOWN:
            #When you match one of these keys we move the bullet
            if event.key == pygame.K_d:
                xPos += ballXChange
            if  event.key == pygame.K_a:
                xNeg -= ballXChange
            if  event.key == pygame.K_w:
                yNeg -= ballYChange
            if  event.key == pygame.K_s:
                yPos += ballYChange

            #When you push space we shoot a tennis ball
            if event.key == pygame.K_SPACE:
                #shoot projectile
                #We are creating a bullet here with these specifications
                bullet = bullets(ballx+55,bally-25,projectileRect)
                #We are adding the bullet to the projectile list
                projectileList.append(bullet)

            #If you push q the game quits
            if  event.key == pygame.K_q:
                sys.exit()

        #When you let go of the key you stop moving in that direction
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                xNeg = 0
            if  event.key == pygame.K_d:
                xPos = 0
            if event.key == pygame.K_w:
                yNeg = 0
            if  event.key == pygame.K_s:
                yPos = 0

    #We are moving the ball based on the values of these variables
    ballx += (xPos + xNeg)
    bally += (yPos + yNeg)

    #We loop through each projectile in our projectile list
    #THings get added to the list based on how many times you pushed space
    for projectile in projectileList:
        #We are showing the projectile on the screen
        screen.blit(projectilePicture,(projectile.xPos,projectile.yPos))
        #Call function that checks if there is collision
        barrierPosition = (barrierXPos,barrierYPos)
        projectile.checkCollision(barrierPicture.get_rect())
        #We are calling the moveBulletFunction in the bullets class which moves the y position
        projectile.moveBullet()
        #If the yPosition is <0 then we call the doneBullet() method which says that the bullet should no longer be on screen
        if projectile.yPos < -15 :
            projectile.doneBullet()
        elif projectile.yPos > height - 15:
            projectile.doneBullet()

    projectileListSize = len(projectileList)
    #We are removing any bullets from the list that are no longer on screen
    #We are looping through the list backwards so that we don't have to worry about removing something then being in the wrong index
    #IF we loop from the start then when we remove something we technically shouldn't move our index. But if we do it from the back then we continue going backwards
    for i in range(projectileListSize):
        if not(projectileList[(projectileListSize-1)-i].onScreen):
            #Removing the projectile with the pop method
            projectileList.pop((projectileListSize-1)-i)




    #If the ball would go out of bounds we keep it in bounds
    if ballx < 0:
        ballx = 0
    elif ballx > width - 110:
        ballx = width - 110

    if bally < 0:
        bally = 0
    elif bally > height -110:
        bally = height - 110

    #Right here I would call the sensor stuff
    #thing = fromSensorTo(sensorRead, width - 110)
    #ballx = thing
    #moving the ball
    ballUpdate(ballx,bally)


    #Moving the barrier
    barrierUpdate(barrierXPos,barrierYPos)

    #Moving the ball according ot x and y change value
    barrierXPos += barrierXChange
    barrierYChange += barrierYChange

    #If we go out of bounds we don't and we change direction
    if barrierXPos < 0:
        barrierXPos = 0
        #changing direction
        barrierXChange *= -1
    elif barrierXPos > width -32:
        barrierXPos = barrierXPos
        #Changing direction
        barrierXChange *= -1



    #Moving the barrier
    # ballrect = ballrect.move(speed)
    # if ballrect.left < 0 or ballrect.right > width:
    #     speed[0] = -speed[0]
    # if ballrect.top < 0 or ballrect.bottom > height:
    #     speed[1] = -speed[1]

    #screen.blit(ball, ballrect)

    #updating the display
    pygame.display.update()

    #pygame.display.flip()
