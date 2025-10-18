import pygame


class SecondScreen:
    def __init__(self):
        self.display_surface = pygame.display.get_surface()

    def handle_event(self, event, game_screen):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                game_screen = 'first_screen'
        return game_screen

    def run(self, game_screen):
        """
        Renders the second screen if the current game screen is 'second_screen'.
        Args:
            game_screen (str): The current game screen identifier.
        Returns:
            None
        """
        if game_screen == 'second_screen':
            self.display_surface.fill('green')
            self.display_surface.fill('white', rect=pygame.Rect(100, 100, 600, 400))
            font = pygame.font.Font(None, 74)
            text = font.render('Segunda Tela', True, 'black')
            text_2 = font.render('Aperte BACKSPACE para voltar', True, 'black')
            text_rect = text.get_rect(center=(400, 300))
            text_rect_2 = text_2.get_rect(center=(400, 370))
            self.display_surface.blit(text, text_rect)
            self.display_surface.blit(text_2, text_rect_2)
