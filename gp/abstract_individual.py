class AbstractIndividual():
    """
    Generic individual class for evolutionary algorithms. Provides container
    for fitness and genome. Derived classes need to define how individuals
    should be cloned, crossovered and mutated.

    """

    def __init__(self, fitness, genome):
        self.fitness = fitness
        self.genome = genome
        self.idx = None  # an identifier to keep track of all unique genomes

    def __repr__(self):
        return 'Individual(idx={}, fitness={}, genome={}))'.format(self.idx, self.fitness, self.genome)

    def clone(self):
        raise NotImplementedError()

    def crossover(self, other_parent, rng):
        raise NotImplementedError()

    def mutate(self, n_mutations, rng):
        raise NotImplementedError
