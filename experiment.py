import random
import copy
import interface
# The survival ratio determines the proportion of the population that survives.
# So it signifies our willingness to explore the potential of currently bad solutions. If this proportion is high
# we have a higher genetic diversity, but also less exploration per generation, so a slower development.
survivalRatio = 0.5

# Two types of reproduction are implemented: mutation and cross-over,
# if reproductionTypeRatio is 1, only matuation is used,
# if it is 0, only cross-over is used. Otherwise a proportion of both.
reproductionTypeRatio = 0.5

# If elite is true then only the best solutions survive, instead of also some random ones.
elite = False

# It prints the best solution of every generation
printValues = True

def generation(population):
    """generates a population's offspring"""
    # Sort the solutions by merit (they've already calculated their own fitness upon being created)
    population.sort(key=lambda x: x.fitness(), reverse=True)

    # Determine the number of solutions allowed to survive from the given survival ratio
    # and how much room that leaves for children.
    survivors = int(len(population) * survivalRatio)

    # number of children that need to be born to restore the same population size
    nr_of_children = len(population) - survivors

    # number of asexually born children through mutation
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
    """makes a population by starting with an empty list and then repeatedly appends individual genes into this list"""
    population = []
    for i in range(population_size):
        population.append(interface.IndividualGene(conf))
    return population

def findbest(population):
    """finds best individual from a population, the higher the fitness the better"""
    best = population[0]
    for i in population:
        if i.fitness() > best.fitness():
            best = i
    return best


def reproduce(individual, partner=None):
    """checks if the individual is supposed to reproduce asexually by mutation or sexually by crossover"""
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

    """makes the population size the square of the board size, so on an 8x8 chess board the population is 64"""
    population_size = conf.board_size ** 2

    """makes a population"""
    population = make_population(conf, population_size)

    """calculates the total number of generations based off the original parents, plus the amount of children per 
    generation, times the amount of generations """
    nrOfGenerations = int((evaluation_max - (population_size*survivalRatio))/
                          (population_size*(1-survivalRatio)))

    """"loops through and generates the population 
    repeats it nrOfGenerations - 1 times because you already start with one generation"""
    for i in range(nrOfGenerations-1):
        population = generation(population)

        if printValues is True:
            best = findbest(population)

            print("Best solution in population " + str(i + 2) + ": length: "+ str(best.fitness()) + ", solution: " + str(best.path()))

    """finds the longest route in the population, returns the path"""
    best_path_found = findbest(population).path()

    return best_path_found


