import pygame as pg
from pygame.draw import *
from random import randint

pg.init()

finished = False
score = 0
FPS = 10
screen = pg.display.set_mode((1200, 900))
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]
ball_number = 3
ball_X = []
ball_Y = []
ball_R = []
ball_Color = []
Vx = []
Vy = []
ball_time = []


def new_ball():
    '''рисует новый шарик '''
    ball_x = randint(100, 1100)
    ball_y = randint(100, 900)
    ball_r = randint(10, 100)
    ball_color = COLORS[randint(0, 5)]
    ball_Vx = randint(-10, 10)
    ball_Vy = randint(-10, 10)
    return (ball_x, ball_y, ball_r, ball_color, ball_Vx, ball_Vy)


for i in range(ball_number):
    (a, b, c, d, e, f) = (new_ball()[0], new_ball()[1], new_ball()[2], new_ball()[3], new_ball()[4], new_ball()[5])
    ball_X.append(a)
    ball_Y.append(b)
    ball_R.append(c)
    ball_Color.append(d)
    Vx.append(e)
    Vy.append(f)
    ball_time.append(0)

pg.display.update()
clock = pg.time.Clock()

while not finished:
    clock.tick(FPS)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            finished = True
        if event.type == pg.MOUSEBUTTONDOWN:
            mouse_x = event.pos[0]
            mouse_y = event.pos[1]
            for i in range(ball_number):
                if (mouse_x - ball_X[i]) ** 2 + (mouse_y - ball_Y[i]) ** 2 <= ball_R[i] ** 2:
                    ball_X[i] = new_ball()[0]
                    ball_Y[i] = new_ball()[1]
                    ball_R[i] = new_ball()[2]
                    ball_Color[i] = new_ball()[3]
                    Vx[i] = new_ball()[4]
                    Vy[i] = new_ball()[5]
                    if ball_R[i] <= 30:
                        score += 5
                    if ball_R[i] > 30 and ball_R[i] <= 60:
                        score += 2
                    if ball_R[i] > 60:
                        score += 1
                    print("Score = ", score)

    for i in range(ball_number):
        R = ball_Color[i][0]+ball_time[i]
        G = ball_Color[i][1]+ball_time[i]
        B = ball_Color[i][2]+ball_time[i]

        circle(screen, ball_Color[i], (ball_X[i], ball_Y[i]), ball_R[i])
        ball_time[i] += 1

        if ball_time[i] >= 90:
            ball_X[i] = new_ball()[0]
            ball_Y[i] = new_ball()[1]
            ball_R[i] = new_ball()[2]
            ball_Color[i] = new_ball()[3]
            Vx[i] = new_ball()[4]
            Vy[i] = new_ball()[5]
            ball_time[i] = 0

        if ball_X[i] > 1100:
            Vx[i] = randint(-10, 0)
        if ball_X[i] < 100:
            Vx[i] = randint(0, 10)
        if ball_Y[i] > 800:
            Vy[i] = randint(-10, 0)
        if ball_Y[i] < 100:
            Vy[i] = randint(0, 10)

        ball_X[i] += Vx[i]
        ball_Y[i] += Vy[i]

    pg.display.update()
    screen.fill(BLACK)

pg.quit()
