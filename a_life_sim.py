import pygame
import random
# import numpy as np
# import json

# initializing imported module
# This initializes pygame and fonts to display text
pygame.init()
pygame.font.init()

# defining the size of the window
window_height = 1000
window_width = 1000

# This is needed to clear the screen during sim,
# as fill function needs the variable
black = (0, 0, 0)

# Initializing the window
window = pygame.display.set_mode((window_height, window_width))
# This code allows us to change the name of the window
pygame.display.set_caption('Artifical Life Sim')

# clock to set frame rate in simulation
clock = pygame.time.Clock()


# Organism class, may be easier to make class for each organsim
# Can discuss or use one class for all and randomly set some values
# If using one class, will need some unique identifier most likely
class Organism:
    def __init__(self, x, y, org_height, org_width, speed, energy):
        self.x = x
        self.y = y
        self.org_height = org_height
        self.org_width = org_width
        self.speed = speed
        self.energy = energy

    # Using rectangle, but can update for a different shape or icon
    def insert_organism(self, window):
        """Function to insert organism with defined size, and grid position"""
        pygame.draw.rect(window, (0, 0, 255), (self.x, self.y, self.org_height,
                                               self.org_width))

    def movement(self):
        """Finding random values for x and y values.
        -speed is max speed in left or down directions
        Reducing energy for each movement made"""
        self.x = self.x + random.randint(-self.speed, self.speed)
        self.y = self.y + random.randint(-self.speed, self.speed)
        self.energy -= 1


# Creating a set organism for testing.
# Can add a function to create mulitple later
organism_test = Organism(
    x=200,
    y=300,
    org_height=50,
    org_width=50,
    speed=10,
    energy=50
)

# setting bool value to run game
sim_running = True

# keep game running till running is false
while sim_running:

    # Set up event for when the user quits out of the screen
    for event in pygame.event.get():
        # if event is of type quit then
        # set running bool to false
        if event.type == pygame.QUIT:
            sim_running = False
    # Move the organism
    organism_test.movement()

    # Clear screen. Important or else is just paints the screen
    # as the organism moves.
    window.fill(black)

    # Inserting organism on screen in new position
    organism_test.insert_organism(window)

    # update the display for the new movement
    pygame.display.update()

    # print to show energy is decreasing with movement
    print(organism_test.energy)

    # Added some code to stop the sim when the organism runs out of energy
    # Take this out to run continuously
    if organism_test.energy == 0:
        sim_running = False

    # Setting frame rate, lower setting seems to be easier to follow
    # Also if higher, the sim runs quickly due to energy consumption
    clock.tick(30)
