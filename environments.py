import random


class Environment:
    def __init__(self, terrain):
        """
        Initialize environment attributes
        *Temperature is in Fahrenheit
        """
        self.weather = "clear"
        self.temperature = 65
        self.total_resources = 1.0
        self.terrain = terrain
        self.disaster_present = None

    def get_weather(self):
        return self.weather

    def get_temperature(self):
        return self.temperature

    def get_total_resources_left(self):
        return self.total_resources

    def get_terrain(self):
        return self.terrain

    def set_weather(self, condition):
        """hardset weather

        Args:
            temp (int): temperature
        """
        # Can add more
        weather_types = ["clear", "rain", "storm", "snow"]
        if condition not in weather_types:
            print(f"Valid weather types {weather_types}")
        else:
            self.weather = condition
            print(f"New Weather condition: {self.weather}")

    def randomize_weather(self):
        weather_types = ["clear", "rain", "storm", "snow"]
        self.weather = random.choice(weather_types)

    def set_temperature(self, temp):
        self.temperature = temp

    def use_resources(self, amt):
        self.total_resources -= amt
        self.total_resources = max(0, self.total_resources - amt)

    def set_terrain(self, terr):
        """
        Hardset terrain

        Args:
            terr (str): terrain of choice
        """
        terrains = ["Grassland", "Forest", "Desert", "Water", "Tundra", "Swamp"]
        if terr not in terrains:
            print(f"{terr} is not in the list of {terrains}")

        else:
            self.terrain = terr
            print(f"Terrain set: {self.terrain}")

    def spawn_disaster(self):
        """
        Randomize a disaster
        *Add more disasters if needed, or change how this works based on what we want
        *Figure out how this affects everything
        """
        disaster_chance = 0.05
        disasters = ["Drought", "Flood", "Earthquake"]

        if random.random() < disaster_chance:
            self.disaster_present = random.choice(disasters)

        print(f"Disaster occured: {self.disaster_present}")

    def end_disaster(self):
        if not self.disaster_present:
            prev_disaster = self.disaster_present
            self.disaster_present = None
            print(f"{prev_disaster} has ended.")
        else:
            print("there is no disaster present")
