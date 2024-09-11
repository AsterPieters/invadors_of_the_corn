# level.py

import pygame
from pygame.sprite import Group

from settings import *
from player import Player
from enemies import Enemy

class Level:
    def __init__(self):

        # Initialize the sprite groups
        self.all_sprites = Group() 
        self.bullets = Group()
        self.enemies = Group()

        # Create player
        self.player = Player(self.all_sprites, self.bullets)
        self.all_sprites.add(self.player)

        # graphics
        self.background = pygame.image.load("graphics/level/0.png")

        # Create enemy
        self.enemy = Enemy(self.all_sprites, self.enemies, self.player)

    def run(self, dt):
        """ Main game loop """

        # Reset the screen
        SCREEN.blit(self.background, (0,0))

        # Check user input
        self.player.get_user_input()

        # Update all sprites
        self.all_sprites.update(dt)
    
        # Update enemies
        self.enemy.update_enemies(self.bullets)

        # Update the display
        pygame.display.update()

    


