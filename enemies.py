# enemies.py

import pygame
from random import randint

from settings import *
from tools import random_coords

class Enemy:
    """ Parent class for enemies """
    
    def __init__(self, all_sprites, enemies):

        # Initialize groups
        self.all_sprites = all_sprites
        self.enemies = enemies
        
        # Spawn the first enemies
        self.spawn_enemies()

    def spawn_enemies(self):
        
        ufo = Ufo() 
        self.enemies.add(ufo)
        self.all_sprites.add(ufo)
    
    def update_enemies(self, bullets):
        
        # Kill enemy if hit by a bullet
        if pygame.sprite.groupcollide(bullets, self.enemies, True, True):
            self.spawn_enemies()
            print("[INFO] Enemy was hit!")

        

class Ufo(pygame.sprite.Sprite):
    """ A ufo that shoots lazers"""

    def __init__(self):
       
        # Initialize sprites
        super().__init__()

        # Initialize characteristics
        self.health = 100

        # Initialize bullet
        self.image = pygame.image.load("graphics/enemies/ufo/0.png")
        self.rect = self.image.get_rect()

        # Spawn ufo above the screen
        self.ufo_x = random_coords(self.rect.width)
        self.ufo_y = -100

    def update(self, dt):

        # Drop the Ufo from the sky
        if self.ufo_y < 100:
            self.ufo_y += 1

        # Display ufo
        SCREEN.blit(self.image, (self.ufo_x, self.ufo_y))

        # Move the rect
        self.rect.y = self.ufo_y
        self.rect.x = self.ufo_x



class Cow(pygame.sprite.Sprite):
    """ A flying cow """

    def __init__(self):
       
        # Initialize sprites
        super().__init__()

        # Initialize starting location
        self.cow_x = randint(0, SCREEN_WIDTH - 150)
        self.cow_y = 100

        # Initialize characteristics
        self.colour = "white"
        self.healt = 100

    def update(self, dt):

        # Set up rectangle
        self.rect = pygame.draw.rect(
            SCREEN,
            self.colour,
            pygame.Rect(self.cow_x, self.cow_y, 150, 100)
        )


