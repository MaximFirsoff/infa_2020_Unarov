import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((400, 400))

circle(screen, (255, 255, 0), (200, 200), 50, 50)
circle(screen, (255, 0, 0), (180, 180), 10, 5,)
circle(screen, (255, 0, 0), (220, 180), 10, 5,)
circle(screen, (255, 0, 0), (180, 180), 10, 5,)
circle(screen, (255, 0, 0), (220, 180), 10, 5,)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()