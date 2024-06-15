import pygame
import os
import time
from components import TextBox, Shape
from .base_screen import BaseScreen
from screens.game_over import GameOverScreen

class GameScreen(BaseScreen):
    """
    This class represents the game screen.

    Attributes:
    - target_image (pygame.surface): The image of the target.
    - target_rect (pygame.rect): The rectangle that bounds the target.
    - target (Shape): The target shape.
    - score (int): The score of the player.
    - score_box (TextBox): The box that displays the score.
    - last_move_time (float): The time when the target was last moved.
    - start_time (float): The time when the game started.
    - time_limit (int): The time limit of the game.
    - time_remaining (int): The time remaining in the game.
    - countdown_box (TextBox): The box that displays the time remaining.
    """
    
    def __init__(self, window):
        super().__init__(window)

        # Load and scale the target image
        target_img_path = os.path.join(os.path.dirname(__file__), "target.png")
        target_image = pygame.image.load(target_img_path)
        self.target_image = pygame.transform.scale(target_image, (50, 50)) 

        # Create target rectangle
        self.target_rect = self.target_image.get_rect()
        self.target = Shape(self.target_rect.size, limits=self.window.get_size())
        self.target.image = self.target_image

        # Initialize score box
        self.score = 0
        self.score_box = TextBox("Score: " + str(self.score), pos=(30, 750), size=(150, 30))
        
        # Initialize target movement timer
        self.last_move_time = time.time()
    
        # Initialize countdown box
        self.start_time = None
        self.time_limit = 10
        self.time_remaining = self.time_limit
        self.countdown_box = TextBox("Time remaining: " + str(self.time_remaining), pos=(470, 750), size=(300, 30))
        
    def reset_score(self):
        """Resets the score to zero"""
        self.score = 0
        
    def update(self):
        """Update the game state, checking for collisions and updating game objects"""
       
        # Start the countdown timer
        if self.start_time is None:
            self.start_time = time.time()
            
        # Check for target-click collision
        mouse_pos = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if self.target.rect.collidepoint(mouse_pos) and click[0] == 1:
            # Increment the score and move the square to a new position
            self.score += 1
            self.target.set_random_position()
            
        # Move the Target every 3 seconds
        current_time = time.time()
        if current_time - self.last_move_time >= 3:
            self.target.set_random_position()
            self.last_move_time = current_time

        # Update score box
        self.score_box.set_text("Score: " + str(self.score))
        self.score_box.update()

        # Update countdown box
        elapsed_time = time.time() - self.start_time
        self.time_remaining = max(0, self.time_limit - int(elapsed_time))
        
        # Check if time_remaining is 0 or less and switch screens
        if self.time_remaining <= 0:
            self.persistent["classic_scores"].append(self.score)
            self.next_screen = "game_over"
            self.persistent["score"] = self.score  # Save the score to the persistent data
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)# Change cursor back to normal
            pygame.mouse.set_visible(True)
            self.running = False
        
        self.countdown_box.set_text("Time remaining: " + str(self.time_remaining))
        self.countdown_box.update()

    def draw(self):
        """
        Draw the game screen including the background image, target, scorebox and countdown timer
        """
        # Load the levels background
        img_path = os.path.join(os.path.dirname(__file__), "gamebackground.png")
        bg_image = pygame.image.load(img_path)
        scaled_bg = pygame.transform.scale(bg_image, self.window.get_size())

        # Blit the background image directly on the window surface
        self.window.blit(scaled_bg, (0, 0))

        # Draw the target image
        self.window.blit(self.target.image, self.target.rect)
            
        # Draw the scorebox
        self.window.blit(self.score_box.image, self.score_box.rect)
        
        # Draw countdown timer
        self.window.blit(self.countdown_box.image, self.countdown_box.rect)
        
        # Hide the default cursor
        pygame.mouse.set_visible(False)

        # Draw custom green cursor
        mouse_position = pygame.mouse.get_pos() # gets current mouse position
        green_cursor = pygame.Surface((18, 16), pygame.SRCALPHA) # Creates new surface with and alpha channel to have transparent parts using SRCALPHA
        green_cursor.fill((0, 0, 0, 0))  # Fill with transparent color
        pygame.draw.line(green_cursor, (0, 255, 0), (9, 2), (9, 14), 2)
        pygame.draw.line(green_cursor, (0, 255, 0), (3, 8), (15, 8), 2)
        self.window.blit(green_cursor, mouse_position)
        
    def manage_event(self, event):
        """
        Event management for the game screen.
        """
        

