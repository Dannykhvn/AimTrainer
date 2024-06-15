import pygame
import random

class Shapes(pygame.sprite.Sprite):
    """
    A sprite that represents a shape on the game screen.

    Attributes:
    - GRID_SIZE (class attribute): The size of each grid cell.
    - size: The size of the shape.
    - color: The color of the shape.
    - image: The image of the shape.
    - rect: The rectangle that bounds the shape.
    - speed: The speed of the shape.
    - limits: The limits of the screen where the shape can move.
    - current_cell: The current cell position of the shape.
    """
    
    GRID_SIZE = 30  

    def __init__(self, size, color=(255, 0, 0), limits=None):
        """
        Initializes a new Shape object
        """
        super().__init__()
        self.image = pygame.Surface((size, size))
        self.color = color
        self.rect = self.image.get_rect()
        self.speed = random.randint(1, 3)
        self.limits = limits
        self.grid_x = (self.limits[0] - self.rect.width) // self.GRID_SIZE
        self.grid_y = (self.limits[1] - self.rect.height) // self.GRID_SIZE
        self.occupied = [[False] * self.grid_y for _ in range(self.grid_x)]
        self.set_random_position()
        self.current_cell = (self.rect.x // self.GRID_SIZE, self.rect.y // self.GRID_SIZE)
        
        # draw the shape
        pygame.draw.rect(self.image, self.color, (0, 0, size, size))

    def check_overlap(self, other_sprites):
        """Check if the shape overlaps with any of the other sprites."""
        for sprite in other_sprites:
            if sprite == self:
                continue
            if self.rect.colliderect(sprite.rect):
                return True
        return False

    def set_random_position(self):
        """
        Sets the position of the shape to a random location on the screen, with no overlap with other shapes.
        """
        while True:
            x = random.randint(0, self.grid_x - 1)
            y = random.randint(0, self.grid_y - 1)
            if not self.occupied[x][y]:
                self.rect.x = x * self.GRID_SIZE
                self.rect.y = y * self.GRID_SIZE
                self.occupied[x][y] = True
                break

    def update(self):
        self.check_limits()

    def move_randomly(self):
        """
        Moves the shape in a random direction.
        """
        dx, dy = random.choice([(0, -1), (1, 0), (0, 1), (-1, 0)])
        x = self.rect.x // self.GRID_SIZE
        y = self.rect.y // self.GRID_SIZE
        self.occupied[x][y] = False

        # Check if the new position is on a colored tile
        new_x = x + dx
        new_y = y + dy
        while (0 <= new_x < self.grid_x and 0 <= new_y < self.grid_y) and self.occupied[new_x][new_y]:
            dx, dy = random.choice([(0, -1), (1, 0), (0, 1), (-1, 0)])
            new_x = x + dx
            new_y = y + dy

        if 0 <= new_x < self.grid_x and 0 <= new_y < self.grid_y:
            self.rect.x += dx * self.GRID_SIZE
            self.rect.y += dy * self.GRID_SIZE
            self.occupied[new_x][new_y] = True
            self.current_cell = (new_x, new_y)

    def check_limits(self):
        """
        Check if the shape is within the screen limits and move it to a new random position if it overlaps with other shapes
        """

        if not self.limits:
            return

        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > self.limits[0]:
            self.rect.right = self.limits[0]
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > self.limits[1]:
            self.rect.bottom = self.limits[1]

        # If shape collides with other shapes, move it to a new random position
        if self.check_overlap(pygame.sprite.Group(self)):
            self.set_random_position()
            