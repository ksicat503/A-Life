"""
SOURCES
Background Image: Generated using Gemini 2.0
"""


import pygame
import os
from menu_assets import Button, Text, Toggle


class Menu_Handler:

    def __init__(self, screen_size, window):
        """ Initalize class variables"""
        self.screen_size = screen_size
        self.window = window
        self.current_menu = 'main'
        self.sim_active = False
        self.load_game = False
        self.game_id = None
        self.paused = False
        self.exit = False
        self.save_game = False
        self.novel_feature = True
        self.speed = 1
        self.scaled_background = pygame.transform.scale(
            pygame.image.load('./assets/menu_background.jpg').convert(),
            (screen_size[0], screen_size[1]))
        self.main_title = Text(self.screen_size[0]//2, 200, 50)
        self.features_text = Text(self.screen_size[0]//3, 350, 30)
        self.speed_text = Text(self.screen_size[0]//3, 450, 30)
        # Initalize buttons
        self.init_buttons()

    def init_buttons(self):
        """ Initalizes all the buttons for each menu """
        # Main Menu Buttons
        self.new_sim_button = Button(
            self.screen_size[0] // 2, 350,
            pygame.image.load('./assets/new_sim_button.png').convert_alpha(),
            0.7
        )
        self.load_sim_button = Button(
            self.screen_size[0] // 2, 450,
            pygame.image.load('./assets/load_sim_button.png').convert_alpha(),
            0.7
        )
        self.exit_button = Button(
            self.screen_size[0] // 2, 550,
            pygame.image.load('./assets/exit_button.png').convert_alpha(),
            0.7
        )
        # New Sim Menu Buttons
        self.on_off_button = Toggle(
            (self.screen_size[0] // 3) * 2, 350,
            [pygame.image.load('./assets/on_button.png').convert_alpha(),
             pygame.image.load('./assets/off_button.png').convert_alpha()],
            0.7
        )
        self.start_button = Button(
            self.screen_size[0] // 2, 450,
            pygame.image.load('./assets/start_button.png').convert_alpha(),
            0.7
        )
        # Load Sim Menu Buttons
        self.sim_1_button = Button(
            self.screen_size[0] // 2, 350,
            pygame.image.load('./assets/saved_sim_1_button.png')
            .convert_alpha(),
            0.7
        )
        self.sim_2_button = Button(
            self.screen_size[0] // 2, 450,
            pygame.image.load('./assets/saved_sim_2_button.png')
            .convert_alpha(),
            0.7
        )
        self.sim_3_button = Button(
            self.screen_size[0] // 2, 550,
            pygame.image.load('./assets/saved_sim_3_button.png')
            .convert_alpha(),
            0.7
        )
        # Back button for both new and load sim menu
        self.back_button = Button(
            self.screen_size[0] // 2, 650,
            pygame.image.load('./assets/back_button.png').convert_alpha(),
            0.7
        )

        # Pause Menu Buttons
        self.resume_button = Button(
            self.screen_size[0] // 2, 350,
            pygame.image.load('./assets/resume_button.png').convert_alpha(),
            0.7
        )
        self.speed_button = Toggle(
            (self.screen_size[0] // 3) * 2, 450,
            [pygame.image.load('./assets/1x_button.png').convert_alpha(),
             pygame.image.load('./assets/2x_button.png').convert_alpha(),
             pygame.image.load('./assets/4x_button.png').convert_alpha()
             ],
            0.7
        )
        self.save_button = Button(
            self.screen_size[0] // 2, 550,
            pygame.image.load('./assets/save_button.png').convert_alpha(),
            0.7
        )
        self.quit_button = Button(
            self.screen_size[0] // 2, 650,
            pygame.image.load('./assets/quit_button.png').convert_alpha(),
            0.7
        )

    def display_menu(self):
        """ Calls the draw method for each menu"""
        if self.current_menu == 'main':
            self.draw_main_menu()
        elif self.current_menu == 'new_sim':
            self.draw_new_sim_menu()
        elif self.current_menu == 'load_sim':
            self.draw_load_sim_menu()

    def draw_main_menu(self):
        """ Displays the main menu """
        # Draws background image
        self.window.blit(self.scaled_background, (0, 0))

        # Draws title
        self.main_title.draw(self.window, 'A-Life Challenge')

        # Draws buttons and checks to see if they are clicked
        if self.new_sim_button.draw(self.window):
            pygame.time.wait(250)
            self.current_menu = 'new_sim'
        if self.load_sim_button.draw(self.window):
            pygame.time.wait(250)
            self.current_menu = 'load_sim'
        if self.exit_button.draw(self.window):
            self.exit = True

    def draw_new_sim_menu(self):
        """ Displays the new sim menu """
        # Draws background image
        self.window.blit(self.scaled_background, (0, 0))

        # Draws title
        self.main_title.draw(self.window, "New Simulation")
        self.features_text.draw(self.window, "Novel Features")

        # Displays buttons and checks if they are clicked
        # Togels on and off button
        if self.on_off_button.draw(self.window):
            self.novel_feature = not self.novel_feature
        if self.start_button.draw(self.window):

            self.game_id = 0 if not os.path.isdir('./saves') \
                else len(os.listdir('./saves'))
            self.sim_active = True
        if self.back_button.draw(self.window):
            pygame.time.wait(100)
            self.current_menu = 'main'

    def draw_load_sim_menu(self):
        """ Displays the load sim menu """
        self.window.blit(self.scaled_background, (0, 0))
        self.main_title.draw(self.window, "Recent Saves")

        # Displays all buttons
        # Gets all saved files displays the three most recent saved files
        saves = [] if not os.path.isdir('./saves') else os.listdir('./saves')
        if len(saves) >= 1:
            if self.sim_1_button.draw(self.window):
                self.game_id = int(saves[max(0, len(saves)-3)][3:])
                self.sim_active = True
                self.load_game = True
        if len(saves) >= 2:
            if self.sim_2_button.draw(self.window):
                self.game_id = int(saves[max(1, len(saves)-2)][3:])
                self.sim_active = True
                self.load_game = True
        if len(saves) >= 3:
            if self.sim_3_button.draw(self.window):
                self.game_id = int(saves[max(2, len(saves)-1)][3:])
                self.sim_active = True
                self.load_game = True

        if self.back_button.draw(self.window):
            pygame.time.wait(100)
            self.current_menu = 'main'

    def draw_pause_menu(self):
        """Displays the pause menu """
        self.window.blit(self.scaled_background, (0, 0))

        self.main_title.draw(self.window, "Paused")
        self.speed_text.draw(self.window, "Speed")

        # Displays all the buttons
        if self.resume_button.draw(self.window):
            self.paused = False
        if self.speed_button.draw(self.window):
            if self.speed_button.current_index == 0:
                self.speed = 1
            elif self.speed_button.current_index == 1:
                self.speed = 2
            else:
                self.speed = 4
        if self.save_button.draw(self.window):
            self.save_game = True
        if self.quit_button.draw(self.window):
            self.sim_active = False
            self.paused = False
            self.speed = 1
            self.current_menu = 'main'
