import pygame


class TextBox(pygame.sprite.Sprite):
    def __init__(self, value=0, text=0, pos=(0, 0), size=(0, 0), font_size=24):
        super().__init__()
        self.value = value
        self.text = text
        pygame.font.init()
        self.font = pygame.font.Font(pygame.font.get_default_font(), font_size)
        self.image = pygame.Surface(size)
        self.image.fill((255, 191, 128)) # Fill the surface with orange background
        self.rect = self.image.get_rect()
        self.rect.topleft = pos # Set the position of the text box

    def set_text(self, text):
        self.value = text

    def update(self):
        font_surface = self.font.render(str(self.value), True, (0, 0, 128)) # Set font color to navy blue
        self.image.fill((255, 191, 128)) # Fill the surface with orange background
        self.image.blit(font_surface, (0, 0))
        
