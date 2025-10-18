import pygame
import sys
from menu_grid import MenuGrid
from utils.screen_helpers import draw_base_screen


class FirstScreen:
    def __init__(self):
        self.display_surface = pygame.display.get_surface()

        # Quatro opções no menu
        self.menu = MenuGrid([
            "1) Opcao 01 (em breve)",
            "2) Opcao 02 (em breve)",
            "3) Conhecer Iniciativas",
            "4) Sair"
        ])

    def handle_event(self, event, game_screen):
        selected = self.menu.handle_event(event)

        if selected is not None:
            if selected == 0:
                return "second_screen"
            elif selected == 1:
                return "third_screen"
            elif selected == 2:
                return "fourth_screen"
            elif selected == 3:
                pygame.quit()
                sys.exit()

        return game_screen

    def run(self):
        draw_base_screen(
            self.display_surface,
            "assets/graphics/personagens_seringal.png",
            "Somos os Guerreiros da Inovação.",
            "Qual caminho vamos trilhar primeiro?"
        )

        self.menu.draw()
