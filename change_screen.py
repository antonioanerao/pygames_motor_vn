class ChangeScreen:
    def __init__(self, screens):
        """
        screens: dicionário com instâncias das telas (first, second, etc.)
        """
        self.screens = screens

    def handle_event(self, game_screen, event):
        """
        Envia o evento para a tela atual e recebe o próximo estado.
        """
        current_screen = self.screens.get(game_screen)
        if current_screen:
            next_screen = current_screen.handle_event(event, game_screen)
            return next_screen or game_screen
        return game_screen

    def render(self, game_screen):
        """
        Desenha a tela correspondente.
        """
        current_screen = self.screens.get(game_screen)
        if current_screen:
            current_screen.run(game_screen)
