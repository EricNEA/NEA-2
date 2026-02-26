import pygame
from Config import *
from ClassSpriteSheet import SpriteSheet


beeSprites = [
    (16, 0, 48, 48),
    (80, 0, 48, 48),
    (144, 0, 48, 48),
    (208, 0, 48, 48)
]


class Bee():

    def __init__(self, position, moveRight):
        # Load spritesheets
        self.flySpriteSheet = SpriteSheet(SPRITESHEET_PATH + "//Assets//SpriteSheets//Mob/Small bee//Fly//Fly-Sheet.png", beeSprites)

        self.image = self.flySpriteSheet.getSprites(moveRight)[0]
        self.rect = self.image.get_rect(bottomleft = position)
        self.movingRight = moveRight
        self.animationIndex = 0
        self.currentState = 'FLY'


    def update(self, level):
        # Update position
        if self.movingRight == False:
            self.rect.x -= SPEED_BEE
        else:
            self.rect.x += SPEED_BEE

        # When the bee gets out of the window turn the sprites around 
        if self.rect.right < 0:
            self.movingRight = True
        if self.rect.left > SCREEN_WIDTH:
            self.movingRight = False

        # Select animation for current action
        self.selectAnimation()

        # Animate sprite
        self.animationIndex += self.animationSpeed
        if self.animationIndex >= len(self.currentAnimation):
            self.animationIndex = 0

        self.image = self.currentAnimation[int(self.animationIndex)]


    def draw(self, displaySurface):
        displaySurface.blit(self.image, self.rect)


    def selectAnimation(self):
        self.animationSpeed = ANIMSPEED_BEE
        if self.currentState == 'FLY':
            self.currentAnimation = self.flySpriteSheet.getSprites(flipped = self.movingRight)

    
