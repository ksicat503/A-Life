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
window_height = 1000
window_width = 1000

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
organism_test = Organism(x_pos=200, y_pos=200)
herbivores_test = Herbivores(x_pos=300, y_pos=500)
carnivores_test = Carnivores(x_pos=800, y_pos=200)

# Initalize menus
menus = Menu_Handler((window_height * 0.9, window_width * 0.9))

# setting bool value to start pygame window.
pygame_active = True

while pygame_active:
    window.fill(black)
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            pygame_active = False

    if menus.main_menu.is_enabled():
        menus.main_menu.draw(window)
        menus.main_menu.update(events)

    if menus.new_sim_menu.is_enabled():
        menus.new_sim_menu.draw(window)
        menus.new_sim_menu.update(events)

    if menus.load_sim_menu.is_enabled():
        menus.load_sim_menu.draw(window)
        menus.load_sim_menu.update(events)

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
            # Move the organism
            organism_test.move(window_width, window_height)
            herbivores_test.move()
            carnivores_test.move()

            # Clear screen. Important or else is just paints the screen
            # as the organism moves.
            window.fill(black)

            # Inserting organism on screen in new position
            # White
            organism_test.insert_organism(window)
            # Green
            herbivores_test.insert_organism(window)
            # Teal
            carnivores_test.insert_organism(window)

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
            clock.tick(30)
