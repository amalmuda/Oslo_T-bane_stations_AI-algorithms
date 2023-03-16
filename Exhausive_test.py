from Moduls import total_distance
from Exhausive import exhausive
from Maps import map_plotter
import time

# Function for testing the Exhausive Search Algorithm with the range of the first a to b amount of stations.
def test_exhausive(a, b):
    for i in range(a, b+1):
        print("")
        print("***Best route for the first " + str(i) + " Metro stations with the Exhausive Algorithm***")

        start_time = time.time()
        best_route = exhausive(i)
        time_end = time.time() - start_time

        route_string = "The route:"
        for i in best_route:
            route_string = route_string + " - " + str(i)

        print("")
        print(route_string)
        print("Distance: " + str(float(total_distance(best_route)/1000)) + " km")
        print("Running time: " + '{0:.4f}'.format(time_end) + " seconds")
        print("")

        map_plotter(best_route)
        print("")