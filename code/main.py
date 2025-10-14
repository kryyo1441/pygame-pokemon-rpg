from settings import *
from pytmx.util_pygame import load_pygame 
from os.path import join

class Game:
    def __init__(self):
        pygame.init()
        self.display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption('pokemon-rpg')

        self.import_assets()
        self.setup(self.tmx_maps['world'], 'house')

    def import_assets(self):
        self.tmx_maps = {'world': load_pygame(join('..', 'data', 'maps', 'world.tmx'))}
    
    def setup(self, tmx_map, player_start_pos):
        for x,y,surf in tmx_map.get_layer_by_name('Terrain').tiles():
            print(x * TILE_SIZE,y * TILE_SIZE, surf)


    def run(self):
        while True:
            # event loop 
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

            # game logic
            pygame.display.update()
                
if __name__ == '__main__':
    game = Game()
    game.run()
