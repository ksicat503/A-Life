import random
from organisms import Organisms


class Herbivores(Organisms):
    def __init__(self, x_pos, y_pos):
        super().__init__(x_pos, y_pos)
        self.maturation_age = 10
        self.offspring_chance = 0.05

    def move(self):
        """Herbivores-speicifc movement features.

        If occupying grassland, reset days_since_fed to 0.
        """
        super().move()
        # TO-DO: reset days_since_fed to 0 if new position overlaps with
        # grassland unit in the environment

    def reproduce(self):
        """Random chance of offspring reproduction.

        If Herbivore age is higher than maturation_age, create a new instance
        of Herbivore object next to it.
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
            Herbivores(new_x_pos, self.y_pos)
