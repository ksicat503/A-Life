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
        self.speed_vals = [1, 2, 4, 0]
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
        self.organism = None
        self.reload_display = False
        self.starting_data = {'herb_count': 10,
                              'carn_count': 3,
                              'mutation_chance': 0.10}
        self.speed = self.speed_vals[0]
        self.stats = {}

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
        elif self.current_menu == 'individual_organism':
            self.draw_single_org_stat_menu()

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
        """        self.ui_components['text']['body_1_1'].draw(self.window,
                                                    "Novel Features")"""

        self.ui_components['text']['body_1_1'].draw(
            self.window,
            f"Herbivore Count: {self.starting_data['herb_count']}")
        self.ui_components['text']['body_1_4'].draw(
            self.window,
            f"Carnivore Count: {self.starting_data['carn_count']}")
        self.ui_components['text']['body_1_7'].draw(
            self.window,
            f"Mutation Rate: {self.starting_data['mutation_chance']}")

        # Draws buttons and toggles
        if self.ui_components['buttons']['herb_add'].draw(
             self.window, self.can_click):
            self.starting_data['herb_count'] += 1
            self.can_click = False
        if self.ui_components['buttons']['herb_sub'].draw(
             self.window, self.can_click):
            if self.starting_data['herb_count'] > 0:
                self.starting_data['herb_count'] -= 1
                self.can_click = False
        if self.ui_components['buttons']['carn_add'].draw(
             self.window, self.can_click):
            self.starting_data['carn_count'] += 1
            self.can_click = False
        if self.ui_components['buttons']['carn_sub'].draw(
             self.window, self.can_click):
            if self.starting_data['carn_count'] > 0:
                self.starting_data['carn_count'] -= 1
                self.can_click = False
        if self.ui_components['buttons']['mutation_add'].draw(
             self.window, self.can_click):
            self.starting_data['mutation_chance'] = round(
                    self.starting_data['mutation_chance'] + 0.01, 2)
            self.can_click = False
        if self.ui_components['buttons']['mutation_sub'].draw(
             self.window, self.can_click):
            if self.starting_data['mutation_chance'] > 0.05:
                self.starting_data['mutation_chance'] = round(
                    self.starting_data['mutation_chance'] - 0.01, 2)
                self.can_click = False
        if self.ui_components['buttons']['start'].draw(
             self.window, self.can_click):
            self.game_id = 0 if not os.path.isdir('./saves') \
                else len(os.listdir('./saves'))
            self.sim_active = True
            self.current_menu = 'none'
        if self.ui_components['buttons']['back_new_sim'].draw(
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
        if self.ui_components['buttons']['back_load_sim'].draw(
             self.window, self.can_click):
            self.current_menu = 'main'
            self.can_click = False

    def draw_pause_menu(self):
        """Displays the pause menu """

        # Draws background
        self.window.blit(self.ui_components['background'], (0, 0))

        # Draws Text
        self.ui_components['text']['title'].draw(self.window, "Paused")
        self.ui_components['text']['speed'].draw(self.window, "Frame Skip")

        # Draws buttons and toggles
        if self.ui_components['buttons']['resume'].draw(
             self.window, self.can_click):
            self.current_menu = 'none'
            self.reload_display = True
        if self.ui_components['toggles']['speed'].draw(
             self.window, self.can_click):
            self.speed = self.speed_vals[
                self.ui_components['toggles']['speed'].current_index]
            self.can_click = False
        if self.ui_components['buttons']['stat'].draw(
             self.window, self.can_click):
            self.current_menu = 'stats'
            self.calculate_stats()
            self.can_click = False
        if self.ui_components['buttons']['save'].draw(
             self.window, self.can_click):
            self.save_game = True
        if self.ui_components['buttons']['quit'].draw(
             self.window, self.can_click):
            self.set_game_state_variables()
            self.can_click = False

    def calculate_stats(self):
        """ Calculates stats for the current sim """
        stat_keys = ['h_alive_count', 'h_death_by_hunger',
                     'h_death_by_age', 'h_death_by_consumed',
                     'c_alive_count', 'c_death_by_hunger',
                     'c_death_by_age', 'c_death_by_consumed']
        self.stats = {key: 0 for key in stat_keys}
        animal_map = {1: 'h', 2: 'c'}
        death_map = {1: 'death_by_consumed',
                     2: 'death_by_hunger',
                     3: 'death_by_age'}

        for organism in self.organisms:
            animal_type = animal_map[organism.animal_type]
            if organism.is_alive:
                self.stats[f"{animal_type}_alive_count"] += 1
            else:
                self.stats[
                    f"{animal_type}_{death_map[organism.death_type]}"
                    ] += 1

    def draw_stat_menu(self):
        """ Displays Stats for the organisms"""

        # Draws background
        self.window.blit(self.ui_components['background'], (0, 0))

        # Draws Text
        self.ui_components['text']['title'].draw(self.window, "Organism Stats")
        self.ui_components['text']['subtitle_1'].draw(
            self.window, "Population")
        self.ui_components['text']['body_1_1'].draw(
            self.window, f"Herbivore : {self.stats['h_alive_count']}")
        self.ui_components['text']['body_1_2'].draw(
            self.window, f"Carnivore : {self.stats['c_alive_count']}")
        self.ui_components['text']['subtitle_2'].draw(self.window, "Deaths")
        self.ui_components['text']['subtitle_2_1'].draw(
            self.window, "By Hunger")
        self.ui_components['text']['body_2_1_1'].draw(
            self.window, f"Herbivore : {self.stats['h_death_by_hunger']}")
        self.ui_components['text']['body_2_1_2'].draw(
            self.window, f"Carnivore : {self.stats['c_death_by_hunger']}")
        self.ui_components['text']['subtitle_2_1.5'].draw(
            self.window, "By Old Age")
        self.ui_components['text']['body_2_1_1.5'].draw(
            self.window, f"Herbivore : {self.stats['h_death_by_age']}")
        self.ui_components['text']['body_2_1_2.5'].draw(
            self.window, f"Carnivore : {self.stats['c_death_by_age']}")
        self.ui_components['text']['subtitle_2_2'].draw(
            self.window, "By Consumed")
        self.ui_components['text']['body_2_2_1'].draw(
            self.window, f"Herbivore : {self.stats['h_death_by_consumed']}")
        self.ui_components['text']['body_2_2_2'].draw(
            self.window, f"Carnivore : {self.stats['c_death_by_consumed']}")

        if self.ui_components['buttons']['back_stats'].draw(
             self.window, self.can_click):
            self.current_menu = 'pause'
            self.can_click = False

    def set_organism(self, position):
        """ Determines what organism was clicked """
        for organism in self.organisms:
            if organism.is_alive:
                if (organism.x_pos < position[0] <
                   organism.x_pos + organism.org_width and
                   organism.y_pos < position[1] <
                   organism.y_pos + organism.org_height):
                    self.organism = organism
                    return True
        return False

    def draw_single_org_stat_menu(self):
        """ Draws stat page for single organism """
        # Draws background
        self.window.blit(self.ui_components['background'], (0, 0))

        if self.organism.animal_type == 1:
            self.ui_components['text']['title'].draw(
                self.window, "Herbivore instance")
        else:
            self.ui_components['text']['title'].draw(
                self.window, "Carnivore instance")
            self.ui_components['text']['body_1_8'].draw(
                self.window,
                f"Amount of animals consumed: {self.organism.consumed_count}")

        self.ui_components['text']['body_1_1'].draw(
            self.window,
            f"Energy Level: {round(self.organism.energy_level, 2)}")
        self.ui_components['text']['body_1_2'].draw(
            self.window, f"Days Since Fed: {self.organism.days_since_fed}")
        self.ui_components['text']['body_1_3'].draw(
            self.window,
            f"Current Age: {round(self.organism.age, 2)}")
        self.ui_components['text']['body_1_4'].draw(
            self.window, f"Life Expectancy: {self.organism.life_expectancy}")
        self.ui_components['text']['body_1_5'].draw(
            self.window, f"Maturation Age: {self.organism.maturation_age}")
        self.ui_components['text']['body_1_6'].draw(
            self.window,
            "Offspring Chance: " + round(
                self.organism.offspring_chance * 100, 2) + "%")
        self.ui_components['text']['body_1_7'].draw(
            self.window,
            f"Child Count: {self.organism.child_count}"
        )

        if self.ui_components['buttons']['resume_stat'].draw(
             self.window, self.can_click):
            self.current_menu = 'none'
            self.organism = None
            self.reload_display = True
