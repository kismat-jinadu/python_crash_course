import pygame

class Rocket:
    """A class to manage the rocket."""

    def __init__(self, ai_game):
        """Initialise the rocket and set its starting position."""
        self.screen = ai_game.screen
        self.screen_rect= ai_game.screen.get_rect()

        #load the rocket image and get its rect.
        self.image =pygame.image.load('rocket.bmp')
        self.rect=self.image.get_rect()
        #add rocket at the centre of the screen.
        self.rect.center =self.screen_rect.center
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def update(self):
        """Update the rocket's position based on the movement flag."""
        if self.moving_right and self.rect.right <self.screen_rect.right:
            self.rect.x += 1
        if self.moving_left and self.rect.left > 0:
            self.rect.x -= 1
        if self.moving_up and self.rect.top > self.screen_rect.top:
            self.rect.y -= 1
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.rect.y += 1  

    def blitme(self):
        """Draw the rocket at its current location."""
        self.screen.blit(self.image,self.rect)