import random
from dino_runner.components.obstacles.obstacle import Obstacle
from dino_runner.utils.constants import BIRD,SCREEN_WIDTH

class Bird(Obstacle):
  Y_POS_BIRD_1 = 300
  Y_POS_BIRD_2 = 200
  Y_POS_BIRD_3 = 100
  
  def __init__(self):
    self.image = BIRD[0]
    super().__init__(self.image)
    self.rect.y = 100 #self.random_pos_y()
    
  def random_pos_y(self):
    random_pos = random.randrange(1,4)
    if random_pos == 1: return self.Y_POS_BIRD_1
    elif random_pos == 2: return self.Y_POS_BIRD_2
    else: return self.Y_POS_BIRD_3