import pygame
from dino_runner.utils.constants import SCREEN_WIDTH

class PowerUp:
  Y_POS_POWER_UP = 125
  POWER_UP_DURACTION = 5000
  
  def __init__(self,image,type):
    self.image = image
    self.type = type
    self.rect = self.image.get_rect()
    self.rect.x = SCREEN_WIDTH
    self.rect.y = self.Y_POS_POWER_UP
    self.start_time = 0
    self.time_up = 0
    self.used = False
    
  def update(self,game_speed,player):
    self.rect.x -= game_speed
    self.start_time += 1
    if self.rect.colliderect(player.dino_rect):
      self.start_time = pygame.time.get_ticks()
      self.time_up = self.start_time + self.POWER_UP_DURACTION
      self.used = True
    if self.start_time > self.time_up:
      pass
      #self.used = False
    
  def draw(self,screen):
    screen.blit(self.image,self.rect)