import pygame
from pygame.sprite import Sprite

class Rain(Sprite):
    """A class to represent a single raindrop."""

    def __init__(self, ai_game):
        """Initialize the raindrop and set its starting position."""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        #load the raindrop image and set its rect attribute.
        self.image = pygame.image.load('raindrop.bmp')
        self.rect = self.image.get_rect()

        #start the first raindrop near the top left of the screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        #store the raindrop's exact position.
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def check_bottom(self):
        """Return True if raindrop is at the bottom of the screen."""
        screen_rect = self.screen.get_rect()
        if self.rect.y==screen_rect.height -(2 * self.rect.height): 
            return True
