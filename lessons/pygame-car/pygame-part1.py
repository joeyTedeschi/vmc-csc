import pygame

# pip install pygame
# This will initiate PyGame, and allow you to then make various commands with PyGame and our game.
pygame.init()

# Next, we define our game's display, which is the main "display" for our game.
# The resolution of our game set to 800 px wide and 600 px tall
# The caption of the window is set 
gameDisplay = pygame.display.set_mode((800,600))
pygame.display.set_caption('VMC Race Game')

# Create a game clock to track time
clock = pygame.time.Clock()


crashed = False
while not crashed:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True

        print(event)

    # Display.update can just update specific areas of the screen. 
    # If you do not pass a parameter, then update will update the entire surface as well,
    pygame.display.update()
    
    # Set the Frames per second for the game
    clock.tick(60)

pygame.quit()
quit()