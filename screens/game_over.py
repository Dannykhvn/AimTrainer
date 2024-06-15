import pygame
import os

from components import Button, TextBox

from .base_screen import BaseScreen


class GameOverScreen(BaseScreen):
    def __init__(self, window):
        super().__init__(window)

        # Create buttons
        self.button1 = Button(200, 100, "Play Again", fgcolor=(25, 25, 112))
        self.button1.rect.x = 320
        self.button1.rect.y = 350

        self.button2 = Button(200, 100, "Quit Game", fgcolor=(25, 25, 112))
        self.button2.rect.x = 50
        self.button2.rect.y = 400

        # Add buttons to sprite group
        self.sprites = pygame.sprite.Group()
        self.sprites.add(self.button1, self.button2)

        # Load and scale background image
        bg_path = os.path.join(os.path.dirname(__file__), "gameover.png")
        self.bg_image = pygame.image.load(bg_path)
        self.bg_image = pygame.transform.scale(self.bg_image, self.window.get_size())

    def update(self):
        """
        Updates the sprites based on the persistent data in the game.
        """
        # Reseting cursor to defualt setting and making it visible again
        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
        pygame.mouse.set_visible(True)
        
        
        # Reset score if going back to levels screen
        if self.next_screen == "levels":
            self.persistent["score"] = 0

    def draw(self):
        # Blit the background image onto the surface
        surface = self.window.copy()
        
        # Draw background image
        surface.blit(self.bg_image, (0, 0))

        # Draw a light orange box around the whole edge of the screen
        screen_rect = self.window.get_rect()
        border_rect = pygame.Rect(screen_rect.left, screen_rect.top, screen_rect.width, screen_rect.height)
        pygame.draw.rect(surface, (255, 191, 128), border_rect, 5)

        # Draw a pastel light orange box on the right side of the screen from the bottom to three-quarters up
        orange_box_rect = pygame.Rect(screen_rect.right - 150, screen_rect.bottom - (3*screen_rect.height // 4), 150, 3*screen_rect.height // 4)
        pygame.draw.rect(surface, (255, 191, 128), orange_box_rect)

        # Draw a pastel light blue border around the orange box
        blue_border_rect = orange_box_rect.inflate(5, 5)
        pygame.draw.rect(surface, (204, 229, 255), blue_border_rect, 5)

        # Draw the classic scores
        classic_scores = self.persistent.get("classic_scores", [])
        classic_font = pygame.font.SysFont(None, 20)
        classic_title_surface = classic_font.render("Classic scores:", True, (0, 0, 128))
        classic_title_rect = classic_title_surface.get_rect(center=(orange_box_rect.centerx, orange_box_rect.top + 30))
        surface.blit(classic_title_surface, classic_title_rect)
        for i, score in enumerate(classic_scores):
            score_surface = classic_font.render(str(score), True, (0, 0, 128))
            score_rect = score_surface.get_rect(center=(orange_box_rect.centerx, orange_box_rect.top + 80 + i * 25))
            surface.blit(score_surface, score_rect)

        # Draw the training scores
        training_scores = self.persistent.get("training_scores", [])
        training_font = pygame.font.SysFont(None, 20)
        training_title_surface = training_font.render("Training scores:", True, (0, 0, 128))
        training_title_rect = training_title_surface.get_rect(center=(orange_box_rect.centerx, orange_box_rect.top + 330))
        surface.blit(training_title_surface, training_title_rect)
        for i, score in enumerate(training_scores):
            score_surface = training_font.render(str(score), True, (0, 0, 128))
            score_rect = score_surface.get_rect(center=(orange_box_rect.centerx, orange_box_rect.top + 380 + i * 25))
            surface.blit(score_surface, score_rect)

        # Draw the buttons and textbox
        self.sprites.draw(surface)

        # Set the background color of the buttons to transparent and the text color to navy blue
        for button in self.sprites:
            if isinstance(button, Button):
                button.image.set_colorkey((0, 0, 0))  # Make the background color of the button transparent

        # Blit the new surface onto the main window
        self.window.blit(surface, (0, 0))

        pygame.display.flip()

    def manage_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            self.running = False
            if self.button1.rect.collidepoint(event.pos):
                self.next_screen = "levels"
            elif self.button2.rect.collidepoint(event.pos):
                self.next_screen = None
            