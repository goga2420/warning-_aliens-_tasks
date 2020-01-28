import pygame

from alien import Alien


def get_number_rows(screen_height, alien_height):
    available_space_y = (screen_height - (3 * alien_height))
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows



def prepare_alien(alien, alien_number, row_number):
    alien_width = alien.rect.width
    alien.rect.x = alien_width + 2 * alien_width * alien_number
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number



def create_fleet(ai_settings, screen, aliens):
    #TODO поправить костыль
    alien_width = Alien(ai_settings, screen).rect.width
    alien_height = Alien(ai_settings, screen).rect.height

    number_aliens_columns = get_number_aliens_x(ai_settings.screen_width, alien_width)
    number_aliens_rows = get_number_rows(ai_settings.screen_height, alien_height)

    for row_number in range(number_aliens_rows):
        for alien_number in range(number_aliens_columns):
            alien = Alien(ai_settings, screen)
            prepare_alien(alien, alien_number, row_number)
            aliens.add(alien)



def get_number_aliens_x(screen_width, alien_width):
    available_space_x = screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x


def update_screen(ai_settings, screen, aliens):
    screen.fill(ai_settings.bg_color)
    aliens.draw(screen)
    pygame.display.flip()


def update_aliens(aliens):
    aliens.update()
    remove_out_of_screen_aliens(aliens)


def remove_out_of_screen_aliens(aliens):
    for a in aliens:
        if a.check_bottom():
            aliens.remove(a)
