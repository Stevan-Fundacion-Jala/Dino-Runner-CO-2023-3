from dino_runner.utils.constants import SCREEN_WIDTH,BIRD

class Obstacle:
  def __init__(self,image):
    self.image = image
    self.rect = self.image.get_rect()
    self.rect.x = SCREEN_WIDTH
    
  def pos_init(self,pos_x):
    self.rect.x = pos_x
  
  def update(self,game_speed,player,id,pos_x,sprite):
    if id == 0: self.rect.x -= game_speed
    else:
      if id == 1:
        self.image = BIRD[0] if sprite < 5 else BIRD[1]
      if self.rect.x > (SCREEN_WIDTH-100):
        self.rect.x = pos_x + (SCREEN_WIDTH/4)
      else: self.rect.x -= game_speed
    if self.rect.colliderect(player.dino_rect):
      player.collider = True
      player.rect_x_obstacle = self.rect.x
      player.rect_y_obstacle = self.image.get_height()
      if not player.shield:
        player.dino_dead = True

  def draw(self,screen):
    screen.blit(self.image,self.rect)