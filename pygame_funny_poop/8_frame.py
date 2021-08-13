import pygame

################################################################################
pygame.init() # initialization

# Screen size setting
screen_width = 480 # width size
screen_height = 640 # height size
screen = pygame.display.set_mode((screen_width, screen_height))

# Screen title setting
pygame.display.set_caption("Python Game") # Game Name

# FPS
clock = pygame.time.Clock()
################################################################################

# 1. Initial User Game(Background, Game Image, Position, Speed, Font, etc)

# Load background image
background = pygame.image.load("C:/Users/leehu/Desktop/Python/pygame_funny_poop/background.png")

# Load character(sprite)
character = pygame.image.load("C:/Users/leehu/Desktop/Python/pygame_funny_poop/character.png")
character_size = character.get_rect().size # Get image size
character_width = character_size[0] # character width size
character_height = character_size[1] # character height size
character_x_pos = (screen_width - character_width) / 2  # locate screen width / 2
character_y_pos = screen_height - character_height # locate screen bottom

# position to move
to_x = 0
to_y = 0

# speed
character_speed = 0.6

# Enemy character
enemy = pygame.image.load("C:/Users/leehu/Desktop/Python/pygame_funny_poop/enemy.png")
enemy_size = enemy.get_rect().size # Get image size
enemy_width = enemy_size[0] # character width size
enemy_height = enemy_size[1] # character height size
enemy_x_pos = (screen_width - enemy_width) / 2  # locate screen width / 2
enemy_y_pos = (screen_height - enemy_height) / 2 # locate screen bottom

# Define Font
game_font = pygame.font.Font(None, 40) # Create font object(font, size)

# total time
total_time = 10

# start time
start_ticks = pygame.time.get_ticks() # get start tick

################################################################################

# Event loop
running = True # Is the game running?
while running:
    dt = clock.tick(60) # set second frame count of game screen

    # 2. Event (Keyboard, Mouse, etc)
    for event in pygame.event.get(): # which event is occured?
        if event.type == pygame.QUIT: # is Window closing event occured?
            running = False # game is not running

        if event.type == pygame.KEYDOWN: # Is key pressed?
            if  event.key == pygame.K_LEFT: # Move character to left
                to_x -= character_speed # to_x = to_x -5
            elif  event.key == pygame.K_RIGHT: # Move character to right
                to_x += character_speed
            elif  event.key == pygame.K_UP: # Move character to up
                to_y -= character_speed
            elif  event.key == pygame.K_DOWN: # Move character to down
                to_y += character_speed
        
        if event.type == pygame.KEYUP: # is key not pressed?
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y = 0

################################################################################

    # 3. Move Game Character
    character_x_pos += to_x * dt
    character_y_pos += to_y * dt

    # Max x position
    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width

    # Max y position
    if character_y_pos < 0:
        character_y_pos = 0
    elif character_y_pos > screen_height - character_height:
        character_y_pos = screen_height - character_height

################################################################################

    # 4. Collision

    # Update rect information for Collision
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemy_x_pos
    enemy_rect.top = enemy_y_pos

    # Check Collision
    if character_rect.colliderect(enemy_rect):
        print("Collision!")
        running = False

################################################################################

    # 5. Print Screen

    screen.blit(background, (0, 0)) # Paint background 
    screen.blit(character, (character_x_pos, character_y_pos)) # Print character
    screen.blit(enemy, (enemy_x_pos, enemy_y_pos)) # Print enemy

    # timer 
    # calculate time
    elapsed_time = (pygame.time.get_ticks() - start_ticks) / 1000 # /1000 is for changing second unit
    timer = game_font.render(str(int(total_time - elapsed_time)), True, (255, 255, 255)) # letter to print, True, Color
    screen.blit(timer, (10, 10))

    # if timer <= 0, close game
    if total_time - elapsed_time <= 0:
        print("Time Out!")
        running = False

    pygame.display.update() # Repaint game screen

# wait
pygame.timer.delay(2000) # wait 2 second

# pygame quit
pygame.quit()

################################################################################