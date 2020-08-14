import pygame as pg
import random


class Apple:
    COLOR = (131, 191, 0)

    def __init__(self):
        self.x = random.randrange(20, 980, step=20)
        self.y = random.randrange(20, 580, step=20)

    def draw(self, win):
        pg.draw.rect(win, self.COLOR, (self.x, self.y, 20, 20))
