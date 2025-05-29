import pygame


class Button:
    def __init__(self, x, y, width, height, color, text, text_color, image_path=None):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color
        self.text = text
        self.text_color = text_color
        self.font = pygame.font.Font(None, 36)
        self.image_path = image_path

    def draw(self, screen):
        if self.image_path:
            screen.blit(pygame.image.load(self.image_path), self.rect)
        else:
            pygame.draw.rect(screen, self.color, self.rect)
            text_surface = self.font.render(self.text, True, self.text_color)
            text_rect = text_surface.get_rect(center=self.rect.center)
            screen.blit(text_surface, text_rect)
        
        pygame.draw.rect(screen, (0, 0, 0), self.rect, 1)

    def is_clicked(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            return self.rect.collidepoint(event.pos)
        return False