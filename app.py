import sys
import pygame

pygame.init()


size = width, height = 800, 600

speed = [2, 2]
black = 0, 0, 0

screen = pygame.display.set_mode(size)

clock = pygame.time.Clock()


cloud = pygame.image.load('cloud.png')

background = pygame.image.load('back.jpg').convert()
background = pygame.transform.scale(background, (800, 600))
spaceship = pygame.image.load('spaceship.png')

bullet = pygame.image.load('bullet.png')


shipX = 360
shipY = 530
ship_position = [shipX, shipY]

bulletY = 526
bulletX = 400
bullet_position = [bulletX, bulletY]

bullets = []

def bulletShoot(pressed):

    if pressed[pygame.K_SPACE]:
        x = shipX
        y = shipY
        bullets.append([x,y])
        pass

    for b in bullets:
        b[0][0] =2
        b[0][1] =2
        screen.blit(bullet,b)
         #screen.blit(bullet, b)

while 1:
    clock.tick(30)

    pressed = pygame.key.get_pressed() 

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

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

    ship_position = [shipX, shipY]
    screen.fill(black)

    screen.blit(background, [0, 0])
    # screen.blit(ball, ballrect

    #if bulletY > 0:
    #    bulletY -= 5
    # print(bulletY)
    #else:
    #    bulletY = 530

    #bullet_position = [bulletX, bulletY]

    screen.blit(bullet, bullet_position)

    bulletShoot(pressed)
    #screen.blit(spaceship, ship_position)

    pygame.display.flip()
