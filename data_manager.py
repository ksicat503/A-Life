import os
import random

from carnivores import Carnivores
from herbivores import Herbivores
from grid_creation import create_grid
from json_writer import org_json_writer, json_reader, sim_json_writer
from test_organism import Organism
from constants import WINDOW_HEIGHT, WINDOW_WIDTH, GRID_S


def save_game(game_id, organisms, grid):
    """ Saves game data"""
    create_folders(game_id)
    org_json_writer(organisms, f'./saves/id_{game_id}/organism.json')
    sim_json_writer(grid, f'./saves/id_{game_id}/sims.json')


def create_folders(game_id):
    """ Creates folders for game data if needed"""
    if not os.path.exists('./saves'):
        os.makedirs('./saves')
    if not os.path.exists(f'./saves/id_{game_id}'):
        os.makedirs(f'./saves/id_{game_id}')


def get_game_data(game_id=None):
    """
    Returns organism and grid data
    """
    if game_id is None:
        return [get_random_starting_organisms(), create_grid()]
    else:
        # Need to implement loading in saved grid data
        return [load_organisms(game_id), create_grid()]


def get_random_starting_organisms():
    """Randomly place a number of herbivores between 8-15
    and add 1/3 that number of carnivores."""
    num_herbivores = random.randint(8, 16)
    num_carnivores = max(1, num_herbivores // 2)
    rows = WINDOW_WIDTH // GRID_S
    cols = WINDOW_HEIGHT // GRID_S

    all_organisms = []

    for _ in range(num_herbivores):
        row = random.randint(0, rows) * GRID_S
        col = random.randint(0, cols) * GRID_S
        all_organisms.append(Herbivores(row,
                                        col
                                        ))

    for _ in range(num_carnivores):
        row = random.randint(0, rows) * GRID_S
        col = random.randint(0, cols) * GRID_S
        all_organisms.append(Carnivores(row,
                                        col
                                        ))

    return all_organisms


def load_organisms(game_id):
    """ Load organism from json file"""

    all_organisms = []
    organism_data = json_reader(
                f"./saves/id_{game_id}/organism.json")
    for organism in organism_data:
        # will need to update.
        if organism['animal_type'] == 0:
            animal = Organism(organism['x_pos'], organism['y_pos'])
        elif organism['animal_type'] == 1:
            animal = Herbivores(organism['x_pos'], organism['y_pos'])
        else:
            animal = Carnivores(organism['x_pos'], organism['y_pos'])
        all_organisms.append(animal)
    return all_organisms
