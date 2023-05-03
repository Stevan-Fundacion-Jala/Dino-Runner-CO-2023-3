import random
from dino_runner.utils.constants import CLOUD
from dino_runner.components.background_accessories.accesories import Accesories

from dino_runner.components.game import SCREEN_WIDTH
class Cloud(Accesories):
  def __init__(self):
    self.image = random.choice(CLOUD)
    super().__init__(self.image)
    self.rect.y = random.randrange(20,260)
    self.game_speed = random.randrange(5,10)