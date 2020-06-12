import pygame

class AlienBoss:
    """A class to manage the alien_boss."""

    def __init__(self, ai_game):
        """Initialise the ship and set its starting position."""
        self.screen = ai_game.screen
        self.screen_rect= ai_game.screen.get_rect()

        #load the alien_boss image and get its rect.
        self.image =pygame.image.load('images/alien_boss.bmp')
        self.rect=self.image.get_rect()
        #add alien_boss at the centre of the screen.
        self.rect.center =self.screen_rect.center

    def blitme(self):
        """Draw the alien_boss at its current location."""
        self.screen.blit(self.image,self.rect)