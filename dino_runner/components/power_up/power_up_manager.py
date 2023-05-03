from dino_runner.components.power_up.shield import Shield
from dino_runner.components.power_up.hammer import Hammer

class PowerUpManager:
  def __init__(self):
    self.power_ups = []
    
  def update(self,game_speed,points,player):
    if points % 220 == 0: 
      self.power_ups.append(Shield())
    if points % 350 == 0: 
      self.power_ups.append(Hammer())
    for power_up in self.power_ups:
      if power_up.used or power_up.rect.x < -power_up.rect.width: 
        self.power_ups.remove(power_up)
      if power_up.used: player.set_power_up(power_up)
      #else: player.set_power_up("DEFAULT_TYPE")
      power_up.update(game_speed,player)
  
  def draw(self,screen):
    for power_up in self.power_ups:
      power_up.draw(screen)