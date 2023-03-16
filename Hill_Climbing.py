from Moduls import station_complete, total_distance
import random

# Function for Hill Climbing Algorithm.
# Takes amount of stations and amount of steps as input. Returns the shortest route.
def HillClimb(station_num, steps):
    rute = station_complete[1][0][:station_num]

    for i in range(0, steps):
        random_a = random.randint(0, len(rute)-1)
        random_b = random.randint(0, len(rute)-1)

        while random_a == random_b:
            random_b = random.randint(0, len(rute)-1)

        rute_tmp = rute[:]
        tmp = rute_tmp[random_a]
        rute_tmp[random_a] = rute_tmp[random_b]
        rute_tmp[random_b] = tmp

        if total_distance(rute_tmp + [rute_tmp[0]]) < total_distance(rute + [rute[0]]):
            rute = rute_tmp[:]

    return rute + [rute[0]]