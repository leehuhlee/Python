import pygame
import os

################################################################################
pygame.init() # initialization

# Screen size setting
screen_width = 640 # width size
screen_height = 480 # height size
screen = pygame.display.set_mode((screen_width, screen_height))

# Screen title setting
pygame.display.set_caption("Python Pang") # Game Name

# FPS
clock = pygame.time.Clock()
################################################################################

# 1. Initial User Game(Background, Game Image, Position, Speed, Font, etc)

# Create background
current_path = os.path.dirname(__file__) # return current file path
image_path = os.path.join(current_path, "images") # return images folder path
background = pygame.image.load(os.path.join(image_path, "background.png"))

# Create stage
stage = pygame.image.load(os.path.join(image_path, "stage.png"))
stage_size = stage.get_rect().size
stage_height = stage_size[1] # To put character on the stage

# Create character
character = pygame.image.load(os.path.join(image_path, "character.png"))
character_size = character.get_rect().size # Get image size
character_width = character_size[0] # character width size
character_height = character_size[1] # character height size
character_x_pos = (screen_width - character_width) / 2  # locate screen width / 2
character_y_pos = screen_height - stage_height - character_height # locate screen bottom

# Character move position
character_to_x = 0

# Character move speed
character_speed = 5

# Create weapon
weapon = pygame.image.load(os.path.join(image_path, "weapon.png"))
weapon_size = weapon.get_rect().size
weapon_width = weapon_size[0]

# Weapon can be shoot several times at once
weapons = []

# Weapon speed
weapon_speed = 10

################################################################################

# Event loop
running = True # Is the game running?
while running:
    dt = clock.tick(60) # set second frame count of game screen

    # 2. Event (Keyboard, Mouse, etc)
    for event in pygame.event.get(): # which event is occured?
        if event.type == pygame.QUIT: # is Window closing event occured?
            running = False # game is not running

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT: # Move charater to left
                character_to_x -= character_speed
            elif event.key == pygame.K_RIGHT: # Move character to right
                character_to_x += character_speed
            elif event.key == pygame.K_SPACE: # shoot
                weapon_x_pos = character_x_pos + (character_width - weapon_width) / 2
                weapon_y_pos = character_y_pos
                weapons.append([weapon_x_pos, weapon_y_pos])

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                character_to_x = 0

################################################################################

    # 3. Move Game Character
    character_x_pos += character_to_x

    if character_x_pos <= 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width

    # Set weapon location
    weapons = [[w[0], w[1] - weapon_speed] for w in weapons] # up weapon location
    
    # Remove weapon
    weapons = [[w[0], w[1]] for w in weapons if w[1] > 0]

################################################################################

    # 4. Collision

################################################################################

    # 5. Print Screen

    screen.blit(background, (0, 0)) # Paint background 

    for weapon_x_pos, weapon_y_pos in weapons:
        screen.blit(weapon, (weapon_x_pos, weapon_y_pos))

    screen.blit(stage, (0, screen_height - stage_height))
    screen.blit(character, (character_x_pos, character_y_pos)) # Print character

    

    pygame.display.update() # Repaint game screen

# wait
pygame.timer.delay(2000) # wait 2 second

# pygame quit
pygame.quit()

################################################################################