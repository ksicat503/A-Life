import pygame
import os
# import numpy as np
import random
# from test_organism import Organism
from carnivores import Carnivores
from herbivores import Herbivores
from menu_handling import Menu_Handler
from json_writer import org_json_writer, json_reader, sim_json_writer
from environments import Grassland, Tundra, Desert, Ocean, Swamp, Forest

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

num_organisms = 10

# Initializing the window
window = pygame.display.set_mode((window_height, window_width))
# This code allows us to change the name of the window
pygame.display.set_caption('Artifical Life Sim')

# clock to set frame rate in simulation
clock = pygame.time.Clock()

# List of terrain types
terrain_classes = [Grassland, Forest, Desert, Ocean, Tundra, Swamp]
# Set organism size
X_PX_SIZE = 50
Y_PX_SIZE = 50
# Setting size of the tiles organisms can move on. Same Size as organism
grid_size = 50
# Setting how many rows and columns
rows = window_height // grid_size
cols = window_width // grid_size
grid = []

# Same code Michael provided but broken out
# Create the grid with each location being assigned a terrain type
# If we are loading a sim, probably a branch here
# to set grid to value of saved info
for _ in range(window_height // Y_PX_SIZE):
    row = []
    for _ in range(window_width // X_PX_SIZE):
        # Randomly select terrain to insert
        # create instance of that terrain
        # then append the terrain in the list
        terrain = random.choice(terrain_classes)
        terrain_instance = terrain()
        row.append(terrain_instance)
    grid.append(row)

# Create Pygame window
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("A-Life Sim Challenge")


# Function to insert different envs for visual representation
def insert_grid_envs():
    for x in range(rows):
        for y in range(cols):
            terrain = grid[x][y]
            pygame.draw.rect(window,
                             terrain.color,
                             (x * grid_size, y * grid_size,
                              grid_size, grid_size))


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
            all_organisms = []
            counter = 0
            for x in range(num_organisms):
                row = random.randint(0, rows - 1)
                col = random.randint(0, cols - 1)
                if counter == 0:
                    all_organisms.append(Herbivores(
                        row*grid_size,
                        col*grid_size,
                        window_h=window_height,
                        window_w=window_width))
                    counter = 1
                else:
                    all_organisms.append(Carnivores(
                        row*grid_size,
                        col*grid_size,
                        window_h=window_height,
                        window_w=window_width))
                    counter = 0
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
            # Make folder for new game save if it doesn't exist
            if not os.path.exists('./saves'):
                os.makedirs('./saves')
            if not os.path.exists(f'./saves/id_{menus.game_id}'):
                os.makedirs(f'./saves/id_{menus.game_id}')
            # Save organism data
            org_json_writer(all_organisms,
                            f'./saves/id_{menus.game_id}/organism.json')
            sim_json_writer(grid,
                            f'./saves/id_{menus.game_id}/sims.json')

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
            sim_json_writer(grid,
                            f'./saves/id_{menus.game_id}/sims.json')
            menus.save_game = False

        if menus.paused:
            menus.draw_pause_menu()
        else:
            # Move all the organisms
            for organism in all_organisms:
                organism.move(grid)

            # Clear screen. Important or else is just paints the screen
            # as the organism moves.
            window.fill(black)
            # Code to insert grid, without moving it constantly
            insert_grid_envs()
            pygame.display.flip()
            # Inserting organism on screen in new position
            for organism in all_organisms:
                organism.insert_organism(window)

        # update the display for the new movement
        pygame.display.update()

        # Setting frame rate, lower setting seems to be easier to follow
        # Also if higher, the sim runs quickly due to energy consumption
        clock.tick(5*menus.speed)
