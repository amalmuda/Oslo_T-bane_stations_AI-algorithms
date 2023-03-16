from Moduls import station_complete, total_distance
from Genetic import genetic
from Maps import map_plotter
import matplotlib.pyplot as plt
import random
import math
import time

# Function that tests the genetic algorithm.
# Takes population, amount of generations, size of Tournament-selected individuals, mutation rate and amount of runs as inputs.
# Amount of runs is 20 by default.
def test_genetic(pop, gen, k, mutate_rate, runs=20):
    best_across_gen = []
    best_each_gen = []
    times = []

    for i in range(0, runs):
        start_time = time.time()
        popu = genetic(pop, gen, k, mutate_rate)
        time_end = time.time() - start_time
        times.append(time_end)

        best = popu[0][0]
        for i in popu[0]:
            if total_distance(i) < total_distance(best):
                best = i

        best_across_gen.append(best + [best[0]])
        best_each_gen.append(popu[1])

    best = best_across_gen[0]
    worst = best_across_gen[0]
    mean = 0
    average_time = 0

    for i in best_across_gen:
        mean += total_distance(i)
        if total_distance(best) > total_distance(i):
            best = i
        if total_distance(worst) < total_distance(i):
            worst = i

    for i in times:
        average_time += i

    best_distance = total_distance(best)
    worst_distance = total_distance(worst)
    mean = mean/len(best_across_gen)
    average_time = average_time/runs
    sum_sd = 0

    for i in best_across_gen:
        sum_sd += (total_distance(i) - mean)**2
    standard_deviation = math.sqrt(sum_sd*(1/len(best_across_gen)))

    route_string = "The route:"
    for i in best:
        route_string = route_string + " - " + str(i)

    print("")
    print("***Testing with population size " + str(len(pop)) +
          " and " + str(len(pop[0])) + " stations with the Genetic Algorithm***")
    print("")
    print(route_string)
    print("")
    print("Across " + str(runs) + " runs")
    print("Best: " + str(int(best_distance)/1000) + " km")
    print("Worst: " + str(int(worst_distance)/1000) + " km")
    print("Mean: " + str(int(mean)/1000) + " km")
    print("Standard deviation: " + str(int(standard_deviation)/1000) + " km")
    print("Average running time: " +
          '{0:.3f}'.format(average_time) + " seconds")
    map_plotter(best)

    x = []
    y = []
    for i in range(0, gen):
        var = 0

        for k in range(0, runs):
            var += total_distance(best_each_gen[k][i] + [best_each_gen[k][i][0]])

        var = var/runs
        y.append(var)
        x.append(i+1)

    plt.plot(x, y)
    plt.title("Average shortest distance across " +
              str(len(pop[0])) + " stations in GA")
    plt.xlabel("Number of generations")
    plt.ylabel("Distance (km)")
    plt.show()

# Function that generates random populations.
# Takes the n-first cities and size of population as inputs.
# Returns a random population.
def populationMaker(station_number, population_number):
    station_amount = station_complete[1][0][:station_number]

    population = []
    for i in range(0, population_number):
        route = random.sample(station_amount, len(station_amount))
        population.append(route)

    return population

#Randomly generated population with 10 stations and population size of 500.
pop10 = populationMaker(10, 500)
pop25 = populationMaker(25, 500)