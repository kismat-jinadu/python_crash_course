import sys

import pygame

from settings import Settings
from battleship import BattleShip
from bullet import Bullet
from alien_ship import AlienShip

class SidewaysShooter: 
    """Overall class to manage game assets and behaviour."""

    def __init__(self):
        """Initialise the game, and create game resources."""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Sideways Shooter")

        self.battleship = BattleShip(self)
        self.bullets = pygame.sprite.Group()
        self.alien_ships = pygame.sprite.Group()
        self._create_fleet()


    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()
            self.battleship.update()
            self._update_bullets()
            self._update_alien_ships()
            self._update_screen()
            

    def _check_events(self):
        """Respond to keypresses and mouse events.""" 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        """Respond to keypresses."""
        if event.key == pygame.K_UP:
            self.battleship.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.battleship.moving_down = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
                  
    def _check_keyup_events(self, event):
        """Respond to key releases."""       
        if event.key == pygame.K_UP:
            self.battleship.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.battleship.moving_down = False

    def _fire_bullet(self):
        """Create a new bullet and add it to the bullets group."""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _create_fleet(self):
        """Create the fleet of alien_ship"""
        #spacing between each alien_ship is equal to one alien_ship width
        alien_ship = AlienShip(self)
        alien_ship_height,alien_ship_width = alien_ship.rect.size
        available_space_y = self.settings.screen_height - (alien_ship_height)
        number_aliens_y = available_space_y //  (2*alien_ship_height)

    #determine the number of rows of aliens that fit on the screen.
        battleship_height = self.battleship.rect.height
        available_space_x = (self.settings.screen_width - 
        (10 * alien_ship_width) - (10*battleship_height))
        number_rows = available_space_x // (2 * alien_ship_width)
        
    #Create the full fleet of alienships.
        for alien_number in range(number_aliens_y):
            for row_number in range(number_rows):
                self._create_alien_ship(row_number,alien_number)
    
    def _create_alien_ship(self, row_number,alien_number):
        """Create an alien and place it in the row."""
        alien_ship = AlienShip(self)
        alien_ship_height,alien_ship_width = alien_ship.rect.size
        alien_ship.y = alien_ship_height + 2 * alien_ship_height * alien_number
        alien_ship.rect.y =alien_ship.y
        alien_ship.x -= alien_ship_width + 2*alien_ship_width * row_number
        alien_ship.rect.x =alien_ship.x

        self.alien_ships.add(alien_ship)

    def _check_fleet_edges(self):
        """Respond appropriately if any alienships have reached an edge."""
        for alien_ship in self.alien_ships.sprites():
            if alien_ship.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        """Drop the entire fleet and change the fleet's direction."""
        for alien_ship in self.alien_ships.sprites():
            alien_ship.rect.x -= self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1
    

    def _update_bullets(self):
        """Update position of bullets and get rid of old bullets."""
        #update bullet positions.
        self.bullets.update()
        #get rid of bullets that have disappeared.
        for bullet in self.bullets.copy():
            if bullet.rect.left >= self.settings.screen_width:
                self.bullets.remove(bullet)
        self._check_bullet_alien_ship_collisions()
    
    def _check_bullet_alien_ship_collisions(self):
        """Respond to bullet-alien collisions"""
        #remove any bullets and aliens that have collided.
        collisions = pygame.sprite.groupcollide(
            self.bullets,self.alien_ships,True,True)
        
        if not self.alien_ships:
            #destroy existing bullets and create new fleet.
            self.bullets.empty()
            self._create_fleet()  

    def _update_alien_ships(self):
        """
        Check if the fleet is at an edge,
        then update the positions of all alienships in the fleet.
        """
        self._check_fleet_edges()
        self.alien_ships.update()

    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        self.screen.fill(self.settings.bg_color)
        self.battleship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.alien_ships.draw(self.screen)


        #Make the most recently drawn screen visible.
        pygame.display.flip()

if __name__ =='__main__':
    #Make a game instance, and run the game. 
    ai = SidewaysShooter()
    ai.run_game()