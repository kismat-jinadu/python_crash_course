import pygame

class Rectangle:
    """Create rectangle target"""
    def __init__(self, ai_game):
        """Initialise button attributes."""
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = self.screen.get_rect()

        #set the dimensions and properties of the rectangle. 
        self.width, self.height = 50, 50
        self.rectangle_color = (0, 0, 128)

        #Build the rect object and center it.
        self.rect = pygame.Rect(0,0, self.width, self.height)
        self.rect.midright = self.screen_rect.midright

        #store the rectangle's position
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
    
    def draw_rectangle(self):
        #draw rectangle
        self.screen.fill(self.rectangle_color,self.rect)

    def update(self):
        """Move the rectangle up or down and stop from going offscreen"""
        if self.rect.top <= self.screen_rect.top:
            self.y -= self.settings.rectangle_speed
        if self.rect.bottom >= self.screen_rect.bottom:
            self.y += self.settings.rectangle_speed
        self.rect.y = self.y
        
