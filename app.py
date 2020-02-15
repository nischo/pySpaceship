import sys
import pygame

pygame.init()

# set the widht and height of the window
size = width, height = 800, 600

speed = [2, 2]
black = 0, 0, 0

# empty list for bullets
bullets = []


screen = pygame.display.set_mode(size)

clock = pygame.time.Clock()

cloud = pygame.image.load('cloud.png')

#load background picture
background = pygame.image.load('back.jpg').convert()
background = pygame.transform.scale(background, size)

#load monster picture 32x32
monster = pygame.image.load('monster.png')

#load SpaceShip picture 64x64
spaceship = pygame.image.load('spaceship.png')

#load bullet picture
bullet = pygame.image.load('bullet.png')


shipX = 360
shipY = 530
shipPosition = [shipX, shipY]

bulletY = 526
bulletX = 400


def moveShip(pressed):
    # Get all the keys currently pressed
    if pressed[pygame.K_RIGHT] and shipPosition[0] < (width - 64):
        shipPosition[0] += 10


    if pressed[pygame.K_LEFT] and shipPosition[0] > 0:
        shipPosition[0] -= 10
  
    screen.blit(spaceship, [shipPosition[0], shipPosition[1]])

def bulletShoot(pressed):

    if pressed[pygame.K_SPACE]:
        bullets.append([shipPosition[0] + 20,shipPosition[1]])
  

    for b in bullets:
        b[1] -=10
        if b[1] < -5:
          bullets.remove(b)
        screen.blit(bullet,b)


while 1:
    clock.tick(30)

    pressed = pygame.key.get_pressed() 

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()



    
    screen.fill(black)

    screen.blit(background, [0, 0])

   
    moveShip(pressed)
    bulletShoot(pressed)
    screen.blit(monster, [400,80])
    

    pygame.display.flip()
