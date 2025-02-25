import random
import pygame
from environments import Grassland, Tundra, Desert, Swamp, Forest
from constants import WINDOW_HEIGHT, WINDOW_WIDTH, GRID_S, X_PX_SIZE, Y_PX_SIZE

# List of terrain types
terrain_classes = [Grassland, Forest, Desert, Tundra, Swamp]

# # Setting how many rows and columns using constans
rows = WINDOW_HEIGHT // GRID_S
cols = WINDOW_WIDTH // GRID_S


def create_grid():
    """Function to create a grid with a chance of placing
    like terrain next to one another.
    As this moves left to right, a neighbor is either directly left or above"""
    grid = []
    # Loop through each row, top to bottom
    for y in range(rows):
        row = []
        # Loop through each position in the row, left to right
        for x in range(cols):
            neighbors = []
            # Checking for an above neighbor
            if y > 0:
                neighbors.append(grid[y-1][x])
            # Checking for a neighbor to the left
            if x > 0:
                neighbors.append(row[x-1])
            # Make a random check to see if a
            # neighboring terrain will be selected
            if neighbors and random.random() < 0.80:
                terrain = random.choice(neighbors)
            else:
                terrain = random.choice(terrain_classes)()
            # append terain to row, then after loop update grid with new row
            row.append(terrain)
        grid.append(row)
    return grid


def insert_grid_envs(window, grid):
    """Function to insert the previously created grid
    within the viewing window"""
    for y in range(rows):
        for x in range(cols):
            terrain = grid[y][x]
            pygame.draw.rect(window,
                             terrain.color,
                             (x * GRID_S,
                              y * GRID_S,
                              X_PX_SIZE,
                              Y_PX_SIZE))
