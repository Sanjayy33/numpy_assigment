import numpy as np

# task 1
ratings = np.array([
    [4, 5, 3, 4, 2],
    [5, 4, 4, 3, 5],
    [3, 4, 5, 2, 4],
    [4, 3, 2, 5, 4]
])
result = ratings[1:3, :]
print(result)


# task 2
steps = np.array([7500, 8200, 9000, 6500, 10500,
                  7800, 8800, 6000, 12000, 8100])
result = steps[steps > 8000]
print(result)


# task 3
scores = np.array([180, 210, 165, 195, 225, 170, 200, 185])
result = scores[[1, 4, 6]]
print(result)


# task 4
prices = np.array([1000, 2500, 500, 3000, 1500])
discounted_prices = prices * 0.90
print(discounted_prices)


# task 5
ratings = np.array([5, -2, 3, 0, -1, 4, -5, 2])
ratings[ratings < 0] = 0
print(ratings)