import matplotlib.pyplot as plt
from Stations import station_coords

# Map of Oslo
map = plt.imread('oslo_map.png')

# Function for visualizing the stations and the route.
def map_plotter(station_order):
    fig, ax = plt.subplots(figsize=(20, 12))
    ax.imshow(map, aspect="auto")

    for index in range(len(station_order) - 1):
        current_station_coords = station_coords[station_order[index]]
        next_station_coords = station_coords[station_order[index+1]]
        x, y = current_station_coords[0], current_station_coords[1]

        next_x, next_y = next_station_coords[0], next_station_coords[1]
        plt.plot([x, next_x], [y, next_y])

        plt.plot(x, y, 'ok', markersize=1)
        plt.text(x, y, index, fontsize=5)
    
    for station, location in station_coords.items():
        x, y = (location[0], location[1])
        plt.plot(x, y, 'ok', markersize=1)
        plt.text(x, y, station, fontsize=5)

    first_station_coords = station_coords[station_order[0]]
    first_x, first_y = first_station_coords[0], first_station_coords[1]
    plt.plot([next_x, first_x], [next_y, first_y])

    plt.plot(next_x, next_y, 'ok', markersize=1)
    plt.text(next_x, next_y, index+1, fontsize=10)
    plt.show()