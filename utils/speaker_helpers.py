import pygame
import settings
import colors


def draw_speaker_area(screen, speaker):
    """
    Desenha o nome do Speaker na cena
    Args:
        screen: A tela principal
        speaker: Informacoes sobre o speaker
    """
    if speaker:
        text_surface = draw_speaker_font(speaker)
        text_rect = text_surface.get_rect(x=10, y=settings.HEIGHT * 0.73)

        # fundo translúcido por trás
        padding = 10
        rect_bg = pygame.Surface((text_rect.width + padding, text_rect.height + padding), pygame.SRCALPHA)
        rect_bg.fill((0, 0, 0, 160))
        rect_rect = rect_bg.get_rect(x=5, y=settings.HEIGHT * 0.72)
        screen.blit(rect_bg, rect_rect)

        # texto principal
        screen.blit(text_surface, text_rect)


def draw_speaker_font(speaker, font_name="great-vibes-regular", size=62, color=colors.SERINGALLAB_LIGHT_2):
    font = pygame.font.Font(f"./assets/font/{font_name}.ttf", size)
    return font.render(speaker, True, pygame.Color(color))
