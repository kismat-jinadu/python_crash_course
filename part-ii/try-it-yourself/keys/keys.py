import sys

import pygame

from settings import Settings

class Keys:
    """Overall class to manage game assets and behaviour."""

    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Key Pressing Game")


    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()
            #redraw the screen during each pass through the loop. 
            self.screen.fill(self.settings.bg_color)
            #make the most recently drawn screen visible.
            pygame.display.flip()

    def _check_events(self):
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                print(event.key)
                if event.key == pygame.K_q:
                    sys.exit()
 

if __name__ == '__main__':
    #make a game instance, and run the game.
    ai = Keys()
    ai.run_game()