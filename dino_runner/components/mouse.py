import pygame
from dino_runner.utils.constants import MOUSE
class Mouse:
  def __init__(self):
    self.image = MOUSE[0]
  
  def update(self):
    pass
  
  def draw(self,screen):
    screen.blit(self.image,self.dino_rect)