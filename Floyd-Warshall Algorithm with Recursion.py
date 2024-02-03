# Floyd-Warshall Algorithm with Recursion

# Number of Vertices in my Network Graph
V = 4

# Defining the 'infinite' value
INF = 9999

# Defining the network matrix as an array
network_matrix = [
    [0, 3, 1, INF],
    [INF, 0, INF, 2],
    [1, INF, 0, 2],
    [3, 1, INF, 0],
]

# Non-Recursive Floyd-Warshall Algorithm Function

# Calling the defined universal variable V into the function
def floydwarshall(matrix,V):

    distance = [row[:] for row in matrix]

    for k in range(V):
        for i in range(V):
            for j in range(V):
                matrix[i][j] = min(matrix[i][j], matrix[i][k] + matrix[k][j])

    return matrix

output = floydwarshall(network_matrix, V)

for row in output:
    print(row)
