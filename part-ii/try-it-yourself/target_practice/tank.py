import pygame

class Tank:
    """A class to manage the tank."""

    def __init__(self, ai_game):
        """Initialise the battle ship and set its starting position."""
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect= ai_game.screen.get_rect()

        #load the tank image and get its rect.
        self.image =pygame.image.load('tank.bmp')
        self.rect=self.image.get_rect()
        #start the tank at the left centre of the screen.
        self.rect.midleft =self.screen_rect.midleft

        #store a decimal value for the tank's vertical position.
        self.y = float(self.rect.y)

        #movement flag
        self.moving_up = False
        self.moving_down = False

    def update(self):
        """Update the tank's position based on the movement flag."""
        if self.moving_up and self.rect.top > self.screen_rect.top:
            self.y -= self.settings.tank_speed
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.tank_speed

        self.rect.y =self.y

    def blitme(self):
        """Draw the tank at its current location."""
        self.screen.blit(self.image,self.rect)

    def reset_tank(self):
        """Move tank back to original position"""
        self.rect.midleft =self.screen_rect.midleft

