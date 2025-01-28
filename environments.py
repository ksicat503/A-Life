import random
import pygame

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

    def get_weather(self):
        return self.weather
   
    def get_temperature(self):
        return self.temperature

    def get_total_resources_left(self):
        return self.total_resources
 
    def get_terrain(self):
        return self.terrain

    def set_weather(self, condition):
        """_summary_

        Args:
            temp (int): hard set weather
        """
        # Can add more
        weather_types = ["clear", "rain", "storm", "drought", "snow"]
        if condition not in weather_types:
            print(f"Valid weather types {weather_types}")
        else:
            self.weather = condition
            print(f"New Weather condition: {self.weather}")

    def randomize_weather(self):
        weather_types = ["clear", "rain", "storm", "drought", "snow"]
        self.weather = random.choice(weather_types)

    def set_temperature(self, temp):
        self.temperature = temp

    def use_resources(self, amt):
        self.total_resources -= amt
        self.total_resources = max(0, self.total_resources - amt)