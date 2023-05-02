from dino_runner.components.background_accessories.clouds import Cloud

class AccesoriesManager:
  def __init__(self):
    self.accesories = []
    
  def update(self,game_speed):
    if len(self.accesories) == 0:
      self.accesories.append(Cloud())
    for accesories in self.accesories:
      if accesories.rect.x < -accesories.rect.width:
        self.accesories.remove(accesories)
      accesories.update(game_speed)
      
  def draw(self,screen):
    for accesories in self.accesories:
      accesories.draw(screen)