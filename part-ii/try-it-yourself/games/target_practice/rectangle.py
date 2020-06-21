import pygame

class Rectangle:
    """Create rectangle target"""
    def __init__(self, ai_game):
        """Initialise rectangle attributes."""
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = self.screen.get_rect()

        #set the dimensions and properties of the rectangle. 
        self.width, self.height = 50, 150
        self.rectangle_color = (0, 0, 128)

        #Build the rect object and center it.
        self.rect = pygame.Rect(0,0, self.width, self.height)
        self.rect.topright = self.screen_rect.topright

        #store the rectangle's position
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    
    def draw_rectangle(self):
        #draw rectangle
        self.screen.fill(self.rectangle_color,self.rect)


    def check_edges(self):
        """Return True if rectangle is at edge of screen."""
        screen_rect = self.screen.get_rect()
        if self.rect.bottom>=screen_rect.bottom or self.rect.top <=0: 
            return True

    def update(self):
        """Move the rectangle up or down"""
        self.y += self.settings.rectangle_speed * self.settings.rectangle_direction
        self.rect.y = self.y

    def reset_position(self):
        """To move rectangle back to original position"""
        self.rect.topright = self.screen_rect.topright
        
