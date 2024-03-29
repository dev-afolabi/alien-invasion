import pygame

class Ship():
    """ the class will manage the behaviour of the ship object"""
    
    def __init__(self, ai_settings, screen):
        """initialize the ship class"""
        self.screen = screen
        self.ai_settings = ai_settings

        #load the ship image and get its rect
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        #set starting position of the ship
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        #store a decimal value for the ship's center
        self.center = float(self.rect.centerx)

        #moving flag
        self.moving_right = False
        self.moving_left = False

        

    def update(self):
        """update the ship's position based on the movement flag"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor

        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor

        #update rect object from self.center
        self.rect.centerx = self.center

    
    def blitme(self):
        """Draw the ship at it's current location"""
        self.screen.blit(self.image,self.rect)

    def center_ship(self):
        """Center the ship on screen"""
        self.center = self.screen_rect.centerx