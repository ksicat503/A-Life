"""
SOURCES
Background Image: Generated using Gemini 2.0
"""
import os

import pygame

from ui_loader import load_ui_components


class Menu_Handler:

    def __init__(self, window):
        """ Initalize class variables"""
        self.window = window
        self.speed_vals = [1, 2, 4]
        self.can_click = True
        self.set_game_state_variables()
        self.ui_components = load_ui_components()

    def set_game_state_variables(self):
        """ Sets variables that control the game state"""
        self.current_menu = 'main'
        self.sim_active = False
        self.load_game = False
        self.game_id = None
        self.exit = False
        self.save_game = False
        self.novel_feature = True
        self.organisms = None
        self.speed = self.speed_vals[0]

    def set_organism_data(self, organisms):
        """ Set organism data so we can view stats"""
        self.organisms = organisms

    def check_if_clickable(self):
        """ Checks to see if mouse press has been lifted"""
        if pygame.mouse.get_pressed()[0] is False:
            self.can_click = True

    def display_menu(self):
        """ Calls the draw method for each menu"""
        if not self.can_click:
            self.check_if_clickable()

        if self.current_menu == 'main':
            self.draw_main_menu()
        elif self.current_menu == 'new_sim':
            self.draw_new_sim_menu()
        elif self.current_menu == 'load_sim':
            self.draw_load_sim_menu()
        elif self.current_menu == 'pause':
            self.draw_pause_menu()
        elif self.current_menu == 'stats':
            self.draw_stat_menu()

    def draw_main_menu(self):
        """ Displays the main menu """
        # Draws background
        self.window.blit(self.ui_components['background'], (0, 0))

        # Draws Text
        self.ui_components['text']['title'].draw(
            self.window, 'A-Life Challenge')

        # Draws buttons
        if self.ui_components['buttons']['new_sim'].draw(
             self.window, self.can_click):
            self.current_menu = 'new_sim'
            self.can_click = False
        if self.ui_components['buttons']['load_sim'].draw(
             self.window, self.can_click):
            self.current_menu = 'load_sim'
            self.can_click = False
        if self.ui_components['buttons']['exit'].draw(
             self.window, self.can_click):
            self.exit = True

    def draw_new_sim_menu(self):
        """ Displays the new sim menu """

        # Draws background
        self.window.blit(self.ui_components['background'], (0, 0))

        # Draws Text
        self.ui_components['text']['title'].draw(self.window, "New Simulation")
        self.ui_components['text']['features'].draw(self.window,
                                                    "Novel Features")

        # Draws buttons and toggles
        if self.ui_components['toggles']['on_off'].draw(
             self.window, self.can_click):
            self.novel_feature = not self.novel_feature
            self.can_click = False
        if self.ui_components['buttons']['start'].draw(
             self.window, self.can_click):
            self.game_id = 0 if not os.path.isdir('./saves') \
                else len(os.listdir('./saves'))
            self.sim_active = True
            self.current_menu = 'none'
        if self.ui_components['buttons']['back'].draw(
             self.window, self.can_click):
            self.current_menu = 'main'
            self.can_click = False

    def draw_load_sim_menu(self):
        """ Displays the load sim menu """

        # Draws background
        self.window.blit(self.ui_components['background'], (0, 0))

        # Draws Text
        self.ui_components['text']['title'].draw(self.window, "Recent Saves")

        # Draws buttons
        # Gets all saved files displays the three most recent saved files
        saves = [] if not os.path.isdir('./saves') else os.listdir('./saves')
        if len(saves) >= 1:
            if self.ui_components['buttons']['sim_1'].draw(
                 self.window, self.can_click):
                self.game_id = int(saves[max(0, len(saves)-3)][3:])
                self.sim_active = True
                self.load_game = True
                self.current_menu = 'none'
        if len(saves) >= 2:
            if self.ui_components['buttons']['sim_2'].draw(
                 self.window, self.can_click):
                self.game_id = int(saves[max(1, len(saves)-2)][3:])
                self.sim_active = True
                self.load_game = True
                self.current_menu = 'none'
        if len(saves) >= 3:
            if self.ui_components['buttons']['sim_3'].draw(
                 self.window, self.can_click):
                self.game_id = int(saves[max(2, len(saves)-1)][3:])
                self.sim_active = True
                self.load_game = True
                self.current_menu = 'none'
        if self.ui_components['buttons']['back'].draw(
             self.window, self.can_click):
            self.current_menu = 'main'
            self.can_click = False

    def draw_pause_menu(self):
        """Displays the pause menu """

        # Draws background
        self.window.blit(self.ui_components['background'], (0, 0))

        # Draws Text
        self.ui_components['text']['title'].draw(self.window, "Paused")
        self.ui_components['text']['speed'].draw(self.window, "Speed")

        # Draws buttons and toggles
        if self.ui_components['buttons']['resume'].draw(
             self.window, self.can_click):
            self.current_menu = 'none'
        if self.ui_components['toggles']['speed'].draw(
             self.window, self.can_click):
            self.speed = self.speed_vals[
                self.ui_components['toggles']['speed'].current_index]
            self.can_click = False
        if self.ui_components['buttons']['stat'].draw(
             self.window, self.can_click):
            self.current_menu = 'stats'
            self.can_click = False
        if self.ui_components['buttons']['save'].draw(
             self.window, self.can_click):
            self.save_game = True
        if self.ui_components['buttons']['quit'].draw(
             self.window, self.can_click):
            self.set_game_state_variables()
            self.can_click = False

    def draw_stat_menu(self):
        print(self.organisms[0].x_pos)
        print(self.organisms[0].y_pos)
        self.current_menu = 'main'
