import pygame
from Config import *
from ClassBackground import Background
from ClassBee import Bee
from ClassHero import Hero
from WorldClasses import Decoration, Water, Exit
import sys
import csv

SPRITESHEET_PATH = "pygame-assets//img//Assets//SpriteSheets//"

FPS = 60

GRAVITY = 0.6
screen_scroll = 0

SCREEN_WIDTH, SCREEN_HEIGHT = 1100,740
SPEED_HERO = 4

ANIMSPEED_HERO_DEFAULT = 0.25
ANIMSPEED_HERO_IDLE = 0.1

ANIMSPEED_BEE_ATTACK = 0.5
ANIMSPEED_BEE = 0.2
SPEED_BEE = 2






class Level():
    def __init__(self, displaySurface):

        self.ROWS = 16
        self.MAX_COLS = 150
        self.SCREEN_HEIGHT = SCREEN_HEIGHT
        self.SCREEN_WIDTH = SCREEN_WIDTH
        self.TILE_SIZE = self.SCREEN_HEIGHT // self.ROWS
        self.TILE_TYPES = 19
        self.level = 1
        self.current_tile = 0
        self.scroll_left = False
        self.scroll_right = False
        self.scroll_speed = 1
        self.screen_scroll = 0
        self.delta_scroll = 0
        self.map_scroll = 0
        
        self.world_data = []
        self.obstacle_list = []

        self.img_list = []
        for x in range(self.TILE_TYPES):
            if x == 15:
                img = pygame.image.load(f'pygame-assets//img//tile//{x}.png').convert_alpha()
                img = pygame.transform.scale(img, (self.TILE_SIZE, self.TILE_SIZE * 2))
                self.img_list.append(img)
            else:
                img = pygame.image.load(f'pygame-assets//img//tile//{x}.png').convert_alpha()
                img = pygame.transform.scale(img, (self.TILE_SIZE, self.TILE_SIZE))
                self.img_list.append(img)

        #Instatiate/creates my classes
 
        self.background = Background()

        self.hero = pygame.sprite.GroupSingle()
        self.bees = pygame.sprite.Group()
        self.decoration = pygame.sprite.Group()
        self.water = pygame.sprite.Group()
        self.exit = pygame.sprite.Group()
        
        self.displaySurface = displaySurface

        for row in range(self.ROWS):
            r = [-1] * self.MAX_COLS
            self.world_data.append(r)
        #load in level data
        with open("level"+str(self.level)+"_data.csv", newline = '') as csvfile:
            reader = csv.reader(csvfile, delimiter=',')
            for x, row in enumerate(reader):
                for y, tile in enumerate(row):
                    self.world_data[x][y] = int(tile)

        self.process_data(self.world_data)

    def process_data(self, data):
        
        for y, row in enumerate(data):
            for x, tile in enumerate(row):
                if tile >= 0:
                    img = self.img_list[tile]
                    img_rect = img.get_rect()
                    img_rect.x = x * self.TILE_SIZE
                    img_rect.y = y * self.TILE_SIZE
                    tile_data = (img, (img_rect.x,img_rect.y))
                    if tile >= 0 and tile <= 8:
                        self.obstacle_list.append(tile_data)
                    elif tile >= 9 and tile <= 10:
                        water = Water(img, x * self.TILE_SIZE, y * self.TILE_SIZE)
                        self.water.add(water)
                    elif tile >= 11 and tile <= 14:
                        decoration = Decoration(img, x * self.TILE_SIZE , y * self.TILE_SIZE + 15)
                        self.decoration.add(decoration)
                    elif tile == 15:#create player
                        self.hero.add(Hero((x * self.TILE_SIZE, y * self.TILE_SIZE), faceRight = True))
                        pass
                    elif tile == 16:#exit
                        exits = Exit(img, x * self.TILE_SIZE , y * self.TILE_SIZE )
                        self.exit.add(exits)
                    elif tile == 17:
                        self.bees.add(Bee((x * self.TILE_SIZE, y * self.TILE_SIZE), moveRight = False))
                        pass
                    elif tile == 18:
                        self.bees.add(Bee((x * self.TILE_SIZE, y * self.TILE_SIZE), moveRight = True))

     
                        
    #def draw_world(self,screen):
        #for img, (x, y) in self.obstacle_list:
        # Create a new position with scrolling applied
            #print(self.map_scroll)
            #screen.blit(img, (x + screen_scroll,y))
            #screen.blit(img, (x,y))

    def draw_world(self,screen):
        for tile in self.obstacle_list:
        # Create a new position with scrolling applied
            #tile[1][0] + self.screen_scroll
            screen.blit(tile[0],(tile[1][0]+ self.delta_scroll,tile[1][1]))
            #screen.blit(img, (x,y))
            
                    
    #self.process_data()
                    

    def update(self):#This Method should handle game logic
        #self.hero.update(self, self.obstacle_list)
        self.screen_scroll = self.hero.sprite.update(self, self.obstacle_list)
        self.delta_scroll = self.screen_scroll
        #if self.screen_scroll == 0:
        #    self.delta_scroll = 0
        #else:
        #    self.delta_scroll += self.screen_scroll
        #print(screen_scroll)
        #self.screen_scroll = int(scroll_delta or 0)
        self.bees.update(self)
        self.decoration.update(self)
        self.water.update(self)
        self.exit.update(self)

    def draw(self):#This should draw the things onto the screen
        self.background.draw(self.displaySurface)
        self.draw_world(self.displaySurface)
        self.hero.draw(self.displaySurface)
        self.bees.draw(self.displaySurface)
        self.decoration.draw(self.displaySurface)
        self.water.draw(self.displaySurface)
        self.exit.draw(self.displaySurface)

        
    def run(self):
        print(self.screen_scroll)
        self.update()
        self.draw()
