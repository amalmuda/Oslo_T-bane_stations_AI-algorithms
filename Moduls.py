import googlemaps
from config import api_key
from datetime import datetime
from Stations import stations
from distanceMap import distances

#API from Google Maps. The api_key needs to be saved in a seperate file named config.py and seperate variable named api_key.
gmaps = googlemaps.Client(key = api_key)

# Function that uses a API from Google Developers to find the distance between posisjons from Google Maps. Mode set defualt to driving.
def distance(pos_a, pos_b, mod = "driving"):
    now = datetime.now()
    result = gmaps.distance_matrix(pos_a, pos_b, mode=mod, units="metric", departure_time=now)

    distance = result['rows'][0]['elements'][0]['distance']['value']
    duration = result['rows'][0]['elements'][0]['duration']['text']

    return(distance)

# A combined 2D-list with list of the stations and lists of distances
array = [stations] + distances

# Function that takes a list as an input and returns a dictionary with all routes and stations, and also returns the original data list.
def readList(list):
    data = list
    station_dict = {}

    for i in range(0, len(data)-1):
        station_dict[data[0][i]] = {}
        for k in range(0, len(data)-1):
            station_dict.get(data[0][i])[data[0][k]] = data[i+1][k]

    return station_dict, data

# Station database created for all algorithms in the same folder.
station_complete = readList(array)

# Function that finds the distance between 2 stations. Takes 2 stations as input.
def route(station_a, station_b):
    return float(station_complete[0][station_a][station_b])

# Function that takes a route as an input and returns the distance. Can also be used as a fitness-function.
def total_distance(rt):
    distance = 0

    for i in range(0, len(rt)-1):
        distance += route(rt[i], rt[i+1])

    return distance