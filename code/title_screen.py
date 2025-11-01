import pygame
from os.path import join

class TitleScreen:
    def __init__(self):
        self.display_surface = pygame.display.get_surface()
        self.font = pygame.font.Font(join('..', 'graphics', 'fonts', 'PixeloidSans.ttf'), 64)
        self.button_font = pygame.font.Font(join('..', 'graphics', 'fonts', 'PixeloidSans.ttf'), 32)
        
        # Title
        self.title = self.font.render('Pokemon RPG', True, 'white')
        self.title_rect = self.title.get_rect(center=(self.display_surface.get_width() // 2, 200))
        
        # Buttons
        self.play_text = self.button_font.render('Play', True, 'white')
        self.play_rect = self.play_text.get_rect(center=(self.display_surface.get_width() // 2, 400))
        
        self.exit_text = self.button_font.render('Exit', True, 'white')
        self.exit_rect = self.exit_text.get_rect(center=(self.display_surface.get_width() // 2, 500))
        
        # Button states
        self.play_hovered = False
        self.exit_hovered = False
        
    def handle_input(self):
        mouse_pos = pygame.mouse.get_pos()
        mouse_clicked = pygame.mouse.get_pressed()[0]  # Left click
        
        # Check play button
        self.play_hovered = self.play_rect.collidepoint(mouse_pos)
        if self.play_hovered and mouse_clicked:
            return 'play'
            
        # Check exit button
        self.exit_hovered = self.exit_rect.collidepoint(mouse_pos)
        if self.exit_hovered and mouse_clicked:
            return 'exit'
            
        return None
        
    def draw(self):
        self.display_surface.fill('black')
        
        # Draw title
        self.display_surface.blit(self.title, self.title_rect)
        
        # Draw buttons with hover effect
        play_color = (200, 200, 200) if self.play_hovered else 'white'
        exit_color = (200, 200, 200) if self.exit_hovered else 'white'
        
        play_text = self.button_font.render('Play', True, play_color)
        exit_text = self.button_font.render('Exit', True, exit_color)
        
        self.display_surface.blit(play_text, self.play_rect)
        self.display_surface.blit(exit_text, self.exit_rect)