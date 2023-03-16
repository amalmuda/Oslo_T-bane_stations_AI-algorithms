from Stations import stations
from Moduls import distance

# Function that creates a 2D-list with distances relative to each other for each station.
def make_2d(stations):
    distances = []
    for station in stations:
        dist_list = []

        for other_station in stations:
            if other_station == station:
                dist = 0
                dist_list.append(dist)
            else:
                dist = distance(station, other_station)
                dist_list.append(dist)
        distances.append(dist_list)

    return distances

# Creating 2D-list with the list of stations and paste the code in file distanceMap.py in the same folder
def createStations():
    print = make_2d(stations)
    f = open("distanceMap.py", "w")
    f.write("distances = " + str(print))
    f.close()

createStations()