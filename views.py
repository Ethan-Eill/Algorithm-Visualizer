import pygame
import random
from button import Button

class Main_View():
    def __init__(self):
        self.screen_width, self.screen_height = 1200, 800
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        self.background_color = (48, 48, 48)
        self.title_font = pygame.font.Font("assets/ARCADE_N.TTF", 50)
        self.title_color = (247, 17, 232)
        self.button_color = (22, 182, 250)
        self.button_font = pygame.font.Font("assets/ARCADE_N.TTF", 40)
        self.information_font = pygame.font.Font("assets/ARCADE_N.TTF", 14)
        self.bar_color = (255,255,255)
        self.sort_button = Button(image=None, pos=(self.screen_width/2, self.screen_height/1.7), 
                        text_input="Sort", font=self.button_font, base_color=self.button_color, hovering_color="White")
        self.options_button = Button(image=None, pos=(self.screen_width/2, self.screen_height/1.5), 
                        text_input="Options", font=self.button_font, base_color=self.button_color, hovering_color="White")
        self.quit_button = Button(image=None, pos=(self.screen_width/2, self.screen_height/1.34), 
                        text_input="Exit", font=self.button_font, base_color=self.button_color, hovering_color="White")
        self.is_sound_on = True
        
        pygame.display.set_caption("Algorithm Visualizer")

    #main menu function to be looped through
    def main_menu(self, mouse_pos):
        self.screen.fill(self.background_color)

        title_text = self.title_font.render("Algorithm Visualizer", True, self.title_color)
        title_text_rect = title_text.get_rect(center=(self.screen_width/2, self.screen_height/8.5))

        self.screen.blit(title_text, title_text_rect)

        for button in [self.sort_button, self.options_button, self.quit_button]:
            button.changeColor(mouse_pos)
            button.update(self.screen)

        pygame.display.update()

    #sorting screen to be looped through
    def sorting(self, model):
        self.screen.fill(self.background_color)

        num = 1

        for i in model.arr:
            pygame.draw.rect(self.screen, self.background_color, pygame.Rect((num*model.width), 300, model.width, model.height*i))

        pygame.draw.rect(self.screen, self.background_color, pygame.Rect(0, 700, 1200, 100))

        pygame.display.update()

