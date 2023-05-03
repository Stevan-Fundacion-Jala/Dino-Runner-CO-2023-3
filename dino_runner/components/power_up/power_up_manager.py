from dino_runner.components.power_up.shield import Shield

class PowerUpManager:
  def __init__(self):
    self.power_ups = []
    self.power_ups.append(Shield())
    
  def update(self):
    pass
  
  def draw(self,screen):
    for power_up in self.power_ups:
      power_up.draw(screen)