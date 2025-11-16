import pygame
import time
import settings
import colors

from pygame._sdl2 import controller

controller.init()

for i in range(controller.get_count()):
    c = controller.Controller(i)
    print("Nome:", c.name)


class MenuGrid:
    def __init__(self, options, start_x=None, start_y=None, rows=2, columns=2, font_size=50):
        self.display_surface = pygame.display.get_surface()
        self.font = pygame.font.Font(None, font_size)

        # Lista de opções (strings)
        self.options = options

        # Controle da seleção
        self.selected_option = 0

        # Layout da grade
        self.columns = columns
        self.rows = rows

        # Cálculo automático da largura dos retângulos
        max_width = max(self.font.size(text)[0] for text in self.options)
        self.rect_width = max_width + 60
        self.rect_height = 50
        self.spacing_x = self.rect_width + 40
        self.spacing_y = 70

        # Posição inicial (centro por padrão)
        self.start_x = settings.WIDTH * 0.95 - (self.rect_width * self.columns)
        vertical_factor = 0.6 + (1 / (self.rows + 1)) * 0.25
        self.start_y = settings.HEIGHT * vertical_factor - (self.rect_height * self.rows) / 2

        self.last_move_time = 0
        self.move_delay = 0.25

    # --- Entrada do usuário ---
    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                if (self.selected_option % self.columns) < self.columns - 1:
                    self.selected_option += 1
            elif event.key == pygame.K_LEFT:
                if (self.selected_option % self.columns) > 0:
                    self.selected_option -= 1
            elif event.key == pygame.K_DOWN:
                if self.selected_option + self.columns < len(self.options):
                    self.selected_option += self.columns
            elif event.key == pygame.K_UP:
                if self.selected_option - self.columns >= 0:
                    self.selected_option -= self.columns
            elif event.key in [pygame.K_RETURN, pygame.K_SPACE]:
                return self.selected_option

        if event.type == pygame.JOYBUTTONDOWN:
            if event.button == 0:  # Botão A
                return self.selected_option
            if event.button == 11:
                if self.selected_option - self.columns >= 0:
                    self.selected_option -= self.columns
            if event.button == 12:
                if self.selected_option + self.columns < len(self.options):
                    self.selected_option += self.columns

        # --- ANALÓGICO ESQUERDO ---
        elif event.type == pygame.JOYAXISMOTION:
            current_time = time.time()

            if current_time - self.last_move_time > self.move_delay:
                if event.axis == 1:
                    if event.value > 0.5:
                        if self.selected_option + self.columns < len(self.options):
                            self.selected_option += self.columns
                        self.last_move_time = current_time
                    elif event.value < -0.5:
                        if self.selected_option - self.columns >= 0:
                            self.selected_option -= self.columns

        return None

    def draw(self,
             highlight_color=colors.SERINGALLAB_DARK,
             normal_color=colors.SERINGALLAB_LIGHT_3,
             text_color=colors.WHITE):
        for i, text in enumerate(self.options):
            row = i // self.columns
            col = i % self.columns

            rect_x = self.start_x + col * self.spacing_x
            rect_y = self.start_y + row * self.spacing_y

            color = pygame.Color(highlight_color if i == self.selected_option else normal_color)
            rect = pygame.Rect(rect_x, rect_y, self.rect_width, self.rect_height)

            box_surface = pygame.Surface((self.rect_width, self.rect_height), pygame.SRCALPHA)
            rgba_color = (*color[:3], 230)
            pygame.draw.rect(box_surface, rgba_color, box_surface.get_rect(), border_radius=16)

            pygame.draw.rect(box_surface,
                             (*pygame.Color(highlight_color)[:3], 255),
                             box_surface.get_rect(),
                             width=3,
                             border_radius=16)

            self.display_surface.blit(box_surface, (rect_x, rect_y))

            text_surface = self.font.render(text, True, pygame.Color(text_color))
            text_rect = text_surface.get_rect(midleft=(rect.x + 20, rect.centery))
            self.display_surface.blit(text_surface, text_rect)
