import pygame_menu


class Menu_Handler:

    def __init__(self, menu_size):
        """ Initalize class variables"""
        self.menu_size = menu_size
        self.sim_active = False
        self.main_menu = self.build_main_menu()
        self.new_sim_menu = self.build_new_sim_menu()
        self.load_sim_menu = self.build_load_sim_menu()
        self.main_menu.enable()

    def build_main_menu(self):
        """ Builds main menu UI """
        main_menu = pygame_menu.Menu(
            'A Life Challenge',
            self.menu_size[0], self.menu_size[1],
            theme=pygame_menu.themes.THEME_BLUE
            )
        main_menu.add.button(
            'New Simulation', self.display_new_sim_menu
            )
        main_menu.add.button(
            'Load Simulation', self.display_load_sim_menu
            )
        main_menu.add.button(
            'Quit', pygame_menu.events.EXIT
            )
        main_menu.disable()
        return main_menu

    def build_new_sim_menu(self):
        """ Builds new sim menu UI """
        new_sim_menu = pygame_menu.Menu(
            'New Simulation',
            self.menu_size[0], self.menu_size[1],
            theme=pygame_menu.themes.THEME_BLUE
            )
        new_sim_menu.add.text_input(
            'Simulation Name: ', maxchar=20
            )
        new_sim_menu.add.selector(
             'Novel Features: ',
             [('Off', 1), ('On', 2)]
            )
        new_sim_menu.add.button(
            'Start Simulation', self.start_new_sim
            )
        new_sim_menu.disable()
        return new_sim_menu

    def build_load_sim_menu(self):
        """
        Builds load sim menu UI
        Still need to implement reading json files to get sim loads.
        """
        # Will need to read json file to get saved sims
        sim_loads = ['Saved sim 1', 'Saved sim 2', 'Saved sim 3']
        load_sim_menu = pygame_menu.Menu(
            'Load Simulation',
            self.menu_size[0], self.menu_size[1],
            theme=pygame_menu.themes.THEME_BLUE
            )
        for index in range(0, len(sim_loads)):
            load_sim_menu.add.button(
                "Name: {}".format(sim_loads[index]),
                self.load_sim,
                index
                )
        load_sim_menu.disable()
        return load_sim_menu

    def disable_all_menus(self):
        """ Disables the 3 starting menus """
        self.main_menu.disable()
        self.new_sim_menu.disable()
        self.load_sim_menu.disable()

    def display_new_sim_menu(self):
        """ Hides all menus and then displays new sim menu"""
        self.disable_all_menus()
        self.new_sim_menu.enable()

    def display_load_sim_menu(self):
        """ Hides all menus and then displays load sim menu"""
        self.disable_all_menus()
        self.load_sim_menu.enable()

    def start_new_sim(self):
        """ Hides all menus and then updates sim_active to True"""
        self.disable_all_menus()
        self.sim_active = True

    def load_sim(self, id):
        """
        Hides all menus and then will load in sim data
        Still need to implement
        """
        self.disable_all_menus()
        print("Sim {} selected".format(str(id)))
