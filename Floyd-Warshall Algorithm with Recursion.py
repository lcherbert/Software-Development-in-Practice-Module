"""
Floyd-Warshall Algorithm with Recursion
"""
# Importing the built-in unit testing module
import unittest
import time

# Number of Vertices in my Network Graph
V = 4

# Defining the 'infinite' value
INF = 9999

# Defining the network matrix as an array
matrix = [
    [0, 3, 1, INF],
    [INF, 0, INF, 2],
    [1, INF, 0, 2],
    [3, 1, INF, 0],
]

iterative_counter = 0

recursive_counter = 0

# Non-Recursive Floyd-Warshall Algorithm Function

# Calling the defined universal variable V into the function
def floydwarshalliterative(matrix,V):
    global iterative_counter

    distance = [row[:] for row in matrix]

    # Implement the Algorithm
    for k in range(V):
        for i in range(V):
            for j in range(V):
                iterative_counter = iterative_counter + int(1)
                matrix[i][j] = min(matrix[i][j], matrix[i][k] + matrix[k][j])

    return (matrix,iterative_counter)


# Recursive Floyd-Warshall Algorithm Function
    
# Calling the previously defined variables into the function
def floydwarshallrecursion(matrix, V, k, i, j):
    global recursive_counter

    recursive_counter = recursive_counter + int(1)
    if k >= V:
        return (matrix)
    
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

# Sets the intial parameters to equal 0 and initiate the recursive function
def algorithm(matrix, V):
    return floydwarshallrecursion(matrix, V, 0, 0, 0)

nonrecursive_output = floydwarshalliterative(matrix, V)

# Print the None-Recursive Algorithm
print("The Floyd-Warshall Algorithm Output without recursion:")
for row in nonrecursive_output:
    print(row)
print("Number of Iterations: ", iterative_counter)

# Assign the output to the variable
recursive_output = algorithm(matrix, V)

# Print the Recursive Implementation of the Algorithm
print("The Floyd-Warshall Algorithm with recursion:")
for row in recursive_output:
    print(row)
print("Number of Recursions: ", recursive_counter)

class TestFloydWarshall(unittest.TestCase):
    def test_floyd_warshall_iterative(self):
        expected_output = [
            [0, 3, 1, 3],
            [5, 0, 6, 2],
            [1, 3, 0, 2],
            [3, 1, 4, 0],
        ]
        
        start_time = time.time()
        actual_output, _ = floydwarshalliterative(matrix, V)
        end_time = time.time()

        self.assertEqual(actual_output, expected_output)

        execution_time = end_time - start_time
        print("Function Execution Time for the Recursive Function: ", execution_time, "seconds.")

    def test_floyd_warshall_recursive(self):
        expected_output = [
            [0, 3, 1, 3],
            [5, 0, 6, 2],
            [1, 3, 0, 2],
            [3, 1, 4, 0],    
        ]
        
        start_time = time.time()
        actual_output = algorithm(matrix, V)
        end_time = time.time()

        self.assertEqual(actual_output, expected_output)

        execution_time = end_time - start_time
        print("Function Execution Time for the Recursive Function: ", execution_time, "seconds.")

if __name__ == '__main__':
    unittest.main()