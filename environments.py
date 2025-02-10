# Do we want to consider doing seasons and stuff?
import random


class Environment:
    def __init__(
            self,
            name,
            base_temp,
            weather_options,
            weather_freq,
            possible_disasters,
            color,
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
        self.color = color
        self.total_resources = (starting_resources
                                if starting_resources is not None
                                else random.uniform(0.3, 1.0)
                                )
        self.disaster_present = None
        self.weather = "clear"

    def get_weather(self):
        return self.weather

    def get_temperature(self):
        return self.temperature

    def get_total_resources(self):
        return self.total_resources

    def get_terrain(self):
        return self.terrain

    def randomize_weather(self, we):
        self.weather = random.choices(
            self.weather_options,
            weights=self.weather_freq,
            k=1)[0]

    def set_temperature(self, temp):
        self.temperature = temp

    def use_resources(self, amt):
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
        if not self.disaster_present:
            prev_disaster = self.disaster_present
            self.disaster_present = None
            print(f"{prev_disaster} has ended.")
        else:
            print("there is no disaster present")


class Grassland(Environment):
    def __init__(self):
        super().__init__(
            "Grassland",
            70,
            ["clear", "rain", "storm"],
            [0.45, 0.4, 0.15],
            ["Drought", "Flood", "Wildfire", "Earthquake"],
            (124, 192, 64)
        )


class Forest(Environment):
    def __init__(self):
        super().__init__(
            "Forest",
            50,
            ["clear", "rain", "snow"],
            [0.5, 0.3, 0.2],
            ["Wildfire", "Drought", "Flood", "Earthquake"],
            (34, 85, 34)
        )

    def regenerate_resources(self):
        # Forests can slowly regenerate resources (trees)
        self.total_resources += random.uniform(0.001, 0.005)


class Desert(Environment):
    def __init__(self):
        super().__init__(
            "Desert",
            90,
            ["clear", "rain"],
            [0.98, 0.02],
            ["Sandstorm", "Earthquake", "Drought"],
            (237, 201, 175)
        )


class Ocean(Environment):
    # Can edit the weather options in the future
    def __init__(self):
        super().__init__(
            "Ocean",
            60.9,
            ["clear"],
            [1.0],
            None,
            (28, 107, 160)
        )


class Tundra(Environment):
    def __init__(self):
        super().__init__(
            "Tundra",
            -30,
            ["clear", "snow", "rain"],
            [0.2, 0.7, 0.1],
            ["Blizzard"],
            (180, 190, 190)
        )


class Swamp(Environment):
    def __init__(self):
        super().__init__(
            "Swamp",
            76,
            ["clear", "rain"],
            [0.45, .55],
            ["Flood", "Hurricane", "Drought"],
            (63, 92, 51)
        )
