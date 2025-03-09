import copy
import time
import pygame
from constants import WINDOW_HEIGHT, WINDOW_WIDTH, GRID_S
from data_manager import save_game, get_game_data
from menu_handling import Menu_Handler
from grid_creation import insert_grid_envs
from collision_handling import handle_collisions
# from test_grid_ks import determine_movement


# initializing imported module
# This initializes pygame and fonts to display text
pygame.init()
pygame.font.init()

# This is needed to clear the screen during sim,
# as fill function needs the variable
black = (0, 0, 0)

# clock to set frame rate in simulation
clock = pygame.time.Clock()

# Create Pygame window
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("A-Life Sim Challenge")

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
        grid = data[1]
        menus.set_organism_data(all_organisms)
        # Keeping track of time, as we may need this for age
        start_time = time.time()

    while menus.sim_active:
        # Set up event for when the user quits out of the screen
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    menus.current_menu = 'pause'
            elif (menus.current_menu == 'none' and
                  event.type == pygame.MOUSEBUTTONUP):
                if menus.set_organism(event.pos):
                    menus.current_menu = 'individual_organism'

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
            if menus.speed != 0:
                # Move all the organisms while managing organism collisions
                for moving_organism in all_organisms:
                    # if this organism is set to dead from previous move step,
                    # continue to next organism in loop
                    if not moving_organism.is_alive:
                        continue

                    # save original organism, in case of collision with a same
                    # animal_type organism
                    original_pos = (moving_organism.x_pos,
                                    moving_organism.y_pos)


                    # move the organism
                    moving_organism.move()
                    # determine_movement(moving_organism, grid)


                    # check for collision, if collided, break and check the
                    # next organism that will be moving
                    did_collide = handle_collisions(
                        moving_organism, all_organisms, original_pos)

                    if did_collide:
                        break


                for organism in all_organisms:
                    y, x = organism.y_pos, organism.x_pos
                    grid_tile = grid[y//GRID_S][x//GRID_S]
                    if organism.animal_type == 1:
                        if grid_tile.__dict__["herb_food"] > 0:
                            grid_tile.__dict__["herb_food"] -= 1
                            organism.energy_level += 1.2
                            # print(organism.__dict__)
                    else:
                        if grid_tile.__dict__["carn_food"] > 0:
                            grid_tile.__dict__["carn_food"] -= 1
                            organism.energy_level += 1.2
                        #     print(organism.__dict__)
                    # print(grid_tile.__dict__)

                # Chance of all organisms to reproduce
                for reproducing_organism in all_organisms:

                    # if successful at reproducing, create a deep copy of it
                    if reproducing_organism.reproduce():
                        new_organism = copy.deepcopy(reproducing_organism)

                        # reset some parameters to default for new organism
                        new_organism.age = 0
                        new_organism.days_since_fed = 0
                        new_organism.energy_level = 10

                        # move the organism so it does not overlap
                        # with the parent
                        new_organism.move()

                        # save original organism, in case of collision with
                        # a same animal_type organism, check for collision
                        original_pos = (new_organism.x_pos, new_organism.y_pos)
                        did_collide = handle_collisions(
                            new_organism, all_organisms, original_pos)

                        # if not collided, add new spawn to list of all
                        # organisms, else delete the object
                        if not did_collide:
                            all_organisms.append(new_organism)
                        else:
                            del new_organism

            # Clear screen. Important or else is just paints the screen
            # as the organism moves.
            window.fill(black)
            # Code to insert grid, without moving it constantly
            insert_grid_envs(window, grid)
            pygame.display.flip()
            # Inserting organism on screen in new position
            for organism in all_organisms:
                organism.insert_organism(window)
                organism.age += .02

        # update the display for the new movement
        pygame.display.update()
        end_time = time.time()

        # Setting frame rate, lower setting seems to be easier to follow
        # Also if higher, the sim runs quickly due to energy consumption
        clock.tick(5*menus.speed if menus.speed != 0 else 60)

        # Printing out time out to 2 decimal placese
        elapsed_time = end_time - start_time
        formatted_time = "{:.2f}".format(elapsed_time)
        # print(formatted_time)
