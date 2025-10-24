from settings import *

class Sprite(pygame.sprite.Sprite):
    def __init__(self, pos, surf, groups):
        super().__init__(groups)
        self.image  = surf
        self.rect = self.image.get_frect(topleft = pos) #get floating point rectangle

class AnimatedSprite(Sprite):
    def __init__(self, pos, frames, groups):
        super().__init__(pos, frames[0], groups)