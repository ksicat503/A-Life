import random
import pygame
from constants import WINDOW_HEIGHT, WINDOW_WIDTH, X_PX_SIZE, Y_PX_SIZE


class Organisms:
    def __init__(self, name, x_pos, y_pos, animal_type, speed,
                 mutation_chance):
        # all values below should be adjusted post test simulations
        self.name = name
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.org_height = Y_PX_SIZE
        self.org_width = X_PX_SIZE
        self.window_h = WINDOW_HEIGHT
        self.window_w = WINDOW_WIDTH
        self.age = 0
        self.days_since_fed = 0
        self.energy_level = 10
        self.life_expectancy = 50
        self.mutation_chance = mutation_chance
        self.child_count = 0
        self.is_alive = True
        self.speed = speed
        self.animal_type = animal_type
        self.death_type = None  # 1 for eatten, 2 for starved, 3 for old age

    def __del__(self):
        return

    def set_attributes_from_saved_file(self, data):
        """ Updates organism attributes based on saved data"""
        self.age = data['age']
        self.days_since_fed = data['days_since_fed']
        self.energy_level = data['energy_level']
        self.is_alive = data['is_alive']
        self.death_type = data['death_type']
        self.child_count = data['child_count'],
        self.life_expectancy = data['life_expectancy']
        self.speed = data['speed']
        self.offspring_chance = data['offspring_chance']

        return self

    # Using rectangle, but can update for a different shape or icon
    def insert_organism(self, window):
        """Function to insert organism with defined size, and grid position"""
        if self.is_alive is True:
            colors = [(51, 255, 51), (204, 0, 0)]
            pygame.draw.rect(window,
                             colors[self.animal_type-1],
                             (self.x_pos, self.y_pos,
                              self.org_height, self.org_width))

    def move(self):
        """Finding random values for x and y values.
        -speed is max speed in left or down directions
        Reducing energy for each movement made"""
        self.x_pos = self.x_pos + self.org_width * random.randint(-self.speed,
                                                                  self.speed)
        self.y_pos = self.y_pos + self.org_height * random.randint(-self.speed,
                                                                   self.speed)
        self.energy_level -= 1

        # Code to ensure the organism does not
        # move beyond the boundaries of the screen
        self.x_pos = max(0, min(self.window_w - self.org_width, self.x_pos))
        self.y_pos = max(0, min(self.window_h - self.org_height, self.y_pos))

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

        if random.random() < self.mutation_chance:
            self.offspring_chance += random.randint(-5, 5) / 1000
            self.offspring_chance = max(0.0, self.offspring_chance)

        if random.random() < self.mutation_chance:
            self.life_expectancy += random.randint(-3, 3)
            self.life_expectancy = max(1, self.life_expectancy)

        if random.random() < self.mutation_chance:
            self.speed += random.randint(-2, 2)
            self.speed = max(1, self.speed)
