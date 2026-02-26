import pygame
from Config import *
from ClassSpriteSheet import *

runSprites = [
    (24, 16, 40, 52),
    (104, 16, 40, 52),
    (184, 16, 40, 52),
    (264, 16, 40, 52),
    (344, 16, 40, 52),
    (424, 16, 40, 52),
    (504, 16, 40, 52),
    (584, 16, 40, 52)
    ]

idleSprites = [
    (12, 12, 44, 52),
    (76, 12, 44, 52),
    (140, 12, 44, 52),
    (204, 12, 44, 52)
    ]

attackSprites = [
    (4, 0, 92, 80),
    (100, 0, 92, 80),
    (196, 0, 92, 80),
    (294, 0, 92, 80),
    (388, 0, 92, 80),
    (484, 0, 92, 80),
    (580, 0, 92, 80),
    (676, 0, 92, 80)
    ]

class Hero():
    def __init__(self, position, faceRight):

        idleSpriteSheet = SpriteSheet(SPRITESHEET_PATH + "//Assets//SpriteSheets//Character//Idle//Idle-Sheet.png", idleSprites)
        runSpriteSheet = SpriteSheet(SPRITESHEET_PATH + "//Assets//SpriteSheets//Character//Run//Run-Sheet.png", runSprites)
        attackSpriteSheet = SpriteSheet(SPRITESHEET_PATH + "//Assets//SpriteSheets//Character//Attack-01/Attack-01-Sheet.png",attackSprites)

        self.spriteSheets = {
            'IDLE' : idleSpriteSheet,
            'RUN' : runSpriteSheet,
            'ATTACK' : attackSpriteSheet
            }

        self.animationIndex = 0
        self.facingRight = faceRight
        self.currentState = 'IDLE'
        self.xPos = position[0]
        self.yPos = position[1]
        
    def update(self, level):
        self.selectAnimation()

        self.image = self.currentAnimation[int(self.animationIndex)]

        if self.currentState == 'IDLE':
            self.rect = pygame.Rect(self.xPos - 22, self.yPos - 52, 44,52) # changes coords from bottom middle to top left

        self.animationIndex += self.animationSpeed
        if self.animationIndex >= len(self.currentAnimation):
            self.animationIndex = 0
            self.currentState = 'IDLE'
            
    def draw(self, displaySurface):
        displaySurface.blit(self.image, self.rect)

    def selectAnimation(self):
        self.animationSpeed = ANIMSPEED_HERO_DEFAULT
        if self.currentState == 'IDLE':
            self.animationSpeed = ANIMSPEED_HERO_IDLE

        spriteSheet = self.spriteSheets[self.currentState]
        self.currentAnimation = spriteSheet.getSprites(flipped = not self.facingRight)
        
            

