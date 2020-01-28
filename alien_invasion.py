import pygame
from pygame.sprite import Group

import game_functions as gf
from settings import Settings


def run_game():
    pygame.init()
    ai_settings = Settings(pygame.image.load('alien.bmp'))
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption('Alien Invasion')
    aliens = Group()

    gf.create_fleet(ai_settings, screen, aliens)

    while True:
        #gf.check_events(ai_settings, screen)
        gf.update_screen(ai_settings, screen, aliens)
        gf.update_aliens(aliens)



run_game()
