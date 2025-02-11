import random
import pygame


class Organisms:
    def __init__(self, x_pos, y_pos, window_h, window_w):
        # all values below should be adjusted post test simulations
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.org_height = 50
        self.org_width = 50
        self.window_h = window_h
        self.window_w = window_w
        self.age = 0
        self.days_since_fed = 0
        self.energy_level = 10
        self.life_expectancy = 50
        self.is_alive = True
        self.speed = 5
        self.animal_type = 0

    def __del__(self):
        return

    # Using rectangle, but can update for a different shape or icon
    def insert_organism(self, window):
        """Function to insert organism with defined size, and grid position"""
        if self.is_alive:
            pygame.draw.rect(window, self.color, (self.x_pos, self.y_pos,
                                                  self.org_height,
                                                  self.org_width))

    def move(self, grid):
        """Finding random values for x and y values.
        -speed is max speed in left or down directions
        Reducing energy for each movement made"""
        # Move organism randomly and reduce energy
        if not self.is_alive:
            return

        new_x = self.x_pos // 50 + random.randint(-2, 2)
        new_y = self.y_pos // 50 + random.randint(-2, 2)

        new_x = max(0, min(len(grid[0])-1, new_x))
        new_y = max(0, min(len(grid)-1, new_y))

        self.x_pos = new_x * 50
        self.y_pos = new_y * 50

    def survival_chance(self):
        """Random survival chance. *** ADD DISASTER-SURVIVAL CHANCE HERE???***

        Age of the organism is incremented, then calculates survival
            chance by:

            (life expectancy - current age) / (life expectancy)

        Days since last feeding day is incremented, then calculates survival
            chance by:

            (energy level - days since fed) / (energy level)

            if either values are below a random float between 0 and 1, set
            self.is_alive to False
        """
        chance_by_age = ((self.life_expectancy - self.age) /
                         self.life_expectancy)

        chance_by_energy = ((self.energy_level - self.days_since_fed) /
                            self.energy_level)

        if chance_by_energy or chance_by_age < random.random():
            self.is_alive = False

        '''
        *** (POTENTIALLY) IMPLEMENT DISASTER PARAMETERS HERE,
        IMPORT DISASTER PAREMETERS FROM 'ENVIRONMENT' CLASS? ***
        '''

    def mutation(self):
        """
        Cause a random mutation in organism.
        Mutation can randomly affect organism traits
        *Decide what traits/numbers we want to use
        """
        mutation_chance = 0.1

        if random.random() < mutation_chance:
            self.offspring_chance += random.randint(-0.05, 0.05)
            self.offspring_chance = max(0.0, self.offspring_chance)

        if random.random() < mutation_chance:
            self.life_expectancy += random.randint(-3, 3)
            self.life_expectancy = max(1, self.life_expectancy)

        if random.random() < mutation_chance:
            self.speed += random.randint(-2, 2)
            self.speed = max(1, self.speed)
