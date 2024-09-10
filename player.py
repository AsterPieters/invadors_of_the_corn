# player.py

import pygame
import time

from settings import *
from tools import import_folder
from bullet import Bullet

class Player(pygame.sprite.Sprite):

    def __init__(self, all_sprites, bullets):

        # Initialize sprites
        super().__init__(all_sprites)

        # Initialize player status
        self.status = 'left_idle'
        self.frame_index = 0
        self.player_x = 600
        self.player_y = 600

        # Graphics
        self.import_graphics()
        self.image = self.animations[self.status][int(self.frame_index)]
        self.rect = self.image.get_rect(center = ((SCREEN_WIDTH // 2), 600))

        # Groups
        self.all_sprites = all_sprites
        self.bullets = bullets

        # Get cooldown timestamp
        self.last_ts = time.time()

        # Movement
        self.speed = 300
        self.direction = pygame.math.Vector2()
        self.pos = pygame.math.Vector2(self.rect.center)



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
        """ Display, move and check the player for boundaries """

	    # Normalize the Vector
        # IDK exactly how it works but it slows down the movement?
        if self.direction.magnitude() > 0:
            self.direction = self.direction.normalize()

		# Calculate the distance to move based on speed and delta time
        distance_x = self.direction.x * self.speed * dt

		# Calculate the new position
        new_x = self.player_x + distance_x

        # Keep player from going too far right
        if 0 <= new_x <= SCREEN_WIDTH - self.rect.width:
            self.player_x = new_x 
            self.rect.centerx = self.player_x

        # Keep player from going too far left
        elif new_x < 0:
            self.player_x = 0
            self.rect.centerx = self.player_x
 
        # Move the player
        else:
            self.player_x = SCREEN_WIDTH - self.rect.width
            self.rect.centerx = self.player_x

        # Display the player
        SCREEN.blit(self.image, (self.player_x, self.player_y))



    def get_user_input(self): 
        """ Grab input for moving and using items """

        # check for keys input
        keys = pygame.key.get_pressed()
        
        # Left arrow is pressed
        if keys[pygame.K_LEFT]:
            self.direction.x = -1
            self.status = 'left'
        
        # Right arrow is pressed
        elif keys[pygame.K_RIGHT]:
            self.direction.x = 1
            self.status = 'right'

        # No key is pressed
        else:
            self.direction.x = 0
            self.status = self.status.split('_')[0] + '_idle'

        # Shoot
        if keys[pygame.K_SPACE]:    
            self.shoot_shotgun()



    def import_graphics(self):
        """ Grab all pictures from the correct folders and put them into dictionaries """

        self.animations = {
                'left': [],
                'right': [],
                'left_idle': [],
                'right_idle': []
                }

        # Put all graphics into dictionary for later use
        for animation in self.animations.keys():
            path = 'graphics/player/' + animation
            self.animations[animation] = import_folder(path)



    def shoot_shotgun(self):
        """ Check cooldown, create bullet object, and add it to the sprite lists """

        # Cooldown function
        # Get current timestamp
        current_ts = time.time()
        
        # Compare last timestamp plus cooldown to current timestamp
        if self.last_ts + 1 < current_ts:

            # Get the new timestamp and shoot
            self.last_ts = time.time()

            # Create bullet object
            bullet = Bullet(self)

            # Add bullet object to the sprite groups
            self.bullets.add(bullet)
            self.all_sprites.add(bullet)



    def update(self, dt):
        """ Call all important fuctions """

        self.get_user_input()
        self.move(dt)
        self.animate(dt)

            
