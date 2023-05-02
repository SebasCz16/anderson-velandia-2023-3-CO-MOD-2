import random
import pygame
from dino_runner.components.obstacles.obstacle import Obstacle
#from dino_runner.utils.constants import BIRD

class SmallCactus(Obstacle):
    def __init__(self, image):
        self.type = random.randint(0, 2) # 0, 1, 2
        super().__init__(image, self.type)
        self.rect.y = 325 

class LargeCactus(Obstacle):
    def __init__(self, image):
        self.type = random.randint(0, 2) # 0, 1, 2
        super().__init__(image, self.type)
        self.rect.y = 300

'''class Bird_High(Obstacle):
    def __init__(self, image):
        self.type = 0
        super().__init__(image, self.type)
        self.rect.y = 170
        self.index = 0 

    def draw(self, screen):
        if self.index >= 9:
            self.index = 0
        screen.blit(self.image[self.index//5], self.rect)
        self.index += 1

class Bird_Half(Obstacle):
    def __init__(self, image):
        self.type = 0
        super().__init__(image, self.type)
        self.rect.y = 220
        self.index = 0 

    def draw(self, screen):
        if self.index >= 9:
            self.index = 0
        screen.blit(self.image[self.index//5], self.rect)
        self.index += 1

class Bird_Low(Obstacle):
    def __init__(self, image):
        self.type = 0
        super().__init__(image, self.type)
        self.rect.y = 260
        self.index = 0 

    def draw(self, screen):
        if self.index >= 9:
            self.index = 0
        screen.blit(self.image[self.index//5], self.rect)
        self.index += 1'''