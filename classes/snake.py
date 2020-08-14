import random
import pygame as pg


class Snake:
    LEFT = False
    RIGHT = False
    UP = False
    DOWN = False
    SPEED = 20

    def __init__(self, x, y, length):
        self.x = x
        self.y = y
        self.length = length
        self.x_vel = 0
        self.y_vel = 0

        self.num_blocks = []

    def left(self):
        if self.LEFT == False and self.RIGHT == False:
            self.x_vel = -1
            self.y_vel = 0
            self.LEFT = True
            self.RIGHT = False
            self.UP = False
            self.DOWN = False
        else:
            self.x_vel = self.x_vel
            self.y_vel = self.y_vel

    def right(self):
        if self.RIGHT == False and self.LEFT == False:
            self.x_vel = 1
            self.y_vel = 0
            self.RIGHT = True
            self.LEFT = False
            self.UP = False
            self.DOWN = False
        else:
            self.x_vel = self.x_vel
            self.y_vel = self.y_vel

    def up(self):
        if self.UP == False and self.DOWN == False:
            self.y_vel = -1
            self.x_vel = 0
            self.UP = True
            self.DOWN = False
            self.LEFT = False
            self.RIGHT = False
        else:
            self.x_vel = self.x_vel
            self.y_vel = self.y_vel

    def down(self):
        if self.DOWN == False and self.UP == False:
            self.y_vel = 20
            self.x_vel = 0
            self.DOWN = True
            self.UP = False
            self.LEFT = False
            self.RIGHT = False
        else:
            self.x_vel = self.x_vel
            self.y_vel = self.y_vel

    def move(self, frame_rate):
        dy = self.y_vel * frame_rate * self.SPEED
        dx = self.x_vel * frame_rate * self.SPEED

        if not self.x_vel == 0:
            self.x = self.x + dx
        elif not self.y_vel == 0:
            self.y = self.y + dy