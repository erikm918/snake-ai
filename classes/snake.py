import random
import pygame as pg


class Block:
    EYE_COLOR = (255, 255, 255)

    def __init__(self, x, y, color, eyes=False):
        self.x = x
        self.y = y
        self.color = color
        self.eyes = eyes

    def draw(self, win):
        pg.draw.rect(win, self.color, (self.x, self.y, 20, 20))

    # draws eyes for moving left/right
    def eyes_lr(self):
        if self.eyes == True:
            eye1 = pg.draw.rect(win, self.EYE_COLOR,
                                (self.x + 3, self.y + 9, 2, 2))
            eye2 = pg.draw.rect(win, self.EYE_COLOR,
                                (self.x + 15, self.y + 9, 2, 2))

    # draws eyes for moving up/down
    def eyes_ud(self):
        if self.eyes == True:
            eye1 = pg.draw.rect(win, self.EYE_COLOR,
                                (self.x + 9, self.y + 3, 2, 2))
            eye2 = pg.draw.rect(win, self.EYE_COLOR,
                                (self.x + 9, self.y + 15, 2, 2))


class Snake:
    LEFT = False
    RIGHT = False
    UP = False
    DOWN = False
    SPEED = 20
    COLOR = (255, 0, 0)
    BODY = []
    x_vel = 0
    y_vel = 0

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.length = 1

        self.head = Block(self.x, self.y, eyes=True)
        self.body.append(self.head)

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

        for block in range(self.BODY):
            pass

    def add_block(self, apple):
        x_mod = 0
        y_mod = 0
        last_block = BODY[-1]

        '''
        if self.LEFT == True:
            x_mod = last_block.x - 20
            y_mod = last_block.y
        if self.RIGHT == True:
            x_mod = last_block.x + 20
            y_mod = 0
        if self.UP == True:
            x_mod = 0
            y_mod = 20 * num_of_blocks
        if self.DOWN == True:
            x_mod = 0
            y_mod = -20 * num_of_blocks
        '''

        if apple.eaten == True:
            self.length += 1
            self.BODY.append(Block(self.x + x_mod, self.y + y_mod, self.COLOR))
