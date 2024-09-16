# level.py

import pygame
from pygame.sprite import Group

from settings import *
from player import Player
from enemies import Enemy
from stats import Stats

class Level:
    def __init__(self):

        # Initialize the sprite groups
        self.all_sprites = Group() 
        self.bullets = Group()
        self.enemies = Group()
        self.lasers = Group()

        # Create game state
        self.stats = Stats()
        
        # Create player
        self.player = Player(self.all_sprites, self.bullets)
        self.all_sprites.add(self.player)

        # graphics
        self.background = pygame.image.load("graphics/level/0.png")

        # Create enemy
        self.enemy = Enemy(self.all_sprites, self.enemies, self.player, self.lasers, self.stats)


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

        self.stats.display_stats()

        # Update the display
        pygame.display.update()

    


