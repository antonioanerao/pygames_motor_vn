import pygame
from menu_grid import MenuGrid
from utils.screen_helpers import draw_base_screen
import utils.speaker_helpers


class StoryScreen:
    def __init__(self, story_manager):
        self.display_surface = pygame.display.get_surface()
        self.story = story_manager
        self.menu = None
        self.current_scene = None

    def _build_menu_once(self):
        """Cria o menu apenas se ainda não existir ou se a cena mudou."""
        if not self.story.has_choices():
            self.menu = None
            return

        if self.current_scene != self.story.current_scene:
            choices = [c["text"] for c in self.story.get_choices()]
            if choices:
                self.menu = MenuGrid(choices, rows=4, columns=1, font_size=46)
                self.current_scene = self.story.current_scene

    def handle_event(self, event):
        block = self.story.get_block()
        if not block:
            return

        if self.story.has_choices() and self.menu:
            selected = self.menu.handle_event(event)
            if selected is not None:
                choice = self.story.get_choices()[selected]

                if "action" in choice:
                    params = {k: v for k, v in choice.items() if k not in ("text", "action", "next")}
                    self.story.do_action(choice["action"], **params)

                current_scene = self.story.current_scene

                if "next" in choice:
                    next_scene = choice["next"]
                    if next_scene in self.story.data:
                        self.story.goto(next_scene)
                    else:
                        print(f"[WARN] Cena '{next_scene}' não encontrada no JSON.")

                if self.story.current_scene != current_scene:
                    self.menu = None

            return

        if event.type == pygame.KEYDOWN and event.key in (pygame.K_RETURN, pygame.K_SPACE):
            advanced = self.story.next_block()
            if not advanced:
                self.story.goto("first_screen")
            self.menu = None

    def run(self):
        block = self.story.get_block()
        if not block:
            return

        # --- Fundo e retângulo base ---
        draw_base_screen(
            self.display_surface,
            block.get("background", "black"),
            block.get("text", ""),
            block.get("text_2", "")
        )

        utils.speaker_helpers.draw_speaker_area(self.display_surface, block.get("speaker", ""))

        self._build_menu_once()
        if self.menu:
            self.menu.draw()
