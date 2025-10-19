import pygame
import sys
import settings
from story_manager import StoryManager
from story_screen import StoryScreen


def main():
    pygame.init()
    pygame.display.set_caption(settings.TITLE)
    pygame.display.set_mode((settings.WIDTH, settings.HEIGHT))
    clock = pygame.time.Clock()

    story = StoryManager("story/dialogo.json")
    story_screen = StoryScreen(story)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            story_screen.handle_event(event)

        story_screen.run()
        pygame.display.update()
        clock.tick(settings.FPS)


if __name__ == "__main__":
    main()
