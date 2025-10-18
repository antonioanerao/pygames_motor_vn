import pygame
import sys
import settings
from menu_grid import MenuGrid


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

    def run(self, game_screen):
        if game_screen == "first_screen":

            background_image = pygame.image.load('assets/graphics/personagens_seringal.png').convert()
            background_image = pygame.transform.scale(background_image, (settings.WIDTH, settings.HEIGHT + 400))
            self.display_surface.blit(background_image, (0, -400))

            self.display_surface.fill('white', rect=pygame.Rect(settings.WIDTH // 2 - (400 + 20), 550, 835, 100))
            font = pygame.font.Font(None, 40)
            text = font.render('Somos os Guerreiros da Inovação.', True, 'black')
            text_2 = font.render('Qual caminhos vamos trilhar primeiro?', True, 'black')
            text_rect = text.get_rect(center=(settings.WIDTH / 2, 580))
            text_2_rect = text.get_rect(center=(settings.WIDTH / 2, 610))
            self.display_surface.blit(text, text_rect)
            self.display_surface.blit(text_2, text_2_rect)

            self.menu.draw()
