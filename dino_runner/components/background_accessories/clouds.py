import random
from dino_runner.utils.constants import CLOUD
from dino_runner.components.background_accessories.accesories import Accesories

from dino_runner.components.game import SCREEN_WIDTH
class Cloud(Accesories):
  X_POS_CLOUD = 1200
  Y_POS_CLOUD = random.randrange(50,200)
  
  def __init__(self):
    self.image = random.choice(CLOUD)
    super().__init__(self.image)
    self.rect.y = self.Y_POS_CLOUD
    self.rect.x = self.X_POS_CLOUD