import random
import copy
import interface

survivalRatio = 0.5
reproductionTypeRatio = 0.5
elite = False
nrOfGenerations = 10000
printValues = True

def generation(population):

    # Sort the solutions by merit (they've already calculated their own fitness upon being created)
    population.sort(key=lambda x: x.fitness(), reverse=True)

    # Determine the number of solutions allowed to survive from the given survival ratio
    # and how much room that leaves for children.
    survivors = int(len(population) * survivalRatio)
    nr_of_children = len(population) - survivors

    nr_of_cloned_children = int(nr_of_children * reproductionTypeRatio)

    # If the elite variable is set to false, we want to keep some solutions that don't look promising
    # yet alive anyway, to keep the genetic varation in the population high. We do this by replacing some of the
    # solutions that endid up in the surviving part of the array (beginning of the array), with some of the solutions
    # that ended up in the 'dying' part of the array (the rest of the array, border is determined by survivalRatio).
    # The number of elite survivors is the total nr twice multiplied by the survival ratio. If that drops below 1, at least
    # the very best solution is kept alive.
    if elite is False:
        elites = max(1, int(len(population) * (survivalRatio * survivalRatio)))
        rest = population[elites + 1:]
        random.shuffle(rest)
        population[elites + 1:] = rest

    for i in range(nr_of_cloned_children):
        individual = population[random.choice(range(survivors))]
        population[survivors + i] = reproduce(individual)

    for i in range(nr_of_children - nr_of_cloned_children):
        individual = reproduce(
            population[random.choice(range(survivors))],
            population[random.choice(range(survivors))]
        )
        population[survivors + i + nr_of_cloned_children] = individual
    return population

def make_population(conf, population_size):
    """makes a population"""
    population = []
    for i in range(population_size):
        population.append(interface.IndividualGene(conf))
    return population

def findbest(population):
    """finds best individual from a population"""
    best = population[0]
    for i in population:
        if i.fitness() > best.fitness():
            best = i
    return best


def reproduce(individual, partner=None):
    if partner is None:
        child = copy.deepcopy(individual)
        child.mutate()
    else:
        child = copy.deepcopy(individual)
        child.crossover(partner)
    return child


def run(board_size, start_row, start_col, evaluation_max):
    """Experiment run"""

    # TODO implement the experiment
    # checking if board size is large enough to work
    if board_size < 2:
        raise Exception("error message")

    # importing the configuration
    conf = interface.Configuration(board_size, start_row, start_col, evaluation_max)
    individual = interface.IndividualGene(conf)
    population_size = conf.board_size ** 2
    population = make_population(conf, population_size)

    for i in range(nrOfGenerations-1):
        population = generation(population)
        if printValues is True:
            best = findbest(population)
            print("Best solution in population " + str(i + 2) + ": length: "+ str(best.fitness()) + ", solution: " + str(best.path()))

    # best = findBest(population)
    # [(2,2), (1,4), (3,3), (4,1)]
    best_path_found = findbest(population).path()

    return best_path_found


