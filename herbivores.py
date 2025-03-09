import random
from organisms import Organisms


class Herbivores(Organisms):
    def __init__(self, x_pos, y_pos, mutation_chance):
        super().__init__(x_pos, y_pos, 1, 1, mutation_chance)
        self.maturation_age = 10
        self.offspring_chance = 0.05
        self.animal_type = 1

    def move(self):
        """Herbivores-speicifc movement features."""
        super().move()

    def reproduce(self):
        """Random chance of offspring reproduction.

        If age-mature and enough energy, random chance of returning True
        """
        if not self.is_alive:
            return

        if (self.age > self.maturation_age and
           self.offspring_chance > random.random() and
           self.energy_level > 50):
            return True
        else:
            return False
