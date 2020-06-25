import pygame.font
from pygame.sprite import Group

from battleship import BattleShip

class Scoreboard:
    """A class to report scoring information."""

    def __init__(self,ai_game):
        """Initialize scorekeeping attributes."""
        self.ai_game =ai_game
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings
        self.stats = ai_game.stats

        #font settings for scoring information.
        self.text_color = (30,30,30)
        self.font = pygame.font.SysFont(None, 38)

        self.prep_images()
        self.prep_high_score()

    def prep_images(self):
        """To prepare the score board images which are reset each time"""
        #prepare the initial score images.
        self.prep_score()
        self.prep_level()
        self.prep_battleships()

    def prep_score(self):
        """Turn the score into a rendered image."""
        rounded_score = round(self.stats.score, -1)
        score_str = "Score: " "{:,}".format(rounded_score)
        self.score_image = self.font.render(score_str,True,
        self.text_color,self.settings.bg_color)

        #display the score at the top left of the screen.
        self.score_rect = self.score_image.get_rect()
        self.score_rect.left = self.screen_rect.left + 20
        self.score_rect.top = 20

    def prep_high_score(self):
        """Turn the high score into a rendered image."""
        high_score = round(self.stats.high_score, -1)
        high_score_str = "High Score: " "{:,}".format(high_score)
        self.high_score_image = self.font.render(high_score_str,True,
        self.text_color,self.settings.bg_color)

        #display the high score beneath the score.
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.left = self.score_rect.left
        self.high_score_rect.top = self.score_rect.bottom + 10

    def prep_level(self):
        """Turn the level into a rendered image."""
        level_str = str(f"Level: {self.stats.level}")
        self.level_image = self.font.render(level_str, True,
        self.text_color, self.settings.bg_color)

        #position the level below the score.
        self.level_rect = self.level_image.get_rect()
        self.level_rect.left = self.score_rect.left
        self.level_rect.top = self.score_rect.bottom + 40

    def prep_battleships(self):
        """Show how many ships are left."""
        self.battleships = Group()
        for battleship_number in range(self.stats.battleships_left):
            battleship = BattleShip(self.ai_game)
            battleship.rect.x = (self.screen_rect.left+ 400) + battleship_number * battleship.rect.width
            battleship.rect.y = 10
            self.battleships.add(battleship)

    def show_score(self):
        """Draw scores, level and ships to the screen."""
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        self.battleships.draw(self.screen)

    def check_high_score(self):
        """Check to see if there's a new high score."""
        if self.stats.score > self.stats.high_score:
            self.stats.high_score = self.stats.score
            self.prep_high_score()
