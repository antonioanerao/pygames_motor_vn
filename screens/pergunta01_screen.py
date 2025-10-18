import pygame
import sys
from menu_grid import MenuGrid
import colors
from utils.screen_helpers import draw_base_screen


class Pergunta01Screen:
    def __init__(self):
        self.display_surface = pygame.display.get_surface()

        # Quatro opções no menu
        self.menu = MenuGrid([
            "1) Testar ideias sem medo de errar",
            "2) Esperar o momento perfeito",
            "3) Repetir o que já funciona",
            "4) Evitar mudanças bruscas"
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
            colors.SERINGALLAB_DARK,
            "Qual atitude representa melhor a inovação?",
            "Escolha uma opção abaixo"
        )

        imagem_01 = pygame.image.load("assets/graphics/personagens/hycaro/sprite_01.png").convert_alpha()
        self.display_surface.blit(imagem_01, (-100, 110))

        self.menu.draw()
