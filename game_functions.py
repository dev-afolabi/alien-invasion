import sys
from time import sleep
import pygame
from bullet import Bullet
from alien import Alien


def check_keydown_events(event, ai_settings, screen, ship, bullets):
    """ Respond to key presses"""
    if event.key == pygame.K_RIGHT:
        #move the ship to the right
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        #move the ship to the left
        ship.moving_left = True

    elif event.key == pygame.K_SPACE:
        fire_bullets(ai_settings, screen, ship, bullets)
    
    elif event.key == pygame.K_q:
        sys.exit()
       

def check_keyup_events(event, ship):
    """Respond to key releases"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False

    elif event.key == pygame.K_LEFT:
        ship.moving_left = False



def check_events(ai_settings, screen, ship, bullets):
    """respond to keypress and mouse events"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)         
        
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)
          

def update_screen(ai_settings, screen, stats, ship, aliens, bullets, play_button):
    """update images on the screen and flip the screen"""
    #redraw the screen during each pass through the loop
    screen.fill(ai_settings.bg_color)
    

    #redraw all bullets behind ship and aliens
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    ship.blitme()
    aliens.draw(screen)

    #Draw the play button if game is inactive
    if not stats.game_active:
        play_button.draw_button()

    #make the most recently drawn screen visible
    pygame.display.flip()

def update_bullets(ai_settings, screen, ship, aliens, bullets):
    """update position of bullets and get rid of old bullets"""
    #update bullet position
    bullets.update()

    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    
    #check for for bullet-alien collision
    check_bullet_alien_collision(ai_settings, screen, ship, aliens, bullets)
        

def check_bullet_alien_collision(ai_settings, screen, ship, aliens, bullets):
    """Respond to bullet-alien collision"""
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
    #check if screen is empty and repopulate it
    if len(aliens)  == 0:
        #Destroy existing bullets and create new one
        create_fleet(ai_settings, screen, ship, aliens)



def fire_bullets(ai_settings, screen, ship, bullets):
    """fire a bullet if limit not reached yet"""
    #create a new bullet and add it to the bullet group
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)


def get_number_alien_x(ai_settings, alien_width):
    """Determine the number of aliens that can fit in a row"""
    available_space_x = ai_settings.screen_width - 2 * alien_width
    number_alien_x = int(available_space_x / (2 * alien_width))
    return number_alien_x


def get_number_rows(ai_settings, ship_height, alien_height):
    """Determine the number of rows to fit on screen"""
    available_space_y = (ai_settings.screen_height - (3 * alien_height) - ship_height)
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows


def create_alien(ai_settings, screen, aliens, alien_number, row_number):
    """Create an alien and place it in the row"""
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)


def create_fleet(ai_settings, screen, ship, aliens):
    """Creates a full fleet of aliens"""
    alien = Alien(ai_settings, screen)
    number_alien_x = get_number_alien_x(ai_settings, alien.rect.width)
    number_rows = get_number_rows(ai_settings, ship.rect.height, alien.rect.height)
    #Create the first row of aliens

    for row_number in range(number_rows):
        for alien_number in range(number_alien_x):
            #create an alien and place it in the row
            create_alien(ai_settings, screen, aliens, alien_number, row_number)


def check_fleet_edges(ai_settings, aliens):
    """Respond appropriately if any alien has reached the edge"""
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings, aliens)
            break 


def change_fleet_direction(ai_settings, aliens):
    """Change the fleet direction and drop the entire fleet"""
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1


def update_aliens(ai_settings, stats, screen, ship, aliens,  bullets):
    """Update the positions of all aliens in the fleet"""
    check_fleet_edges(ai_settings, aliens)
    aliens.update()
    #look for alien-ship collision
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(ai_settings, stats, screen, ship, aliens, bullets)
    
    #look for aliens hitting the bottom of the screen
    check_alien_bottom(ai_settings, stats, screen, ship, aliens, bullets)

        
def ship_hit(ai_settings, stats, screen, ship, aliens, bullets):
    """Respond to ship being hit by an alien"""
    if stats.ships_left > 0:
        #decrement ships left
        stats.ships_left -= 1

        #Empty the list of aliens and bullet
        aliens.empty()
        bullets.empty()

        #create a new fleet and center ship
        create_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()

        #Pause the game
        sleep(0.5)
    else:
        stats.game_active = False


def check_alien_bottom(ai_settings, stats, screen, ship, aliens, bullets):
    """Check if any alien have reached the bottom of the screen"""
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            #treat this the same way as if the ship got hit
            ship_hit(ai_settings, stats, screen, ship, aliens, bullets)
            break
