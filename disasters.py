import random


class Disaster():
    """Parent class for all disasters."""
    def __init__(self, name, duration):
        self.name = name
        self.duration = (duration
                         if duration
                         else random.randint(2, 5)
                         )

    def apply_effect(self, environment):
        """Disaster subclasses will take care of logic"""
        raise NotImplementedError("Each disaster"
                                  "must implement its own effects.")

    def end_effect(self, environment):
        pass

    def __str__(self):
        return f"Disaster: {self.name} \n Duration: {self.duration}"


class Drought(Disaster):
    """Reduces resource, raises temperature"""
    def __init__(self):
        super().__init__("Drought")

    def apply_effect(self, environment):
        environment.temperature += random.randint(7, 10)
        environment.total_resources -= random.uniform(0.08, 0.15)


class Flood(Disaster):
    """Reduce resource, slightly lower temperate.
    ***DISCUSS: kill off some of population?"""
    def __init__(self):
        super().__init__("Flood")

    def apply_effect(self, environment):
        environment.temperature -= random.randint(3, 5)
        environment.total_resources -= random.uniform(0.1, 0.15)


class Earthquake(Disaster):
    """Small reduction of resources
    ***DISCUSS: kill off some of population?"""
    def __init__(self):
        super().__init__("Earthquake")

    def apply_effect(self, environment):
        environment.total_resources -= random.uniform(0.03, 0.07)


class Wildfire(Disaster):
    """Increase in temp, loss of resource
    ***this definetly kills off some of the population. will implement later"""
    def __init__(self):
        super().__init__("Wildfire")

    def apply_effect(self, environment):
        environment.temperate += random.randint(5, 7)
        environment.total_resources -= random.uniform(0.1, 0.3)


class Sandstorm(Disaster):
    def __init__(self):
        super().__init__("Sandstorm")

    def apply_effect(self, environment):
        environment.temperature += random.randint(5, 7)
