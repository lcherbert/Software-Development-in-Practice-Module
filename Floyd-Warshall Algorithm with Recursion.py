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

# Implement the Algorithm
    for k in range(V):
        for i in range(V):
            for j in range(V):
                matrix[i][j] = min(matrix[i][j], matrix[i][k] + matrix[k][j])

    return matrix

nonrecursive_output = floydwarshall(network_matrix, V)

# Print the None-Recursive Algorithm
print("The Floyd-Warshall Algorithm Output without recursion:")
for row in nonrecursive_output:
    print(row)

# Recursive Floyd-Warshall Algorithm Function
    
# Calling the previously defined variables into the function
def floydwarshallrecursion(matrix, V, k, i, j):
    if k >= V:
        return matrix
    
# Check the distances between the nodes in the network (represented by i, j, and k)
    if matrix[i][j] > matrix[i][k] + matrix[k][j]:
        matrix[i][j] = matrix[i][k] + matrix[k][j]


# Ensures all nodes have been processed in the algorithm
    if j < V - 1:
        return floydwarshallrecursion(matrix, V, k, i, j + 1)
    elif i < V - 1:
        return floydwarshallrecursion(matrix, V, k, i + 1, 0)
    else:
        return floydwarshallrecursion(matrix, V, k + 1, 0, 0)

def floydwarshall(matrix, V):
    return floydwarshallrecursion(matrix, V, 0, 0, 0)

recursive_output = floydwarshall(network_matrix, V)

# Print the Recursive Implementation of the Algorithm
print("The Floyd-Warshall Algorithm with recursion:")
for row in recursive_output:
    print(row)
