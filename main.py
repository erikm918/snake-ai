#!/usr/bin/env python3
import pygame as pg

from classes.snake import Snake
from classes.apple import Apple

WIDTH = 1040
HEIGHT = 640
WIN = pg.display.set_mode((WIDTH, HEIGHT))

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREY = (128, 128, 128)


def draw_border(win):
    # vertical lines
    pg.draw.line(win, GREY, (14, 15), (14, 629), 10)
    pg.draw.line(win, GREY, (1024, 15), (1024, 629), 10)

    # horizontal lines
    pg.draw.line(win, GREY, (10, 14), (1029, 14), 10)
    pg.draw.line(win, GREY, (10, 624), (1029, 624), 10)


def draw_win(win, apple):
    win.fill(BLACK)
    draw_border(win)

    apple.draw(win)

    pg.display.update()


def main_loop(win):
    running = True
    clock = pg.time.Clock()

    apple = Apple()

    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False

        clock.tick(2)
        draw_win(win, apple)


if __name__ == "__main__":
    main_loop(WIN)
