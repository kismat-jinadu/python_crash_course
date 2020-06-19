import sys

from time import sleep

import pygame

from settings import Settings
from game_stats import GameStats
from button import Button
from tank import Tank
from bullet import Bullet
from rectangle import Rectangle

class TargetPractice: 
    """Overall class to manage game assets and behaviour."""

    def __init__(self):
        """Initialise the game, and create game resources."""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Target Practice")
        
        self.stats =GameStats(self)

        self.tank = Tank(self)
        self.bullets = pygame.sprite.Group()
        self.rectangle = Rectangle(self)

        #make the play button.
        self.play_button = Button(self, "Play")


    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()

            if self.stats.game_active:
                self.tank.update()
                self.rectangle.update()
                self._update_bullets()
            self._update_screen()
            

    def _check_events(self):
        """Respond to keypresses and mouse events.""" 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_play_button(self, mouse_pos):
        """Start a new game when the player clicks Play."""
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.stats.game_active:
            self._start_game()
                  
    def _check_keydown_events(self, event):
        """Respond to keypresses."""
        if event.key == pygame.K_p and not self.stats.game_active:
            self._start_game()
        elif event.key == pygame.K_UP:
            self.tank.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.tank.moving_down = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_events(self, event):
        """Respond to key releases."""       
        if event.key == pygame.K_UP:
            self.tank.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.tank.moving_down = False

    def _start_game(self):
        """Start the game if play is click or P is pressed"""
        #reset the game statistics each time play button is clicked
        self.stats.game_active = True

        #get rid of the target and bullets when restarting the game
        self.bullets.empty()

        #recreate the rectangle and center the tank each time play is clicked
        self.rectangle.update()
        self.tank.update()

        #hide the mouse cursor.
        pygame.mouse.set_visible(False)

    def _fire_bullet(self):
        """Create a new bullet and add it to the bullets group."""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)
 

    def _update_bullets(self):
        """Update position of bullets and get rid of old bullets."""
        #update bullet positions.
        self.bullets.update()
        #get rid of bullets that have disappeared.
        for bullet in self.bullets.copy():
            if bullet.rect.left >= self.settings.screen_width:
                self.bullets.remove(bullet)
       
 

    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        self.screen.fill(self.settings.bg_color)
        self.tank.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.rectangle.draw_rectangle()
        self.rectangle.update()

        #draw the play button if the game is inactive.
        if not self.stats.game_active:
            self.play_button.draw_button()

        #Make the most recently drawn screen visible.
        pygame.display.flip()

if __name__ =='__main__':
    #Make a game instance, and run the game. 
    ai = TargetPractice()
    ai.run_game()