from Moduls import total_distance
import random

# Function for selection in the Genetic Algorithm.
# Implements Tournament-selection and takes a population as an input and returns k-individuals.
def selection(pop, k):
    selected = []

    for i in range(0, k):
        tournament = []
        for j in range(0, 5):
            tournament.append(pop[random.randrange(len(pop))])

        best = tournament[0]
        for i in tournament:
            if total_distance(i+[i[0]]) < total_distance(best+[best[0]]):
                best = i

        selected.append(best)

    return selected

# Function for crossover in the Genetic Algorithm.
# Implements Partially Mapped Crossover (PMX) and takes 2 parents (routes) as input. Returns a route-offspring.
def crossover(a, b):
    slice = random.randrange(len(a))
    start = random.randrange(len(a))
    end = start + slice

    while end > len(a):
        slice = random.randrange(len(a))
        end = start + slice

    offspring = []
    for i in range(len(a)-len(a[start:end])+1):
        if i == start:
            offspring.extend(a[start:end])
        else:
            offspring.append(0)

    for i in range(0, len(b[start:end])):
        if b[start:end][i] not in a[start:end]:
            p = b.index(a[start:end][i])

            while p >= start and p <= end-1:
                p = b.index(offspring[p])
            offspring[p] = b[start:end][i]

    for i in range(0, len(b)):
        if b[i] not in offspring:
            offspring[i] = b[i]

    return offspring

# Function for mutation in the Genetic Algorithm.
# Implements swap-mutation and takes a route as input. Returns the mutated route.
def mutate(route):
    random_a = random.randint(0, len(route)-1)
    random_b = random.randint(0, len(route)-1)

    while random_a == random_b:
        random_b = random.randint(0, len(route)-1)

    route[random_a], route[random_b] = route[random_b], route[random_a]
    return route

# Function for the Genetic Algorithm.
# Takes population, amount of generations, size of Tournament-selected individuals and mutation rate as inputs.
# Returns the nth-generation of the population and a list of the best individual amoung each generation.
def genetic(pop, gen, k, mutate_rate):
    run_n = []
    for i in range(0, gen):
        new_gen = []
        selected_n = selection(pop, k)

        for k in range(0, len(pop)-len(selected_n)):
            random_a = random.randint(0, len(selected_n)-1)
            random_b = random.randint(0, len(selected_n)-1)

            while random_a == random_b:
                random_b = random.randint(0, len(selected_n)-1)

            route = crossover(selected_n[random_a], selected_n[random_b])

            mutate_number = (random.randint(0, 101))/100
            if mutate_number < mutate_rate:
                route = mutate(route)

            new_gen.append(route)

        pop = selected_n + new_gen
        best_of_gen = pop[0]

        for i in pop:
            if total_distance(i+[i[0]]) > total_distance(best_of_gen + [best_of_gen[0]]):
                best_of_gen = i

        run_n.append(best_of_gen)
        
    return pop, run_n