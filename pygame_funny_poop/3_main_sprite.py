import pygame

pygame.init() # initialization

# Screen size setting
screen_width = 480 # width size
screen_height = 640 # height size
screen = pygame.display.set_mode((screen_width, screen_height))

# Screen title setting
pygame.display.set_caption("Python Game") # Game Name

# Load background image
background = pygame.image.load("C:/Users/leehu/Desktop/Python/pygame_funny_poop/background.png")

# Load character(sprite)
character = pygame.image.load("C:/Users/leehu/Desktop/Python/pygame_funny_poop/character.png")
character_size = character.get_rect().size # Get image size
character_width = character_size[0] # character width size
character_height = character_size[1] # character height size
character_x_pos = (screen_width - character_width) / 2  # locate screen width / 2
character_y_pos = screen_height - character_height # locate screen bottom

# Event loop
running = True # Is the game running?
while running:
    for event in pygame.event.get(): # which event is occured?
        if event.type == pygame.QUIT: # is Window closing event occured?
            running = False # game is not running

    screen.blit(background, (0, 0)) # Paint background 
    
    screen.blit(character, (character_x_pos, character_y_pos)) # Print character

    pygame.display.update() # Repaint game screen

# pygame quit
pygame.quit()
