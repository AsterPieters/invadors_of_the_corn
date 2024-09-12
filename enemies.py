# enemies.py

import pygame
import time
from random import randint

from settings import *
from bullet import Laser
from tools import random_coords

class Enemy:
    """ Parent class for enemies """
    
    def __init__(self, all_sprites, enemies, player, lasers):

        # Initialize groups
        self.all_sprites = all_sprites
        self.enemies = enemies
        self.lasers = lasers
        
        self.player = player
        
        # Spawn the first enemies
        self.spawn_enemies()



    def spawn_enemies(self):

        #TODO: make multiple enemies with levels
        ufo = Ufo(self.player, self.all_sprites, self.lasers) 
        self.enemies.add(ufo)
        self.all_sprites.add(ufo)



    def update_enemies(self, bullets):
        
        # Kill enemy if hit by a bullet
        if pygame.sprite.groupcollide(bullets, self.enemies, True, True):
            self.spawn_enemies()
            print("[INFO] Enemy was hit!")
        
        # Kill player if hit by a laser
        if pygame.sprite.spritecollide(self.player, self.lasers, True):
            print("[INFO] Player was hit!")
            self.player.die()



class Ufo(pygame.sprite.Sprite):
    """ A ufo that shoots lazers"""

    def __init__(self, player, all_sprites, lasers):
       
        # Initialize sprites
        super().__init__()

        # Set player
        self.player = player

        self.all_sprites = all_sprites
        self.lasers = lasers

        # Initialize characteristics
        self.last_ts = time.time()
        self.health = 100

        # Load image
        self.image = pygame.image.load("graphics/enemies/ufo/0.png")
       
        # Randomize the x coordinate and spawn the rect
        x_coord = random_coords(100)
        self.rect = self.image.get_rect(center = (x_coord, -100))

        # Movement
        self.pos = pygame.math.Vector2(self.rect.center)
        self.speed = 1
        self.flying_up = False



    def move(self, dt):

        # Get the direction of the ufo
        direction = self.player.pos - self.pos

        # Normalize the Vector
        # Again, wizard shit
        if direction.length() != 0:
            direction = direction.normalize()

        # Send ufo back up when too low 
        if self.pos.y >= 300:
            self.flying_up = True

        # Send ufo down when too high up
        elif self.pos.y <= 50:
            self.flying_up = False

        # Go up but follow player
        if self.flying_up:
            self.pos.x += direction[0] * self.speed
            self.pos.y -= direction[1] * self.speed
        
        # Go down but follow player
        else:
            self.pos += direction * self.speed

        # Display ufo and rect
        self.rect.x = self.pos.x
        self.rect.y = self.pos.y
        SCREEN.blit(self.image, self.pos)



    def shoot_laser(self): 
       
        # Cooldown function
        # Get current timestamp
        current_ts = time.time()
        
        # Compare last timestamp plus cooldown to current timestamp
        if self.last_ts + 2 < current_ts:

            # Get the new timestamp and shoot
            self.last_ts = time.time()

            # Create bullet object
            laser = Laser(self)

            # Add bullet object to the sprite groups
            self.lasers.add(laser)
            self.all_sprites.add(laser)



    def update(self, dt):

        self.move(dt)
        self.shoot_laser()



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


