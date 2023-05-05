import random
import pygame
from pygame.sprite import Sprite
from dino_runner.utils.constants import SCREEN_WIDTH, HAMMER

class LaucnhHummer(Sprite):
    def __init__(self):
        self.image = HAMMER
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0

    def update(self, game):
        self.rect.x += game.game_speed
        if self.rect.x == SCREEN_WIDTH + 200:
            game.yes_launch = False

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))
            