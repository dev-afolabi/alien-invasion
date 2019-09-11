"""this is the setti ngs module"""

class Settings():
    """a class to store all settings for Alien-invasion"""

    def __init__(self):
        """initialize the game's settings"""
        #Screen settings
        self.screen_width = 1200
        self.screen_height = 600
        self.bg_color = (230, 230, 230)

        #ship settings
        self.ship_speed_factor = 1.5
        self.ship_limit = 3

        #alien settings
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 10
        #fleet direction of 1 represent right; -1 represent left
        self.fleet_direction = -1

        #bullet settings
        self.bullet_speed_factor = 3
        self.bullet_width = 4
        self.bullet_height = 10
        self.bullet_color = (226, 88, 34)
        self.bullets_allowed = 10

