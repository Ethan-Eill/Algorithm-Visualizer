import pygame
from views import Main_View

def main():
    pygame.init()
    global loop_state, view
    print("Algorithm Visualizer")
    loop_state = "main-menu"
    view = Main_View()
    while True:
        if loop_state == "main-menu":
            main_menu()
        elif loop_state == "sorting":
            print("were sorting")
        elif loop_state == "options":
            print("were in options")

        

def main_menu():
    global loop_state, view
    mouse_pos = pygame.mouse.get_pos()

    view.main_menu(mouse_pos)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if view.sort_button.checkForInput(mouse_pos):
                loop_state = "sorting"
            elif view.options_button.checkForInput(mouse_pos):
                loop_state = "options"
            elif view.quit_button.checkForInput(mouse_pos):
                pygame.quit()

if __name__ == "__main__":
    main()