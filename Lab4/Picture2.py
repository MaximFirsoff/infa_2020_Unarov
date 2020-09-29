import pygame as pg
import random
import numpy as np

pg.init()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

process = True
sc_width = 1000
sc_height: int = 700
hedgehog_width = 220
hedgehog_height = 80
sc = pg.display.set_mode((1000, 700))

# Создаем фон
pg.draw.rect(sc, (84, 200, 117), (0, 0, sc_width, sc_height))
pg.draw.rect(sc, (70, 70, 70), (0, 400, sc_width, sc_height))
pg.draw.rect(sc, (236, 205, 0), (int(sc_width * 0.75), 0, 100, 440))
pg.draw.rect(sc, (236, 205, 0), (int(sc_width * 0.1), 0, 200, 650))
pg.draw.rect(sc, (236, 205, 0), (int(sc_width * 0.9), 0, 60, 520))
pg.draw.rect(sc, (236, 205, 0), (int(sc_width * 0), 0, 40, 440))


# Создаем функцию, создающую ежа
def hedgehog(x, y):
    """

    :param x:
    :param y:
    :return:
    """
    a = hedgehog_width / 2.3
    b = hedgehog_height / 2.3
    pg.draw.ellipse(sc, (68, 0, 19), (sc_width * x, sc_height * y, hedgehog_width, hedgehog_height))
    pg.draw.ellipse(sc, (100, 100, 100), (sc_width * x, sc_height * y, hedgehog_width, hedgehog_height), 3)

    pg.draw.ellipse(sc, (68, 0, 19),
                    (sc_width * x + hedgehog_width * 0.9, sc_height * y + hedgehog_height * 0.4, 50, 30))
    pg.draw.ellipse(sc, (0, 0, 0),
                    (sc_width * x + hedgehog_width * 0.9, sc_height * y + hedgehog_height * 0.4, 50, 30),1)

    pg.draw.ellipse(sc, BLACK,
                    (sc_width * x + hedgehog_width + 13, sc_height * y + hedgehog_height * 0.4 + 6, 8, 8))
    pg.draw.ellipse(sc, BLACK,
                    (sc_width * x + hedgehog_width + 2, sc_height * y + hedgehog_height * 0.4 + 10, 8, 8))
    pg.draw.ellipse(sc, BLACK,
                    (sc_width * x + hedgehog_width + 23, sc_height * y + hedgehog_height * 0.4 + 11, 6, 6))
    pg.draw.ellipse(sc, WHITE,
                    (sc_width * x + hedgehog_width + 13, sc_height * y + hedgehog_height * 0.4 + 6, 8, 8), 1)
    pg.draw.ellipse(sc, WHITE,
                    (sc_width * x + hedgehog_width + 2, sc_height * y + hedgehog_height * 0.4 + 10, 8, 8), 1)
    pg.draw.ellipse(sc, WHITE,
                    (sc_width * x + hedgehog_width + 23, sc_height * y + hedgehog_height * 0.4 + 11, 6, 6), 1)

    pg.draw.ellipse(sc, (68, 0, 19), (sc_width * x, sc_height * y + hedgehog_height - 20, 40, 20))
    pg.draw.ellipse(sc, (100, 100, 100), (sc_width * x, sc_height * y + hedgehog_height - 20, 40, 20), 2)
    pg.draw.ellipse(sc, (68, 0, 19), (sc_width * x + hedgehog_width - 35, sc_height * y + hedgehog_height - 20, 40, 20))
    pg.draw.ellipse(sc, (100, 100, 100),
                    (sc_width * x + hedgehog_width - 35, sc_height * y + hedgehog_height - 20, 40, 20), 2)

    for i in range(30):
        x0 = random.randint(-int(a), int(a))
        y0 = random.randint(-int(b * (1 - (x0 / a) ** 2) ** 0.5), int(b * (1 - (x0 / a) ** 2) ** 0.5))
        k = random.uniform(-np.pi / 5, np.pi / 5)
        ver_1 = [sc_width * x + a + x0, sc_height * y + b + y0]
        ver_2 = [sc_width * x + a + x0 + 20 * np.cos(k), sc_height * y + b + y0 - 20 * np.sin(k)]
        ver_3 = [sc_width * x + a + x0 + 5 - 90 * np.sin(k), sc_height * y + b + y0 - 90 * np.cos(k)]
        pg.draw.polygon(sc, (30, 30, 30), [ver_1, ver_2, ver_3], )
        pg.draw.polygon(sc, (0, 0, 0), [ver_1, ver_2, ver_3], 1)

    pg.draw.ellipse(sc, (255, 33, 0),
                    (sc_width * x + hedgehog_width - 100, sc_height * y + hedgehog_height - 140, 70, 70))
    pg.draw.ellipse(sc, (230, 145, 0),
                    (sc_width * x + hedgehog_width - 200, sc_height * y + hedgehog_height - 140, 50, 50))

    for i in range(20):
        x0 = random.randint(-int(a), int(a))
        y0 = random.randint(-int(b * (1 - (x0 / a) ** 2) ** 0.5), int(b * (1 - (x0 / a) ** 2) ** 0.5))
        k = random.uniform(-np.pi / 5, np.pi / 5)
        ver_1 = [sc_width * x + a + x0, sc_height * y + b + y0]
        ver_2 = [sc_width * x + a + x0 + 20 * np.cos(k), sc_height * y + b + y0 - 20 * np.sin(k)]
        ver_3 = [sc_width * x + a + x0 + 5 - 90 * np.sin(k), sc_height * y + b + y0 - 90 * np.cos(k)]
        pg.draw.polygon(sc, (30, 30, 30), [ver_1, ver_2, ver_3], )
        pg.draw.polygon(sc, (0, 0, 0), [ver_1, ver_2, ver_3], 1)

    pg.draw.ellipse(sc, WHITE,
                    (sc_width * x + hedgehog_width - 140, sc_height * y + hedgehog_height - 160, 20, 70))
    pg.draw.ellipse(sc, (255, 127, 116),
                    (sc_width * x + hedgehog_width - 175, sc_height * y + hedgehog_height - 160, 90, 30))

    for i in range(10):
        x0 = random.randint(-int(a), int(a))
        y0 = random.randint(-int(b * (1 - (x0 / a) ** 2) ** 0.5), int(b * (1 - (x0 / a) ** 2) ** 0.5))
        k = random.uniform(-np.pi / 5, np.pi / 5)
        ver_1 = [sc_width * x + a + x0, sc_height * y + b + y0]
        ver_2 = [sc_width * x + a + x0 + 20 * np.cos(k), sc_height * y + b + y0 - 20 * np.sin(k)]
        ver_3 = [sc_width * x + a + x0 + 5 - 90 * np.sin(k), sc_height * y + b + y0 - 90 * np.cos(k)]
        pg.draw.polygon(sc, (30, 30, 30), [ver_1, ver_2, ver_3], )
        pg.draw.polygon(sc, BLACK, [ver_1, ver_2, ver_3], 1)


hedgehog(0.6, 0.7)
hedgehog(0, 0.7)
pg.display.update()

while process:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            process = False
