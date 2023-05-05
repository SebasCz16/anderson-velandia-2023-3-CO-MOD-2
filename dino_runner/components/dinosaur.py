import pygame

from pygame.sprite import Sprite
from dino_runner.components import game
from dino_runner.utils.constants import RUNNING, JUMPING, DUCKING, DEFAULT_TYPE, SHIELD_TYPE, RUNNING_SHIELD, JUMPING_SHIELD, DUCKING_SHIELD, HAMMER_TYPE, RUNNING_HAMMER, JUMPING_HAMMER, DUCKING_HAMMER 


RUN_IMAGE = {DEFAULT_TYPE: RUNNING, SHIELD_TYPE: RUNNING_SHIELD, HAMMER_TYPE: RUNNING_HAMMER}
DUCK_IMAGE = {DEFAULT_TYPE: DUCKING, SHIELD_TYPE: DUCKING_SHIELD, HAMMER_TYPE: DUCKING_HAMMER}
JUMP_IMAGE = {DEFAULT_TYPE: JUMPING, SHIELD_TYPE: JUMPING_SHIELD, HAMMER_TYPE: JUMPING_HAMMER}
    
class Dinosaur:
    Y_POS_DUCK = 340
    X_POS = 80
    Y_POS = 310
    JUMP_SPEED = 8.5 

    def __init__(self):
        self.image = RUNNING[0]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS 
        self.dino_rect.y = self.Y_POS
        self.dino_run = True
        self.step_index = 0
        self.dino_jump = False
        self.jump_speed = self.JUMP_SPEED 
        self.dino_duck = False
        self.type = DEFAULT_TYPE
        self.image = RUN_IMAGE[self.type][0]
        self.has_power_up = False
        self.power_up_time = 0
        #self.launch = False
        

    def draw(self, screen):
        screen.blit(self.image, (self.dino_rect.x, self.dino_rect.y))

    def run(self):
       # self.image = RUNNING[0] if self.step_index < 5 else RUNNING[1]
        self.image = RUN_IMAGE[self.type][self.step_index // 5] 
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS
        self.step_index += 1

    def jump(self):
     #  self.image = JUMPING  
        self.image = JUMP_IMAGE[self.type]
        #EN EL EJE Y
        self.dino_rect.y -= self.jump_speed*4
        self.jump_speed -= 0.8
        if self.jump_speed < -self.JUMP_SPEED:
            self.dino_rect.y = self.Y_POS
            self.dino_jump = False
            self.jump_speed = self.JUMP_SPEED
    
    def duck(self):
      #  self.image = DUCKING[0] if self.step_index < 5 else DUCKING[1]
        self.image = DUCK_IMAGE[self.type][self.step_index // 5]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS_DUCK
        self.step_index += 1

    def reset(self):
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS
        self.dino_run = True
        self.step_index = 0
        self.dino_jump = False  
        self.jump_speed = self.JUMP_SPEED 
        self.dino_duck = False

    def update (self, user_imput, game):
        #SI EL DINO ESTA AGACHADO ES TRUE
        if self.dino_duck:
            self.duck()

        #SI EL DINO ESTA CORRIENDO ES TRUE
        elif self.dino_run:
            self.run()

        #SI EL DINO ESTA SALTANDO ES TRUE
        elif self.dino_jump:
            self.jump()

        #COLOCAR A 0 STEP_INDEX CUANDO ES MAYOR A 10    
        if self.step_index > 9:
            self.step_index = 0        
        
        if user_imput[pygame.K_UP] and not self.dino_jump: 
            self.dino_jump = True
            self.dino_run = False
            self.dino_duck = False
        elif user_imput[pygame.K_DOWN] and not self.dino_jump:
            self.dino_duck = True
            self.dino_run = False
            self.dino_jump = False
        elif not (self.dino_jump or user_imput[pygame.K_DOWN]):
            self.dino_run = True
            self.dino_jump = False
            self.dino_duck = False

        elif user_imput[pygame.K_SPACE] and self.type == HAMMER_TYPE:
            game.yes_launch = True
            game.hammer.rect.x = self.dino_rect.x 
            game.hammer.rect.y = self.dino_rect.y
            self.type = DEFAULT_TYPE
            

