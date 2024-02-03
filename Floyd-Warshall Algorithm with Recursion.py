# Floyd-Warshall Algorithm with Recursion

# Number of Vertices in my Network Graph
V = 5

# Defining the 'infinite' value
INF = 9999

# Defining the network matrix as an array
network_matrix = {
    0: {0: 0,1: 4,2:1 ,3: INF,4:INF},
    1: {0: INF, 1: 0, 2: INF, 3: 4, 2: 2},
    2: {0: 1,1: INF,2: 0,3: 2,4: INF},
    3: {0: 4,1: 1,2: INF,3: 0,4: 3},
    4: {0: INF,1: 3,2: INF,3: 1,4: 0}
}

# Non-Recursive Floyd-Warshall Algorithm Function

# Calling the defined universal variable V into the function
def floydwarshall(matrix,V):

    # using V-1 as Python starts at 0 and not at 1
    for k in range(V-1):
        for i in range(V-1):
            for j in range(V-1):
                matrix[i][j] = min(matrix[i][j], matrix[i][k] + matrix[k][j])

    return matrix

output = floydwarshall(network_matrix, V)

for row in output:
    print(row)
