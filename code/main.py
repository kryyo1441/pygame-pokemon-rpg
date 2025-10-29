from settings import *
from pytmx.util_pygame import load_pygame 
from os.path import join
from sprites import Sprite, AnimatedSprite, MonsterPatchSprite, BorderSprite
from entites import Player, Character
from groups import AllSprites

from support import *

class Game:
    def __init__(self):
        pygame.init()
        self.display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption('pokemon-rpg')
        self.clock= pygame.time.Clock()

        #groups
        self.all_sprites = AllSprites() # this group will contain all the sprites, well all the visible ones atleast :)
        self.collision_sprites = pygame.sprite.Group()

        self.import_assets()
        self.setup(self.tmx_maps['world'], 'house')

    def import_assets(self):
        self.tmx_maps = {
            'world': load_pygame(join('..', 'data', 'maps', 'world.tmx')),
            'hospital': load_pygame(join('..', 'data', 'maps', 'hospital.tmx')),
            }
        
        self.overworld_frames = {
            'water': import_folder('..','graphics','tilesets','water'),
            'coast': coast_importer(24,12,'..','graphics', 'tilesets','coast'),
            'characters': all_character_import('..','graphics','characters')
        }

    def setup(self, tmx_map, player_start_pos):
        #terrain 
        for layer in ['Terrain','Terrain Top']:
            for x,y,surf in tmx_map.get_layer_by_name(layer).tiles():
                Sprite((x * TILE_SIZE,y * TILE_SIZE), surf, self.all_sprites, WORLD_LAYERS['bg'])

        #water
        for obj in tmx_map.get_layer_by_name('Water'):
            for x in range(int(obj.x), int(obj.x + obj.width), TILE_SIZE):
                for y in range(int(obj.y), int(obj.y + obj.height), TILE_SIZE):
                    AnimatedSprite((x,y), self.overworld_frames['water'], self.all_sprites,  WORLD_LAYERS['water'])

        # coast
        for obj in tmx_map.get_layer_by_name('Coast'):
            terrain = obj.properties['terrain']
            side = obj.properties['side']
            AnimatedSprite((obj.x, obj.y), self.overworld_frames['coast'][terrain][side], self.all_sprites,  WORLD_LAYERS['bg'])
  
        #objects
        for obj in tmx_map.get_layer_by_name('Objects'):
            if obj.name == "top":
                Sprite((obj.x,obj.y), obj.image, self.all_sprites, WORLD_LAYERS['top'])
            else:
                Sprite((obj.x,obj.y), obj.image, (self.all_sprites, self.collision_sprites))

        # collision Objects
        for obj in tmx_map.get_layer_by_name('Collisions'):
        BorderSprite((obj.x, obj.y), pygame.Surface((obj.width, obj.height)), (self.all_sprites, self.collision_sprites))
        
        #grass sections
        for obj in tmx_map.get_layer_by_name('Monsters'):
            MonsterPatchSprite((obj.x,obj.y), obj.image, self.all_sprites, obj.properties['biome'])

        #entitites
        for obj in tmx_map.get_layer_by_name('Entities'):
            if obj.name == 'Player':
                if obj.properties['pos'] == player_start_pos:
                    self.player = Player(
                        pos= (obj.x, obj.y),
                        frames = self.overworld_frames['characters']['player'], 
                        groups = self.all_sprites,
                        facing_direction=obj.properties['direction']) 
            else:
                Character(
                        pos= (obj.x, obj.y),
                        frames = self.overworld_frames['characters'][obj.properties['graphic']], 
                        groups = (self.all_sprites, self.collision_sprites),
                        facing_direction=obj.properties['direction']) 

    def run(self):
        while True:
            # event loop 
            dt = self.clock.tick() / 1000 #dt will give the diff of current frame and the last frame
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

            # game logic
            self.all_sprites.update(dt)
            self.display_surface.fill("Black")
            self.all_sprites.draw(self.player.rect.center)
            pygame.display.update()
                
if __name__ == '__main__':
    game = Game()
    game.run()

