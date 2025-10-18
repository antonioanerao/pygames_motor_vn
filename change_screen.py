import importlib
import pkgutil
from screens import __path__ as screens_path


class ChangeScreen:
    def __init__(self):
        """
        Inicializa o gerenciador de telas.
        """
        self.screens = self._load_screens()

    def _load_screens(self):
        """
        Percorre a pasta 'screens' e carrega automaticamente todas as classes de tela.
        """
        screens = {}

        for module_info in pkgutil.iter_modules(screens_path):
            module_name = module_info.name
            module = importlib.import_module(f"screens.{module_name}")

            for attr_name in dir(module):
                attr = getattr(module, attr_name)

                if isinstance(attr, type) and attr_name.endswith("Screen"):
                    key = module_name
                    screens[key] = attr()

        return screens

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
        Renderiza a tela atual.
        """
        current_screen = self.screens.get(game_screen)
        if current_screen:
            current_screen.run()
