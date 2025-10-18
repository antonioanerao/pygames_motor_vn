import pygame
import sys
from menu_grid import MenuGrid


class ThirdScreen:
    def __init__(self):
        self.display_surface = pygame.display.get_surface()

        self.menu = MenuGrid([
            "1) Tela 01",
            "2) Tela 02",
        ])

    def handle_event(self, event, game_screen):
        selected = self.menu.handle_event(event)

        if selected is not None:
            if selected == 0:
                return "first_screen"
            elif selected == 1:
                return "second_screen"
            elif selected == 2:
                pygame.quit()
                sys.exit()

    def run(self, game_screen):
        """
        Renders the third screen if the current game screen is 'third_screen'.
        Args:
            game_screen (str): The current game screen identifier.
        Returns:
            None
        """
        if game_screen == 'third_screen':
            self.display_surface.fill('pink')
            self.display_surface.fill('white', rect=pygame.Rect(100, 100, 600, 400))
            font = pygame.font.Font(None, 74)
            text = font.render('Terceira tela', True, 'black')
            text_2 = font.render('Aperte BACKSPACE para voltar', True, 'black')
            text_rect = text.get_rect(center=(400, 300))
            text_rect_2 = text_2.get_rect(center=(400, 370))
            text_3 = font.render('Aperte SPACE para sair', True, 'black')
            text_rect_3 = text_3.get_rect(center=(400, 440))
            self.display_surface.blit(text, text_rect)
            self.display_surface.blit(text_2, text_rect_2)
            self.display_surface.blit(text_3, text_rect_3)

            self.menu.draw()
