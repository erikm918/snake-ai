import pygame as pg
import random


class Apple:
    COLOR = (131, 191, 0)

    def __init__(self):
        self.x = random.randrange(20, 980, step=20)
        self.y = random.randrange(20, 580, step=20)
        self.eaten = False

    def draw(self, win):
        pg.draw.rect(win, self.COLOR, (self.x, self.y, 20, 20))

    def is_eaten(self, snake):
        if snake.x == self.x and snake.y == self.y:
            self.eaten = True
        else:
            self.eaten = False

    def replace(self):
        if self.eaten == True:
            self.x = random.randrange(20, 980, step=20)
            self.y = random.randrange(20, 580, step=20)
            self.eaten = False
