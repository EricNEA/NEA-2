import pygame
from Config import *
from ClassLevel import Level

pygame.init()
displaySurface = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption("My NEA Project") #Sets up the Basic pygame screen lines 5-8 
clock = pygame.time.Clock()

level = Level(displaySurface)

game_running = True

while game_running:

    for event in pygame.event.get(): #This for loop contains where most of the pygame events are handled.
        if event.type == pygame.QUIT:
            game_running = False


    
    pygame.display.flip()#Allows the things drawn onto the screen to be shown and clears the screen so last screen does not show
    
    level.run() # Run functions draws everthing on which would include my backgrounds etc
    
    clock.tick(60)#Caps loop/frame rate to 60

pygame.quit()#Closes pygame
