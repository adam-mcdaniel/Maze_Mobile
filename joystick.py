import os
import sys
import easy_sdl
from maze import *
from random import *
from entities.wall import *
from easy_sdl.tools import *
from easy_sdl.sprite import Sprite
from entities.fatbot import *


class Joystick(Sprite):
    def __init__(self, x, y):
        super(Joystick, self).__init__(x, y, image="circle.png")
        self.x_val = 0
        self.y_val = 0
        self.setStaticPosition(True)

    def update(self, screen):
        if not self.getTouchUp():
            self.x_val = 5 * min(max((self.getTouch().pos[0] - self.getX() - self.getWidth()/2) / (player.getWidth()), -10), 10)
            self.y_val = 5 * min(max((self.getTouch().pos[1] - self.getY() - self.getHeight()/2) / (player.getHeight()), -10), 10)
        else:
            self.x_val = 0
            self.y_val = 0

    def getDirection(self):
        return self.x_val, self.y_val