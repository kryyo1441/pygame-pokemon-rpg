from settings import *
from random import uniform
from support import draw_bar

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
        self.z = BATTLE_LAYERS['monster']
        self.highlight = False

        #sprite setup
        # Removed the redundant/misplaced 'super().__init__(groups)' call here.
        self.image = self.frames[self.state][self.frame_index]
        self.rect = self.image.get_frect(center = pos)

    def animate(self, dt):
        self.frame_index += ANIMATION_SPEED * dt
        self.adjusted_frame_index = int(self.frame_index) % len(self.frames[self.state])
        # The animation uses the frame list corresponding to the current 'self.state'
        self.image = self.frames[self.state][self.adjusted_frame_index]

        if self.highlight:
            white_surf = pygame.mask.from_surface(self.image).to_surface()
            white_surf.set_colorkey('black')
            self.image = white_surf

    def set_highlight(self, value):
        self.highlight = value

    def update(self, dt):
        # This method is correctly called by the group.update() in battle.py
        self.animate(dt)
        self.monster.update(dt)

class MonsterOutlineSprite(pygame.sprite.Sprite):
    def __init__(self, monster_sprite, groups, frames):
        super().__init__(groups)
        self.z = BATTLE_LAYERS['outline']
        self.monster_sprite = monster_sprite
        self.frames = frames

        self.image = self.frames[self.monster_sprite.state][self.monster_sprite.frame_index]
        self.rect = self.image.get_frect(center = self.monster_sprite.rect.center)

    def update(self, _):
        self.image = self.frames[self.monster_sprite.state][self.monster_sprite.adjusted_frame_index]


class MonsterNameSprite(pygame.sprite.Sprite):
    def __init__(self, pos, monster_sprite, groups, font):
        super().__init__(groups)
        self.monster_sprite = monster_sprite
        self.z = BATTLE_LAYERS['name']

        text_surf = font.render(monster_sprite.monster.name, False, COLORS['black'])
        padding = 10

        self.image = pygame.Surface((text_surf.get_width() + 2 * padding, text_surf.get_height() + 2 * padding))
        self.image.fill(COLORS['white'])
        self.image.blit(text_surf, (padding,padding))
        self.rect = self.image.get_rect(midtop = pos)

class MonsterLevelSprite(pygame.sprite.Sprite):


    def __init__(self, entity, pos, monster_sprite, groups, font):
        super().__init__(groups)
        self.monster_sprite = monster_sprite
        self.font = font
        self.z = BATTLE_LAYERS['name']

        

        self.image = pygame.Surface((60, 26))
        self.rect = self.image.get_rect(topleft = pos) if entity == 'player' else self.image.get_rect(topright = pos)
        self.xp_rect = pygame.Rect(0, self.rect.height - 2, self.rect.width, 2)

    def update(self, _):
        self.image.fill(COLORS['white'])

        text_surf = self.font.render(f'Lvl {self.monster_sprite.monster.level}', False, COLORS['black'])
        text_rect = text_surf.get_rect(center = (self.rect.width / 2, self.rect.height / 2))
        self.image.blit(text_surf, text_rect)

        draw_bar(self.image, self.xp_rect, self.monster_sprite.monster.xp, self.monster_sprite.monster.level_up, COLORS['black'], COLORS['white'], 0)


class MonsterStatsSprite(pygame.sprite.Sprite):
    def __init__(self, pos, monster_sprite, size, groups, font):
        super().__init__(groups)
        self.monster_sprite = monster_sprite
        self.image = pygame.Surface(size)
        self.rect = self.image.get_frect(midbottom = pos)
        self.font = font
        self.z = BATTLE_LAYERS['overlay']


    def update(self, _):
        self.image.fill(COLORS['white'])
        
        for index, (value, max_value) in enumerate(self.monster_sprite.monster.get_info()):
            color = (COLORS['red'], COLORS['blue'], COLORS['gray'])[index]
            
            if index < 2: # health and energy
                text_surf = self.font.render(f'{int(value)}/{max_value}', False, COLORS['black'])
                text_rect = text_surf.get_frect(topleft = (self.rect.width * 0.05, index * self.rect.height / 2))
                bar_rect = pygame.FRect(text_rect.bottomleft + vector(0, -2), (self.rect.width * 0.9, 4))
                
                self.image.blit(text_surf, text_rect)
                draw_bar(self.image, bar_rect, value, max_value, color, COLORS['black'], 2)
            else: # Initiative
                init_rect = pygame.FRect((self.rect.width * 0.05, self.rect.height * 0.75), (self.rect.width * 0.9, 4))
                draw_bar(self.image, init_rect, value, max_value, color, COLORS['white'], 2)