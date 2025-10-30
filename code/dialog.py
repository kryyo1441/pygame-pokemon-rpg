from settings import *

class DialogTree:
    def __init__(self, character, player, all_sprites, font):
        self.player = player
        self.character = character
        self.font = font
        self.all_sprites = all_sprites
        self.dialog = character.get_dialog()
        self.dialog_num = len(self.dialog)
        self.dialog_index = 0
        self.current_dialog = DialogSprite(self.dialog[self.dialog_index], self.character, self.all_sprites, self.font)

class DialogSprite(pygame.sprite.Sprite):
    def __init__(self, message, character, groups, font):
        
        super().__init__(groups)
        self.z = WORLD_LAYERS['top']
        
        # text
        text_surf = font.render(message, False, COLORS['black'])
        padding = 5
        width = max(30, text_surf.get_width() + padding * 2)
        height = text_surf.get_height() + padding * 2

        # background
        surf = pygame.Surface((width, height))
        surf.fill(COLORS['pure white'])
        surf.blit(text_surf, text_surf.get_rect(center = (width / 2, height / 2)))
        
        # sprite setup
        self.image = surf
        self.rect = self.image.get_rect(midbottom = character.rect.midtop + vector(0, -10))

