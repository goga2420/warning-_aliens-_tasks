import sys
import pygame
from alien import Alien


def get_number_rows(ai_settings, alien_height):
    available_space_y = (ai_settings.screen_height - (3 * alien_height))
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows



def create_alien(ai_settings, screen, aliens, alien_number, row_number):
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)


def create_fleet(ai_settings, screen, aliens):
    alien = Alien(ai_settings, screen)
    number_aliens_x = get_number_aliens_x(ai_settings, alien.rect.width)
    number_rows = get_number_rows(ai_settings, alien.rect.height)

    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            create_alien(ai_settings, screen, alien, alien_number, row_number)



def get_number_aliens_x(ai_settings, alien_width):
    available_space_x = ai_settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x


#def check_keydown_events(event, ai_settings, screen, ship):
    #    if event.key == pygame.K_RIGHT:
    #   ship.moving_right = True
    #elif event.key == pygame.K_LEFT:
    #   ship.moving_left = True
    #elif event.key == pygame.K_UP:
    #   ship.moving_up = True
    #elif event.key == pygame.K_DOWN:
#   ship.moving_down = True


#def check_keyup_events(event, ship):
    #   if event.key == pygame.K_RIGHT:
    #   ship.moving_right = False
    #elif event.key == pygame.K_LEFT:
    #   ship.moving_left = False
    #elif event.key == pygame.K_UP:
    #   ship.moving_up = False
    #elif event.key == pygame.K_DOWN:
#   ship.moving_down = False


#def check_events(ai_settings, screen, ship, bullets):
    #for event in pygame.event.get():
        #if event.type == pygame.QUIT:
            #sys.exit()
        #elif event.type == pygame.KEYDOWN:
            #check_keydown_events(event, ai_settings, screen, ship, bullets)

       # elif event.type == pygame.KEYUP:
           # check_keyup_events(event, ship)


def update_screen(ai_settings, screen, aliens):
    screen.fill(ai_settings.bg_color)
    #for bullet in bullets.sprites():
        #bullet.draw_bullet()
    #ship.blitme()
    aliens.draw(screen)
    pygame.display.flip()


def update_aliens(aliens):
    aliens.update()