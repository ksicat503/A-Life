# Do we want to consider doing seasons and stuff?
import random


class Environment:
    """
    Represents an Environment. Should be able to take a square in the sim board

    Attributes:
        name: name of the terrain/environment type
        base_temp: the starting temp of the environment
        weather_options: list of possible weather types present in environment
        weather_freq: list of weighted frequencies for weather_options
        possible_disasters: list of disasters allowed in environment
        starting_resources: starting amount of resources, number between 0 to 1
    """
    def __init__(
            self,
            name,
            base_temp,
            weather_options,
            weather_freq,
            possible_disasters,
            starting_resources=None
            ):
        """
        Initialize environment attributes
        *self.total_resources is randomized
        *Temperature is in Fahrenheit
        """
        self.terrain = name
        self.temperature = base_temp
        self.weather_options = weather_options
        self.weather_freq = weather_freq
        self.possible_disasters = possible_disasters
        self.total_resources = (starting_resources
                                if starting_resources is not None
                                else random.uniform(0.3, 1.0)
                                )
        self.disaster_present = None
        self.weather = "clear"

    def get_weather(self):
        """Returns weather"""
        return self.weather

    def get_temperature(self):
        """Returns temperature"""
        return self.temperature

    def get_total_resources(self):
        """Returns resource amount"""
        return self.total_resources

    def get_terrain(self):
        """Returns terrain"""
        return self.terrain

    def randomize_weather(self):
        """
        Creates a random weather event based on possible weather options
        and weighted frequencies per event.
        """
        self.weather = random.choices(
            self.weather_options,
            weights=self.weather_freq,
            k=1)[0]

    def set_temperature(self, temp):
        """Hard sets temperature"""
        self.temperature = temp

    def use_resources(self, amt):
        """Uses resources. Makes sure the total amount doesnt go below zero"""
        self.total_resources -= amt
        self.total_resources = max(0, self.total_resources - amt)

    def spawn_disaster(self):
        """
        Randomize a disaster
        *Add more disasters if needed and change based on discussions
        *Figure out how this affects everything
        ***Figure out how to end a disaster using game
        """
        disaster_chance = 0.05

        if random.random() < disaster_chance:
            disaster_class = random.choice(self.possible_disasters)
            self.disaster_present = disaster_class()
            print(f"Disaster occured: {self.disaster_present}")

    def end_disaster(self):
        """Ends current disaster if one is present"""
        if self.disaster_present:
            prev_disaster = self.disaster_present
            self.disaster_present = None
            print(f"{prev_disaster} has ended.")
        else:
            print("there is no disaster present")


class Grassland(Environment):
    """Represents a Grassland environment, inherits from Environment."""
    def __init__(self):
        super().__init__(
            "Grassland",
            70,
            ["clear", "rain", "storm"],
            [0.45, 0.4, 0.15],
            ["Drought", "Flood", "Wildfire", "Earthquake"],
        )


class Forest(Environment):
    """Represents a Forest environment, inherits from Environment."""
    def __init__(self):
        super().__init__(
            "Forest",
            50,
            ["clear", "rain", "snow"],
            [0.5, 0.3, 0.2],
            ["Wildfire", "Drought", "Flood", "Earthquake"]
        )

    def regenerate_resources(self):
        """
        Allows regeneration of some resources, 
        randomized between .001 and .005
        """
        # Forests can slowly regenerate resources (trees)
        self.total_resources += random.uniform(0.001, 0.005)


class Desert(Environment):
    """Represents a Desert environment, inherits from Environment."""
    def __init__(self):
        super().__init__(
            "Desert",
            90,
            ["clear", "rain"],
            [0.98, 0.02],
            ["Sandstorm", "Earthquake", "Drought"]
        )


class Ocean(Environment):
    """Represents an Ocean environment, inherits from Environment."""
    # Can edit the weather options in the future
    def __init__(self):
        super().__init__(
            "Ocean",
            60.9,
            ["clear"],
            [1.0],
            None
        )


class Tundra(Environment):
    """Represents a Tundra environment, inherits from Environment."""
    def __init__(self):
        super().__init__(
            "Tundra",
            -30,
            ["clear", "snow", "rain"],
            [0.2, 0.7, 0.1],
            ["Blizzard"]
        )


class Swamp(Environment):
    """Represents a Swamp environment, inherits from Environment."""
    def __init__(self):
        super().__init__(
            "Swamp",
            76,
            ["clear", "rain"],
            [0.45, .55],
            ["Flood", "Hurricane", "Drought"]
        )
