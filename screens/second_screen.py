import pygame
import sys
from menu_grid import MenuGrid
from utils.screen_helpers import draw_base_screen
import colors


class SecondScreen:
    def __init__(self):
        self.display_surface = pygame.display.get_surface()

        self.menu = MenuGrid([
            "<- Voltar",
            "Tela 03",
        ])

    def handle_event(self, event, game_screen):
        selected = self.menu.handle_event(event)

        if selected is not None:
            if selected == 0:
                return "first_screen"
            elif selected == 1:
                return "third_screen"
            elif selected == 2:
                pygame.quit()
                sys.exit()

    def run(self):
        """
        Desenha a tela com fundo de cor sólida e menu de opções.
        Args:
            game_screen: nome da tela atual (não utilizado aqui).
        Returns:
            None
        """
        draw_base_screen(
            self.display_surface,
            colors.SERINGALLAB_DARK,
            "Bla bla bla",
            "Escolha uma opção do menu abaixo"
        )

        self.menu.draw()
