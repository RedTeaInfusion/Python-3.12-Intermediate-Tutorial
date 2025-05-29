import pygame
from button import Button
from constants import WIDTH, HEIGHT, WHITE, BLACK, DARK_GREY, RED

class MessageBox:
    def __init__(self, screen, message, sub_message):
        self.screen = screen
        self.message = message
        self.sub_message = sub_message
        self.box_width = 400
        self.box_height = 200
        self.box_x = (WIDTH - self.box_width) // 2
        self.box_y = (HEIGHT - self.box_height) // 2
        self.font = pygame.font.SysFont('Verdana', 48)
        self.sub_font = pygame.font.SysFont('Verdana', 36)
        self.button_ok = Button(self.box_x + self.box_width // 2 - 50, self.box_y +self.box_height // 2 + 50, 100, 50, RED, "OK", BLACK, '')

    def draw(self):
        # Draw the border and the box
        pygame.draw.rect(self.screen, WHITE, (self.box_x - 5, self.box_y - 5, self.box_width + 10, self.box_height + 10), 10)
        pygame.draw.rect(self.screen, DARK_GREY, (self.box_x, self.box_y, self.box_width, self.box_height))

        # Render the text and calculate its position
        text_surface = self.font.render(self.message, True, WHITE)
        sub_text_surface = self.sub_font.render(self.sub_message, True, WHITE)
        text_rect = text_surface.get_rect(center=(self.box_x + self.box_width // 2, self.box_y + self.box_height // 3))
        sub_text_rect = sub_text_surface.get_rect(center=(self.box_x + self.box_width // 2, self.box_y + 2 * self.box_height // 3))

        # Blit the text to the screen
        self.screen.blit(text_surface, text_rect)
        self.screen.blit(sub_text_surface, sub_text_rect)

        # Draw the OK button
        self.button_ok.draw(self.screen)

    def handle_interaction(self):
        # Handle the message box interaction
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return False
                elif event.type == pygame.MOUSEBUTTONDOWN and self.button_ok.is_clicked(event):
                    return True

    def show(self):
        # Call draw and handle interaction
        self.draw()
        pygame.display.flip()
        return self.handle_interaction()
