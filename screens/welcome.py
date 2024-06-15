import pygame
import os
import sys

from components.button import Button
# from components.textbox import TextBox
from .base_screen import BaseScreen


# sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

class WelcomeScreen(BaseScreen):
    def __init__(self, window):
        super().__init__(window)
        self.sprites = pygame.sprite.Group()

        # Load the game title image
        img_path = os.path.join(os.path.dirname(__file__), "clickbot.png")
        self.image = pygame.image.load(img_path)
        self.title_rect = self.image.get_rect()
        self.title_rect.x = (self.window.get_width() - self.title_rect.width) // 2
        self.title_rect.y = 50

        # Create the "Play" button
        self.button1 = Button(200, 100, "Play Game", bgcolor=(255, 191, 128), fgcolor=(25, 25, 112))
        self.button1.rect.x = 300 # was 100
        self.button1.rect.y = 525

        # Create the "Exit" button
        self.button_exit = Button(170, 50, "Quit Game", bgcolor=(255, 99, 71), fgcolor=(25, 25, 112))
        self.button_exit.rect.x = self.window.get_width() - self.button_exit.rect.width - 20
        self.button_exit.rect.y = self.window.get_height() - self.button_exit.rect.height - 20

        # Add the buttons to the sprite group
        self.sprites.add(self.button1)
        # self.sprites.add(self.button2)
        self.sprites.add(self.button_exit)
        
        

    def draw(self):        
        # Load your PNG image and scale it to the size of the window
        bg_path = os.path.join(os.path.dirname(__file__), "welcome_background.png")
        bg_image = pygame.image.load(bg_path)
        scaled_bg = pygame.transform.scale(bg_image, self.window.get_size())

        # Create a new surface with the same size as the window
        surface = pygame.Surface(self.window.get_size())

        # Blit the scaled image onto the surface
        surface.blit(scaled_bg, (0, 0))
        
        # Load the clouds image
        clouds_path = os.path.join(os.path.dirname(__file__), "clouds.png")
        self.clouds_image = pygame.image.load(clouds_path)

        # Scale the clouds image to the size of the window surface
        scaled_clouds = pygame.transform.scale(self.clouds_image, self.window.get_size())
        surface.blit(scaled_clouds, (0, -115))
        
        # Load the sun image
        sun_path = os.path.join(os.path.dirname(__file__), "sun.png")
        self.sun_image = pygame.image.load(sun_path)

        # Scale the clouds image to the size of the window surface
        scaled_sun = pygame.transform.scale(self.sun_image, self.window.get_size())
        surface.blit(scaled_sun, (-65, 300))

        # Draw a light orange box around the whole edge of the screen
        screen_rect = self.window.get_rect()
        border_rect = pygame.Rect(screen_rect.left, screen_rect.top, screen_rect.width, screen_rect.height)
        pygame.draw.rect(surface, (255, 215, 165), border_rect, 5)

        # Draw a light orange box behind the image
        box_rect = pygame.Rect(self.title_rect.left - 10, self.title_rect.top - 10, self.title_rect.width + 20, self.title_rect.height + 20)
        pygame.draw.rect(surface, (255, 215, 165), box_rect)
        
        # Draw the game title
        self.title_rect.x = (self.window.get_width() - self.title_rect.width) // 2
        self.title_rect.y = 50
        surface.blit(self.image, self.title_rect)

        # Draw the border line on top of the box
        pygame.draw.rect(surface, (255, 191, 128), box_rect, 3)

        # Draw the text below the image
        font = pygame.font.SysFont(None, 25)
        text_color = (0, 0, 128) # Navy blue color
        text_surface = font.render('Art and Code Created By: Maia Bell & Danny Khavin', True, text_color)
        text_rect = text_surface.get_rect()
        text_rect.centerx = self.title_rect.centerx # Center the text horizontally
        text_rect.top = self.title_rect.bottom + 40 # Position the text below the image

        # Draw a light orange underline under the text
        underline_rect = pygame.Rect(text_rect.left, text_rect.bottom + 5, text_rect.width, 3)
        pygame.draw.rect(surface, (255, 191, 128), underline_rect)

        surface.blit(text_surface, text_rect)

        text_surface2 = font.render('Test your speed and accuracy with the ClickBot aim training game!', True, text_color)
        text_rect2 = text_surface2.get_rect()
        text_rect2.centerx = self.title_rect.centerx # Center the text horizontally
        text_rect2.top = text_rect.bottom + 80 # Position the text below the first text

        # Draw a light orange underline under the text
        underline_rect2 = pygame.Rect(text_rect2.left, text_rect2.bottom + 5, text_rect2.width, 3)
        pygame.draw.rect(surface, (255, 191, 128), underline_rect2)

        surface.blit(text_surface2, text_rect2)

        # Draw the buttons
        self.sprites.draw(surface)

        # Blit the new surface onto the main window
        self.window.blit(surface, (0, 0))
        
        pygame.display.flip()


    def manage_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Clicked on the "Play" button? Go to the next screen.
            if self.button1.rect.collidepoint(event.pos):
                self.running = False
                self.next_screen = "levels"
                self.persistent["player"] = 1

            # Clicked on the "Exit" button? Quit the game.
            if self.button_exit.rect.collidepoint(event.pos):
                self.running = False
                self.next_screen = None
                self.persistent = {}