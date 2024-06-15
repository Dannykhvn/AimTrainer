import pygame
import random

class Shape(pygame.sprite.Sprite):
    """
    A sprite that represents a shape on the game screen.

    Attributes:
    - GRID_SIZE (class attribute): The size of each grid cell.
    - size: The size of the shape.
    - limits: The limits of the screen where the shape can move.
    - target_img_path: The path of the image for the target shape.
    - image: The image of the shape.
    - rect: The rectangle that bounds the shape.
    """

    GRID_SIZE = 30

    def __init__(self, size, limits=None, target_img_path=None):
        """
        Initializes a new Shape object
        """
        super().__init__()
        self.image = pygame.Surface(size) # Initialize the surface of the shape
        self.rect = self.image.get_rect() # Initialize the bounding rectangle of the shape
        self.limits = limits # Set the limits of the screen where the shape can move
        self.set_random_position() # Set the initial position of the shape
        
        # Set the image of the shape to a target image if provided
        if target_img_path:
            self.image = pygame.image.load(target_img_path).convert_alpha()
            self.image = pygame.transform.scale(self.image, size)
            
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
        grid_x = (self.limits[0] - self.rect.width) // self.GRID_SIZE
        grid_y = (self.limits[1] - self.rect.height) // self.GRID_SIZE

        self.rect.x = random.randint(0, grid_x) * self.GRID_SIZE
        self.rect.y = random.randint(0, grid_y) * self.GRID_SIZE

    def update(self):
        self.check_limits()
    
    def check_limits(self):
        """
        Check if the shape is within the screen limits and move it to a new random position if it overlaps with other shapes.
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
