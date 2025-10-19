import pygame
import os
import settings


def draw_base_screen(display_surface, bg, text, text_2,
                     rect_width=settings.WIDTH, rect_height=100, rect_offset_y=settings.HEIGHT - 100,
                     text_color='black', rect_color='white'):
    """
    Desenha o plano de fundo (imagem ou cor), a faixa branca e duas linhas de texto centralizadas.

    Args:
        display_surface: superfície principal do pygame.
        bg (str or tuple): caminho da imagem OU nome/código da cor.
        text (str): texto da primeira linha.
        text_2 (str): texto da segunda linha.
        rect_width (int): largura do retângulo branco.
        rect_height (int): altura do retângulo branco.
        rect_offset_y (int): posição Y do retângulo.
        text_color (str or tuple): cor do texto.
        rect_color (str or tuple): cor do retângulo.
    """

    # --- Fundo ---
    if isinstance(bg, str) and os.path.exists(bg):
        # Se for um caminho válido, carrega imagem
        background_image = pygame.image.load(bg).convert()
        background_image = pygame.transform.scale(
            background_image, (settings.WIDTH, settings.HEIGHT)
        )
        display_surface.blit(background_image, (0, 0))
    else:
        # Caso contrário, usa como cor de fundo
        display_surface.fill(bg)

    # --- Retângulo branco ---
    rect_x = 0
    rect = pygame.Rect(rect_x, rect_offset_y, rect_width, rect_height)
    display_surface.fill(rect_color, rect=rect)

    # --- Textos ---
    font = pygame.font.Font(None, 40)
    text_surface = font.render(text, True, text_color)
    text_surface_2 = font.render(text_2, True, text_color)

    text_rect = text_surface.get_rect(x=50, y=settings.HEIGHT * 0.90)
    text_2_rect = text_surface_2.get_rect(x=50, y=settings.HEIGHT * 0.94)

    display_surface.blit(text_surface, text_rect)
    display_surface.blit(text_surface_2, text_2_rect)
