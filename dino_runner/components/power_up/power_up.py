import pygame
from dino_runner.utils.constants import SCREEN_WIDTH

class PowerUp:
  Y_POS_POWER_UP = 110
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
    
  def print_power_up(self,player):
    self.rect.x = 40
    if player.power_up_use:
      self.rect.y = 40
    else:
      self.rect.y = -100
    
  def update(self,game_speed,player):
    self.rect.x -= game_speed
    if self.rect.colliderect(player.dino_rect):
      self.start_time = pygame.time.get_ticks()
      self.time_up = self.start_time + self.POWER_UP_DURACTION
      self.used = True
    
  def draw(self,screen):
    screen.blit(self.image,self.rect)