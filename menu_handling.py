import pygame_menu


class Menu_Handler:

    def __init__(self, screen_size, window):
        """ Initalize class variables"""
        self.screen_size = screen_size
        self.window = window
        self.current_menu = 'main'
        self.sim_active = False
        self.paused = False
        self.exit = False
        self.novel_feature = True
        self.scaled_background = pygame.transform.scale(
            pygame.image.load('./assets/menu_background.jpg').convert(),
            (screen_size[0], screen_size[1]))
        self.main_title = Text(self.screen_size[0]//2, 200, 50)
        self.togel_text = Text(self.screen_size[0]//3, 350, 30)
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
        self.on_button = Button(
            (self.screen_size[0] // 3) * 2, 350,
            pygame.image.load('./assets/on_button.png').convert_alpha(),
            0.7
        )
        self.off_button = Button(
            (self.screen_size[0] // 3) * 2, 350,
            pygame.image.load('./assets/off_button.png').convert_alpha(),
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
        load_sim_menu.add.button(
            'Back', self.display_main_menu
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
            self.current_menu = 'new_sim'
        if self.load_sim_button.draw(self.window):
            self.current_menu = 'load_sim'
        if self.exit_button.draw(self.window):
            print('clicked')
            self.exit = True

    def draw_new_sim_menu(self):
        """ Displays the new sim menu """
        # Draws background image
        self.window.blit(self.scaled_background, (0, 0))

        # Draws title
        self.main_title.draw(self.window, "New Simulation")
        self.togel_text.draw(self.window, "Novel Features")

        # Displays buttons and checks if they are clicked
        # Togels on and off button
        if self.novel_feature:
            if self.on_button.draw(self.window):
                self.novel_feature = False
        else:
            if self.off_button.draw(self.window):
                self.novel_feature = True
        if self.start_button.draw(self.window):
            self.sim_active = True
        if self.back_button.draw(self.window):
            self.current_menu = 'main'

    def draw_load_sim_menu(self):
        """ Displays the load sim menu """
        self.window.blit(self.scaled_background, (0, 0))
        self.main_title.draw(self.window, "Load Simulation")

        # Draws buttons and checks to see if they are clicked
        if self.sim_1_button.draw(self.window):
            pass
        if self.sim_2_button.draw(self.window):
            pass
        if self.sim_3_button.draw(self.window):
            pass
        if self.back_button.draw(self.window):
            self.current_menu = 'main'
