import keyboard
import pygame
from dino_runner.utils.constants import (JUMPING, RUNNING, DUCKING, DEAD,
                                        JUMPING_SHIELD, RUNNING_SHIELD, DUCKING_SHIELD,
                                        JUMPING_HAMMER, RUNNING_HAMMER, DUCKING_HAMMER,
                                        DEFAULT_TYPE, SHIELD_TYPE,HAMMER_TYPE,ACCELERATOR_TYPE)

class Dinosaur:
  X_POS = 80
  Y_POS = 310
  Y_POS_DUCK = 345
  JUMP_VEL = 11
  JUMP_POWER = 2
  BOTTOM_JUMP = "space"
  BOTTOM_DUCK = "down"
  
  def __init__(self):
    self.run_img = {DEFAULT_TYPE:RUNNING, SHIELD_TYPE:RUNNING_SHIELD, HAMMER_TYPE:RUNNING_HAMMER}
    self.duck_img = {DEFAULT_TYPE:DUCKING, SHIELD_TYPE:DUCKING_SHIELD, HAMMER_TYPE:DUCKING_HAMMER}
    self.jump_img = {DEFAULT_TYPE:JUMPING, SHIELD_TYPE:JUMPING_SHIELD, HAMMER_TYPE:JUMPING_HAMMER}
    self.type = DEFAULT_TYPE
    self.image = self.run_img[self.type][0]
    self.dino_rect = self.image.get_rect()
    self.dino_rect.x = self.X_POS
    self.dino_rect.y = self.Y_POS
    self.step_index = 0
    self.dino_run = True
    self.dino_duck = False
    self.dino_jump = False
    self.jump_vel = self.JUMP_VEL
    self.jump_power = self.JUMP_POWER
    self.dino_dead = [False,False]
    self.rect_y_obstacle = 0
    self.rect_x_obstacle = 0
    self.collider = False
    self.shield = False
    self.hammer = False
    self.accelerator = False
    self.time_up_power_up = 0
    self.time_to_show = 0
    self.lowered_speed = False
    self.sprite = 0
    self.power_up_use = False
    self.game_speed = 5
    self.quantity_points = 1
  
  def update(self):
    if self.dino_dead[0]: self.dead()
    elif self.dino_run: self.run()
    elif self.dino_duck: self.duck()
    else: self.jump()
    
    if keyboard.is_pressed(self.BOTTOM_DUCK) and not self.dino_jump:
      self.dino_run = False
      self.dino_duck = True
      self.dino_jump = False
    elif keyboard.is_pressed(self.BOTTOM_JUMP) and not self.dino_jump:
      self.dino_run = False
      self.dino_duck = False
      self.dino_jump = True
    elif not self.dino_jump:
      self.dino_run = True
      self.dino_duck = False
      self.dino_jump = False
    
    if self.step_index >= 10:
      self.step_index = 0
      
    if self.shield or self.hammer or self.accelerator:
      if self.accelerator:
        self.game_speed = 30
        self.quantity_points = 6
      self.time_to_show = round((self.time_up_power_up - pygame.time.get_ticks())/ 1000, 2)
      if self.time_to_show < 0:
        self.reset()
  
  def draw(self,screen):
    screen.blit(self.image,self.dino_rect)
    
  def dead(self):
    if self.dino_duck and self.sprite == 0:
      self.dino_rect.y = self.Y_POS
      self.dino_rect.x += 25
    if self.sprite >= 30:
      self.dino_dead[1] = True
    if self.sprite < len(DEAD):
      self.image = DEAD[self.sprite]
    self.sprite += 1
    
      
    
  def run(self):
    self.image = self.run_img[self.type][0] if self.step_index < 5 else self.run_img[self.type][1]
    self.dino_rect = self.image.get_rect()
    self.dino_rect.x = self.X_POS
    self.dino_rect.y = self.Y_POS
    self.step_index += 0.9
  
  def duck(self):
    self.image = self.duck_img[self.type][0] if self.step_index < 5 else self.duck_img[self.type][1]
    self.dino_rect = self.image.get_rect()
    self.dino_rect.x = self.X_POS
    self.dino_rect.y = self.Y_POS_DUCK
    self.step_index += 0.9
  
  def jump(self):
    self.image = self.jump_img[self.type]
    if self.dino_jump:
      self.dino_rect.y -= self.jump_vel * self.jump_power
    if keyboard.is_pressed(self.BOTTOM_DUCK):
      self.lowered_speed = down_press()
    if self.lowered_speed:
      self.jump_vel -= 0.8
      self.jump_power = 4
    else: 
        self.jump_vel -= 0.4
    if self.jump_vel < -self.JUMP_VEL:
      self.lowered_speed = False
      self.dino_rect.y = self.Y_POS
      self.jump_power = self.JUMP_POWER
      self.dino_jump = False
      self.jump_vel = self.JUMP_VEL
      
  def set_power_up(self, power_up):
    self.power_up_use = True
    if power_up.type == SHIELD_TYPE:
      self.type = SHIELD_TYPE
      self.shield = True
      self.time_up_power_up = power_up.time_up
    elif power_up.type == HAMMER_TYPE: 
      self.type = HAMMER_TYPE
      self.hammer = True
      self.time_up_power_up = power_up.time_up
    elif power_up.type == ACCELERATOR_TYPE: 
      self.type = DEFAULT_TYPE
      self.accelerator = True
      self.time_up_power_up = power_up.time_up
    
  def reset(self):
    self.game_speed = 5
    self.quantity_points = 1
    self.power_up_use = False
    self.type = DEFAULT_TYPE
    self.shield = False
    self.hammer = False
    self.accelerator = False
    self.time_up_power_up = 0
    self.time_to_show = 0
    
def down_press():
  return True