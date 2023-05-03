from dino_runner.utils.constants import SCREEN_WIDTH

class Accesories:
  def __init__(self,image):
    self.image = image
    self.rect = self.image.get_rect()
    self.rect.x = SCREEN_WIDTH
  
  def pos_init(self,pos_x):
    self.rect.x = pos_x
  
  def update(self,game_speed):
    self.rect.x -= game_speed

  def draw(self,screen):
    screen.blit(self.image,self.rect)