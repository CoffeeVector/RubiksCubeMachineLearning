#!/usr/bin/python3
from typing import Dict
import RubiksCube as rc
import numpy as np
import numpy.linalg
import matplotlib.pyplot as plt
import random as rand

def random_algorithm(size):
    out = [rand.randint(-6, 5) for _ in range(size)]
    return out

def apply_algorithm(cube, algorithm):
    for move in algorithm:
        cube = rc.apply(cube, move)
    return cube

r = rc.solved

scramble = random_algorithm(20)

r = apply_algorithm(r, scramble)

sort_matrix = np.identity(len(r), dtype=int)

for i in range(len(r) - 1):
    for j in range(len(r) - i - 1):
        if r[j] > r[j + 1]:
            m = np.identity(len(r), dtype=int)
            m[j    ][j    ] = 0;
            m[j + 1][j + 1] = 0;
            m[j    ][j + 1] = 1;
            m[j + 1][j    ] = 1;
            sort_matrix = np.dot(m, sort_matrix)
            r = np.dot(m, r)

print(np.linalg.det(sort_matrix))
plt.imshow(sort_matrix)

plt.show()

