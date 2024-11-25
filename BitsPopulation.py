import random
import helpers


class BitsPopulation:
    # define variables
    # initial population of individuals
    population = []
    # selected population for mating pool
    pool = []
    # offspring population after mating
    mated = []
    # offspring after mutation
    final = []
    max = []

    # init variables
    def __init__(self, population_size, gene_length):
        # Initialize population and other parameters
        self.population_size = population_size
        self.gene_length = gene_length

    # generate the population at random
    def generate_population(self):
        for i in range(0, self.population_size):
            ind = []
            for j in range(0, self.gene_length):
                ind.append(random.randint(0, 1))
            self.population.append(ind)

    # evaluate the fitness of an individual
    def evaluate_fitness(self, individual):
        # Define the fitness function
        return round(helpers.pop_function(helpers.get_decimal(individual)) / helpers.pop_fitness(self.population), 2)

    # selection with roulette wheel
    def select_wheel(self):
        # generate the selection wheel
        wheel = []
        for i in range(0, self.population_size):
            portion = int(self.evaluate_fitness(self.population[i]) * 100)
            for j in range(0, portion):
                wheel.append(i)
        # select from the wheel
        for i in range(0, self.population_size):
            self.pool.append(self.population[wheel[random.randint(0, 99)]])

    # one point crossover between two parents
    def one_point_crossover(self, parent1, parent2):
        # randomly generate the position of the crossover
        pos = random.randint(1, self.gene_length - 1)
        # Implement crossover logic
        temp = parent1[:pos]
        parent1[:pos] = parent2[:pos]
        parent2[:pos] = temp

    # n point crossover between two parents
    def n_point_crossover(self, parent1, parent2):
        # randomly generate the number of points n
        n = random.randint(1, self.gene_length - 1)
        # randomly select the positions of each point n
        pos = []
        while len(pos) < n:
            rand = random.randint(1, self.gene_length)
            if rand in pos:
                continue
            else:
                pos.append(rand)
        pos.sort()
        # implement the crossover logic
        n_one = 0
        for i in range(0, n):
            n_two = pos[i]
            if i % 2:
                temp = parent1[n_one:n_two]
                parent1[n_one:n_two] = parent2[n_one:n_two]
                parent2[n_one:n_two] = temp
            n_one = n_two

    # uniform crossover between two parents
    def uniform_crossover(self, parent1, parent2):
        # treat every bit at a flip coin chance of swapping
        for i in range(0, self.gene_length):
            if random.randint(0,1):
                temp = parent1[i]
                parent1[i] = parent2[i]
                parent2[i] = temp

    # crossover for the entire population and generate an offspring pool
    def crossover(self, type_crossover):
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
            if type_crossover == "ONE_POINT_CROSSOVER":
                self.one_point_crossover(parent1, parent2)
            elif type_crossover == "N_POINT_CROSSOVER":
                self.n_point_crossover(parent1, parent2)
            elif type_crossover == "UNIFORM_CROSSOVER":
                self.uniform_crossover(parent1, parent2)
            else:
                print("no crossover type included")
                return
            # add to the mating pool
            self.mated.append(parent1)
            self.mated.append(parent2)

    def mutate(self, individual):
        # Implement mutation logic
        for i in range(0, self.gene_length):
            res = random.randint(0,1000)
            if res == 1:
                individual[i] = 0 if individual[i] == 1 else 0

    def evolve(self, generations):
        # Main loop to evolve the population
        print("used")

    def print_population(self):
        for ind in self.population:
            print(ind, " ---> ", helpers.get_decimal(ind), " ---> ", self.evaluate_fitness(ind))

    def print_pool(self):
        for ind in self.pool:
            print(ind, " ---> ", helpers.get_decimal(ind), " ---> ", self.evaluate_fitness(ind))

    def print_mated(self):
        for ind in self.mated:
            print(ind, " ---> ", helpers.get_decimal(ind), " ---> ", self.evaluate_fitness(ind))
