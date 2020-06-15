import pygame
from pygame.sprite import Sprite

class Star(Sprite):
    """A class to represent a single star"""

    def __init__(self, ai_game):
        """Initialize the star and set its starting position."""
        super().__init__()
        self.screen = ai_game.screen

        self.image = pygame.image.load('star.bmp')
        self.rect = self.image.get_rect()

        #start the first star near the top left of the screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        #store the star's exact positions.
        self.x = float(self.rect.x)
   