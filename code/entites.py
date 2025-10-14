from settings import *


class Player(pygame.sprite.Sprite):
    def __init__(self,pos,groups):
        super().__init__(groups)
        self.image = pygame.Surface((100,100))
        self.image.fill("Red") 
        self.rect = self.image.get_frect(center = pos)