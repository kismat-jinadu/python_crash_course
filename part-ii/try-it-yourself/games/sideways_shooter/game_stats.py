import json

class GameStats:
    """Track statistics for Alien Invasion"""

    def __init__(self,ai_game):
        """Initialise statistics."""
        self.settings = ai_game.settings
        self.reset_stats()

        #start Sideways Shooter in an inactive state.
        self.game_active = False

        #difficculty level selected 
        self.difficulty_selected = False

        #initialise high score
        filename = 'high_score.json'
        with open(filename) as f:
            self.high_score = json.load(f)


    
    def reset_stats(self):
        """Initialise statistics that can change during the game."""
        self.battleships_left = self.settings.battleship_limit
        self.score =0
        self.level = 1