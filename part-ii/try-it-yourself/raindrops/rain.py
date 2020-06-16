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

        #store the raindrop's exact horizontal position.
        self.x = float(self.rect.x)

