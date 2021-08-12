import pygame

pygame.init() # initialization

# Screen size setting
screen_width = 480 # width size
screen_height = 640 # height size
screen = pygame.display.set_mode((screen_width, screen_height))

# Screen title setting
pygame.display.set_caption("Python Game") # Game Name

# Load background image
background = pygame.image.load("C:/Users/leehu/Desktop/Python/pygame_basic/background.png")

# Load character(sprite)
character = pygame.image.load("C:/Users/leehu/Desktop/Python/pygame_basic/character.png")
character_size = character.get_rect().size # Get image size
character_width = character_size[0] # character width size
character_height = character_size[1] # character height size
character_x_pos = (screen_width - character_width) / 2  # locate screen width / 2
character_y_pos = screen_height - character_height # locate screen bottom

# position to move
to_x = 0
to_y = 0

# Event loop
running = True # Is the game running?
while running:
    for event in pygame.event.get(): # which event is occured?
        if event.type == pygame.QUIT: # is Window closing event occured?
            running = False # game is not running

        if event.type == pygame.KEYDOWN: # Is key pressed?
            if  event.key == pygame.K_LEFT: # Move character to left
                to_x -= 5 # to_x = to_x -5
            elif  event.key == pygame.K_RIGHT: # Move character to right
                to_x += 5
            elif  event.key == pygame.K_UP: # Move character to up
                to_y -= 5
            elif  event.key == pygame.K_DOWN: # Move character to down
                to_y += 5
        
        if event.type == pygame.KEYUP: # is key not pressed?
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y = 0

    character_x_pos += to_x
    character_y_pos += to_y

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

    screen.blit(background, (0, 0)) # Paint background 
    
    screen.blit(character, (character_x_pos, character_y_pos)) # Print character

    pygame.display.update() # Repaint game screen

# pygame quit
pygame.quit()