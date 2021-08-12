import pygame

pygame.init() # initialization

# Screen size setting
screen_width = 480 # width size
screen_height = 640 # height size
screen = pygame.display.set_mode((screen_width, screen_height))

# Screen title setting
pygame.display.set_caption("Python Game") # Game Name

# Event loop
running = True # Is the game running?
while running:
    for event in pygame.event.get(): # which event is occured?
        if event.type == pygame.QUIT: # is Window closing event occured?
            running = False # game is not running

# pygame quit
pygame.quit()
