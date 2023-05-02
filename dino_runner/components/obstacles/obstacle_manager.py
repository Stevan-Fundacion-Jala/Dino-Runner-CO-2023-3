from dino_runner.components.obstacles.cactus import Cactus

class ObstacleManager:
  def __init__(self):
    self.obstacle = []
    
  def update(self,game_speed,player):
    if len(self.obstacle) == 0:
      self.obstacle.append(Cactus())
    for obstacle in self.obstacle:
      if obstacle.rect.x < -obstacle.rect.width:
        self.obstacle.remove(obstacle)
      obstacle.update(game_speed,player)
      
  def draw(self,screen):
    for obstacle in self.obstacle:
      obstacle.draw(screen)