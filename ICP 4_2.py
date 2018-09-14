# Use Numpy to create a random vector of size 15 having only integers in the range 0-20.

import numpy as np

vect = np.random.randint(0,20,15)

# print("Vector of integer:")

print(vect)

# # Write a program to find the most frequent item/value in the vector list

print("The most frequent value in the vector is:")

print(np.bincount(vect).argmax())
