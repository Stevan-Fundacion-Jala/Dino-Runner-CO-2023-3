import random
from dino_runner.components.obstacles.obstacle import Obstacle
from dino_runner.utils.constants import SMALL_CACTUS,LARGE_CACTUS

class Cactus(Obstacle):
  Y_POS_CACTUS = 325
  
  def __init__(self):
    random_cactus_zise = 1 #random.randrange(1,3)
    if random_cactus_zise == 1: 
      self.image = SMALL_CACTUS[0] #random.choice(SMALL_CACTUS)
      self.Y_POS_CACTUS = 325
    else: 
      self.image = random.choice(LARGE_CACTUS)
      self.Y_POS_CACTUS = 300
    super().__init__(self.image)
    self.rect.y = self.Y_POS_CACTUS