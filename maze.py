import os
import sys
import easy_sdl
from maze import *
from random import *
from easy_sdl.tools import *
from easy_sdl.sprite import Sprite
from entities.fatbot import *
from entities.wall import *


def GenerateMap(dimensions):
    map_string = MakeMaze(dimensions).split("\n")
    for i, line in enumerate(map_string):
        if line == "\n":
            del map_string[i]

    map_string = list(filter(lambda line: line != "\n" and line != "",
                        map_string))
    return map_string

def MakeMaze(dimensions):
    w, h = dimensions
    vis = [[0] * w + [1] for _ in range(h)] + [[1] * (w + 1)]
    ver = [["| "] * w + ['|'] for _ in range(h)] + [[]]
    hor = [["+-"] * w + ['+'] for _ in range(h + 1)]

    def walk(x, y):
        vis[y][x] = 1

        d = [(x - 1, y), (x, y + 1), (x + 1, y), (x, y - 1)]
        shuffle(d)
        for (xx, yy) in d:
            if vis[yy][xx]:
                continue

            if xx == x:
                hor[max(y, yy)][x] = "+ "

            if yy == y:
                ver[y][max(x, xx)] = "  "

            walk(xx, yy)

    walk(randrange(w), randrange(h))

    s = ""
    for (a, b) in zip(hor, ver):
        s += ''.join(a + ['\n'] + b + ['\n'])
    return s


def convertMap(m):
    walls = []
    x, y = 0, 0
    for line in m:
        for column in line:
            if column in ["+", "|", "-"]:
                walls.append(Wall(x, y))
            x += 256
        y += 256
        x = 0
    return walls