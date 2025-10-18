import pygame
from menu_grid import MenuGrid
import colors
from utils.screen_helpers import draw_base_screen


class FourthScreen:
    def __init__(self):
        self.display_surface = pygame.display.get_surface()

        self.menu = MenuGrid([
            "1) Ouvir sobre o Bora!",
            "2) Ouvir sobre o Simplifica",
            "3) Ouvir sobre o TranscreveAI",
            "4) Voltar"
        ])

    def handle_event(self, event, game_screen):
        selected = self.menu.handle_event(event)
        print(selected)

    def run(self):
        draw_base_screen(
            self.display_surface,
            colors.SERINGALLAB_LIGHT_3,
            "Conheça nossas Iniciativas!",
            "Selecione uma das opções abaixo para saber mais."
        )

        self.menu.draw()
