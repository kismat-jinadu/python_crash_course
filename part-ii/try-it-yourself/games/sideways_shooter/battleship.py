import pygame
from pygame.sprite import Sprite

class BattleShip(Sprite):
    """A class to manage the battleship."""

    def __init__(self, ai_game):
        """Initialise the battle ship and set its starting position."""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect= ai_game.screen.get_rect()

        #load the battleship image and get its rect.
        self.image =pygame.image.load('battleship.bmp')
        self.rect=self.image.get_rect()
        #start the battleship at the left centre of the screen.
        self.rect.midleft =self.screen_rect.midleft

        #store a decimal value for the battleship's vertical position.
        self.y = float(self.rect.y)

        #movement flag
        self.moving_up = False
        self.moving_down = False

    def update(self):
        """Update the battleship's position based on the movement flag."""
        if self.moving_up and self.rect.top > self.screen_rect.top:
            self.y -= self.settings.battleship_speed
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.battleship_speed

        self.rect.y =self.y

    def blitme(self):
        """Draw the battleship at its current location."""
        self.screen.blit(self.image,self.rect)

    def center_battleship(self):
        """Center the ship on the screen."""
        self.rect.midleft =self.screen_rect.midleft
        self.y = float(self.rect.y)