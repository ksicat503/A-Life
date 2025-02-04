import pygame
# import random
# import numpy as np
# import json
from test_organism import Organism
from carnivores import Carnivores
from herbivores import Herbivores
from menu_handling import Menu_Handler

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

# Creating a set organism for testing.
# Can add a function to create mulitple later
all_organisms = [
    Organism(x_pos=200, y_pos=200,
             window_h=window_height, window_w=window_width
             ),
    Herbivores(x_pos=300, y_pos=500),
    Carnivores(x_pos=800, y_pos=200)
]


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
        # Set variable to start simulation
        sim_running = True
        # keep game running till running is false
        while sim_running:
            # Set up event for when the user quits out of the screen
            for event in pygame.event.get():
                # if event is of type quit then
                # set running bool to false
                if event.type == pygame.QUIT:
                    sim_running = False
                    pygame_active = False

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
            clock.tick(60)
