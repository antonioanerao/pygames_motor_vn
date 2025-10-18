import pygame
import sys
import settings
import colors


class FirstScreen:
    def __init__(self):
        self.display_surface = pygame.display.get_surface()
        self.font = pygame.font.Font(None, 50)

        # Quatro opções no menu
        self.options = [
            "1) Tela 02",
            "2) Tela 03",
            "3) Tela 04 (em breve)",
            "4) Sair"
        ]

        # Controle da seleção (índice de 0 a 3)
        self.selected_option = 0

        # Layout da grade
        self.columns = 2
        self.rows = 2

        # calcula a largura real da maior string, em pixels
        max_width = 0
        for text in self.options:
            width, _ = self.font.size(text)
            if width > max_width:
                max_width = width

        # Dimensões dos retângulos
        self.rect_width = max_width + 60
        self.rect_height = 80
        self.spacing_x = self.rect_width + 40  # espaço horizontal entre colunas
        self.spacing_y = 100  # espaço vertical entre linhas
        self.start_x = settings.WIDTH // 2 - (self.rect_width + 20)
        self.start_y = settings.HEIGHT - self.rect_height * self.rows - 100

    def handle_event(self, event, game_screen):
        if event.type == pygame.KEYDOWN:
            # Movimento na horizontal
            if event.key == pygame.K_RIGHT:
                # move 1 posição à direita se não estiver na última coluna
                if (self.selected_option % self.columns) < self.columns - 1:
                    self.selected_option += 1
            elif event.key == pygame.K_LEFT:
                # move 1 posição à esquerda se não estiver na primeira coluna
                if (self.selected_option % self.columns) > 0:
                    self.selected_option -= 1

            # Movimento na vertical
            elif event.key == pygame.K_DOWN:
                # move uma linha pra baixo se existir próxima linha
                if self.selected_option + self.columns < len(self.options):
                    self.selected_option += self.columns
            elif event.key == pygame.K_UP:
                # move uma linha pra cima se existir anterior
                if self.selected_option - self.columns >= 0:
                    self.selected_option -= self.columns

            # Confirmação
            elif event.key in [pygame.K_RETURN, pygame.K_SPACE]:
                if self.selected_option == 0:
                    return "second_screen"
                elif self.selected_option == 1:
                    return "third_screen"
                elif self.selected_option == 2:
                    print("Mostrar créditos...")
                elif self.selected_option == 3:
                    pygame.quit()
                    sys.exit()

        return game_screen

    def run(self, game_screen):
        self.display_surface.fill(colors.SERINGALLAB_DARK)
        self.display_surface.fill('white', rect=pygame.Rect(settings.WIDTH // 2 - (self.rect_width + 20), 145, 835, 100))
        font = pygame.font.Font(None, 74)
        text = font.render('Seringal Lab', True, 'black')
        text_rect = text.get_rect(center=(settings.WIDTH / 2, 200))
        self.display_surface.blit(text, text_rect)

        for i, text in enumerate(self.options):
            # Calcula a linha e coluna do item (0 a 1)
            row = i // self.columns
            col = i % self.columns

            # Calcula posição com base na linha/coluna
            rect_x = self.start_x + col * self.spacing_x
            rect_y = self.start_y + row * self.spacing_y

            rect = pygame.Rect(rect_x, rect_y, self.rect_width, self.rect_height)

            # Cor diferente para a opção selecionada
            color = colors.SERINGALLAB_LIGHT_2 if i == self.selected_option else "gray"
            pygame.draw.rect(self.display_surface, color, rect, border_radius=8)

            # Texto centralizado no retângulo
            text_surface = self.font.render(text, True, (0, 0, 0))
            text_rect = text_surface.get_rect(midleft=(rect.x + 20, rect.centery))
            self.display_surface.blit(text_surface, text_rect)
