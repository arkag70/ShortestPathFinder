from map import *
from util import print_
import matplotlib.pyplot as plt
from random import random, randint
POP_SIZE = N * 5
K = 10000
CROSSOVER_RATE = 0
MUTATION_RATE = 0.05
MATINGPOOL_CAPACITY = 1000

class Optimizer:

    def __init__(self, screen) -> None:
        print_(__name__)
        self.population = []
        self.crossoverRate = CROSSOVER_RATE
        self.mutationRate = MUTATION_RATE
        self.screen = screen
        self.matingPool = []

    def createPopulation(self):
        self.population = []
        if len(self.matingPool) == 0:
            print_("mating pool empty")
            for _ in range(POP_SIZE):
                chart = Map()
                chart.randomize()
                self.calculateFitness(chart)
                self.population.append(chart)
        else:
            print_("mating pool full")
            for chart in self.matingPool:
                # chart = self.selection()
                self.calculateFitness(chart)
                self.population.append(chart)

    def calculateFitness(self, chart):
        
        distance = Map.getDistance(chart)
        chart.fitness = round(K/(distance),4)
        chart.distance = distance

    def prepareMatingPool(self):
        
        self.matingPool = []
        # sort population based on fitness in descending order
        self.matingPool = sorted(self.population, key=lambda x : x.distance)
        # create new population who could potentially replace them
        # if the newly created population has better fitness
        for i, pop in enumerate(self.matingPool):
            newChart = self.crossover(pop)
            newChart = self.mutation(newChart)
            self.calculateFitness(newChart)
            if newChart.fitness > pop.fitness:
                self.matingPool[i] = newChart
        for pop in self.matingPool:
            print_(f"Fitness : {pop.fitness}")


    def selection(self):
        chart = choice(self.matingPool)
        return chart

    def crossover(self, chart):
        newChart = chart
        if round(random(),3) < self.crossoverRate:
            blocks = newChart.blocks
            source = blocks[0]
            mid = len(blocks)//2
            partA = blocks[1:mid]
            partB = blocks[mid:]
            blocks = partB + partA
            blocks.insert(0, source)
            newChart.blocks = blocks

        return newChart
    
    def mutation(self, chart):
        if round(random(),5) < self.mutationRate:
            chart = Map()
            chart.randomize()
        return chart

    def draw(self):
        bestRoute = self.matingPool[0]
        print_(f"Best distance : {bestRoute.distance}")
        bestRoute.draw(self.screen)
        return bestRoute.distance
            