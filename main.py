#importing necessary things
import pygame,sys

# Initialize Pygame modules
pygame.init()

# Screen and Window Setup
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Puzzled - Prototype") #name of game for now ont he top bar thing

# Colors (RGB format)
BG_COLOR = (30, 30, 40)          # Dark testing facility background
PLAYER_COLOR = (240, 200, 50)    # Crow yellow color
PLATFORM_COLOR = (100, 110, 130) # Metallic platform color
CAT_COLOR = (220, 60, 60)        # Killer cat hazard color (Red/Dangerous)

current_level = 1
platforms = []
boxes = []
cats = []
foods = []

# Player Variables 
player_x = 100
player_y = 400
player_width = 40
player_height = 40
player_vel_x = 0
player_vel_y = 0
player_speed = 5
player_jump_force = -12
gravity = 0.5
friction = 0.85  
is_jumping = False

# Clock to control frame rate (FPS)
clock = pygame.time.Clock()
FPS = 60



class Platform:
    def __init__(self, x, y, width, height, color = PLATFORM_COLOR):
        self.rect = pygame.Rect(x, y, width, height)
        self. color = color

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)

class Cat(Platform):
    def __init__ (self, x, y, width, height):
        super().__init__(x, y, width, height, color = CAT_COLOR)

class Food(Platform):
    def __init__(self, x, y, width=30, height=30):
        super().__init__(x, y, width, height, color=(50, 220, 100))

class Box(Platform):
    def __init__(self, x, y, width=40, height=40):
        super().__init__(x, y, width, height, color=(160, 100, 50))
        self.vel_y = 0




def load_level(level_num):
    global current_level, platforms,boxes, cats, foods, player_x, player_y
    current_level = level_num
    
    if level_num == 1:
        platforms = [
            Platform(0, 550, 800, 50),   # Ground floor
            Platform(150, 430, 200, 20), # Platform 1
            Platform(450, 330, 200, 20), # Platform 2
        ]
        cats = [Cat(300, 510, 40, 40)]
        foods = [Food(500, 290)]
        boxes = []
        player_x, player_y = 100, 400
        
    elif level_num == 2:
        platforms = [
            Platform(0, 550, 800, 50),   # Ground floor
            Platform(200, 400, 150, 20), # Level 2 Platform A
            Platform(500, 280, 150, 20), # Level 2 Platform B
        ]
        cats = [Cat(250, 510, 40, 40), Cat(550, 240, 40, 40)]
        foods = [Food(570, 240)] 
        boxes = [Box(300, 500)]
        player_x, player_y = 250, 400
        
# Call Level 1 to start the game
load_level(1)

# Main Game Loop
running = True
while running:
    # jumping and quitting the game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and not is_jumping:
                player_vel_y = player_jump_force
                is_jumping = True
    # movement 
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a] or keys[pygame.K_LEFT]:
        player_vel_x = -player_speed
    if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
        player_vel_x = player_speed

    #friction
    player_vel_x *= friction
    #gravity
    player_vel_y += gravity
    player_y += player_vel_y

# Create a temporary (recreated every frame) hitbox for player collision checking (Y-axis)
    player_rect = pygame.Rect(player_x, player_y, player_width, player_height)
    #vertical collision
    for p in platforms:
        if player_rect.colliderect(p.rect):
            if player_vel_y > 0:  # Falling down onto a platform
                player_y = p.rect.top - player_height
                player_vel_y = 0
                is_jumping = False
            elif player_vel_y < 0:  # Hitting ceiling from below
                player_y = p.rect.bottom
                player_vel_y = 0

   # horizontal movement and screen bounds
    player_x += player_vel_x

    if player_x < 0:
        player_x = 0
    elif player_x > SCREEN_WIDTH - player_width:
        player_x = SCREEN_WIDTH - player_width

    # Recreate hitbox for horizontal wall checks
    player_rect = pygame.Rect(player_x, player_y, player_width, player_height)

    for p in platforms:
        if player_rect.colliderect(p.rect):
            if player_vel_x > 0:  # Moving right into a platform wall
                player_x = p.rect.left - player_width
            elif player_vel_x < 0:  # Moving left into a platform wall
                player_x = p.rect.right

    for b in boxes:
        # Apply gravity to the box so it falls to the ground
        b.vel_y += gravity
        b.rect.y += b.vel_y

        # Box vertical collision with platforms
        for p in platforms:
            if b.rect.colliderect(p.rect):
                if b.vel_y > 0:
                    b.rect.bottom = p.rect.top
                    b.vel_y = 0
    # Push box horizontally when player walks into it
            if player_rect.colliderect(b.rect):
                if player_vel_x > 0:  # Pushing right
                    b.rect.x += player_vel_x
                    player_x = b.rect.left - player_width
                elif player_vel_x < 0:  # Pushing left
                    b.rect.x += player_vel_x
                    player_x = b.rect.right

    # Update hitbox again after wall collision
    player_rect = pygame.Rect(player_x, player_y, player_width, player_height)

    #collision of cat vertical or horizontal
    for c in cats:
        if player_rect.colliderect(c.rect):
            # If you touch killer cats, reset position
            load_level(current_level)
            player_vel_y = 0

    for f in foods[:]:
        if player_rect.colliderect(f.rect):
            foods.remove(f)
            # This automatically loads the next level
            load_level(current_level + 1)



# Screen Refresh
    screen.fill(BG_COLOR)

    # Draw Platforms and Cats
    for p in platforms:
        p.draw(screen)
    for c in cats:
        c.draw(screen)
    for f in foods:
        f.draw(screen)
    for b in boxes:
        b.draw(screen)

    # Draw the player (Yellow Crow block)
    pygame.draw.rect(screen, PLAYER_COLOR, (player_x, player_y, player_width, player_height))

    # Refresh display
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
sys.exit()
    
    





