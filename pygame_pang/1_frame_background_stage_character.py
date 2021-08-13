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

################################################################################

# Event loop
running = True # Is the game running?
while running:
    dt = clock.tick(60) # set second frame count of game screen

    # 2. Event (Keyboard, Mouse, etc)
    for event in pygame.event.get(): # which event is occured?
        if event.type == pygame.QUIT: # is Window closing event occured?
            running = False # game is not running

################################################################################

    # 3. Move Game Character

################################################################################

    # 4. Collision

################################################################################

    # 5. Print Screen

    screen.blit(background, (0, 0)) # Paint background 
    screen.blit(stage, (0, screen_height - stage_height))
    screen.blit(character, (character_x_pos, character_y_pos)) # Print character

    pygame.display.update() # Repaint game screen

# wait
pygame.timer.delay(2000) # wait 2 second

# pygame quit
pygame.quit()

################################################################################