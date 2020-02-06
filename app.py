import sys, pygame

# Import pygame.locals for easier access to key coordinates
# Updated to conform to flake8 and black standards
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)


pygame.init()

size = width, height = 800, 600
speed = [2, 2]
black = 0, 0, 0

screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

ball = pygame.image.load("intro_ball.gif")
cloud = pygame.image.load('cloud.png')
background = pygame.image.load('back.jpg').convert()
background = pygame.transform.scale(background, (800,600))
spaceship = pygame.image.load('spaceship.png')

bullet = pygame.image.load('bullet.png')

ballrect = ball.get_rect()

shipX = 360
shipY = 530
ship_position = [shipX,shipY]

bulletY = 526
bulletX = 400
bullet_position = [bulletX,bulletY]

while 1:
    clock.tick(30)

    pressed = pygame.key.get_pressed()

    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    # ballrect = ballrect.move(speed)

    # if ballrect.left < 0 or ballrect.right > width:
    #     speed[0] = -speed[0]
    # if ballrect.top < 0 or ballrect.bottom > height:
    #     speed[1] = -speed[1]

     # Get all the keys currently pressed


    if pressed[pygame.K_RIGHT]:
        shipX += 10

    if pressed[pygame.K_LEFT]:
        shipX -= 10

    ship_position = [shipX,shipY]
    screen.fill(black)
    
    screen.blit(background,[0,0])
    # screen.blit(ball, ballrect
    
    if bulletY > 0:
        bulletY -= 5
    #print(bulletY)
    else:
       bulletY = 530

    bullet_position = [bulletX,bulletY]

    screen.blit(bullet, bullet_position)    
    screen.blit(spaceship, ship_position)

    pygame.display.flip()