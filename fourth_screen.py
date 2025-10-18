import pygame
from menu_grid import MenuGrid
import settings
import colors


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

    def run(self, game_screen):
        if game_screen == "fourth_screen":
            self.display_surface.fill(colors.SERINGALLAB_DARK)
            self.display_surface.fill('white', rect=pygame.Rect(settings.WIDTH // 2 - (400 + 20), 550, 835, 100))

            background_image = pygame.image.load('assets/graphics/personagens/hycaro/sprite_01.png').convert_alpha()
            # background_image = pygame.transform.scale(background_image, (settings.WIDTH, settings.HEIGHT + 400))
            self.display_surface.blit(background_image, (0, 50))

            font = pygame.font.Font(None, 40)
            text = font.render('Aqui no Seringal Lab temos muitas inovadoras.', True, 'black')
            text_2 = font.render('Qual quer conhecer primeiro?', True, 'black')
            text_rect = text.get_rect(center=(settings.WIDTH / 2 - 80, 580))
            text_2_rect = text.get_rect(center=(settings.WIDTH / 2 - 80, 610))
            self.display_surface.blit(text, text_rect)
            self.display_surface.blit(text_2, text_2_rect)

            self.menu.draw()
