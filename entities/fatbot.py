from easy_sdl.sprite import Sprite
from .wall import *


class Fatbot(Sprite):
	def __init__(self, x, y):
		super(Fatbot, self).__init__(x, y, image="fatbot.png")
		self.xvel = 0
		self.yvel = 0

	def update(self, screen):
		self.move(self.xvel, 0)
		self.hitWall(self.xvel, 0, screen)
		self.move(0, self.yvel)
		self.hitWall(0, self.yvel, screen)

	def hitWall(self, xvel, yvel, screen):
		for entity in screen:
			if isinstance(entity, Wall):
				if self.collide(entity):
					print(xvel, yvel)
					if xvel > 0:
						self.goto(entity.getX() - self.getWidth(), self.getY())
					if xvel < 0:
						self.goto(entity.getX() + entity.getWidth(), self.getY())
					if yvel > 0:
						self.goto(self.getX(), entity.getY() - self.getHeight())
					if yvel < 0:
						self.goto(self.getX(), entity.getY() + entity.getHeight())