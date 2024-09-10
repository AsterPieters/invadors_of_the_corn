# Bullet.py

import pygame

from settings import *

class Bullet(pygame.sprite.Sprite):

    def __init__(self, player):

        super().__init__()

        # Initialize bullet
        self.image = pygame.image.load("graphics/shotgun/bullet/0.png")
        self.rect = self.image.get_rect()

        self.player = player
        
        # Set up original location
        self.bullet_x, self.bullet_y = self.player.rect.midtop

    def update(self, dt):
        
        # Display bullet as long as its active
        self.bullet_y -= self.player.speed / 100

        # Display the bullet 
        SCREEN.blit(self.image, (self.bullet_x, self.bullet_y))

        # Move the rect
        self.rect.centery = self.bullet_y
        self.rect.centerx = self.bullet_x

        # Remove bullet if it goes off screen
        if self.bullet_y < 1:
            self.player.bullets.remove(self)
            self.player.all_sprites.remove(self)
