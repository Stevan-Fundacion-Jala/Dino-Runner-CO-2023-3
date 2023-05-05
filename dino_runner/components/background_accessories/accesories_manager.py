import random
import pygame
from dino_runner.components.background_accessories.clouds import Cloud
from dino_runner.utils.constants import SCREEN_WIDTH

class AccesoriesManager:
  def __init__(self):
    self.accesories = []
    self.cloud = Cloud()
    self.pos_x = SCREEN_WIDTH
    self.max_cloud = 20
    self.move_pos_x = int((SCREEN_WIDTH/self.max_cloud))
    for i in range(self.max_cloud):
      self.accesories.append(Cloud())
      self.accesories[i].pos_init(self.pos_x)
      self.pos_x -= self.move_pos_x
      
    
  def update(self):
    for accesories in self.accesories:
      if accesories.rect.x < -accesories.rect.width:
        self.accesories.remove(accesories)
        self.accesories.append(Cloud())
      accesories.update(accesories.game_speed)
      
  def draw(self,screen):
    for accesories in self.accesories:
      accesories.draw(screen)