import os
import random

from carnivores import Carnivores
from constants import GRID_COLS, GRID_ROWS, GRID_S
from environments import Grassland, Tundra, Desert, Swamp, Forest
from grid_creation import create_grid
from herbivores import Herbivores
from json_writer import org_json_writer, json_reader, sim_json_writer
from test_organism import Organism

env_mapping = {
    "Grassland": Grassland,
    "Tundra": Tundra,
    "Desert": Desert,
    "Swamp": Swamp,
    "Forest": Forest
    }
org_mapping = [
    Organism, Herbivores, Carnivores
]


def save_game(game_id, organisms, grid):
    """ Saves game data"""
    create_folders(game_id)
    org_json_writer(organisms, f'./saves/id_{game_id}/organism.json')
    sim_json_writer(grid, f'./saves/id_{game_id}/grid.json')


def create_folders(game_id):
    """ Creates folders for game data if needed"""
    if not os.path.exists('./saves'):
        os.makedirs('./saves')
    if not os.path.exists(f'./saves/id_{game_id}'):
        os.makedirs(f'./saves/id_{game_id}')


def get_game_data(data=None, game_id=None):
    """
    Returns organism and grid data
    """
    if game_id is None:
        return [get_random_starting_organisms(data), create_grid()]
    else:
        # Need to implement loading in saved grid data
        return [load_organisms(game_id), load_grid(game_id)]


def get_random_starting_organisms(data):
    """Randomly place a number of herbivores and carnivores."""
    all_organisms = []

    for _ in range(data['herb_count']):
        row = random.randint(0, GRID_ROWS) * GRID_S
        col = random.randint(0, GRID_COLS) * GRID_S
        all_organisms.append(Herbivores(_,
                                        row,
                                        col,
                                        data['mutation_chance']
                                        ))

    for _ in range(data['carn_count']):
        row = random.randint(0, GRID_ROWS) * GRID_S
        col = random.randint(0, GRID_COLS) * GRID_S
        all_organisms.append(Carnivores(_,
                                        row,
                                        col,
                                        data['mutation_chance']
                                        ))

    return all_organisms


def load_organisms(game_id):
    """ Load organism from json file"""
    organism_data = json_reader(
                f"./saves/id_{game_id}/organism.json")
    # Makes new organisms and loads saved data
    all_organisms = [
        org_mapping[organism['animal_type']](
            organism['x_pos'],
            organism['y_pos'],
            organism['mutation_chance']
        ).set_attributes_from_saved_file({
            'age': organism['age'],
            'days_since_fed': organism['days_since_fed'],
            'energy_level': organism['energy_level'],
            'is_alive': organism['is_alive'],
            'death_type': organism['death_type']
        })
        for organism in organism_data
    ]

    return all_organisms


def load_grid(game_id):
    """ Builds grid based on saved grid data"""
    grid_data = json_reader(
                f"./saves/id_{game_id}/grid.json")

    # Makes new env instances and loads saved data
    env_instances = [
        env_mapping[element['terrain']]().set_attributes_from_saved_file({
            'temperature': element['temperature'],
            'total_resources': element['total_resources'],
            'disaster_present': element['disaster_present'],
            'weather': element['weather']
        })
        for element in grid_data
    ]

    # Converts 1d array to 2d array
    grid = [env_instances[index:index+GRID_COLS] for index in range(
        0, GRID_COLS*GRID_ROWS, GRID_COLS)
        ]
    return grid
