class GameStats:
    """Track statistics for Alien Invasion"""

    def __init__(self,ai_game):
        """Initialise statistics."""
        self.settings = ai_game.settings
        self.reset_stats()
        
        #start Target Practice in an inactive state.
        self.game_active = False
    
    def reset_stats(self):
        """Initialise statistics that can change during the game."""
        self.tries_left = self.settings.number_of_tries