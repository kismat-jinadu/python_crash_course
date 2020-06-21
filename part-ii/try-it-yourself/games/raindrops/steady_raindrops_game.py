import sys
import pygame

from settings import Settings
from rain import Rain

class Raindrops:
    """Class to display a grid of raindrops"""
    def __init__(self):
        """Initialise the grid."""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Raindrops")
   
        self.raindrop = pygame.sprite.Group()
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
        """Create the grid of raindrops"""
        #spacing between each raindrop is equal to one raindrop image width
        rain = Rain(self)
        rain_width,rain_height = rain.rect.size
        available_space_x = self.settings.screen_width - (2 * rain_width)
        number_rain_x = available_space_x // (2 * rain_width)

        #determine the number of rows of raindrops that fit on the screen.
  
        available_space_y = (self.settings.screen_height - 
        (2*rain_height))
        number_rows = available_space_y // (2 * rain_height)
        
        #Create the grid of raindrops.
        for row_number in range(number_rows):
            for rain_number in range(number_rain_x):
                self._create_rain(rain_number,row_number)

    def _create_rain(self, rain_number,row_number):
        """Create a raindrop and place it in the row."""
        rain = Rain(self)
        rain_width, rain_height = rain.rect.size
        rain.x = rain_width + 2 * rain_width * rain_number
        rain.rect.x =rain.x
        rain.rect.y =rain.rect.height + 2 * rain.rect.height * row_number
        self.raindrop.add(rain)

    def _drop_rain(self):
        """Drop the entire grid of rain."""
        for rain in self.raindrop.sprites():
            rain.rect.y += self.settings.raindrop_speed

    def _check_raindrop_bottom(self):
        """Check if raindrop is at the bottom of screen and draw new row."""
        for rain in self.raindrop.sprites():
            if rain.check_bottom():
                self._create_new_row()
                break
               
    def _create_new_row(self):
        """Create new row of raindrops"""
        rain = Rain(self)
        rain_width = rain.rect.width
        available_space_x = self.settings.screen_width - (2 * rain_width)
        number_rain_x = available_space_x // (2 * rain_width)
        for rain_number in range(number_rain_x):
            rain = Rain(self)
            rain.x = rain_width + 2 * rain_width * rain_number
            rain.rect.x = rain.x
            self.raindrop.add(rain)

    def _update_screen(self):
        """Update images on the screen, and flip to the new screen.""" 
        self.screen.fill(self.settings.bg_color)
        self.raindrop.draw(self.screen)
        self._drop_rain()
        self._check_raindrop_bottom()

        pygame.display.flip()

if __name__ =='__main__':
    #Make a game instance, and run the game. 
    ai = Raindrops()
    ai.run_game()