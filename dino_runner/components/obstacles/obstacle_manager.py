from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.components.obstacles.bird import Bird
from dino_runner.utils.constants import SCREEN_WIDTH,BIRD

class ObstacleManager:
  def __init__(self):
    self.obstacle_1 = []
    self.obstacle_2 = []
    self.cactus = Cactus()
    self.distance = []
    self.id = [True,True]
    self.step_index = 0
    self.obstacle_1.append(Cactus())
    self.obstacle_2.append(Bird())
    
  def update(self,game_speed,player):
    for i in range(len(self.obstacle_1)):
      if self.id[0]:
        if self.obstacle_1[i].rect.x < (SCREEN_WIDTH/2):
          self.obstacle_1.append(Cactus())
          self.id[0] = False
      if self.obstacle_1[i].rect.x < -self.obstacle_1[i].rect.width:
        self.obstacle_1.remove(self.obstacle_1[i])
        self.obstacle_1.append(Cactus())
      self.obstacle_1[i].update(game_speed,player)
    
    for i in range(len(self.obstacle_2)):
      if self.id[1]:
        if self.obstacle_1[i].rect.x < (SCREEN_WIDTH/2): #((SCREEN_WIDTH/2)+((SCREEN_WIDTH/2)/2)):
          self.obstacle_1.append(Bird())
          self.id[1] = False
      self.obstacle_2[i].image = BIRD[0] if self.step_index < 5 else BIRD[1]
      if self.obstacle_2[i].rect.x < -self.obstacle_2[i].rect.width:
        self.obstacle_2.remove(self.obstacle_2[i])
        self.obstacle_2.append(Bird())
      self.obstacle_2[i].update(game_speed,player)
      self.step_index += 0.9
      
  def draw(self,screen):
    for obstacle in self.obstacle_1:
      obstacle.draw(screen)
      
    for obstacle in self.obstacle_2:
      obstacle.draw(screen)