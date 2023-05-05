from dino_runner.components.power_up.power_up import PowerUp
from dino_runner.utils.constants import ACCELERATOR,ACCELERATOR_TYPE

class Accelerator(PowerUp):
  def __init__(self):
    self.image = ACCELERATOR
    self.type = ACCELERATOR_TYPE
    super().__init__(self.image,self.type)
    