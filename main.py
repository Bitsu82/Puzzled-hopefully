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
buttons = []
doors = []

# Player Variables 
player_x = 100
player_y = 400
player_width = 40
player_height = 40
player_vel_x = 0
player_vel_y = 0
player_speed = 5
player_jump_force = -13
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

class Button(Platform):
    def __init__(self, x, y):
        super().__init__(x, y, 30, 15, color=(255, 220, 0)) # Gold pressure plate

class Door(Platform):
    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height, color=(80, 160, 220)) # Blue barrier door

def load_level(level_num):
    global current_level, platforms,boxes, cats, foods, buttons, doors, player_x, player_y
    current_level = level_num
    
    if level_num == 1:

        platforms = [
            Platform(0, 550, 800, 50),   # Ground floor
            Platform(150, 430, 200, 20), # Platform 1
            Platform(450, 330, 200, 20), # Platform 2
        ]
        cats = [Cat(200, 390, 40, 40)]
        foods = [Food(500, 290)]
        boxes = []
        buttons = []
        doors = []
        player_x, player_y = 100, 400
        
    elif level_num == 2:

        platforms = [
            Platform(0, 550, 800, 50),   # Ground floor
            Platform(300, 420, 150, 20), # Level 2 Platform A
            Platform(600, 220, 150, 20), # Level 2 Platform B
        ]
        cats = [Cat(450, 510, 40, 40)]
        foods = [Food(660, 200)] 
        boxes = [Box(350, 380)]
        buttons = []
        doors = []
        player_x, player_y = 50, 400

    elif level_num == 3:

        platforms = [
            Platform(0, 550, 800, 50),   # Ground
            Platform(500, 400, 200, 20), # High ledge holding food
        ]
        cats = []
        foods = [Food(600, 350)]         # Food behind the door
        boxes = []
        buttons = [Button(200, 530)]     # Button on the ground
        doors = [Door(500, 350, 20, 70),Door(685, 350, 15, 70)] # Door blocking access to the ledge
        player_x, player_y = 500, 500

    elif level_num == 4:

        platforms = [
            Platform(0, 550, 800, 50),
            Platform(100, 430, 120, 20),
            Platform(300, 330, 120, 20),
            Platform(520, 230, 150, 20),
        ]
        cats = [Cat(320, 290, 40, 40)]
        foods = [Food(580, 190)]
        boxes = []
        buttons = []
        doors = []
        player_x, player_y = 50, 500

    elif level_num == 5:

        platforms = [
            Platform(0, 550, 800, 50),   # Ground floor
            Platform(500, 350, 180, 20), # High platform holding food
        ]
        cats = [Cat(200, 510, 40, 40)]   # Cat safely placed on the left
        foods = [Food(580, 270)]         # Food on the high platform
        boxes = [Box(550, 500)]          # Box placed with room to breathe, ready to push right
        buttons = []
        doors = []
        player_x, player_y = 50, 400     #

    elif level_num == 6:

        platforms = [
            Platform(0, 550, 800, 50),   # Ground floor
            Platform(100, 420, 180, 20), # Button platform 
            Platform(600, 350, 180, 20), # Food & door platform 
        ]
        cats = [
            Cat(170, 380, 40, 40),       # Cat on platform 1
        ]
        foods = [Food(690, 300)]         # Food tucked safely behind the door
        boxes = [Box(80, 500)]           # Box on the floor
        buttons = [Button(120, 405)]     # Button on platform 1
        doors = [
            Door(680, 280, 20, 70),  # Door directly blocking the food
        ] 

        player_x, player_y = 50, 400     # Player start

    elif level_num == 7:
        platforms = [
            Platform(0, 550, 800, 50),   # Ground floor
            Platform(150, 430, 150, 20), # Ledge holding the box
            Platform(450, 320, 200, 20), # High platform holding the food
        ]
        cats = [
            Cat(300, 510, 40, 40),       # Ground patroller guarding the button area
        ]
        foods = [Food(540, 270)]         
        boxes = [Box(180, 390)]           
        buttons = [Button(350, 530)]     
        doors = [
            Door(450, 250, 20, 70),      # Door blocking access to the high platform
        ] 

        player_x, player_y = 50, 400

    elif level_num == 8:
        platforms = [
            Platform(0, 550, 800, 50),   # Ground floor
            Platform(150, 490, 140, 20), # 1st platform 
            Platform(380, 360, 120, 20), # Step 2
            Platform(600, 240, 180, 20), # Final ledge holding food
        ]
        cats = [
            Cat(300, 510, 40, 40),       # Ground cat (safely away from the button)
            Cat(420, 320, 40, 40),       # Cat on Step 2
        ]
        foods = [Food(670, 190)]         # Final victory food
        boxes = [Box(180, 450)]          # Box sitting on the 1st platform
        buttons = [Button(210, 475)]     # Button on the 1st platform
        doors = [
            Door(600, 170, 20, 70),      # Final door guarding the food
        ] 
        player_x, player_y = 50, 400    
        
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
    for p in platforms + doors + boxes:
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

    for p in platforms + doors:
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
                if player_rect.bottom > b.rect.top + 10:
                    if player_vel_x > 0:  # Pushing right
                        b.rect.x += player_vel_x
                        player_x = b.rect.left - player_width
                    elif player_vel_x < 0:  # Pushing left
                        b.rect.x += player_vel_x
                        player_x = b.rect.right

    # Update hitbox again after wall collision
    player_rect = pygame.Rect(player_x, player_y, player_width, player_height)

    button_pressed = False
    for btn in buttons:
        if player_rect.colliderect(btn.rect):
            button_pressed = True
        for b in boxes:
            if b.rect.colliderect(btn.rect):
                button_pressed = True
                
    if button_pressed:
        doors = [] # Erase the door from existence


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
    for d in doors:
        d.draw(screen)
    for btn in buttons:
        btn.draw(screen)        
    for b in boxes:
        b.draw(screen)
    for f in foods:
        f.draw(screen) 
    for c in cats:
        c.draw(screen)


    # Draw the player (Yellow Crow block)
    pygame.draw.rect(screen, PLAYER_COLOR, (player_x, player_y, player_width, player_height))

    # Refresh display
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
sys.exit()
    
    