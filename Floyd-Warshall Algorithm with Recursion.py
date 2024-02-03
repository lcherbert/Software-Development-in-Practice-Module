# Floyd-Warshall Algorithm with Recursion

# Number of Vertices in my Network Graph
V = 5

# Define the 'infinite' value
INF = 9999

# Defining my matrix as an array

network_matrix = {
    0: {0: 0,1: 4,2:1 ,3: INF,4:INF},
    1: {0: INF, 1: 0, 2: INF, 3: 4, 2: 2},
    2: {0: 1,1: INF,2: 0,3: 2,4: INF},
    3: {0: 4,1: 1,2: INF,3: 0,4: 3},
    4: {0: INF,1: 3,2: INF,3: 1,4: 0}
}
