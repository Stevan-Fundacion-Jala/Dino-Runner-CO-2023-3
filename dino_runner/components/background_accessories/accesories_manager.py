import random
import pygame
from dino_runner.components.background_accessories.clouds import Cloud

class AccesoriesManager:
  def __init__(self):
    self.accesories = []
    self.cloud = Cloud()
    for i in range(20):
      self.accesories.append(Cloud())
    
  def update(self):
    for accesories in self.accesories:
      #accesories.rect.x -= 5
      if accesories.rect.x < -accesories.rect.width:
        self.accesories.remove(accesories)
        self.accesories.append(Cloud())
      accesories.update(accesories.game_speed)
      
  def draw(self,screen):
    for accesories in self.accesories:
      accesories.draw(screen)