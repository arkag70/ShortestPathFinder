import pygame
from random import choice, shuffle
from math import sqrt

width, height = 800, 600
BLOCK_SIZE = 10
MARGIN = BLOCK_SIZE/2
N = 20
xcoordinates = list(range(2 * BLOCK_SIZE, width, 2*BLOCK_SIZE))
ycoordinates = list(range(2 * BLOCK_SIZE, height, 2*BLOCK_SIZE))
cities = [(choice(xcoordinates), choice(ycoordinates)) for _ in range(N)]

class Map:

    def __init__(self) -> None:
        self.blocks = [pygame.Rect(city[0], city[1], BLOCK_SIZE, BLOCK_SIZE) for city in cities]
        self.distance = 0
        self.fitness = 0

    def randomize(self):
        # keep start city aside before randomizing
        source = self.blocks[:1]
        destinations = self.blocks[1:]
        shuffle(destinations)
        self.blocks = source + destinations

    @staticmethod
    def getDistance(chart):
        distance = 0
        for i,block in enumerate(chart.blocks):
            block1 = block
            block2 = chart.blocks[(i+1) % N]
            x1, y1 = block1.x, block1.y
            x2, y2 = block2.x, block2.y
            distance += int(sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2))
        return distance

    def draw(self, screen):

        for i, block in enumerate(self.blocks):
            color = "red"
            if i == 0:
                color = "yellow" # first block yellow
            pygame.draw.rect(screen, color, block)
            pygame.draw.line(screen, "white", (block.x + MARGIN, block.y + MARGIN), (self.blocks[(i+1) % N].x + MARGIN, self.blocks[(i+1) % N].y + MARGIN))

