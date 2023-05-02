import pygame
from models import Algorithm
from views import Main_View

class Controller():
    def __init__(self):
        pygame.init()

        self.loop_state = "main-menu"
        self.view = Main_View()
        self.model = Algorithm()

    def main_game_loop(self):
        while True:
            if self.loop_state == "main-menu":
                self.main_menu()
            elif self.loop_state == "sorting":
                self.sorting_menu()
            elif self.loop_state == "options":
                print("were in options")

    def main_menu(self):
        mouse_pos = pygame.mouse.get_pos()

        self.view.main_menu(mouse_pos)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.view.sort_button.checkForInput(mouse_pos):
                    self.loop_state = "sorting"
                elif self.view.options_button.checkForInput(mouse_pos):
                    self.loop_state = "options"
                elif self.view.quit_button.checkForInput(mouse_pos):
                    pygame.quit()

    def sorting_menu(self):

        self.view.sorting(self.model)

def main():
    controller = Controller()
    controller.main_game_loop()


if __name__ == "__main__":
    main()