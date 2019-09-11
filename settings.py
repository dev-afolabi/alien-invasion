"""this is the setti ngs module"""

class Settings():
    """a class to store all settings for Alien-invasion"""

    def __init__(self):
        """initialize the game's static settings"""
        #Screen settings
        self.screen_width = 1200
        self.screen_height = 600
        self.bg_color = (230, 230, 230)

        #ship settings
        self.ship_limit = 3

        #alien settings
        self.fleet_drop_speed = 10

        #bullet settings
        
        self.bullet_width = 4
        self.bullet_height = 10
        self.bullet_color = (226, 88, 34)
        self.bullets_allowed = 10

        #How quickly the game speeds up
        self.speedup_scale = 1.1

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Increase speed settings"""
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 1

        #fleet direction of 1 represent right; -1 represent left
        self.fleet_direction = -1

        #Scoring
        self.alien_points = 10

    
    def increase_speed(self):
        """Increase speed settings"""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale


