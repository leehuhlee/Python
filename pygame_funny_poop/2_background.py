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

# Event loop
running = True # Is the game running?
while running:
    for event in pygame.event.get(): # which event is occured?
        if event.type == pygame.QUIT: # is Window closing event occured?
            running = False # game is not running

    #screen.fill((0, 0, 255))
    screen.blit(background, (0, 0)) # Paint background 
    
    pygame.display.update() # Repaint game screen

# pygame quit
pygame.quit()
