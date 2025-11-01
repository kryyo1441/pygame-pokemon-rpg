import pygame
from os.path import join

class GameOverScreen:
    def __init__(self):
        self.display_surface = pygame.display.get_surface()
        self.font = pygame.font.Font(join('..', 'graphics', 'fonts', 'PixeloidSans.ttf'), 64)
        self.button_font = pygame.font.Font(join('..', 'graphics', 'fonts', 'PixeloidSans.ttf'), 32)
        
        # Game Over Text
        self.title = self.font.render('Game Over', True, 'red')
        self.title_rect = self.title.get_rect(center=(self.display_surface.get_width() // 2, 200))
        
        # Buttons
        self.play_again_text = self.button_font.render('Play Again', True, 'white')
        self.play_again_rect = self.play_again_text.get_rect(center=(self.display_surface.get_width() // 2, 400))
        
        self.exit_text = self.button_font.render('Exit', True, 'white')
        self.exit_rect = self.exit_text.get_rect(center=(self.display_surface.get_width() // 2, 500))
        
        # Button states
        self.play_again_hovered = False
        self.exit_hovered = False
        
    def handle_input(self):
        mouse_pos = pygame.mouse.get_pos()
        mouse_clicked = pygame.mouse.get_pressed()[0]  # Left click
        
        # Check play again button
        self.play_again_hovered = self.play_again_rect.collidepoint(mouse_pos)
        if self.play_again_hovered and mouse_clicked:
            return 'play_again'
            
        # Check exit button
        self.exit_hovered = self.exit_rect.collidepoint(mouse_pos)
        if self.exit_hovered and mouse_clicked:
            return 'exit'
            
        return None
        
    def draw(self):
        self.display_surface.fill('black')
        
        # Draw game over text
        self.display_surface.blit(self.title, self.title_rect)
        
        # Draw buttons with hover effect
        play_again_color = (200, 200, 200) if self.play_again_hovered else 'white'
        exit_color = (200, 200, 200) if self.exit_hovered else 'white'
        
        play_again_text = self.button_font.render('Play Again', True, play_again_color)
        exit_text = self.button_font.render('Exit', True, exit_color)
        
        self.display_surface.blit(play_again_text, self.play_again_rect)
        self.display_surface.blit(exit_text, self.exit_rect)