import random
import pygame, sys
from pygame.locals import QUIT, K_ESCAPE, KEYDOWN

width = 750
height = 500

white = (255,255,255)
grey = (105,105,105)
dark_grey = (59,59,56)
black = (0,0,0)
red = (255,0,0)
green = (0,175,0)
pine_green = (2, 48, 32)
blue = (135,206,235)
midnight_blue = (7,22,48)
maroon = (128,0,0)
yellow = (255,223,0)
slate = (47,79,79)
brown = (92, 64, 51)

cloud_x = random.randrange(0,width)
cloud_y = 100
cloud_x_speed = random.randrange(1,5)
cloud2_x = random.randrange(0,width)
cloud2_y = 150
cloud2_x_speed = random.randrange(1,5)
cloud3_x = random.randrange(0,width)
cloud3_y = 50
cloud3_x_speed = random.randrange(1,5)

sun_y = 75
sun_radius = 50
sun_speed = 1

tree_x = 600
tree_y = 466
tree_width = 2
tree_height = 10
tree_radius = 8
tree_growth = .05

star_list = []
for i in range(50):
    star_x = random.randrange(0, 750)
    star_y = random.randrange(0, 500)
    star_list.append ([star_x, star_y])

smoke_list = []
for i in range(20):
    smoke_x = random.randrange(387,413)
    smoke_y = random.randrange(170,240)
    smoke_list.append ([smoke_x, smoke_y])

pygame.init()
screen = pygame.display.set_mode((width, height))
fade = pygame.Surface((width, height))
pygame.display.set_caption('Landscape Assignment')
clock = pygame.time.Clock()

running = True
day = True
night = False
while running:
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
        elif event.type == QUIT:
            running = False

    screen.fill(blue)
    
    if cloud_x - 100 >= width:
        cloud_x = random.randrange(-300,-100)
        cloud_x_speed = random.randrange(1,5)
    if cloud2_x - 100 >= width:
        cloud2_x = random.randrange(-300,-100)
        cloud2_x_speed = random.randrange(1,5)
    if cloud3_x - 100 >= width:
        cloud3_x = random.randrange(-300,-100)
        cloud3_x_speed = random.randrange(1,5)

    if day and sun_y - sun_radius == height:
        sun_y = height + 50
        sun_speed *= -1
        yellow = (255,255,255)
        blue = (7,22,48)
        green = (2,48,32)
        slate = (255,223,0)
        white = (105,105,105)
        night = True
        day = False

    if night and sun_y - sun_radius == height:
        if sun_speed == 1:
            sun_y = height + 50
            sun_speed *= -1
            yellow = (255,223,0)
            blue = (135,206,235)
            green = (0,175,0)
            slate = (47,79,79)
            white = (255,255,255)
            day = True
            night = False

    if night:
        for star in star_list:
            pygame.draw.circle(screen, (255,255,255), star, 2)
    
    if night and sun_y == 75:
        sun_speed *= -1

    if day and sun_y == 75:
        if sun_speed == -1:
            sun_speed *= -1

    if day:
        tree_y -= tree_growth
        tree_x -= tree_growth / 8
        tree_width += tree_growth / 4
        tree_height += tree_growth
        tree_radius += tree_growth / 2
    
    if tree_height + tree_radius >= height/2:
        tree_growth = 0

    cloud_x += cloud_x_speed
    cloud2_x += cloud2_x_speed
    cloud3_x += cloud3_x_speed

    sun_y += sun_speed
    
    pygame.draw.circle(screen, yellow, [75,sun_y],50)

    pygame.draw.circle(screen, white, [cloud_x, cloud_y],40)
    pygame.draw.circle(screen, white, [cloud_x + 50, cloud_y + 25],40)
    pygame.draw.circle(screen, white, [cloud_x -50, cloud_y + 25],40)
    pygame.draw.circle(screen, white, [cloud_x, cloud_y + 30],40)

    pygame.draw.circle(screen, white, [cloud2_x, cloud2_y],40)
    pygame.draw.circle(screen, white, [cloud2_x + 50, cloud2_y + 25],40)
    pygame.draw.circle(screen, white, [cloud2_x -50, cloud2_y + 25],40)
    pygame.draw.circle(screen, white, [cloud2_x, cloud2_y + 30],40)

    pygame.draw.circle(screen, white, [cloud3_x, cloud3_y],40)
    pygame.draw.circle(screen, white, [cloud3_x + 50, cloud3_y + 25],40)
    pygame.draw.circle(screen, white, [cloud3_x -50, cloud3_y + 25],40)
    pygame.draw.circle(screen, white, [cloud3_x, cloud3_y + 30],40)

    pygame.draw.rect(screen, brown, [tree_x, tree_y, tree_width, tree_height])
    pygame.draw.circle(screen,pine_green,[tree_x+tree_width/2,tree_y],tree_radius)

    pygame.draw.rect(screen, green, [0,475,750,25])

    pygame.draw.rect(screen, maroon , [275, 325, 150, 150])
    pygame.draw.rect(screen, maroon, (387,250,25,50))

    if night:
        for smoke in smoke_list:
            smoke[1] -= 2
            pygame.draw.circle(screen,dark_grey, smoke,15)
            if smoke[1] <= 170:
                smoke[1] = 240
                smoke[0] = random.randrange(387,413)

    pygame.draw.polygon(screen, black, ((250,325), (350,250), (450,325)))
    pygame.draw.rect(screen, slate, (300,350,30,30))
    pygame.draw.rect(screen, slate, (370, 350, 30,30))
    pygame.draw.rect(screen, black, (300,350,30,30),3)
    pygame.draw.rect(screen, black, (370,350,30,30),3)
    pygame.draw.line(screen, black, (314,350), (314,377),3)
    pygame.draw.line(screen, black, (384,350), (384,377),3)
    pygame.draw.rect(screen, black, (330,410,40,65))
    pygame.draw.circle(screen, maroon, [357,445],3)

    pygame.display.flip()
    clock.tick(30)
