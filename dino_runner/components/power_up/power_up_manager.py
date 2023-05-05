import random
from dino_runner.components.power_up.shield import Shield
from dino_runner.components.power_up.hammer import Hammer
from dino_runner.components.power_up.accelerator import Accelerator

class PowerUpManager:
  def __init__(self):
    self.power_ups = []
    self.random_spawn_power_ups = random.randrange(300,600,10)
    self.select_power_up = [Shield(),Hammer(),Accelerator()]
    self.power_up_print = [Shield()]
    
  def update(self,game_speed,points,player):
    if not player.power_up_use and len(self.power_ups) == 0:
      if points % 200 == 0: 
        self.power_ups.append(random.choice(self.select_power_up))
        self.random_spawn_power_ups = random.randrange(200,630,10)
    for power_up in self.power_ups:
      if power_up.used or power_up.rect.x < -power_up.rect.width: 
        self.power_ups.remove(power_up)
      if power_up.used:
        self.power_up_print.remove(self.power_up_print[0])
        self.power_up_print.append(power_up)
        player.set_power_up(power_up)
      power_up.update(game_speed,player)
    self.power_up_print[0].print_power_up(player)
  
  def draw(self,screen):
    for power_up in self.power_ups:
      power_up.draw(screen)
    self.power_up_print[0].draw(screen)