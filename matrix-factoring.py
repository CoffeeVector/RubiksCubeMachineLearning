#!/usr/bin/python3
import RubiksCube as rc
import random as r

import numpy as np
import numpy.linalg

import matplotlib.pyplot as plt

m = rc.r

# Prepare an A matrix
n = 20 # upper bound for sequence. This mathematically caps out at 20 for Rubiks cubes
sequence = [r.randint(-6, 6) for i in range(n)]

A = [rc.r[s] for s in sequence]
A = np.linalg.multi_dot(A)

plt.imshow(A)
plt.show()
