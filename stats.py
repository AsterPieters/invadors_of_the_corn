# stats.py

import pygame
from settings import *

class Stats():

    def __init__(self):

        self.ufos_destroyed = 0
        self.font = pygame.font.Font('freesansbold.ttf', 32)
        self.gameover = False
        self.font2 = pygame.font.Font('freesansbold.ttf', 64)
    
    def display_stats(self):

        text = self.font.render(f"Ufo's destroyed: {self.ufos_destroyed}", True, GREEN, BLUE)
        textRect = text.get_rect()
        textRect.center = (SCREEN_WIDTH //2, 50)
        SCREEN.blit(text, textRect)

        if self.gameover:


            gameover_text = self.font2.render("Game Over", True, GREEN, BLUE)
            gameover_textRect = gameover_text.get_rect()
            gameover_textRect.center = (SCREEN_WIDTH //2, SCREEN_HEIGHT // 2)
            SCREEN.blit(gameover_text, gameover_textRect)
