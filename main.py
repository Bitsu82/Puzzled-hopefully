#importing necessary things
import pygame,sys

# 1. Initialize Pygame modules
pygame.init()

# 2. Screen and Window Setup
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Puzzled - Prototype") #name of game for now ont he top bar thing

# Colors (RGB format)
BG_COLOR = (30, 30, 40)          # Dark testing facility background
PLAYER_COLOR = (240, 200, 50)    # Crow yellow color
PLATFORM_COLOR = (100, 110, 130) # Metallic platform color
CAT_COLOR = (220, 60, 60)        # Killer cat hazard color (Red/Dangerous)

# Player Variables 
player_x = 100
player_y = 400
player_width = 40
player_height = 40
player_vel_x = 0
player_vel_y = 0
player_speed = 5
player_jump_force = -11
gravity = 0.5
friction = 0.85  
is_jumping = False

# Clock to control frame rate (FPS)
clock = pygame.time.Clock()
FPS = 60
...
# Main Game Loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


































































































































































































































































