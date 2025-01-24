import random
#import pygame

class Herbivores:
    def __init__(self, x_pos, y_pos):
        # all values below should be adjusted post test simulations
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.age = 0
        self.days_since_fed = 0
        self.energy_level = 5
        self.life_expectancy = 20
        self.offspring_chance = 0.2
        self.can_reproduce = False
        if self.age >= 5 and self.age <= 15:
            self.can_reproduce = True
        self.is_alive = True
    
    def move(self):
        """Change position of the carnivore organism.
        
        Is limited by the environmental grid, and self.is_alive sets to False
        if an instance of Carnivores object occupies same position. Instances
        of Herbivore objects can occupy the same position. 
        """
        if not self.is_alive:
            return
        
        self.x_pos = self.x_pos + random.randint(-1, 1)
        self.y_pos = self.y_pos + random.randint(-1, 1)

        # implement game events of next cycle post movement here
        # multiple organisms of the same class can occupy same pos
        # if new x_pos or y_pos is outside grid, return original pos
        # if new pos is occupied by food resources, reset
        #   self.days_since_fed to 0
        # if new pos is occupied by a carnivore on the same turn,
        #   set self.is_alive to False and carnivore.days_since_fed to 0

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
        if not self.is_alive:
            return
        
        self.age += 1
        chance_by_age = (self.life_expectancy - self.age) \
            / self.life_expectancy
        
        self.days_since_fed += 1
        chance_by_energy = (self.energy_level - self.days_since_fed) \
            / self.energy_level

        if chance_by_energy or chance_by_age < random.random():
            self.is_alive = False
        
        '''
        *** (POTENTIALLY) IMPLEMENT DISASTER PARAMETERS HERE,
        IMPORT DISASTER PAREMETERS FROM 'ENVIRONMENT' CLASS? ***
        '''

    def reproduction_chance(self):
        """Random chance of offspring reproduction.
        
        If organism age is between 5 and 15 inclusive, there is a
        self.offspring_chance probability that a new Herbivores instance of
        object created in the same position.
        """
        if not self.is_alive:
            return
        
        if self.can_reproduce and self.offspring_chance > random.random():
            Herbivores(self.x_pos, self.y_pos)