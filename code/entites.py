from settings import *

class Entity(pygame.sprite.Sprite):
    def __init__(self, pos, frames, groups, facing_direction):
        super().__init__(groups)
        self.z = WORLD_LAYERS['main']

        # graphics
        self.frame_index, self.frames = 0, frames
        self.facing_direction = facing_direction

        # movement
        self.direction = vector()
        self.speed = 250
        self.blocked = False

        # sprite setup
        self.image = self.frames[self.get_state()][self.frame_index]
        self.rect = self.image.get_rect(center = pos)  #prolly frect or rect
        self.hitbox = self.rect.inflate(-self.rect.width / 2, -60)
        
        self.y_sort = self.rect.centery
    
    def animate(self, dt):
        self.frame_index += ANIMATION_SPEED * dt
        self.image = self.frames[self.get_state()][int(self.frame_index % len(self.frames[self.get_state()]))]

    def get_state(self):
        #logic
        moving = bool(self.direction)
        if moving:
            if self.direction.x != 0:
                self.facing_direction = "right" if self.direction.x > 0 else "left"
            if self.direction.y != 0:
                self.facing_direction = "down" if self.direction.y > 0 else "up"
        return f"{self.facing_direction}{'' if moving else '_idle'}"


    def change_facing_direction(self, target_pos):
        relation = vector(target_pos) - vector(self.rect.center)
        if abs(relation.y) < 30:
            self.facing_direction = "right" if relation.x > 0 else "left"
        else:
            self.facing_direction = "down" if relation.y > 0 else "up"



    def block(self):
        self.blocked = True
        self.direction = vector(0,0)
    
    def unblock(self):
        self.blocked = False

class Character(Entity):
    def __init__(self, pos, frames, groups, facing_direction):
        super().__init__(pos, frames, groups, facing_direction) 

    def update(self, dt):
        self.animate(dt) 
class Player(Entity):
    def __init__(self, pos, frames, groups, facing_direction, collision_sprites):
        super().__init__(pos, frames, groups, facing_direction)
        self.collision_sprites = collision_sprites
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
        # compute movement as a Vector2 and apply to rect coordinates to avoid tuple/Vector2 addition errors
        self.rect.centerx += self.direction.x * self.speed * dt
        #For Collision Moving The Collision With Object/Entity
        self.hitbox.centerx = self.rect.centerx
        self.collisions('horizontal')

        self.rect.centery += self.direction.y * self.speed * dt
        #For Collision Moving The Collision With Object/Entity
        self.hitbox.centery = self.rect.centery
        self.collisions('vertical')


    def collisions(self, axis):
        for sprite in self.collision_sprites:
            if sprite.hitbox.colliderect(self.hitbox):
                if axis == 'horizontal':
                    if self.direction.x > 0:
                        self.hitbox.right = sprite.hitbox.left
                        if self.direction.x > 0:
                            self.rect.centerx = self.hitbox.centerx
                    if self.direction.x < 0:
                        self.hitbox.left = sprite.hitbox.right
                else:
                    if self.direction.y > 0:
                        self.hitbox.bottom = sprite.hitbox.top
                    if self.direction.y < 0:
                        self.hitbox.top = sprite.hitbox.bottom
                    self.rect.centery = self.hitbox.centery

    def update(self, dt):
        self.y_sort = self.rect.centery
        if not self.blocked:
            self.input()
            self.move(dt)
        self.animate(dt)