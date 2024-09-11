# enemies.py

import pygame
from random import randint

from settings import *
from tools import random_coords

class Enemy:
    """ Parent class for enemies """
    
    def __init__(self, all_sprites, enemies, player):

        # Initialize groups
        self.all_sprites = all_sprites
        self.enemies = enemies
        
        self.player = player
        
        # Spawn the first enemies
        self.spawn_enemies()


    def spawn_enemies(self):
        
        ufo = Ufo(self.player) 
        self.enemies.add(ufo)
        self.all_sprites.add(ufo)
    
    def update_enemies(self, bullets):
        
        # Kill enemy if hit by a bullet
        if pygame.sprite.groupcollide(bullets, self.enemies, True, True):
            self.spawn_enemies()
            print("[INFO] Enemy was hit!")
        

class Ufo(pygame.sprite.Sprite):
    """ A ufo that shoots lazers"""

    def __init__(self, player):
       
        # Initialize sprites
        super().__init__()

        # Set player
        self.player = player

        # Initialize characteristics
        self.health = 100

        # Load image
        self.image = pygame.image.load("graphics/enemies/ufo/0.png")
       
        # Randomize the x coordinate and spawn the rect
        x_coord = random_coords(100)
        self.rect = self.image.get_rect(center = (x_coord, -100))

        # Movement
        self.pos = pygame.math.Vector2(self.rect.center)
        self.speed = 1



    def move(self, dt):

        # Drop the Ufo from the sky
        if self.pos.y < 100:
            self.pos.y += 1

        # Get the direction of the ufo
        direction = self.player.pos - self.pos

        # Normalize the Vector
        # Again, wizard shit
        if direction.length() != 0:
            direction = direction.normalize()

        # Move the ufo to the player
        self.pos += direction * self.speed

        # Display ufo and rect
        self.rect.x = self.pos.x
        self.rect.y = self.pos.y
        SCREEN.blit(self.image, self.pos)



    def update(self, dt):

        self.move(dt)


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


