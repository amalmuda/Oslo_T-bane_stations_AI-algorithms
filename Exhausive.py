from Moduls import station_complete, total_distance
import itertools

# Function for Exhausive Search Algorithm that takes n-first stations as an input. Returns the shortest (best) route.
def exhausive(number_station):
    station_num = station_complete[1][0][:number_station]
    permu = list(itertools.permutations(station_num))
    best = permu[0]+(permu[0][0], )

    for i in permu:
        if total_distance(i + (i[0], )) < total_distance(best):
            best = i + (i[0], )
            
    return best