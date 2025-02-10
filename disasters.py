import random


class Disaster():
    """Represents a Disaster"""
    def __init__(self, name, duration):
        self.name = name
        self.duration = (duration
                         if duration
                         else random.randint(2, 5)
                         )

    def apply_effect(self, environment):
        """Disaster child classes will take care of logic"""
        raise NotImplementedError("Each disaster"
                                  "must implement its own effects.")

    def end_effect(self, environment):
        """
        Ends effects of a disaster if any are present.
        Will be handled by child class
        """
        pass

    def __str__(self):
        return f"Disaster: {self.name} \n Duration: {self.duration}"


class Drought(Disaster):
    """Represents a Drought disaster, inherits from Disaster"""
    def __init__(self):
        super().__init__("Drought")

    def apply_effect(self, environment):
        environment.temperature += random.randint(7, 10)
        environment.total_resources -= random.uniform(0.08, 0.15)


class Flood(Disaster):
    """Represents a Flood disaster, inherits from Disaster"""
    def __init__(self):
        super().__init__("Flood")

    def apply_effect(self, environment):
        """
        reduces resource and lowers temperature
        ***DISCUSS: kill of some of population?
        """
        environment.temperature -= random.randint(3, 5)
        environment.total_resources -= random.uniform(0.1, 0.15)


class Earthquake(Disaster):
    """Represents a Earthquake disaster, inherits from Disaster"""
    def __init__(self):
        super().__init__("Earthquake")

    def apply_effect(self, environment):
        """Reduces resources."""

        environment.total_resources -= random.uniform(0.03, 0.07)


class Wildfire(Disaster):
    """Represents a Wildfire disaster, inherits from Disaster"""

    def __init__(self):
        super().__init__("Wildfire")

    def apply_effect(self, environment):
        """
        Increases temperature and loses some resources.
        ***DISCUSS: This should kill some of the population?
        """
        environment.temperature += random.randint(5, 7)
        environment.total_resources -= random.uniform(0.1, 0.3)


class Sandstorm(Disaster):
    """Represents a Wildfire disaster, inherits from Disaster"""
    def __init__(self):
        super().__init__("Sandstorm")

    def apply_effect(self, environment):
        """Increases temperature slightly"""
        environment.temperature += random.randint(5, 7)
