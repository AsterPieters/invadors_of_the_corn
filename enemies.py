# enemies.py

import pygame
import time
from random import randint

from settings import *
from bullet import Laser
from tools import random_coords
from tools import import_folder

class Enemy:
    """ Parent class for enemies """
    
    def __init__(self, all_sprites, enemies, player, lasers, stats):

        # Initialize groups
        self.all_sprites = all_sprites
        self.enemies = enemies
        self.lasers = lasers
        
        self.stats = stats
        self.player = player
        
        # Spawn the first enemies
        self.spawn_enemies()



    def spawn_enemies(self):

        #TODO: make multiple enemies with levels
        ufo = Ufo(self.player, self.all_sprites, self.lasers, self.enemies)
        self.enemies.add(ufo)
        self.all_sprites.add(ufo)



    def update_enemies(self, bullets):
        
        # Kill enemy if hit by a bullet
        collisions = pygame.sprite.groupcollide(bullets, self.enemies, True, False)
        for bullet, enemies_hit in collisions.items():
            for enemy in enemies_hit:
                print("[INFO] Enemy was hit!")
                enemy_killed = enemy.get_hit(bullet.damage)
                if enemy_killed:
                    self.spawn_enemies()

                    # Add one to the score
                    self.stats.ufos_destroyed += 1

        # Kill player if hit by a laser
        if pygame.sprite.spritecollide(self.player, self.lasers, True):
            
            # Kill the player
            print("[INFO] Player was hit!")
            self.player.die(self.stats)

            # Kill the enemies
            for enemy in self.enemies, self.all_sprites:
                self.enemies.remove(enemy)
                self.all_sprites.remove(enemy)


class Ufo(pygame.sprite.Sprite):
    """ A ufo that shoots lazers"""

    def __init__(self, player, all_sprites, lasers, enemies):
       
        # Initialize sprites
        super().__init__()
        self.player = player

        # Groups
        self.all_sprites = all_sprites
        self.lasers = lasers
        self.enemies = enemies

        # Status
        self.frame_index = 0
        self.status = 'flying'
        self.last_ts = time.time() # Timestamp for laser cooldown
        self.health = 100

        # Graphics 
        self.import_graphics()
        self.image = self.animations[self.status][int(self.frame_index)]
        self.font = pygame.font.Font('freesansbold.ttf', 32) 
    
        # Randomize the x coordinate and spawn the rect
        x_coord = random_coords(100)
        self.rect = self.image.get_rect(center = (x_coord, -100))

        # Movement
        self.pos = pygame.math.Vector2(self.rect.center)
        self.speed = 200
        self.flying_up = False



    def animate(self, dt):
        """ Switch between images to animate the players movement """

        # Change the animation speed according to the player speed
        animation_speed = (self.speed / 80) 

        # Change the images
        self.frame_index += animation_speed * dt
        
        # Reset the loop if run out of images
        if self.frame_index >= len(self.animations[self.status]):
            self.frame_index = 0
        
        # Set the image to display
        self.image = self.animations[self.status][int(self.frame_index)]



    def move(self, dt):

        # Get the direction of the ufo
        direction = self.player.pos - self.pos

        # Normalize the Vector
        # Again, wizard shit
        if direction.magnitude() != 0:
            direction = direction.normalize()

        # Send ufo back up when too low 
        if self.pos.y >= 300:
            self.flying_up = True

        # Send ufo down when too high up
        elif self.pos.y <= 50:
            self.flying_up = False

        # Go up but follow player
        if self.flying_up:
            self.pos.x += direction[0] * self.speed * dt
            self.pos.y -= direction[1] * self.speed * dt
        
        # Go down but follow player
        else:
            self.pos += direction * self.speed * dt

        # Display ufo and rect
        self.rect.x = self.pos.x
        self.rect.y = self.pos.y
        SCREEN.blit(self.image, self.pos)

        # Display health
        text = self.font.render(str(self.health), True, GREEN, BLUE)
        textRect = text.get_rect()
        textRect.center = (self.pos)
        SCREEN.blit(text, textRect)


    def import_graphics(self):
        """ Grab all pictures from the correct folders and put them into dictionaries """

        self.animations = {
                'flying': [],
                }

        # Put all graphics into dictionary for later use
        for animation in self.animations.keys():
            path = 'graphics/enemies/ufo/' + animation
            self.animations[animation] = import_folder(path)



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



    def get_hit(self, damage):
        """ Handle ufo hits and destroying """

        # Take damage
        self.health -= damage
        
        # Destroy if health reaches 0
        if self.health <= 0:
            self.enemies.remove(self)
            self.all_sprites.remove(self)

            return True

        else:
            return False

    def update(self, dt):

        self.move(dt)
        self.animate(dt)
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


