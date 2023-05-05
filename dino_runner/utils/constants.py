import pygame
import os

# Global Constants
TITLE = "Chrome Dino Runner"
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 1100
FPS = 60
IMG_DIR = os.path.join(os.path.dirname(__file__), "..", "assets")

# Assets Constants
ICON = pygame.image.load(os.path.join(IMG_DIR, "DinoWallpaper.png"))

BOTTOM_START = pygame.image.load(os.path.join(IMG_DIR, "Other/Start.png"))
BOTTOM_RETRY = pygame.image.load(os.path.join(IMG_DIR, "Other/Reset.png"))
BOTTOM_START_TYPE = "start"
BOTTOM_RETRY_TYPE = "retry"

DEAD = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDead/DinoDead.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDead/DinoDead1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDead/DinoDead2.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDead/DinoDead3.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDead/DinoDead4.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDead/DinoDead5.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDead/DinoDead6.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDead/DinoDead7.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDead/DinoDead8.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDead/DinoDead9.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDead/DinoDead10.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDead/DinoDead11.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDead/DinoDead12.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDead/DinoDead13.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDead/DinoDead14.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDead/DinoDead15.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDead/DinoDead16.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDead/DinoDead17.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDead/DinoDead18.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDead/DinoDead19.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDead/DinoDead20.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDead/DinoDead21.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDead/DinoDead22.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDead/DinoDead23.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDead/DinoDead24.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDead/DinoDead25.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDead/DinoDead26.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDead/DinoDead27.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDead/DinoDead28.png"))
]

MOUSE = [
    pygame.image.load(os.path.join(IMG_DIR, "mouse.png")),
    pygame.image.load(os.path.join(IMG_DIR, "mouse2.png"))
]

RUNNING = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoRun1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoRun2.png")),
]

RUNNING_SHIELD = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoRun1Shield.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoRun2.png")),
]

RUNNING_HAMMER = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoRun1Hammer.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoRun2Hammer1.png")),
]

JUMPING = pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoJump.png"))
JUMPING_SHIELD = pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoJumpShield.png"))
JUMPING_HAMMER = pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoJumpHammer.png"))

DUCKING = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck2.png")),
]

DUCKING_SHIELD = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck1Shield.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck2.png")),
]

DUCKING_HAMMER = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck1Hammer.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck2Hammer.png")),
]

SMALL_CACTUS = [
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/SmallCactus1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/SmallCactus2.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/SmallCactus3.png")),
]
LARGE_CACTUS = [
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/LargeCactus1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/LargeCactus2.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/LargeCactus3.png")),
]

BIRD = [
    pygame.image.load(os.path.join(IMG_DIR, "Bird/Bird1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Bird/Bird2.png")),
]

CLOUD = [
    pygame.image.load(os.path.join(IMG_DIR, 'Other/Cloud1.png')),
    pygame.image.load(os.path.join(IMG_DIR, 'Other/Cloud2.png')),
    pygame.image.load(os.path.join(IMG_DIR, 'Other/Cloud3.png'))
]

MOUNTAIN = pygame.image.load(os.path.join(IMG_DIR, 'Other/mountain2.png'))

SHIELD = pygame.image.load(os.path.join(IMG_DIR, 'Other/shield.png'))
HAMMER = pygame.image.load(os.path.join(IMG_DIR, 'Other/hammer.png'))
ACCELERATOR = pygame.image.load(os.path.join(IMG_DIR, 'Other/accelerator.png'))

BG = pygame.image.load(os.path.join(IMG_DIR, 'Other/Track.png'))

HEART = pygame.image.load(os.path.join(IMG_DIR, 'Other/SmallHeart.png'))

DEFAULT_TYPE = "default"
SHIELD_TYPE = "shield"
HAMMER_TYPE = "hammer"
ACCELERATOR_TYPE = "accelerator"
