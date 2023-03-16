from Exhausive_test import test_exhausive
from Hill_Climbing_test import test_hillclimb
from Genetic_test import test_genetic, pop10, pop25

# *** Test of all three algorithms. It might take some time, depending on the input ***
# In addition to text output in the terminal, the algorithms will also output a map of Oslo with the best route visually.
# The Genetic Algorithm will also output a graph showing the evolution of the algorithm.

# Testing the Exhausive Search Algorithm for 6 to 10 stations.
# The reason I limit the algorithm is because it would take an enormous amount of time to have multiple stations with this method.
test_exhausive(6,  10)
print("")
print("")

# Testing the Hill Climbing Algorithm with 10 and 25 stations (maximum amount), 20 runs of the algorithm and 10000 steps.
test_hillclimb(25, 20, 10000)
print("")
test_hillclimb(10, 20, 10000)
print("")
print("")

# Testing the Genetic Algorithm with 300 generations, Tournament-selection of the 250 best inviduals and a mutation rate of 0.25 (population size pop of 500). 
# Testing with both 10 and 25 stations.
test_genetic(pop10, 300, 250, 0.25)
print("")
test_genetic(pop25, 300, 250, 0.25)