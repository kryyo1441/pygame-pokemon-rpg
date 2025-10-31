from settings import *
from random import uniform
class Sprite(pygame.sprite.Sprite):
    def __init__(self, pos, surf, groups, z = WORLD_LAYERS["main"]):
        super().__init__(groups)
        self.image  = surf
        self.rect = self.image.get_frect(topleft = pos) #get floating point rectangle
        self.z = z
        self.y_sort  = self.rect.centery
        self.hitbox = self.rect.copy()

class BorderSprite(Sprite):
    def __init__(self, pos, surf, groups):
        super().__init__(pos, surf, groups)
        self.hitbox = self.rect.copy()

class CollidableSprite(Sprite):
    def __init__(self, pos, surf, groups):
        super().__init__(pos, surf, groups)
        self.hitbox = self.rect.inflate(0, -self.rect.height * 0.6)

class MonsterPatchSprite(Sprite):
    def __init__(self, pos, surf, groups,biome):
        super().__init__(pos, surf, groups, WORLD_LAYERS['main' if biome != 'sand' else 'bg' ]) 
        self.y_sort -= 40

class AnimatedSprite(Sprite):
    def __init__(self, pos, frames, groups, z=WORLD_LAYERS["main"]):
        self.frame_index, self.frames = 0, frames
        super().__init__(pos, frames[self.frame_index], groups, z)


    def animate(self, dt):
        self.frame_index += ANIMATION_SPEED * dt
        # The use of 'self.frames' here implies a list of surfaces for animation
        self.image = self.frames[int(self.frame_index  % len(self.frames))]

    def update(self, dt):
        self.animate(dt)

class TransitionSprite(Sprite):
    def __init__(self, pos, size, target, groups):
        surf = pygame.Surface(size)
        super().__init__(pos, surf, groups)
        self.target = target

# battle sprites
class MonsterSprite(pygame.sprite.Sprite):
    def __init__(self, pos, frames, groups, monster, index, pos_index, entity):
        # ✅ FIX: Call the parent constructor first to ensure the sprite is added to its groups
        # (e.g., self.battle_sprites) before it is used.
        super().__init__(groups)
        
        self.index = index
        self.pos_index = pos_index
        self.entity = entity
        self.monster = monster
        # 'frames' here is a dictionary: {'state': [frame1, frame2, ...]}
        self.frame_index, self.frames, self.state = 0, frames, 'idle' 
        self.animation_speed = ANIMATION_SPEED + uniform(-1 , 1)

        #sprite setup
        # Removed the redundant/misplaced 'super().__init__(groups)' call here.
        self.image = self.frames[self.state][self.frame_index]
        self.rect = self.image.get_frect(center = pos)

    def animate(self, dt):
        self.frame_index += ANIMATION_SPEED * dt
        # The animation uses the frame list corresponding to the current 'self.state'
        self.image = self.frames[self.state][int(self.frame_index) % len(self.frames[self.state])]

    def update(self, dt):
        # This method is correctly called by the group.update() in battle.py
        self.animate(dt)

class MonsterNameSprite(pygame.sprite.Sprite):
    def __init__(self, pos, monster_sprite, groups, font):
        super().__init__(groups)

        text_surf = font.render(monster_sprite.monster.name, False, COLORS['black'])
        padding = 20

        self.image = pygame.Surface((text_surf.get_width() + 2 * padding, text_surf.get_height() + 2 * padding))
        self.rect = self.image.get_rect(midtop = pos)