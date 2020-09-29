import pygame
from pygame.draw import *

pygame.init()

FPS = 30
black = (0, 0, 0)
grey = (128, 128, 128)
orange = (255, 165, 0)
white = (255, 255, 255)
yellow = (255, 255, 0)
screen = pygame.display.set_mode((500, 400))

def day(x):
    if x == True:
        # солнце
        rect(screen, (0,250,255), (0, 0, 500, 200))
        circle(screen, (255, 255, 0), (30, 30), 30)
        line(screen, yellow, (30, 30), (80, 50), 7)
        line(screen, yellow, (30, 30), (70, 80), 7)
        line(screen, yellow, (30, 30), (55, 84), 7)
        line(screen, yellow, (30, 30), (40, 87), 7)
        line(screen, yellow, (20, 30), (25, 80), 7)
        line(screen, yellow, (30, 30), (87, 30), 7)
    else:
        # moon
        rect(screen, (0, 25, 114), (0, 0, 500, 200))
        circle(screen, (255, 249, 140), (30, 30), 30)


# фон
rect(screen, (0, 255, 0), (0, 200, 500, 200))
day(False)

# человек слева
ellipse(screen, grey, (100, 130, 70, 180))
line(screen, black, (120, 300), (80, 350), 5)
line(screen, black, (150, 300), (190, 350), 5)
line(screen, black, (110, 170), (60, 250), 5)
line(screen, black, (160, 170), (225, 250), 5)
circle(screen, orange, (135, 130), 30)
circle(screen, black, (145, 117), 3)
circle(screen, black, (125, 117), 3)
circle(screen, black, (135, 130), 3)
arc(screen, black, (125, 132, 20, 15), 4, 6)

# мороженое
polygon(screen, (128, 0, 0), [(60, 250), (60, 220), (20, 235)])
circle(screen, (255, 0, 0), (30, 230), 10)
circle(screen, (0, 0, 0), (35, 225), 10)
circle(screen, (, (50, 220), 10)

# человек справа
polygon(screen, (128, 0, 0), [(230, 300), (400, 300), (315, 130)])
line(screen, (0, 0, 0), (300, 300), (250, 350), 5)
line(screen, (0, 0, 0), (340, 300), (390, 350), 5)
line(screen, (0, 0, 0), (300, 170), (225, 250), 5)
line(screen, (0, 0, 0), (330, 170), (370, 210), 5)
line(screen, (0, 0, 0), (370, 210), (410, 210), 5)
circle(screen, (255, 165, 0), (315, 130), 30)
circle(screen, (0, 0, 0), (325, 117), 3)
circle(screen, (0, 0, 0), (305, 117), 3)
circle(screen, (0, 0, 0), (315, 130), 3)
arc(screen, (0, 0, 0), (305, 132, 20, 15), 4, 6)

# шарик
line(screen, (128, 128, 128), (410, 210), (470, 100), 2)
# ellipse(screen, (255, 0, 0), (460, 50, 40, 50))
polygon(screen, (255, 0, 0), [[470, 100], [480, 55], [510, 80]])
ellipse(screen, (255, 0, 0), (478, 50, 20, 20))
ellipse(screen, (255, 0, 0), (485, 60, 20, 20))

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
