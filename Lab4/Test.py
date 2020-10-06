import pygame as pg

pg.init()

fps = 30
screen = pg.display.set_mode((400,400))
finished = False
BLACK = (0,0,0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

while not finished:
    for event in pg.event.get():
        if event == pg.QUIT:
            finished = True

    screen.fill(BLACK)
    screen.update()