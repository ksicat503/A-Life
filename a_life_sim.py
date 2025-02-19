import random

import pygame

from constants import WINDOW_HEIGHT, WINDOW_WIDTH, X_PX_SIZE, Y_PX_SIZE
from data_manager import save_game, get_game_data
from environments import Grassland, Tundra, Desert, Swamp, Forest
from menu_handling import Menu_Handler

# initializing imported module
# This initializes pygame and fonts to display text
pygame.init()
pygame.font.init()

# This is needed to clear the screen during sim,
# as fill function needs the variable
black = (0, 0, 0)

# clock to set frame rate in simulation
clock = pygame.time.Clock()

# List of terrain types
terrain_classes = [Grassland, Forest, Desert, Tundra, Swamp]

# Setting size of the tiles organisms can move on. Same Size as organism
grid_size = 20
# Setting how many rows and columns
rows = WINDOW_HEIGHT // grid_size
cols = WINDOW_WIDTH // grid_size
grid = []

# Same code Michael provided but broken out
# Create the grid with each location being assigned a terrain type
# If we are loading a sim, probably a branch here
# to set grid to value of saved info
for _ in range(WINDOW_HEIGHT // Y_PX_SIZE):
    row = []
    for _ in range(WINDOW_WIDTH // X_PX_SIZE):
        # Randomly select terrain to insert
        # create instance of that terrain
        # then append the terrain in the list
        terrain = random.choice(terrain_classes)
        terrain_instance = terrain()
        row.append(terrain_instance)
    grid.append(row)

# Create Pygame window
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("A-Life Sim Challenge")


# Function to insert different envs for visual representation
def insert_grid_envs():
    for y in range(rows):
        for x in range(cols):
            terrain = grid[y][x]
            pygame.draw.rect(window,
                             terrain.color,
                             (x * grid_size, y * grid_size,
                              grid_size, grid_size))


# Initalize menus
menus = Menu_Handler(window)

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
            data = get_game_data()
        else:
            data = get_game_data(menus.game_id)

        all_organisms = data[0]
        # Need to implement loading grid in get_game_data func
        # grid = data[1]
        menus.set_organism_data(all_organisms)

    while menus.sim_active:
        # Set up event for when the user quits out of the screen
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    menus.current_menu = 'pause'
            # if event is of type quit then
            # set running bool to false
            if event.type == pygame.QUIT:
                menus.sim_active = False
                pygame_active = False
                # Should we save here? or only save when the user presses
                # the save button in the pause menu?
                save_game(menus.game_id, all_organisms, grid)

        if menus.current_menu != 'none':
            menus.display_menu()
            # Check if game needs to be saved
            if menus.save_game:
                save_game(menus.game_id, all_organisms, grid)
                menus.save_game = False
        else:
            # Move all the organisms
            # Move all the organisms, manage organism collisions
            for moving_organism in all_organisms:
                # if this organism is set to dead from previous move step,
                # continue to next organism in loop
                if not moving_organism.is_alive:
                    continue

                # save original organism, in case of collision with a same
                # animal_type organism
                original_organism = (moving_organism.x_pos,
                                     moving_organism.y_pos)
                moving_organism.move()

                # check all other organisms for collisions
                for check_organism in all_organisms:
                    if not check_organism.is_alive:
                        continue
                    # check to avoid self-collision
                    if moving_organism is check_organism:
                        continue
                    moving_org = pygame.Rect(moving_organism.x_pos,
                                             moving_organism.y_pos,
                                             X_PX_SIZE,
                                             Y_PX_SIZE)
                    check_org = pygame.Rect(check_organism.x_pos,
                                            check_organism.y_pos,
                                            X_PX_SIZE,
                                            Y_PX_SIZE)

                    if moving_org.colliderect(check_org):
                        # manage herbivore and carnivore collisions
                        if (
                            moving_organism.animal_type == 1 and
                            check_organism.animal_type == 2
                        ):
                            moving_organism.is_alive = False
                            check_organism.days_since_fed = 0
                            break
                        if (
                            moving_organism.animal_type == 2 and
                            check_organism.animal_type == 1
                        ):
                            check_organism.is_alive = False
                            moving_organism.days_since_fed = 0
                            break
                        # when same animal_type collides, revert back the
                        # moving_organism to its original position
                        else:
                            (moving_organism.x_pos,
                             moving_organism.y_pos) = original_organism

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
