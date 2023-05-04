import pygame
from dino_runner.utils.constants import MOUSE
class Mouse:
  def __init__(self):
    self.image = pygame.transform.scale(MOUSE[0],(64,63))
    self.mouse_pos = []
    self.mouse_rect = self.image.get_rect()
    self.mouse_rect.x = 0
    self.mouse_rect.x = 0
  
  def update(self):
    pygame.mouse.set_visible(0)
    self.mouse_pos = pygame.mouse.get_pos()
    self.mouse_rect.x = self.mouse_pos[0]
    self.mouse_rect.y = self.mouse_pos[1]
  
  def draw(self,screen):
    screen.blit(self.image,self.mouse_rect)