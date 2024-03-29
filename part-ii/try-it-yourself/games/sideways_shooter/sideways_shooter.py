import sys

from time import sleep

import pygame

import json

from settings import Settings
from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button
from button_easy import ButtonEasy
from button_medium import ButtonMedium
from button_hard import ButtonHard
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
        
        #create an instance to store game statistics,
        #and create a scoreboard.
        self.stats = GameStats(self)
        self.sb = Scoreboard(self)

        self.battleship = BattleShip(self)
        self.bullets = pygame.sprite.Group()
        self.alien_ships = pygame.sprite.Group()
        self._create_fleet()

        #make the play button.
        self.play_button = Button(self, "Play")
        #make other buttons
        self.easy_button = ButtonEasy(self, "Easy")
        self.medium_button = ButtonMedium(self, "Medium")
        self.hard_button = ButtonHard(self, "Hard")

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()

            if self.stats.game_active:
                self.battleship.update()
                self._update_bullets()
                self._update_alien_ships()
            self._update_screen()
            

    def _check_events(self):
        """Respond to keypresses and mouse events.""" 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                filename = 'high_score.json'
                with open(filename,'w') as f:
                    json.dump(self.stats.high_score,f)
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)
                self._check_easy_button(mouse_pos)
                self._check_medium_button(mouse_pos)
                self._check_hard_button(mouse_pos)
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_easy_button(self, mouse_pos):
        """Set the game to easy mode."""
        easy_clicked = self.easy_button.rect.collidepoint(mouse_pos)
        if easy_clicked and not self.stats.game_active:
            #reset the game settings.
            self.settings.initialize_easy_settings()
            self.stats.difficulty_selected = True
            self._check_play_button(mouse_pos)

    def _check_medium_button(self, mouse_pos):
        """Set the game to medium mode."""
        medium_clicked = self.medium_button.rect.collidepoint(mouse_pos)
        if medium_clicked and not self.stats.game_active:
            #reset the game settings.
            self.settings.initialize_medium_settings()
            self.stats.difficulty_selected = True
            self._check_play_button(mouse_pos)

    def _check_hard_button(self, mouse_pos):
        """Set the game to hard mode."""
        hard_clicked = self.hard_button.rect.collidepoint(mouse_pos)
        if hard_clicked and not self.stats.game_active:
            #reset the game settings.
            self.settings.initialize_hard_settings()
            self.stats.difficulty_selected = True
            self._check_play_button(mouse_pos)

    def _check_play_button(self, mouse_pos):
        """Start a new game when the player clicks Play."""
        play_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if (play_clicked and self.stats.difficulty_selected 
        and not self.stats.game_active):
        #reset game statistics
            self.stats.reset_stats()
            self.stats.game_active = True
            self.sb.prep_images()
            #start the game
            self._start_game()

    def _check_keydown_events(self, event):
        """Respond to keypresses."""
        if (event.key == pygame.K_p and self.stats.difficulty_selected
        and not self.stats.game_active):
            self._start_game()
        if event.key == pygame.K_UP:
            self.battleship.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.battleship.moving_down = True
        elif event.key == pygame.K_q:
            filename = 'high_score.json'
            with open(filename,'w') as f:
                json.dump(self.stats.high_score,f)
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
                  
    def _check_keyup_events(self, event):
        """Respond to key releases."""       
        if event.key == pygame.K_UP:
            self.battleship.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.battleship.moving_down = False

    def _start_game(self):
        """Start the game if play is clicked or P is pressed"""
        #reset the game statistics each time play button is clicked
        self.stats.reset_stats()
        self.stats.game_active = True

        #get rid of any remaining aliens and bullets when restarting the game
        self.alien_ships.empty()
        self.bullets.empty()

        #create a new fleet and center the ship each time play is clicked
        self._create_fleet()
        self.battleship.center_battleship()

        #hide the mouse cursor.
        pygame.mouse.set_visible(False)

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
        alien_ship.rect.x =int(alien_ship.x)

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
        
        if collisions:
            for alien_ships in collisions.values():
                self.stats.score += self.settings.alien_ship_points * len(alien_ships)
                self.sb.prep_score()
                self.sb.check_high_score()
        
        if not self.alien_ships:
            self.start_new_level()

    def start_new_level(self):
        """to start a new level of the game"""
        #destroy existing bullets and create new fleet.
        self.bullets.empty()
        self._create_fleet()
        self.settings.increase_speed()

        #increase level.
        self.stats.level += 1
        self.sb.prep_level()

    def _update_alien_ships(self):
        """
        Check if the fleet is at an edge,
        then update the positions of all alienships in the fleet.
        """
        self._check_fleet_edges()
        self.alien_ships.update()
        #look for alien_battleship collisions.
        if pygame.sprite.spritecollideany(self.battleship, self.alien_ships):
            self._battleship_hit()

        #look for alien ships hitting the left of the screen.
        self._check_alien_ships_leftedge()

    def _check_alien_ships_leftedge(self):
        """Check if any alien_ships have reached the left side of the screen."""
        screen_rect = self.screen.get_rect()
        for alien_ship in self.alien_ships.sprites():
            if alien_ship.rect.left <=screen_rect.left:
                #treat this the same as if the ship got hit.
                self._battleship_hit()
                break

    def _battleship_hit(self):
        """Respond to the battleship being hit by an alien ship."""
        if self.stats.battleships_left > 0:
            #decrement battleships_left and update scoreboard..
            self.stats.battleships_left -= 1
            self.sb.prep_battleships()

            #get rid of any remaining alien ships and bullets.
            self.alien_ships.empty()
            self.bullets.empty()

            #create a new fleet and centre the ship.
            self._create_fleet()
            self.battleship.center_battleship()

            #pause.
            sleep(0.5)
        else:
            self.stats.difficulty_selected =False
            self.stats.game_active =False
            pygame.mouse.set_visible(True)

    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        self.screen.fill(self.settings.bg_color)

        #Draw the score information.
        self.sb.show_score()

        #draw ships and bullets
        self.battleship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.alien_ships.draw(self.screen)

 

        #draw the play button if the game is inactive.
        if not self.stats.game_active:
            self.play_button.draw_button()
            if not self.stats.difficulty_selected:
                self.easy_button.draw_button()
                self.medium_button.draw_button()
                self.hard_button.draw_button()


        #Make the most recently drawn screen visible.
        pygame.display.flip()

if __name__ =='__main__':
    #Make a game instance, and run the game. 
    ai = SidewaysShooter()
    ai.run_game()