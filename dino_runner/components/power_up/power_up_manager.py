import random
from dino_runner.components.power_up.shield import Shield
from dino_runner.components.power_up.hammer import Hammer

class PowerUpManager:
  def __init__(self):
    self.power_ups = []
    self.random_spawn_power_ups = random.randrange(300,600,10)
    self.select_power_up = [Shield(),Hammer()]
    
  def update(self,game_speed,points,player):
    if points % 200 == 0: 
      self.power_ups.append(Shield())
      #self.random_spawn_power_ups = random.randrange(200,400,10)
    for power_up in self.power_ups:
      if power_up.used or power_up.rect.x < -power_up.rect.width: 
        self.power_ups.remove(power_up)
      if power_up.used: 
        player.set_power_up(power_up)
      power_up.update(game_speed,player)
  
  def draw(self,screen):
    for power_up in self.power_ups:
      power_up.draw(screen)