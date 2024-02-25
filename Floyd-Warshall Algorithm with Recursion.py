"""
Floyd-Warshall Algorithm with Recursion
"""
# Importing the built-in unit testing module
import unittest
import time
import resource

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

# Defining variables to track the number of recursions and iterations
ITERATIVE_COUNTER = 0
RECURSIVE_COUNTER = 0

def get_memory_usage():
    memory_usage = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    # Change the memory usage to MB from KB for clarity
    memory_usage_mb = memory_usage / 1024.0
    return memory_usage_mb

# Non-Recursive Floyd-Warshall Algorithm Function

# Calling the defined universal variable V into the function
def floydwarshalliterative(matrix,V):
    global ITERATIVE_COUNTER

    # Changing the iterative function to use a copy of the matrix
    matrix_copy = [row[:] for row in matrix]

    distance = [row[:] for row in matrix_copy]

    start_time = time.time()

    # Implement the Algorithm
    for k in range(V):
        for i in range(V):
            for j in range(V):
                ITERATIVE_COUNTER = ITERATIVE_COUNTER + int(1)
                if ITERATIVE_COUNTER % 16 == 0:
                    print("Memory Usage per iteration:", ITERATIVE_COUNTER, get_memory_usage(), "MB")
                matrix_copy[i][j] = min(matrix_copy[i][j], matrix_copy[i][k] + matrix_copy[k][j])

    end_time = time.time()
    execution_time = end_time - start_time
    print("Execution Time for the Iterative Function: ", execution_time, "seconds.")
    print("The Floyd-Warshall Algorithm Output without recursion:")
    for row in matrix_copy:
        print(row)

    print("Number of Iterations: ", ITERATIVE_COUNTER)

    return matrix_copy

# Recursive Floyd-Warshall Algorithm Function
    
def floydwarshallrecursion(matrix, V, k, i, j):
    global RECURSIVE_COUNTER

    RECURSIVE_COUNTER = RECURSIVE_COUNTER + int(1)

    if RECURSIVE_COUNTER % 16 == 0:
        print("Memory Usage per recursion:", RECURSIVE_COUNTER, get_memory_usage(), "MB")

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
    start_time = time.time()
    result = floydwarshallrecursion(matrix, V, 0, 0, 0)
    end_time = time.time()
    execution_time = end_time - start_time
    print("Execution Time for the Recursive Function: ", execution_time, "seconds.")
    # Print the Recursive Implementation of the Algorithm
    print("The Floyd-Warshall Algorithm with recursion:")
    for row in matrix:
        print(row)
    
    print("Number of Recursions: ", RECURSIVE_COUNTER)

    return result

# Test the iterative and recursive functions

class TestFloydWarshall(unittest.TestCase):
    def test_floyd_warshall_iterative(self):
        expected_output = [
            [0, 3, 1, 3],
            [5, 0, 6, 2],
            [1, 3, 0, 2],
            [3, 1, 4, 0],
        ]

        # Tests the iterative version
        actual_output = floydwarshalliterative(matrix, V)
        self.assertEqual(actual_output, expected_output)

    def test_floyd_warshall_recursive(self):
        expected_output = [
            [0, 3, 1, 3],
            [5, 0, 6, 2],
            [1, 3, 0, 2],
            [3, 1, 4, 0],    
        ]
        
        # Tests the recursive version
        actual_output = algorithm(matrix, V)
        self.assertEqual(actual_output, expected_output)

if __name__ == '__main__':
    unittest.main() 