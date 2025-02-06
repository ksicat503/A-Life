import random
from organisms import Organisms


class Carnivores(Organisms):
    def __init__(self, x_pos, y_pos, window_h, window_w):
        super().__init__(x_pos, y_pos, window_h, window_w)
        self.maturation_age = 10
        self.offspring_chance = 0.05
        self.animal_type = 2

    def move(self):
        """Carnivores-speicifc movement features.

        If new position overlaps with a Herbivore object, reset days_since_fed
        to 0 and delete instance of the consumed Herbivore object
        """
        super().move()
        # TO-DO: reset days_since_fed to 0 when new position overlaps with a
        # Herbivore object, remove consumed Herbivore object

    def reproduce(self):
        """Random chance of offspring reproduction.

        If Carnivore age is higher than maturation_age, create a new instance
        of Carnivore object next to it.
        """
        if not self.is_alive:
            return

        if (self.age > self.maturation_age and
                self.offspring_chance > random.random()):
            new_x_pos = self.x_pos + self.org_width
            if new_x_pos > self.window_w:
                new_x_pos = self.x_pos - self.org_width
            # TO-DO: if new organism instance location is already occupied,
            # return without reproducing
            Carnivores(new_x_pos, self.y_pos)
