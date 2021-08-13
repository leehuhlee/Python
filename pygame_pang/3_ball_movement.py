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

# Create ball
ball_images = [
    pygame.image.load(os.path.join(image_path, "balloon1.png")),
    pygame.image.load(os.path.join(image_path, "balloon2.png")),
    pygame.image.load(os.path.join(image_path, "balloon3.png")),
    pygame.image.load(os.path.join(image_path, "balloon4.png"))]

# ball speed
ball_speed_y = [-18, -15, -12, -9] # value of index 0, 1, 2, 3

# balls
balls = []

balls.append({
    "pos_x" : 50, # x pos of ball
    "pos_y" : 50, # y pos of ball
    "img_idx" : 0, # image index of ball
    "to_x" : 3, # move direction of x axis 
    "to_y" : -6, # move direction of y axis
    "init_spd_y" : ball_speed_y[0] # first y speed
})

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

    # Define ball location
    for ball_idx, ball_val in enumerate(balls):
        ball_pos_x = ball_val["pos_x"]
        ball_pos_y = ball_val["pos_y"]
        ball_img_idx = ball_val["img_idx"]

        ball_size = ball_images[ball_img_idx].get_rect().size
        ball_width = ball_size[0]
        ball_height = ball_size[1]

        # move ball position when ball touch horizental wall
        if ball_pos_x < 0 or ball_pos_x > screen_width - ball_width:
            ball_val["to_x"] = ball_val["to_x"] * -1

        # move ball position when ball touch vertical wall
        if ball_pos_y >= screen_height - stage_height - ball_height:
            ball_val["to_y"] = ball_val["init_spd_y"]
        else:
            ball_val["to_y"] += 0.5

        ball_val["pos_x"] += ball_val["to_x"]
        ball_val["pos_y"] += ball_val["to_y"]
        

################################################################################

    # 4. Collision

################################################################################

    # 5. Print Screen

    screen.blit(background, (0, 0)) # Paint background 

    for weapon_x_pos, weapon_y_pos in weapons:
        screen.blit(weapon, (weapon_x_pos, weapon_y_pos))

    for idx, val in enumerate(balls):
        ball_pos_x = val["pos_x"]
        ball_pos_y = val["pos_y"]
        ball_img_idx - val["img_idx"]
        screen.blit(ball_images[ball_img_idx], (ball_pos_x, ball_pos_y))

    screen.blit(stage, (0, screen_height - stage_height))
    screen.blit(character, (character_x_pos, character_y_pos)) # Print character

    pygame.display.update() # Repaint game screen

# wait
pygame.timer.delay(2000) # wait 2 second

# pygame quit
pygame.quit()

################################################################################