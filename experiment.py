import interface

def run(board_size, start_row, start_col, genration_max):
    """Experiment run"""

    #TODO implement the experiment
    if board_size < 2:
        raise Exception("error message")

    def make_population():
        population = []
        for i in range(populationSize):
            population.append(individual())
        return population

    conf = interface.Configuration(board_size, start_row, start_col, generation_max)
    individual = interface.Individual(conf)

    #best = findBest(population)
    # [(2,2), (1,4), (3,3), (4,1)]
    best_path_found = best_individual.path()

    return best_path_found


