import pygame
from pygame.sprite import Group
from settings import Settings
from ship import Ship
from game_stats import GameStats
import game_functions as gf
from button import Button

def run_game():
    #initialize pygame settings and screen object
    pygame.init()
    ai_settings = Settings()

    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height)
    )
    pygame.display.set_caption("Alien_invasion")

    #Create an instance to store game statistics
    stats = GameStats(ai_settings)

    #Make a ship
    ship = Ship(ai_settings, screen)

    #make a group of aliens
    aliens = Group()

    #make a group to store bullet in
    bullets = Group()

    #Create the fleet of aliens
    gf.create_fleet(ai_settings, screen, ship, aliens)

    #make the play button for the game
    play_button = Button(ai_settings, screen, "Play")
    

    #start the games main loop

    while True:

        #watch for keyboard and mouse events
        gf.check_events(ai_settings, screen, ship, bullets)

        if stats.game_active:
            #control the movement of the ship
            ship.update()

            #get rid of old bullets that have disappeared
            gf.update_bullets(ai_settings, screen, ship, aliens, bullets)

            #update the alien's position
            gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets)

            #redraw the screen during each pass through the loop and make most recently
            #draw screen visible
            gf.update_screen(ai_settings, screen, stats, ship, aliens, bullets, play_button)
        
#run the game
run_game()
