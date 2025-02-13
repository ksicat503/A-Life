import random
from environments import Grassland, Forest, Desert, Ocean, Tundra, Swamp
from carnivores import Carnivores
from herbivores import Herbivores


def search_food(carnivore, grid):
    """Carnivore searches for other organisms, right now herbivores
    for food. Uses greedy search and then moves the shortest
    direction if food is found.
    *TO IMPLEMENT: MOVE WHEN PREY FOUND AND IF NO PREY FOUND
        WILL RANDOMLY MOVE IF NO PREY FOUND
    Args:
        carnivore: Carnivore object of interest
        grid: environment grid we are working with

    ***IMPLEMENT LATER AFTER DISCUSSION:
    1. Check carnivore energy levels as they can affect how far they
      can move/hunt
    2. What to do with sensing radius? For this test I make it
        fixed at 2.
    3. Is a hunt always successful, energy levels, can carnivore
        hunt carnivore?
    """
    # prey_positions stores any positions with possible food
    sense_radius = 2
    prey_positions = []

    # Scan tiles
    for dx in range(-sense_radius, sense_radius + 1):
        for dy in range(-sense_radius, sense_radius + 1):
            new_x, new_y = carnivore.x_pos + dx, carnivore.y_pos + dy

            # Stay within grid
            if 0 <= new_x < len(grid) and 0 <= new_y < len(grid[0]):
                tile = grid[new_x][new_y]

                # Checks if herbivore is on the square
                # in the future tiles will have multiple orgnaisms?
                for organism in tile.inhabitants:
                    if isinstance(organism, Herbivores):
                        prey_positions.append((new_x, new_y))

    # if prey_positions:

    return prey_positions


def flee(herbivore, grid):
    """Herbivore detects predators and has a 50% chance
    to flee 1-2 tiles away
    Uses same algorithm as search_food
    ***Moving is not implmeneted yet

    Args:
        herbivore: herbivore object of interest
        grid: environment grid we are working with

    ***IMPLEMENT LATER AFTER DISCUSSION:
    1. Fleeing, how far and if always successful"""

    sense_radius = 2
    predator_positions = []

    for dx in range(-sense_radius, sense_radius + 1):
        for dy in range(-sense_radius, sense_radius + 1):
            new_x, new_y = herbivore.x_pos + dx, herbivore.y_pos + dy

            # Ensure position is within grid bounds
            if 0 <= new_x < len(grid) and 0 <= new_y < len(grid[0]):
                tile = grid[new_x][new_y]

                # Check only the first occupant (since only 1 per tile)
                for organism in tile.inhabitants:
                    if isinstance(organism, Carnivores):
                        predator_positions.append((new_x, new_y))
    # TO IMPLEMENT: FLEEING DYNAMICS AND WHERE
    return predator_positions


def print_grid(grid):
    """Print grid for visualization"""
    environment_symbols = {
        "Grassland": "G",
        "Forest": "F",
        "Desert": "D",
        "Ocean": "O",
        "Tundra": "T",
        "Swamp": "S"
    }

    organism_symbols = {
        "Carnivores": "C",
        "Herbivores": "H"
    }

    for row in grid:
        row_display = []
        for cell in row:
            # Check if any organisms present
            # CURENT VERSION: ONLY DISPLAY FIRST ORG IN LIST
            if cell.inhabitants:
                first_organism = cell.inhabitants[0]
                row_display.append(
                    organism_symbols.get(type(first_organism).__name__, "?"))
            else:
                row_display.append(environment_symbols[cell.terrain])
        print(" ".join(environment_symbols[cell.terrain] for cell in row))
    print("\n")


# test grid sizes
grid_x = 10
grid_y = 10

# create test grid
environment_classes = [Grassland, Forest, Desert, Ocean, Tundra, Swamp]
test_grid = []
for x in range(grid_x):
    test_col = []
    for y in range(grid_y):
        environment = random.choice(environment_classes)
        environment_instance = environment()
        test_col.append(environment_instance)
    test_grid.append(test_col)


# Initialize test organisms
# Random x, y coordinate to test algorithm and logic
carn_1_x = random.choice([1, 2, 3, 4, 6, 7, 8, 9, 10])
carn_1_y = random.randint(1, 10)
herb_1_x = 5
herb_1_y = 6

# Test that should return values for search and flee
# carn_1_x = 4
# carn_1_y = 6
# herb_1_x = 5
# herb_1_y = 6

print(f"carn_1 x, y: {carn_1_x}, {carn_1_y}")
print(f"herb_1 x, y: {herb_1_x}, {herb_1_y}")

# Test organisms
carn_1 = Carnivores(carn_1_x, carn_1_y, grid_x,
                    grid_y, org_height=1, org_width=1)

herb_1 = Herbivores(herb_1_x, herb_1_y, grid_x, grid_y,
                    org_height=1, org_width=1)

# Place organisms on the grid
test_grid[carn_1.x_pos][carn_1.y_pos].inhabitants.append(carn_1)
test_grid[herb_1.x_pos][herb_1.y_pos].inhabitants.append(herb_1)

# Print the initial grid state
print("Initial Grid State:")
print_grid(test_grid)

# print function results
print(search_food(carn_1, test_grid))
print(flee(herb_1, test_grid))
