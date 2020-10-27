from random import randrange as rnd, choice
import tkinter as tk
import math
import time

# print (dir(math))
screen_width = 800
screen_height = 600
ball_live = 60
ball_radius = 10
ball_x = 40
ball_y = 450
bullet = 0
gun_x = 20
gun_y = 450
balls = []
root = tk.Tk()
fr = tk.Frame(root)
root.geometry(str(screen_width) + 'x' + str(screen_height))
canv = tk.Canvas(root, bg='white')
canv.pack(fill=tk.BOTH, expand=1)


class ball():
    def __init__(self, x=ball_x, y=ball_y):
        """
        Конструктор класса ball

        Args:
        x - начальное положение мяча по горизонтали
        y - начальное положение мяча по вертикали
        r - радиус шарика
        vx - скорость шарика по оси x
        xy - скорость шарика по оси y
        color - цвет шарика
        id - полотно на котором размещается шарик
        live - время жизни шарика
        """
        self.x = x
        self.y = y
        self.r = ball_radius
        self.vx = 0
        self.vy = 0
        self.color = choice(['blue', 'green', 'red', 'brown'])
        self.id = canv.create_oval(
            self.x - self.r,
            self.y - self.r,
            self.x + self.r,
            self.y + self.r,
            fill=self.color
        )
        self.live = ball_live

    def set_coords(self):
        """Метод устанавливает координаты холста с мячом"""
        canv.coords(self.id, self.x - self.r, self.y - self.r, self.x + self.r, self.y + self.r)

    def move(self):
        """
        Переместить мяч по прошествии единицы времени.

        Метод описывает перемещение мяча за один кадр перерисовки. То есть, обновляет значения
        self.x и self.y с учетом скоростей self.vx и self.vy, силы гравитации, действующей на мяч,
        и стен по краям окна (размер окна 800х600).
        """
        if self.live == 0:
            balls.pop(balls.index(self))
            canv.delete(self.id)
        else:
            if self.y > screen_height or self.y < 0:
                self.vy = -self.vy
            if self.x > screen_width or self.x < 0:
                self.vx = -self.vx
            self.vy += 1
            self.live -= 1
            self.x += self.vx
            self.y += self.vy
            self.set_coords()

    def hittest(self, ob):
        """
        Функция проверяет сталкивалкивается ли данный обьект с целью, описываемой в обьекте obj.

        Args:
            obj: Обьект, с которым проверяется столкновение.
        Returns:
            Возвращает True в случае столкновения мяча и цели. В противном случае возвращает False.
        """
        if (ob.x - self.x) ** 2 + (ob.y - self.y) ** 2 <= (self.r + ob.r) ** 2:
            return True
        else:
            return False

    def die(self):
        canv.delete(self.id)


class gun():
    def __init__(self):
        """
        f2_power - сила, с которой стреляет пушка
        f2_on - 1 если пушка готова стрелять, 0 - если нет
        an - угол пушки
        id - полтно с пушкой
        """
        self.f2_power = 10
        self.f2_on = 0
        self.an = 1
        self.id = canv.create_line(20, 450, 50, 420, width=7)

    def fire2_start(self, event):
        """Меняет переменную, обозначающую заряженность пушки, на 1"""
        self.f2_on = 1

    def fire2_end(self, event):
        """
        Выстрел мячом.

        Происходит при отпускании кнопки мыши.
        Начальные значения компонент скорости мяча vx и vy зависят от положения мыши.

        :param event:
        y - координата курсора по оси y
        x - координата кусора по оси x
        bullets - количесто затраченных пуль
        :return: none
        """
        global balls, bullet
        bullet += 1
        new_ball = ball()
        self.an = math.atan((event.y - new_ball.y) / (event.x - new_ball.x))
        new_ball.vx = self.f2_power * math.cos(self.an)
        new_ball.vy = self.f2_power * math.sin(self.an)
        balls += [new_ball]
        self.f2_on = 0
        self.f2_power = 10

    def targetting(self, event=0):
        """Меняет направление пушки"""

        if event:
            self.an = math.atan((event.y - gun_y) / (event.x - gun_x))
        canv.coords(self.id, gun_x, gun_y,
                    gun_x + max(self.f2_power, 20) * math.cos(self.an),
                    gun_y + max(self.f2_power, 20) * math.sin(self.an)
                    )
        if t1.live == 1:
            t1.move()
        if t2.live == 1:
            t2.move()

    def power_up(self):
        """увеличивает силу выстрела пушки и закрашивает ее"""
        if self.f2_on:
            if self.f2_power < 40:
                self.f2_power += 0.4
            canv.itemconfig(self.id, fill='orange')
        else:
            canv.itemconfig(self.id, fill='black')


class target():
    def __init__(self):
        """
        points - количсество уничтоженных шариков
        id - полотно с целью
        id_points - полотно со счетом
        live - 1 если цель жива 0 - если нет
        """
        self.points = 0
        self.id = canv.create_oval(0, 0, 0, 0)
        self.id_points = canv.create_text(30, 30, text=self.points, font='28')
        self.new_target()
        self.live = 1

    def new_target(self):
        """ Инициализация новой цели. """
        x = self.x = rnd(500, 700)
        y = self.y = rnd(300, 500)
        r = self.r = rnd(2, 50)
        vx = self.vx = rnd(-10, 10)
        vy = self.vy = rnd(-10, 10)
        color = self.color = 'red'
        canv.coords(self.id, x - r, y - r, x + r, y + r)
        canv.itemconfig(self.id, fill=color)

    def hit(self, points=1):
        """Попадание шарика в цель."""
        canv.coords(self.id, -10, -10, -10, -10)
        canv.itemconfig(self.id_points, text=self.points)

    def move(self):
        if self.x >= 700:
            self.vx = -self.vx
        if self.x <= 100:
            self.vx = -self.vx
        if self.y >= 500:
            self.vy = -self.vy
        if self.y <= 100:
            self.vy = -self.vy

        self.x += self.vx
        self.y += self.vy
        canv.coords(self.id, self.x - self.r, self.y - self.r, self.x + self.r, self.y + self.r)
        canv.itemconfig(self.id, fill=self.color)


t1 = target()
t2 = target()
screen1 = canv.create_text(400, 300, text='', font='28')  # создает полотно со счетом
g1 = gun()


def new_game(event=''):
    global gun, t1, t2, screen1, balls, bullet
    t1.new_target()
    t2.new_target()
    bullet = 0
    balls = []
    canv.bind('<Button-1>', g1.fire2_start)  # Нажатие ПКМ вызывает функцию g1.fire2_start
    canv.bind('<ButtonRelease-1>', g1.fire2_end)  # Отпускание ПКМ
    canv.bind('<Motion>', g1.targetting)  # Движение курсора

    t1.live = 1
    t2.live = 1
    while (t1.live or t2.live):
        for b in balls:
            if t1.live == 1 or t2.live == 1:
                b.move()
            if b.hittest(t1) and t1.live:
                t1.live = 0
                t1.hit()
            if b.hittest(t2) and t2.live:
                t2.live = 0
                t2.hit()
            if t2.live == 0 and t1.live == 0:
                canv.itemconfig(screen1, text='Вы уничтожили цель за ' + str(bullet) + ' выстрелов')
        if t1.live == 1:
            t1.move()
        if t2.live == 1:
            t2.move()
        g1.targetting()
        canv.update()
        time.sleep(0.03)
        g1.power_up()
    canv.itemconfig(screen1, text='')
    for i in balls:
        i.die()
    root.after(750, new_game)


new_game()
root.mainloop()
