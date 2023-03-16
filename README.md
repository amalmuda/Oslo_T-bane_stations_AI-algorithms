# Oslo_T-bane_stations_AI-algorithms

What if the subway network in Oslo was redesigned? How to use the shortest possible distance from station to station? Can artificial intelligence find shorter routes?

In this program I try to implement three different evolutionary algorithms to find the shortest distance between subway stations in Oslo. The program is written with Python and is in English.

I currently only have 25 subway stations (out of totally 101 in Oslo), but plan to add more in the future. I also have a desire to, in addition to optimizing for distance, also have the opportunity in this program to optimize for time. It would have been interesting to see if the shortest route in distance in Oslo also corresponds to the shortest possible time.

The program uses an API from Google Developers to find the distance between two points in Google Maps. By default, the program has the driving mode of Google Maps, but it can also use other modes with the same API.

The first algorithm The Exhaustive Search is a naive way of trying to find the shortest path. This is because it can take an extremely long time if the input is large. That's why I'm testing it at only 10 subway stations. The reason I am testing this algorithm is to find a facet answer to the shortest distance for the first 10 stations in my list. I can further use this answer to compare with the other two algorithms.

The second algorithm is The Hill Climbing Algorithm and the third is The Genetic Algorithm, which is more advanced.

For all algorithms, you get output in the terminal with information about the route, the distance on the route, the time it takes to run the software with the hardware you use, etc. The program also provides a map that I have taken from Google Maps (screenshot as .png file) which is used with the program. On the tube you will see the shortest route as well as the names of the subway stations in Oslo. On Genetic Algorithm you will also get a graph showing the evolution of the algorithm through the generations.

In future updates I will implement more evolutionary algorithms such as Baldwinian and Hybrid Algorithms.

There is also a PDF file on the repository now with an output example tested with Juypiter Notebook.
