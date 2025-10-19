import pygame
import settings
import colors


def draw_dialog_box(display_surface, rect_offset_y, rect_width=settings.WIDTH, rect_height=220, padding=5):
    rect = pygame.Rect(0, rect_offset_y, rect_width, rect_height)

    box_surface = pygame.Surface((rect_width, rect_height), pygame.SRCALPHA)
    inner_rect = pygame.Rect(
        padding,
        padding,
        rect_width - padding * 2,
        rect_height - padding * 2
    )

    pygame.draw.rect(box_surface, (255, 255, 255, 150), inner_rect, border_radius=16)
    pygame.draw.rect(box_surface, colors.SERINGALLAB_DARK, inner_rect, 3, border_radius=16)

    display_surface.blit(box_surface, rect)
