import numpy as np

# task 1
friend1 = np.array([5000, 7000, 8000, 6500, 9000, 10000, 7500])
friend2 = np.array([6000, 6500, 7500, 7000, 8500, 9500, 8000])

addition = friend1 + friend2
subtraction = friend1 - friend2
multiplication = friend1 * friend2
division = friend1 / friend2
print("Addition:", addition)
print("Subtraction:", subtraction)
print("Multiplication:", multiplication)
print("Division:", division)


# task 2
preferences = np.array([
    [5, 2, 4],
    [1, 3, 5],
    [4, 4, 2]
])

popularity = np.array([
    [4, 1, 2],
    [2, 5, 1],
    [3, 2, 4]
])

result_dot = np.dot(preferences, popularity)
result_matmul = np.matmul(preferences, popularity)

print("Using dot():")
print(result_dot)
print("\nUsing matmul():")
print(result_matmul)


# task 3
image = np.array([
    [10,  20,  30,  40],
    [50,  60,  70,  80],
    [90, 100, 110, 120],
    [130, 140, 150, 160]
])

transposed_image = image.T
mean_value = np.mean(image)
median_value = np.median(image)
std_value = np.std(image)
variance_value = np.var(image)

print("Original image:")
print(image)
print("\nTransposed image:")
print(transposed_image)
print("\nMean:", mean_value)
print("Median:", median_value)
print("Standard deviation:", std_value)
print("Variance:", variance_value)



# task 4
ratings = np.array([
    [4, 2, 1],
    [2, 5, 2],
    [1, 2, 4]
], dtype=float)

determinant = np.linalg.det(ratings)
inverse = np.linalg.inv(ratings)
eigenvalues, eigenvectors = np.linalg.eig(ratings)

print("Original matrix:")
print(ratings)
print("\nDeterminant:")
print(determinant)
print("\nInverse:")
print(inverse)
print("\nEigenvalues:")
print(eigenvalues)
print("\nEigenvectors:")
print(eigenvectors)



# task 5
orders = np.array([
    [120, 150, 130, 180, 200, 170],
    [100, 110, 140, 160, 190, 210]
])

print("Original array:")
print(orders)

reshaped = orders.reshape(3, 4)

print("\nReshaped array:")
print(reshaped)

flattened = reshaped.flatten()

print("\nFlattened array:")
print(flattened)

part1, part2 = np.split(flattened, 2)

print("\nFirst part:")
print(part1)

print("\nSecond part:")
print(part2)

stacked = np.vstack((part1, part2))
print("\nVertically stacked array:")
print(stacked)