from settings import *
from pytmx.util_pygame import load_pygame 
from os.path import join

class Game:
    def __init__(self):
        pygame.init()
        self.display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption('pokemon-rpg')

        self.import_assets()

    def import_assets(self):
        self.tmx_maps = {'world': load_pygame(join('..', 'data', 'maps', 'world.tmx'))}
        print(self.tmx_maps)

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
