import random
from organisms import Organisms


class Carnivores(Organisms):
    def __init__(self, name, x_pos, y_pos, mutation_chance):
        super().__init__(name, x_pos, y_pos, 2, 2, mutation_chance)
        self.name = f"carn{name}"
        self.maturation_age = 15
        self.offspring_chance = 0.05
        self.animal_type = 2
        self.consumed_count = 0

    def move(self):
        """Carnivores-speicifc movement features."""
        super().move()

    def reproduce(self):
        """Random chance of offspring reproduction.

        If age-mature and enough energy, random chance of returning True
        """
        if not self.is_alive:
            return

        if (self.age > self.maturation_age and
                self.offspring_chance > random.random() and
                self.energy_level > 40):
            self.energy_level -= 25
            return True
        else:
            return False
