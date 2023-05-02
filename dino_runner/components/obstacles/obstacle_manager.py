import pygame
from dino_runner.components.cactus import Cactus
from dino_runner.utils.constants import SMALL_CACTUS

class ObstacleManager:
    def __init__ (self):
        self.obtacles = []

    def update (self, game):
        #Add obstacle to list 
        if len(self.obtacles) == 0:
            cactus = Cactus(SMALL_CACTUS)
            self.obtacles.append(cactus)
        
        for obstacle in self.obtacles:
            obstacle.update(game.game_speed, self.obtacles)
          #  pygame.time.delay(100)
           # print(game.player.dino_rect.colliderect(obstacle.rect))
            if game.player.dino_rect.colliderect(obstacle.rect):
                game.playing = False
                break


    def draw (self, screen):
        for obstacle in self.obtacles:
            obstacle.draw(screen)