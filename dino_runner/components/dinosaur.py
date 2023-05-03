import keyboard
from dino_runner.utils.constants import (JUMPING, RUNNING, DUCKING, DEAD,
                                        JUMPING_SHIELD, RUNNING_SHIELD, DUCKING_SHIELD,
                                        JUMPING_HAMMER, RUNNING_HAMMER, DUCKING_HAMMER,
                                        DEFAULT_TYPE, SHIELD_TYPE,HAMMER_TYPE)

class Dinosaur:
  X_POS = 80
  Y_POS = 310
  Y_POS_DUCK = 345
  JUMP_VEL = 11
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
    self.dino_dead = False
    self.rect_y_obstacle = 0
    self.rect_x_obstacle = 0
    self.collider = False
  
  def update(self):
    if self.dino_dead: self.dead()
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
  
  def draw(self,screen):
    screen.blit(self.image,self.dino_rect)
    
  def dead(self):
    self.image = DEAD
    if self.dino_duck:
      self.dino_rect.y = self.Y_POS
      self.dino_rect.x += 25
      
    
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
      self.dino_rect.y -= self.jump_vel * 2
      self.jump_vel -= 0.4
    if self.jump_vel < -self.JUMP_VEL:
      self.dino_rect.y = self.Y_POS
      self.dino_jump = False
      self.jump_vel = self.JUMP_VEL
      
  def set_power_up(self, power_up):
    if power_up == "DEFAULT_TYPE": self.type = DEFAULT_TYPE
    elif power_up.type == SHIELD_TYPE: self.type = SHIELD_TYPE
    elif power_up.type == HAMMER_TYPE: self.type = HAMMER_TYPE