import pygame
import random
import time

from components import Shapes, TextBox
from .base_screen import BaseScreen
from .game_over import GameOverScreen

class TrainScreen(BaseScreen):
    """
    A screen where a red square appears randomly on a grid and the player has to click on it to score points.

    Attributes:
    - square (Shapes): A Shapes object representing the red square.
    - score (int): The player's score.
    - score_box (TextBox): A TextBox object that displays the player's score on the screen.
    - last_move_time (float): The time since the last movement of the square.
    - start_time (float): The time the game started.
    - time_limit (int): The time limit for the game in seconds.
    - time_remaining (int): The time remaining in the game.
    - countdown_box (TextBox): A TextBox object that displays the time remaining on the screen.
    """
    def __init__(self, window):
        super().__init__(window)

        # Initialize grid
        self.grid = [[(255, 255, 255) for _ in range(window.get_width() // Shapes.GRID_SIZE)] 
                    for _ in range(window.get_height() // Shapes.GRID_SIZE)]

        # Initialize score box
        self.score = 0
        self.score_box = TextBox("Score: " + str(self.score), pos=(30, 750), size=(150, 30))
        
        # Initialize square movement timer
        self.last_move_time = time.time()
        
        # Initialize countdown box
        self.start_time = None
        self.time_limit = 10
        self.time_remaining = self.time_limit
        self.countdown_box = TextBox("Time remaining: " + str(self.time_remaining), pos=(470, 750), size=(300, 30))
        
        # Create the red square
        self.square = Shapes(Shapes.GRID_SIZE, (255, 0, 0), limits=self.window.get_size())

        self.clicked_cells = []
        
    def reset_score(self):
        """Resets the score to zero"""
        self.score = 0
        
    def update(self):
        """Update the game state, checking for collisions and updating game objects"""
        if self.start_time is None:
            self.start_time = time.time()
            
        # Check for square-click collision
        mouse_pos = pygame.mouse.get_pos() 
        click = pygame.mouse.get_pressed()
        if self.square.rect.collidepoint(mouse_pos) and click[0] == 1:
            # Get the cell that the square is on
            cell_x = self.square.rect.x // Shapes.GRID_SIZE
            cell_y = self.square.rect.y // Shapes.GRID_SIZE

            # Check if the cell is the target and hasn't been clicked before
            if (cell_x, cell_y) == self.square.current_cell and (cell_x, cell_y) not in self.clicked_cells:
                # Turn the cell orange
                self.grid[cell_y][cell_x] = (255, 165, 0)
                self.clicked_cells.append((cell_x, cell_y))
                
                # Increment the score and move the square to a new position
                self.score += 1
                self.square.move_randomly()
            
        # Set random position for the square if the time runs out
        current_time = time.time()
        if current_time - self.last_move_time >= 1:
            self.square.move_randomly()
            self.last_move_time = current_time

        # Update score box
        self.score_box.set_text("Score: " + str(self.score))
        self.score_box.update()

        # Update countdown box
        elapsed_time = time.time() - self.start_time
        self.time_remaining = max(0, self.time_limit - int(elapsed_time))
        
        # Check if time_remaining is 0 or less and switch screens
        if self.time_remaining <= 0:
            # Add the score to the persistent data and switch to the game over screen
            self.persistent["training_scores"].append(self.score)
            self.next_screen = "game_over"
            self.persistent["score"] = self.score  # Save the score to the persistent data
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)# Change cursor back to normal
            pygame.mouse.set_visible(True) # Set cursor back to visible
            self.running = False
        
        self.countdown_box.set_text("Time remaining: " + str(self.time_remaining))
        self.countdown_box.update()

            
    def draw(self):
        """Draw the screen"""
        self.window.fill((0, 0, 0))  # Fill the screen with black

        # Draw the grid
        for y in range(0, self.window.get_height(), Shapes.GRID_SIZE):
            pygame.draw.line(self.window, (255, 255, 255), (0, y), (self.window.get_width(), y))
        for x in range(0, self.window.get_width(), Shapes.GRID_SIZE):
            pygame.draw.line(self.window, (255, 255, 255), (x, 0), (x, self.window.get_height()))

        # Draw the clicked cells in orange
        for cell_x, cell_y in self.clicked_cells:
            rect = pygame.Rect(cell_x * Shapes.GRID_SIZE, cell_y * Shapes.GRID_SIZE, Shapes.GRID_SIZE, Shapes.GRID_SIZE)
            pygame.draw.rect(self.window, (255, 165, 0), rect)

        # Draw the square
        self.window.blit(self.square.image, self.square.rect)

        # Draw score box
        self.window.blit(self.score_box.image, self.score_box.rect)

        # Draw countdown timer
        self.window.blit(self.countdown_box.image, self.countdown_box.rect)

        # Hide the default cursor
        pygame.mouse.set_visible(False)

        # Draw custom green cursor
        mouse_position = pygame.mouse.get_pos()  # gets current mouse position
        green_cursor = pygame.Surface((18, 16), pygame.SRCALPHA)  # Creates new surface with an alpha channel to have transparent parts using SRCALPHA
        green_cursor.fill((0, 0, 0, 0))  # Fill with transparent color
        pygame.draw.line(green_cursor, (0, 255, 0), (9, 2), (9, 14), 2)
        pygame.draw.line(green_cursor, (0, 255, 0), (3, 8), (15, 8), 2)
        self.window.blit(green_cursor, mouse_position)

        
    def manage_event(self, event):
        """
        Event management for the game screen.
        """
        pass

