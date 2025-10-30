from settings import *

class MonsterIndex:
    def __init__(self, monsters, fonts):
        self.display_surface = pygame.display.get_surface()
        self.fonts = fonts
        
        #tint surf
        self.tint_surf = pygame.Surface((WINDOW_WIDTH, WINDOW_HEIGHT))
        self.tint_surf.set_alpha(200)


       #dimension
        self.main_rect = pygame.FRect(0,0, WINDOW_WIDTH * 0.6, WINDOW_HEIGHT * 0.8).move_to(center = (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2))

    def update(self, dt):
        #input
        self.display_surface.blit(self.tint_surf, (0,0))
        pygame.draw.rect(self.display_surface, 'black' , self.main_rect)
        #display the main screen
        #display the main section

    