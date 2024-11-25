from BitsPopulation import BitsPopulation

# init pop
population = BitsPopulation(8,6)

# generate pop
population.generate_population()

# print generated pop
#print("generated population")
#population.print_population()

# doing selection
#population.select_wheel()

# print selected pool
#print("selected pool")
#population.print_pool()

# do the crossover
#population.do_crossover()

# print the mated pop
#print("mated population")
#population.print_mated()
# evaluate pop fitness
#population.evaluate_fitness(population.population[1])

#population.uniform_crossover([0,0,0,0,0,0],[1,1,1,1,1,1])
population.mutate([])