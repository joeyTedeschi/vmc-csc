import pygame

pygame.init()

# Lets make these variables
display_width = 800
display_height = 600

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('VMC Race Game')

black = (0,0,0)
white = (255,255,255)

# Create a game clock to track time
clock = pygame.time.Clock()
crashed = False
carImg = pygame.image.load('src/racecar.png')

# Lets create a method that will display our car image
def car(x,y):
    # blitting is doing a complete copy of one set of pixels onto another
    # If I were drawing a car, I could do this:
    # circle_surface = pygame.draw.circle(COLOR, RADIUS, WIDTH)
    # screen.blit(circle_surface, POS)
    gameDisplay.blit(carImg, (x,y))

x =  (display_width * 0.45)
y = (display_height * 0.8)

while not crashed:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True

        print(event)

    # Make the background white
    gameDisplay.fill(white)
    
    # Call the method to display the car image
    car(x,y)

    pygame.display.update()
    clock.tick(60)

pygame.quit()
quit()