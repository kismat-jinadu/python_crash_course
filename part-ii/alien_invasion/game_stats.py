class GameStats:
    """Track statistics for Alien Invasion"""

    def __init__(self,ai_game):
        """Initialise statistics."""
        self.settings = ai_game.settings
        self.reset_stats()

        #start Alien Invasion in an inactive state.
        self.game_active = False

        #level selected 
        self.level_selected = False
    
    def reset_stats(self):
        """Initialise statistics that can change during the game."""
        self.ships_left = self.settings.ship_limit