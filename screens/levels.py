import pygame
import os

from components.button import Button
from .base_screen import BaseScreen

class LevelScreen(BaseScreen):
    def __init__(self, window):
        super().__init__(window)
        self.sprites = pygame.sprite.Group()

        # Load the clouds image
        clouds_path = os.path.join(os.path.dirname(__file__), "clouds.png")
        self.clouds_image = pygame.image.load(clouds_path)

        # Create the "Exit" button
        self.quit_button = Button(170, 50, "Quit Game", bgcolor=(255, 99, 71), fgcolor=(25, 25, 112))
        self.quit_button.rect.x = self.window.get_width() - self.quit_button.rect.width - 20
        self.quit_button.rect.y = self.window.get_height() - self.quit_button.rect.height - 20

        # Create the "Player 1" button
        self.classic = Button(200, 100, "Classic Mode", bgcolor=(255, 191, 128), fgcolor=(25, 25, 112))
        self.classic.rect.x = 100
        self.classic.rect.y = 350

        # Create the "Player 2" button
        self.training = Button(200, 100, "Training Mode", bgcolor=(255, 191, 128), fgcolor=(25, 25, 112))
        self.training.rect.x = 500
        self.training.rect.y = 350

        # Add the buttons to the sprite group
        self.sprites.add(self.quit_button)
        self.sprites.add(self.classic)
        self.sprites.add(self.training)

    def draw(self):
        # Load the levels background
        img_path = os.path.join(os.path.dirname(__file__), "levelsbackground.png")
        bg_image = pygame.image.load(img_path)
        scaled_bg = pygame.transform.scale(bg_image, self.window.get_size())

        # Create a new surface with the same size as the window
        surface = pygame.Surface(self.window.get_size())

        # Draw the background image
        surface.blit(scaled_bg, (0, 0))

        # Scale the clouds image to the size of the window surface
        scaled_clouds = pygame.transform.scale(self.clouds_image, self.window.get_size())
        surface.blit(scaled_clouds, (0, -350))

        # Load the sun image
        sun_path = os.path.join(os.path.dirname(__file__), "sun.png")
        self.sun_image = pygame.image.load(sun_path)

        # Scale the clouds image to the size of the window surface
        scaled_sun = pygame.transform.scale(self.sun_image, self.window.get_size())
        surface.blit(scaled_sun, (-65, -150))

        # Draw a light orange box around the whole edge of the screen
        screen_rect = self.window.get_rect()
        border_rect = pygame.Rect(screen_rect.left, screen_rect.top, screen_rect.width, screen_rect.height)
        pygame.draw.rect(surface, (255, 215, 165), border_rect, 5)

        # Draw the buttons
        self.sprites.draw(surface)

        # Blit the new surface onto the main window
        self.window.blit(surface, (0, 0))

        pygame.display.flip()

    def manage_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Clicked on the "Quit" button? Quit the game.
            if self.quit_button.rect.collidepoint(event.pos):
                self.running = False
                self.next_screen = None
                self.peristent = {}

            # Clicked on the "Classic" button? Start the "Classic" level.
            if self.classic.rect.collidepoint(event.pos):
                self.running = False
                self.next_screen = "game"
                self.persistent["level"] = "classic"
                self.persistent["score"] = 0
                
            # Clicked on the "Training" button? Start the "Classic" level.
            if self.training.rect.collidepoint(event.pos):
                self.running = False
                self.next_screen = "train"
                self.persistent["level"] = "training"
                self.persistent["score"] = 0