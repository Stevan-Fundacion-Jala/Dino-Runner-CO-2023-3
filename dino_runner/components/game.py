import pygame
import random

from dino_runner.utils.constants import BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS
from dino_runner.components.dinosaur import Dinosaur
from dino_runner.components.obstacles.obstacle_manager import ObstacleManager
from dino_runner.components.background_accessories.accesories_manager import AccesoriesManager
from dino_runner.components.power_up.power_up_manager import PowerUpManager
from dino_runner.components.mouse import Mouse
from dino_runner.components import text_utils

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.running = False
        self.delay_end_game = False
        self.game_speed = 5
        self.points = 0
        self.x_pos_bg = 0
        self.y_pos_bg = 380
        self.player = Dinosaur()
        self.accesories_manager = AccesoriesManager()
        self.obstacle_manager = ObstacleManager()
        self.power_up_manager = PowerUpManager()
        self.mouse = Mouse()
        self.dead_count = 0

    def run(self):
        # Game loop: events - update - draw
        self.running = True
        while self.running:
            self.events()
            self.update()
            self.draw()
        pygame.time.delay(500)
        pygame.quit()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                self.playing = False
            if event.type == pygame.KEYDOWN and not self.playing:
                self.playing = True
                self.reset_game()

    def update(self):
        self.mouse.update()
        if self.playing:
            self.points += 1
            user_input = pygame.key.get_pressed()
            self.player.update()
            self.accesories_manager.update()
            self.obstacle_manager.update(self.game_speed,self.player)
            self.power_up_manager.update(self.game_speed,self.points,self.player)
            if self.player.dino_dead: 
                self.playing = False
                self.dead_count += 1

    def draw(self):
        if self.playing:
            self.clock.tick(FPS)
            self.screen.fill((36, 36, 36))
            self.draw_background()
            self.accesories_manager.draw(self.screen)
            self.obstacle_manager.draw(self.screen)
            self.power_up_manager.draw(self.screen)
            self.player.draw(self.screen)
            self.draw_score()
        else:
            self.draw_menu()
        self.mouse.draw(self.screen)
        pygame.display.update()
        pygame.display.flip()

    def draw_background(self):
        image_width = BG.get_width()
        self.screen.blit(BG, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
        if self.x_pos_bg <= -image_width:
            self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
            self.x_pos_bg = 0
        self.x_pos_bg -= self.game_speed
        
    def draw_score(self):
        score, score_rect = text_utils.get_message("Score: "+ str(self.points), 20, 1000, 40)
        self.screen.blit(score,score_rect)
        
    def draw_menu(self):
        white_color = (36,36,36)
        self.screen.fill(white_color)
        if self.dead_count == 0:
            text,text_rect = text_utils.get_message("Press any key to start",30)
            self.screen.blit(text, text_rect)
        else:
            text,text_rect = text_utils.get_message("Press any key to Restart",30)
            score, score_rect = text_utils.get_message("Your Score: "+ str(self.points), 30, height= SCREEN_HEIGHT//2 + 50)
            self.screen.blit(text, text_rect)
            self.screen.blit(score, score_rect)

    def reset_game(self):
        self.game_speed = 5
        self.player = Dinosaur()
        self.obstacle_manager = ObstacleManager()
        self.power_up_manager = PowerUpManager()
        self.points = 0