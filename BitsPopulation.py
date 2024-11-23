import random
import helpers

class BitsPopulation:
    # define variables
    population = []
    pool = []
    mated = []

    def __init__(self, population_size, gene_length):
        # Initialize population and other parameters
        self.population_size = population_size
        self.gene_length = gene_length

    def generate_population(self):
        for i in range(0, self.population_size):
            ind = []
            for j in range(0, self.gene_length):
                ind.append(random.randint(0, 1))
            self.population.append(ind)

    def evaluate_fitness(self, individual):
        # Define the fitness function
        return round(helpers.pop_function(helpers.get_decimal(individual))/helpers.pop_fitness(self.population),2)


    def mutate(self, individual):
        # Implement mutation logic
        print("used")

    def crossover(self, parent1, parent2):
        # Implement crossover logic
        pos = random.randint(1, self.gene_length-1)
        temp = parent1[:pos]
        parent1[:pos] = parent2[:pos]
        parent2[:pos] = temp

    def do_crossover(self):
        index = list(range(self.population_size))
        while len(index) > 0:
            # get first parent
            pos = random.randint(0, len(index) - 1)
            parent1 = self.pool[index[pos]]
            index.remove(index[pos])
            # get second parent
            pos = random.randint(0, len(index) - 1)
            parent2 = self.pool[index[pos]]
            index.remove(index[pos])
            # do the crossover
            self.crossover(parent1, parent2)
            # add to the mating pool
            self.mated.append(parent1)
            self.mated.append(parent2)

    def evolve(self, generations):
        # Main loop to evolve the population
        print("used")

    def print_population(self):
        for ind in self.population:
            print(ind, " ---> ", helpers.get_decimal(ind), " ---> ", self.evaluate_fitness(ind))

    def print_pool(self):
        for ind in self.pool:
            print(ind, " ---> ", helpers.get_decimal(ind), " ---> ", self.evaluate_fitness(ind))

    def select_wheel(self):
        # generate the selection wheel
        wheel = []
        for i in range(0, self.population_size):
            portion = int(self.evaluate_fitness(self.population[i])*100)
            for j in range(0, portion):
                wheel.append(i)
        # select from the wheel
        for i in range(0, self.population_size):
            self.pool.append(self.population[wheel[random.randint(0, 99)]])