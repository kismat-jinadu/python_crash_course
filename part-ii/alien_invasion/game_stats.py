class GameStats:
    """Track statistics for Alien Invasion"""

    def __init__(self,ai_game):
        """Initialise statistics."""
        self.settings = ai_game.settings
        self.reset_stats()

        #start Alien Invasion in an inactive state.
        self.game_active = False

        #difficculty level selected 
        self.difficulty_selected = False

        #set high score
        self.high_score = 0
    
    def reset_stats(self):
        """Initialise statistics that can change during the game."""
        self.ships_left = self.settings.ship_limit
        self.score =0
        self.level = 1