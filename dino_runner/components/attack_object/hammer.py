from dino_runner.utils.constants import HAMMER

class HammerObject:
  POS_X = 320
  def __init__(self):
    self.image = HAMMER
    self.hammer_rect = self.image.get_rect()
    self.hammer_rect.x = self.POS_X
    
    