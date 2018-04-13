import os
import sys
import easy_sdl
from maze import *
from random import *
from joystick import *
from entities.wall import *
from easy_sdl.tools import *
from easy_sdl.sprite import Sprite
from entities.fatbot import *


CELL_SIZE = 256
MAZE_WIDTH, MAZE_HEIGHT = 8, 8
LEVEL_WIDTH, LEVEL_HEIGHT = 2 * (CELL_SIZE * MAZE_WIDTH) + CELL_SIZE, 2 * (CELL_SIZE * MAZE_HEIGHT) + CELL_SIZE


player = Fatbot(256, 256)
j = Joystick(300, 300)


walls = convertMap(GenerateMap((MAZE_WIDTH, MAZE_HEIGHT)))
print(walls)


screen = easy_sdl.setup.setup(win_width=2220,
                              win_height=1080,
                              level_width=LEVEL_WIDTH,
                              level_height=LEVEL_HEIGHT)

screen.add(walls)
screen.append(j)
screen.append(player)


def f():
    player.xvel, player.yvel = j.getDirection()
    screen.focus(player)

screen.run(f)


