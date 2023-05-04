import random
from dino_runner.components.obstacles.obstacle import Obstacle
from dino_runner.utils.constants import BIRD,SCREEN_WIDTH

class Bird(Obstacle):
  Y_POS_BIRD = [320,260,200]
  
  def __init__(self):
    self.image = BIRD[0]
    super().__init__(self.image)
    self.rect.y = random.choice(self.Y_POS_BIRD)