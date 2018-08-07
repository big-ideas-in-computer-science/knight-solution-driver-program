import random

class IndividualGene:
    def __init__(self, configuration):
        self.configuration = configuration
        self._fitness = random.randint(0, 100)

    def mutate(self):
        self._fitness = random.randint(0, 100)

    def crossover(self, other):
        self._fitness = random.randint(0, 100)

    def fitness(self):
        return self._fitness

    def path(self):
        return [(2,2), (1,4), (3,3), (4,1)]

    def __repr__(self):
        return repr((self.fitness()))


class Configuration:
    """board_Size is the side length of the square chess board"""
    def __init__(self, board_size, start_row, start_col, generation_max):
        self.board_size = board_size
        self.start_row = start_row
        self.start_col = start_col
        self.generation_max = generation_max

