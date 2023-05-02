import keyboard
from dino_runner.utils.constants import JUMPING, RUNNING, DUCKING, DEAD

class Dinosaur:
  X_POS = 80
  Y_POS = 310
  Y_POS_DUCK = 345
  JUMP_VEL = 8.5
  BOTTOM_JUMP = "space"
  BOTTOM_DUCK = "down"
  
  def __init__(self):
    self.image = RUNNING[0]
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
      self.dino_rect.x = self.X_POS + 30
      self.dino_rect.y = self.Y_POS
    elif (self.dino_rect.y < self.Y_POS) and (self.collider):
      self.dino_rect.y = self.Y_POS - self.rect_y_obstacle
      
    
  def run(self):
    self.image = RUNNING[0] if self.step_index < 5 else RUNNING[1]
    self.dino_rect = self.image.get_rect()
    self.dino_rect.x = self.X_POS
    self.dino_rect.y = self.Y_POS
    self.step_index += 0.9
  
  def duck(self):
    self.image = DUCKING[0] if self.step_index < 5 else DUCKING[1]
    self.dino_rect = self.image.get_rect()
    self.dino_rect.x = self.X_POS
    self.dino_rect.y = self.Y_POS_DUCK
    self.step_index += 0.9
  
  def jump(self):
    self.image = JUMPING
    if self.dino_jump:
      self.dino_rect.y -= self.jump_vel * 3.5
      self.jump_vel -=0.5
    if self.jump_vel < -self.JUMP_VEL:
      self.dino_rect.y = self.Y_POS
      self.dino_jump = False
      self.jump_vel = self.JUMP_VEL