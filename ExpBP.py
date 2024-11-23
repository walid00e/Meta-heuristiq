from BitsPopulation import BitsPopulation

# init pop
population = BitsPopulation(8,5)

# generate pop
population.generate_population()



# print wheel
population.select_wheel()

# print pop
population.print_pool()

population.do_crossover()

# evaluate pop fitness
#population.evaluate_fitness(population.population[1])