from pygame.font import Font
from dino_runner.utils.constants import SCREEN_WIDTH, SCREEN_HEIGHT

FONT_STYLE = "freesansbold.ttf"
set_color = (0,0,0)
color = set_color

def get_message(message, size, width = SCREEN_WIDTH // 2, height = SCREEN_HEIGHT // 2):
  font = Font(FONT_STYLE, size)
  text = font.render(message, True, color)
  text_rect = text.get_rect()
  text_rect.center = (width, height)
  return text, text_rect