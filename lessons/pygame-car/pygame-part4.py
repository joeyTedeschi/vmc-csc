import pygame

pygame.init()

display_width = 800
display_height = 600
black = (0,0,0)
white = (255,255,255)

# Add red for the block
red = (255,0,0)

# This is the width of the image
car_width = 73

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('VMC Race Game')

clock = pygame.time.Clock()
carImg = pygame.image.load('src/racecar.png')

def car(x,y):
    gameDisplay.blit(carImg, (x,y))

# Make the game loop in its own method
def game_loop():
    x = (display_width * 0.45)
    y = (display_height * 0.8)

    x_change = 0
    car_speed = 0

    # Update the name of this variable so its more descriptive
    gameExit = False

    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5
                if event.key == pygame.K_RIGHT:
                    x_change = 5

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0

        x += x_change

        gameDisplay.fill(white)
        car(x,y)

        # If my image is at far right or the far left
        if x > display_width - car_width or x < 0:
            gameExit = True
            
        pygame.display.update()
        clock.tick(60)

game_loop()
pygame.quit()
quit()