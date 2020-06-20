class Settings:
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (51, 51, 51)

#tank settings 
        self.tank_speed = 3

#Bullet settings
        self.bullet_speed = 1.0
        self.bullet_width = 20
        self.bullet_height =3
        self.bullet_color = (255,0,0)
        self.bullets_allowed = 10

#Rectangle settings
        self.rectangle_speed = 5
        self.rectangle_direction = 1
