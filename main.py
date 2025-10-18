import pygame
import sys
import settings
from first_screen import FirstScreen
from second_screen import SecondScreen
from third_screen import ThirdScreen
from fourth_screen import FourthScreen
from change_screen import ChangeScreen


class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(settings.TITLE)
        self.screen = pygame.display.set_mode((int(settings.WIDTH), int(settings.HEIGHT)))
        self.clock = pygame.time.Clock()
        self.screens = {
            "first_screen": FirstScreen(),
            "second_screen": SecondScreen(),
            "third_screen": ThirdScreen(),
            "fourth_screen": FourthScreen()
        }
        self.change_screen = ChangeScreen(self.screens)

    def run(self):
        game_screen = "first_screen"

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                game_screen = self.change_screen.handle_event(game_screen, event)

            self.change_screen.render(game_screen)

            pygame.display.update()
            self.clock.tick(int(settings.FPS))


if __name__ == '__main__':
    game = Game()
    game.run()
