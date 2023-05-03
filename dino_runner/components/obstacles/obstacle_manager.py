from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.components.obstacles.bird import Bird
from dino_runner.utils.constants import SCREEN_WIDTH

class ObstacleManager:
  def __init__(self):
    self.obstacle_1 = []
    self.obstacle_2 = []
    self.cactus = Cactus()
    self.distance = []
    self.id = [True,True]
    self.step_index = 0
    self.pos_x = SCREEN_WIDTH
    for i in range(2):
      self.obstacle_1.append(Cactus())
      self.obstacle_1[i].pos_init(self.pos_x)
      self.pos_x += int((SCREEN_WIDTH/2))
    self.pos_x = SCREEN_WIDTH + int((SCREEN_WIDTH/4))
    for i in range(2):
      self.obstacle_2.append(Bird())
      self.obstacle_2[i].pos_init(self.pos_x)
      self.pos_x += int((SCREEN_WIDTH/2))
    
  def update(self,game_speed,player):
    for i in range(len(self.obstacle_1)):
      if self.obstacle_1[i].rect.x < -self.obstacle_1[i].rect.width:
        self.obstacle_1.remove(self.obstacle_1[i])
        self.obstacle_1.append(Cactus())
      self.obstacle_1[i].update(game_speed,player,0,0,0)
    
    for i in range(len(self.obstacle_2)):
      self.step_index += 0.1
      if self.obstacle_2[i].rect.x < -self.obstacle_2[i].rect.width:
        self.obstacle_2.remove(self.obstacle_2[i])
        self.obstacle_2.append(Bird())
      self.obstacle_2[i].update(game_speed,player,1,self.obstacle_1[i].rect.x,self.step_index)
    if self.step_index >= 10:
      self.step_index = 0
      
  def draw(self,screen):
    for obstacle in self.obstacle_1:
      obstacle.draw(screen)
      
    for obstacle in self.obstacle_2:
      obstacle.draw(screen)