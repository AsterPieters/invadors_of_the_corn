# Bullet.py

import pygame

from settings import *

class Bullet(pygame.sprite.Sprite):

    def __init__(self, player):

        super().__init__()

        # Initialize bullet
        self.image = pygame.image.load("graphics/shotgun/bullet/0.png")
        self.rect = self.image.get_rect()
        self.damage = 20

        self.player = player
        
        # Set up original location
        self.bullet_x, self.bullet_y = self.player.rect.midtop

    def update(self, dt):
        
        # Display bullet as long as its active
        self.bullet_y -= 100

        # Display the bullet 
        SCREEN.blit(self.image, (self.bullet_x, self.bullet_y))

        # Move the rect
        self.rect.centery = self.bullet_y
        self.rect.centerx = self.bullet_x

        # Remove bullet if it goes off screen
        if self.bullet_y < 1:
            self.player.bullets.remove(self)
            self.player.all_sprites.remove(self)



class Laser(pygame.sprite.Sprite):
    
    def __init__(self, ufo):

        # Initialize sprites
        super().__init__()

        # Set ufo
        self.ufo = ufo
        
        # Characteristics
        self.damage = 100

        # Load image
        self.image = pygame.image.load("graphics/laser/0.png")
        
        # Spawn the rect
        self.rect = self.image.get_rect(midbottom=self.ufo.rect.midbottom)

        # Movement
        self.pos = pygame.math.Vector2(self.rect.center)
        self.speed = 600

    def update(self, dt):

        # Move the lazer 
        self.pos.y += self.speed * dt

        # Display the bullet 
        SCREEN.blit(self.image, self.pos)

        # Move the rect
        self.rect.y = self.pos.y
        self.rect.x = self.pos.x

        # Remove bullet if it goes off screen
        if self.pos.y < 1:
            self.ufo.lasers.remove(self)
            self.ufo.all_sprites.remove(self)


