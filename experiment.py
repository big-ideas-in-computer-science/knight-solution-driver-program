

def run(board_size, start_row, start_col, genration_max):
    """Experiment run"""

    #TODO implement the experiment
    if board_size < 2:
        raise Exception("error message")

    #best = findBest(population)
    best_path_found = [(2,2), (1,4), (3,3), (4,1)]

    return best_path_found


class IndividualGene:
    def __init__(self, configuration):
        self.configuration = configuration

    def mutate(self):
        pass

    def crossover(self, other):
        pass


class Configuration:
    def __init__(self, board_size, start_row, start_col, generation_max):
        self.board_size = board_size
        self.start_row = start_row
        self.start_col = start_col
        self.generation_max = generation_max

