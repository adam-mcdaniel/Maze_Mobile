from easy_sdl.sprite import Sprite


class Wall(Sprite):
	def __init__(self, x, y):
            super(Wall, self).__init__(x, y, image="brick.png")


