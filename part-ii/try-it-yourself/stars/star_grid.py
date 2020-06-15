import sys
import pygame

from settings import Settings
from star import Star

class StarGrid:
    """Class to display a grid of stars"""
    def __init__(self):
        """Initialise the grid."""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Star Grid")
   
        self.stars = pygame.sprite.Group()
        self._create_grid()
 
    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()
            self._update_screen()
            

    def _check_events(self):
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    sys.exit()
            
    def _create_grid(self):
        """Create the grid of stars"""
        #spacing between each star is equal to one star image width
        star = Star(self)
        star_width,star_height = star.rect.size
        available_space_x = self.settings.screen_width - (2 * star_width)
        number_stars_x = available_space_x // (2 * star_width)

        #determine the number of rows of stars that fit on the screen.
  
        available_space_y = (self.settings.screen_height - 
        (2 * star_height))
        number_rows = available_space_y // (2 * star_height)
        
        #Create the grid of stars.
        for row_number in range(number_rows):
            for star_number in range(number_stars_x):
                self._create_star(star_number,row_number)

    def _create_star(self, star_number,row_number):
        """Create a star and place it in the row."""
        star = Star(self)
        star_width, star_height = star.rect.size
        star.x = star_width + 2 * star_width * star_number
        star.rect.x =star.x
        star.rect.y =star.rect.height + 2 * star.rect.height * row_number
        self.stars.add(star)

    def _update_screen(self):
        """Update images on the screen, and flip to the new screen.""" 
        self.screen.fill(self.settings.bg_color)
        self.stars.draw(self.screen)

        pygame.display.flip()

if __name__ =='__main__':
    #Make a game instance, and run the game. 
    ai = StarGrid()
    ai.run_game()