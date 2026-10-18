# task 1

# for creating virtual env : python -m venv venv
# for activate : venv\scripts\activate (for windows)
# install numpy : pip install numpy (inside venv)

import numpy as np

# task 2
insta_influencer = np.array([1200, 15000, 67000, 340000, 1250000])
print("Array : ",insta_influencer)
print("Dimension of Array : ",np.ndim(insta_influencer))
print("Shape of Array : ",np.shape(insta_influencer))
print("Data Type of Array : ",insta_influencer.dtype)


# task 3
zomato_order_id = np.arange(101,111)
print("Zomato Orer ID : ",zomato_order_id)
print("Size of ID : ",zomato_order_id.size)


# task 4
spotify_like = np.eye(3,3)
print("Spotify Like : ",spotify_like)
# Diagonal value is 1.


# task 5
list_cricket_score =  [45, 67, 120, 89, 54]
array_cricket_score = np.array(list_cricket_score)
print("convert list to array of cricket score : ",array_cricket_score)
print("total bytes array take : ",array_cricket_score.itemsize)