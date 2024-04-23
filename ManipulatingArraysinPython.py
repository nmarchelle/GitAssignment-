import numpy as np

# Generate a random 2-dimensional numpy array with dimensions 5x5
array = np.random.randint(0, 10, size=(5, 5), dtype=int)

# Print the entire array
print("Generated Array:")
print(array)

# Print the number from the 2nd row, 3rd column
print("\nNumber from the 2nd row, 3rd column:", array[1, 2])

# Print the sum of all the elements in the array
print("\nSum of all elements in the array:", np.sum(array))

# Print the mean of each row in the array
print("\nMean of each row in the array:")
print(np.mean(array, axis=1))

# Print the maximum value in each column of the array
print("\nMaximum value in each column of the array:")
print(np.max(array, axis=0))