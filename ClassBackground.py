import pygame
from Config import *

class Background():

    def __init__(self):
        self.skyImage = pygame.image.load(SPRITESHEET_PATH + "\\background\\sky_cloud.png") # Sets my image sky_cloud as Self.
        self.skyImage = pygame.transform.scale(self.skyImage, (SCREEN_WIDTH, SCREEN_HEIGHT))


    def draw(self, displaySurface):
        displaySurface.blit(self.skyImage, (0,0))

        
        
