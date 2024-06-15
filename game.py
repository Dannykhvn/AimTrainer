import pygame
import time
from screens import GameOverScreen, GameScreen, WelcomeScreen, LevelScreen, TrainScreen


class App:
    """
    This is the main class for our application.
    It runs the "screens" and manages state (persistent data).
    """

    def __init__(self):
        """Creates a Pygame window"""
        self.window = pygame.display.set_mode((800, 800))
        self.persistent = {"classic_scores": [], "training_scores": []}

    def run(self):
        """
        This method runs the main loop, and switches between screens using the next_screen attribute.
        """
        screens = {
            "welcome": WelcomeScreen(self.window),
            "game": GameScreen(self.window),
            "game_over": GameOverScreen(self.window),
            "levels": LevelScreen(self.window),
            "train": TrainScreen(self.window),
        }
        running = True
        current_screen = "welcome"
        while running:
            # Gets the screen instance to "run"
            screen = screens.get(current_screen)
            if not screen:
                raise RuntimeError(f"Screen {current_screen} not found!")

            # Updates the persistent data on the instance
            screen.persistent = self.persistent
            # Runs the main loop of the screen
            screen.run()
            # Exits the loop if necessary
            if screen.next_screen is False:
                running = False

            # Switch to the next screen and update the persistent data
            current_screen = screen.next_screen
            self.persistent = screen.persistent
            
           # Reset the persistent score data                  
            if current_screen == "game":
                screens["game"].reset_score()
            if current_screen == "train":
                screens["train"].reset_score()  
                  
            # Reset the timer for the game screen if we transitioned from the game over screen
            if current_screen == "game":
                screens["game"].start_time = time.time()
                
            # Reset the timer for the game screen if we transitioned from the game over screen
            if current_screen == "train":
                screens["train"].start_time = time.time()
            # Exit if the user closes the window
            if current_screen is None:
                running = False
                
if __name__ == "__main__":
    g = App()
    g.run()

