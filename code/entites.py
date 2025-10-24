from settings import *

class Entity(pygame.sprite.Sprite):
    def __init__(self, pos, frames, groups):
        super().__init__(groups)

         # graphics
        self.frame_index, self.frames = 0, frames

         # sprite setup
        self.image = self.frames[self.get_state()][self.frame_index]
        self.rect = self.image.get_frect(center = pos)
    
    def animate(self, dt):
        self.frame_index += ANIMATION_SPEED * dt
        self.image = self.frames[self.get_state()][int(self.frame_index % len(self.frames[self.get_state()]))]

    def get_state(self):
        #logic
        return 'right'

class Player(Entity):
    def __init__(self, pos, frames, groups):
        super().__init__(pos, frames, groups)
     
        self.direction = vector()

    def input(self):
        keys = pygame.key.get_pressed()
        input_vector = vector() 
        if keys[pygame.K_UP]:
            input_vector.y -= 1
        if keys[pygame.K_DOWN]:
            input_vector.y += 1
        if keys[pygame.K_LEFT]:
            input_vector.x -= 1
        if keys[pygame.K_RIGHT]:
            input_vector.x += 1
        self.direction = input_vector

    def move(self, dt):
        self.rect.center += self.direction * 250 * dt

    def update(self, dt):
        self.input()
        self.move(dt)
        self.animate(dt)
