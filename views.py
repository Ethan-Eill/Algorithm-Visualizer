import pygame
import random
from button import Button

class Main_View():
    def __init__(self):
        self.screen_width, self.screen_height = 1200, 800
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        self.background_color = (48, 48, 48)
        self.title_font = pygame.font.Font("assets/ARCADE_R.TTF", 70)
        self.title_color = (247, 17, 232)
        self.button_color = (22, 182, 250)
        self.button_font = pygame.font.Font("assets/ARCADE_R.TTF", 50)
        self.is_sound_on = True
        
        pygame.display.set_caption("Algorithm Visualizer")

    def main_menu(self):
        self.screen.fill(self.background_color)
        mouse_pos = pygame.mouse.get_pos()



