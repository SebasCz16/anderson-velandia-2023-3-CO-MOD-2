import random
import pygame
from dino_runner.components.cactus import SmallCactus, LargeCactus
from dino_runner.components.obstacles.bird import Bird_High, Bird_Low, Bird_Half
from dino_runner.utils.constants import SMALL_CACTUS, LARGE_CACTUS, BIRD

class ObstacleManager:
    def __init__ (self):
        self.obstacles = []

    def update (self, game):
        #Add obstacle to list 
        if len(self.obstacles) == 0:
            if random.randint(0, 4) == 0:
                small_cactus = SmallCactus(SMALL_CACTUS)
                self.obstacles.append(small_cactus)
            
            elif random.randint (0, 4) == 1:
                large_cactus = LargeCactus(LARGE_CACTUS)
                self.obstacles.append(large_cactus)
            
            elif random.randint (0, 4) == 2:
                bird_one = Bird_High(BIRD)
                self.obstacles.append(bird_one)
            
            elif random.randint (0, 4) == 3:
                bird_two = Bird_Half(BIRD)
                self.obstacles.append(bird_two)

            elif random.randint (0, 4) == 4:
                bird_three = Bird_Low(BIRD)
                self.obstacles.append(bird_three)
        
        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)
          #  pygame.time.delay(100)
           # print(game.player.dino_rect.colliderect(obstacle.rect))
            if game.player.dino_rect.colliderect(obstacle.rect):
                game.playing = False
                game.death_count.update()
                break


    def draw (self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)

    def reset_obstacles(self):
        self.obstacles = []
