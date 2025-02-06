import pygame
import os
# import numpy as np
# import json
from test_organism import Organism
from carnivores import Carnivores
from herbivores import Herbivores
from menu_handling import Menu_Handler
from json_writer import org_json_writer, json_reader  # , sim_json_writer

# initializing imported module
# This initializes pygame and fonts to display text
pygame.init()
pygame.font.init()

# defining the size of the window
window_height = 800
window_width = 800

# This is needed to clear the screen during sim,
# as fill function needs the variable
black = (0, 0, 0)

# Initializing the window
window = pygame.display.set_mode((window_height, window_width))
# This code allows us to change the name of the window
pygame.display.set_caption('Artifical Life Sim')

# clock to set frame rate in simulation
clock = pygame.time.Clock()

# Initalize menus
menus = Menu_Handler((window_height, window_width), window)

# setting bool value to start pygame window.
pygame_active = True

while pygame_active:
    # Displays the current menu
    menus.display_menu()
    if menus.exit:
        pygame_active = False

    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            pygame_active = False

    pygame.display.update()

    if menus.sim_active:
        if menus.load_game is False:
            # Will need to update this later
            all_organisms = [
                Organism(x_pos=200, y_pos=200,
                         window_h=window_height, window_w=window_width
                         ),
                Herbivores(x_pos=300, y_pos=500,
                           window_h=window_height, window_w=window_width),
                Carnivores(x_pos=800, y_pos=200, window_h=window_height,
                           window_w=window_width)
                ]
        else:
            organism_data = json_reader(f"./saves/id_{menus.game_id}")
            all_organisms = []
            for organism in organism_data:
                # will need to update. Right now I will assume
                # they are all herbivores.
                all_organisms.append(
                    Herbivores(organism_data['x_pos'], organism_data['y_pos'])
                    )

    while menus.sim_active:
        # Set up event for when the user quits out of the screen
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    menus.paused = True
            # if event is of type quit then
            # set running bool to false
            if event.type == pygame.QUIT:
                menus.sim_active = False
                pygame_active = False

        # Checks if game needs to be saved.
        if menus.save_game:
            # Make folder for new game save if it doesn't exist
            if not os.path.exists('./saves'):
                os.makedirs('./saves')
            if not os.path.exists(f'./saves/id_{menus.game_id}'):
                os.makedirs(f'./saves/id_{menus.game_id}')
            # Save organism data
            org_json_writer(all_organisms,
                            f'./saves/id_{menus.game_id}/organism.json')
            menus.save_game = False

        if menus.paused:
            menus.draw_pause_menu()
        else:
            # Move all the organisms
            for organism in all_organisms:
                organism.move()

            # Clear screen. Important or else is just paints the screen
            # as the organism moves.
            window.fill(black)

            # Inserting organism on screen in new position
            for organism in all_organisms:
                organism.insert_organism(window)

        # update the display for the new movement
        pygame.display.update()

        # # print to show energy is decreasing with movement
        # print(organism_test.energy)

        # # Added some code to stop the sim when the organism runs out of
        # energy
        # # Take this out to run continuously
        # if organism_test.energy == 0:
        #     sim_running = False

        # Setting frame rate, lower setting seems to be easier to follow
        # Also if higher, the sim runs quickly due to energy consumption
        clock.tick(30*menus.speed)
