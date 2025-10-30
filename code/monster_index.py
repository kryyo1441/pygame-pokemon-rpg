from settings import *

class MonsterIndex:
    def __init__(self, monsters, fonts):
        self.display_surface = pygame.display.get_surface()
        self.fonts = fonts
        
        #tint surf
        self.tint_surf = pygame.Surface((WINDOW_WIDTH, WINDOW_HEIGHT))
        self.tint_surf.set_alpha(200)


    def update(self, dt):
        #input
        self.display_surface.blit(self.tint_surf, (0,0))
        #display the main screen
        #display the main section

    