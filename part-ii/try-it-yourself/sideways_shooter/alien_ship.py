import pygame
from pygame.sprite import Sprite

class AlienShip(Sprite):
    """A class to represent a single alien in the fleet."""

    def __init__(self, ai_game):
        """Initialize the alien_ship and set its starting position."""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect= ai_game.screen.get_rect()

        #load the alien_ship image and set its rect attribute.
        self.image = pygame.image.load('alien_ship.bmp')
        self.rect = self.image.get_rect()

        #start each new alien_ship near the top right of the screen.
        self.rect.topright =self.screen_rect.topright

        #store the alien's exact position.
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def check_edges(self):
        """Return True if alien_ship is at edge of screen."""
        screen_rect = self.screen.get_rect()
        if self.rect.bottom>=screen_rect.bottom or self.rect.top <=0: 
            return True

    def update(self):
        """Move the alien_ship up or down."""
        self.y += (self.settings.alien_ship_speed * 
                self.settings.fleet_direction)
        self.rect.y = self.y