import random
import pygame

black = (0, 0, 0)


# Organism class, may be easier to make class for each organsim
# Can discuss or use one class for all and randomly set some values
# If using one class, will need some unique identifier most likely
class Organism:
    def __init__(self, x_pos, y_pos, window_h, window_w,
                 org_height, org_width):
        # all values below should be adjusted post test simulations
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.org_height = org_height
        self.org_width = org_width
        self.window_h = window_h
        self.window_w = window_w
        self.age = 0
        self.days_since_fed = 0
        self.energy_level = 3
        self.life_expectancy = 10
        self.offspring_chance = 0.1
        self.can_reproduce = False
        if self.age >= 3 and self.age <= 7:
            self.can_reproduce = True
        self.is_alive = True
        self.speed = 2

    # Using rectangle, but can update for a different shape or icon
    def insert_organism(self, window):
        """Function to insert organism with defined size, and grid position"""
        pygame.draw.rect(window, (255, 255, 255), (self.x_pos, self.y_pos,
                                                   self.org_height,
                                                   self.org_width))

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
