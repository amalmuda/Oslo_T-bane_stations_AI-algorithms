from Moduls import total_distance
from Hill_Climbing import HillClimb
from Maps import map_plotter
import time
import math

# Function for testing the Hill Climbing Algorithm.
# Takes amout of stations, runs and steps as inputs.
def test_hillclimb(station_size, runs, steps):
    route = []
    times = []
    for i in range(0, runs):
        start_time = time.time()
        route.append(list(HillClimb(station_size, steps)))
        time_end = time.time() - start_time
        times.append(time_end)

    best = route[0]
    worst = route[0]
    mean = 0
    average_time = 0

    for i in route:
        mean += total_distance(i)
        if total_distance(best) > total_distance(i):
            best = i
        if total_distance(worst) < total_distance(i):
            worst = i

    for i in times:
        average_time += i

    best_distance = total_distance(best)
    worst_distance = total_distance(worst)
    mean = mean/len(route)
    average_time = average_time/runs
    sum_sd = 0
    for i in route:
        sum_sd += (total_distance(i) - mean)**2
    standard_deviation = math.sqrt(sum_sd*(1/len(route)))

    route_string = "The route:"
    for i in best:
        route_string = route_string + " - " + str(i)

    print("")
    print("***First " + str(station_size) + " Metro stations with the Hill Climbing Algorithm***")
    print("")
    print(route_string)
    print("")
    print("Best: " + str(int(best_distance)/1000) + " km")
    print("Worst: " + str(int(worst_distance)/1000) + " km")
    print("Mean: " + str(int(mean)/1000) + " km")
    print("Standard deviation: " + str(int(standard_deviation)/1000) + " km")
    print("Average running time: " + '{0:.3f}'.format(average_time) + " seconds")
    print("")
    map_plotter(best)
    print("")