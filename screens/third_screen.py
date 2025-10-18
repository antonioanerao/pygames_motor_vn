import pygame
from menu_grid import MenuGrid
from utils.screen_helpers import draw_base_screen


class ThirdScreen:
    def __init__(self):
        self.display_surface = pygame.display.get_surface()

        self.menu = MenuGrid([
            "1) <-- Voltar",
            "2) Tela 02",
        ])

    def handle_event(self, event, game_screen):
        selected = self.menu.handle_event(event)

        if selected is not None:
            if selected == 0:
                return "first_screen"
            elif selected == 1:
                return "second_screen"

    def run(self):
        draw_base_screen(
            self.display_surface,
            (200, 200, 250),
            "Tela 03",
            "Escolha uma opção do menu abaixo"
        )

        self.menu.draw()
