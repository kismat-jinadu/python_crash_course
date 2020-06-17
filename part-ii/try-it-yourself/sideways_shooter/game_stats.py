class GameStats:
    """Track statistics for Alien Invasion"""

    def __init__(self,ai_game):
        """Initialise statistics."""
        self.settings = ai_game.settings
        self.reset_stats()

        #start Sideways Shooter in an active state.
        self.game_active = True
    
    def reset_stats(self):
        """Initialise statistics that can change during the game."""
        self.battleships_left = self.settings.battleship_limit