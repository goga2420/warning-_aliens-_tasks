import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    def __init__(self, ai_settings, screen):
        super(Alien, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        self.image = pygame.image.load('images/alien.bmp')

        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.center = float(self.rect.centerx)


    def blitme(self):
        self.screen.blit(self.image, self.rect)


    def update(self):
        self.y += self.ai_settings.alien_speed_factor * self.ai_settings.fleet_direection
        self.rect.y = self.y


    def check_bottom(self):
        screen_rect = self.screen_rect.bottom()
        if self.rect.bottom >= screen_rect.bottom:
            return True

