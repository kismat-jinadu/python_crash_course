class Settings:
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initialize the game's static settings."""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (51, 51, 51)



#Bullet settings
        
        self.bullet_width = 20
        self.bullet_height =3
        self.bullet_color = (255,0,0)
        self.bullets_allowed = 10

#Number of tries allowed
        self.number_of_tries = 3

#How quickly the game speeds up
        self.speedup_scale = 1.1

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Initialize settings that change throughout the game."""
        #tank settings 
        self.tank_speed = 3

        #bullet speed
        self.bullet_speed = 20

        #Rectangle settings
        self.rectangle_speed = 1.0
        self.rectangle_direction = 1

    def increase_speed(self):
        """Increase speed settings."""
        self.tank_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.rectangle_speed *=self.speedup_scale


