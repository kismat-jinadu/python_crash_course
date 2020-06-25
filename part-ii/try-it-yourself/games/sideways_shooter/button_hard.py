import pygame.font

class ButtonHard:
    """Create a button to start the game"""
    def __init__(self, ai_game, msg):
        """Initialise button attributes."""
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()

        #set the dimensions and properties of the button. 
        self.width, self.height = 50, 50
        self.button_color = (255,0,0)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 20)

        #Build the button's rect object and center it.
        self.rect = pygame.Rect(800,500, self.width, self.height)

        #The button message needs to be prepped only once.
        self._prep_msg(msg)

    def _prep_msg(self,msg):
        """Turn msg into a rendered image and center text on the button."""
        self.msg_image = self.font.render(msg, True, self.text_color,
        self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        #draw blank button and then draw message.
        self.screen.fill(self.button_color,self.rect)
        self.screen.blit(self.msg_image,self.msg_image_rect)