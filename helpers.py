def get_decimal(binary):
    decimal = 0
    for i in range(len(binary)):
        decimal += binary[i] * pow(2, i)
    return decimal

def pop_function(val):
    return pow(val, 2)

def pop_fitness(pop):
    fitness = 0
    for i in range(len(pop)):
        fitness += pop_function(get_decimal(pop[i]))
    return fitness