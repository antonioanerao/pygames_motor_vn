import pygame
import settings


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
        self.start_x = start_x or settings.WIDTH // 2 - (self.rect_width + 20)
        self.start_y = start_y or settings.HEIGHT - self.rect_height * self.rows - 40

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
                return self.selected_option  # retorna o índice da opção selecionada
        return None

    # --- Desenho do menu ---
    def draw(self, highlight_color="#b9eb2e", normal_color="#3c7170", text_color="#ffffff"):
        for i, text in enumerate(self.options):
            row = i // self.columns
            col = i % self.columns

            rect_x = self.start_x + col * self.spacing_x
            rect_y = self.start_y + row * self.spacing_y
            rect = pygame.Rect(rect_x, rect_y, self.rect_width, self.rect_height)

            color = pygame.Color(highlight_color if i == self.selected_option else normal_color)
            pygame.draw.rect(self.display_surface, color, rect, border_radius=6)

            text_surface = self.font.render(text, True, pygame.Color(text_color))
            text_rect = text_surface.get_rect(midleft=(rect.x + 20, rect.centery))
            self.display_surface.blit(text_surface, text_rect)
