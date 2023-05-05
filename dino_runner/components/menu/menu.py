import pygame
from dino_runner.utils.constants import SCREEN_WIDTH,SCREEN_HEIGHT,BOTTOM_RETRY,BOTTOM_START,BOTTOM_RETRY_TYPE,BOTTOM_START_TYPE
from dino_runner.components.menu.bottom_start import BottomStart

class Menu:
  POS_X = int(SCREEN_WIDTH/2)
  POS_Y = int(SCREEN_HEIGHT/2)
  def __init__(self):
    self.bottom_start_image = BOTTOM_START
    self.bottom_retry_image = BOTTOM_RETRY
    self.bottom_start_rect = self.bottom_start_image.get_rect()
    self.bottom_retry_rect = self.bottom_retry_image.get_rect()
    self.bottom_start_image_width = self.bottom_start_image.get_width()
    self.width = self.bottom_retry_image.get_width()
    self.bottom_start_image_height = self.bottom_start_image.get_height()
    self.height = self.bottom_retry_image.get_height()
    self.bottom_start_rect.x = self.POS_X - (self.width/2)
    self.bottom_start_rect.y = self.POS_Y - (self.height/2)
    self.bottom_start = BottomStart()
    self.bottom_retry = BottomStart()
    self.click_start = False
  def update(self):
    for i in pygame.event.get():
      if i.type == pygame.MOUSEBUTTONDOWN and i.button == 1:
        x,y = pygame.mouse.get_pos()
        if x <= self.bottom_start_image_width and x >= self.bottom_start_image_width:
          self.click_start = True
          print("Click")
        else: print("No_click")
        
    
  def draw(self,screen):
      screen.blit(self.bottom_start_image,self.bottom_start_rect)