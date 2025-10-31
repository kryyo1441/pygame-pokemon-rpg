from settings import * # Assuming this imports pygame
from sprites import MonsterPatchSprite

class Battle:
    def __init__(self, player_monsters, opponent_monsters, monster_frames, bg_surf, fonts):
        #genral
        self.display_surface = pygame.display.get_surface()
        self.bg_surf = bg_surf
        self.monster_frame = monster_frames
        self.fonts = fonts
        self.monster_data = {'player': player_monsters, 'opponent': opponent_monsters}

        #groups
        self.battle_sprites = pygame.sprite.Group()
        self.player_sprites = pygame.sprite.Group()
        self.opponent_sprites = pygame.sprite.Group()


        self.setup()

    def setup(self):
        for entity, monster in self.monster_data.items():
            for index, monster in {k:v for k,v in monster.items() if k <= 2}.items():
                self.create_monster(monster, index, index, entity)

    def create_monster(self, monster, index, pos_index, entity):
        frames = self.monster_frame['monsters'][monster.name]
        if entity == 'player':
            pos = list(BATTLE_POSITIONS['left'].values)[pos_index]
            groups = (self.battle_sprites, self.player_sprites)
        

        MonsterSprite(pos, frames, groups, monster, index, pos_index, entity)
        
        

    # FIX 2: Move the update method out of __init__ to be a proper class method
    def update(self, dt):
        
        self.display_surface.blit(self.bg_surf, (0,0))
        self.battle_sprites.draw(self.display_surface)