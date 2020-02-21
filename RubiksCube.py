# Rubiks Cube with white facing up and red facing towards the POV
import numpy as np
import random as r

# Color reference:
# white: 0
# yellow: 1
# green: 2
# red: 3
# blue: 4
# orange: 5

# Face reference:
# top: 0
# bottom: 1
# left: 2
# front: 3
# right: 4
# back: 5

# Matrix responsible for rotating the rubiks cube face
clockwiseRotationFace = np.array([[0, 0, 0, 0, 0, 0, 1, 0, 0],
                                  [0, 0, 0, 1, 0, 0, 0, 0, 0],
                                  [1, 0, 0, 0, 0, 0, 0, 0, 0],
                                  [0, 0, 0, 0, 0, 0, 0, 1, 0],
                                  [0, 0, 0, 0, 1, 0, 0, 0, 0],
                                  [0, 1, 0, 0, 0, 0, 0, 0, 0],
                                  [0, 0, 0, 0, 0, 0, 0, 0, 1],
                                  [0, 0, 0, 0, 0, 1, 0, 0, 0],
                                  [0, 0, 1, 0, 0, 0, 0, 0, 0]])

solved = np.array([(int) (i / 9)for i in range(54)])

def getFace(arr, f):
    return arr[9 * f:9 * (f + 1)]

def getColor(arr, f, y, x):
    if x >= 3 or x < 0 or y >= 3 or y < 0 or f >= 5 or f < 0:
        raise ValueError("Input invalid")
    else:
        return getFace(arr, f)[y * 3 + x]

def toIndex(face, y, x):
    return face * 9 + y * 3 + x

def fitness(arr):
    return sum([1 if d == t else 0 for d,t in zip(arr, [((int)(i/9))for i in range(54)])])

# Set of 12 matrices, each representing each of the possible moves
rotationMatrices = [None] * 12

for f in range(6):
    rotation = [[1 if i == j else 0 for j in range(54)] for i in range(54)]  # I_54 matrix ( identity matrix )
    # Add the matrix that rotates the face that's desired by offsetting it
    for i in range(9 * f, 9 * (f + 1)): # the row vectors that correspond to that face
        rotation[i] = [ 0 if j < 9 * f or j >= 9 * (f + 1) else clockwiseRotationFace[i - 9 * f][j - 9 * f] for j in range(54) ]

    if f == 0:
        # Replace left with front
        rotation[toIndex(2, 0, 0)][toIndex(3, 0, 0)] = 1  # Add the 1 that does the operation
        rotation[toIndex(2, 0, 0)][toIndex(2, 0, 0)] = 0  # Remove the 1 from the identity matrix prior

        rotation[toIndex(2, 0, 1)][toIndex(3, 0, 1)] = 1
        rotation[toIndex(2, 0, 1)][toIndex(2, 0, 1)] = 0

        rotation[toIndex(2, 0, 2)][toIndex(3, 0, 2)] = 1
        rotation[toIndex(2, 0, 2)][toIndex(2, 0, 2)] = 0

        # Replace front with right
        rotation[toIndex(3, 0, 0)][toIndex(4, 0, 0)] = 1
        rotation[toIndex(3, 0, 0)][toIndex(3, 0, 0)] = 0

        rotation[toIndex(3, 0, 1)][toIndex(4, 0, 1)] = 1
        rotation[toIndex(3, 0, 1)][toIndex(3, 0, 1)] = 0

        rotation[toIndex(3, 0, 2)][toIndex(4, 0, 2)] = 1
        rotation[toIndex(3, 0, 2)][toIndex(3, 0, 2)] = 0

        # Replace right with back
        rotation[toIndex(4, 0, 0)][toIndex(5, 0, 0)] = 1
        rotation[toIndex(4, 0, 0)][toIndex(4, 0, 0)] = 0

        rotation[toIndex(4, 0, 1)][toIndex(5, 0, 1)] = 1
        rotation[toIndex(4, 0, 1)][toIndex(4, 0, 1)] = 0

        rotation[toIndex(4, 0, 2)][toIndex(5, 0, 2)] = 1
        rotation[toIndex(4, 0, 2)][toIndex(4, 0, 2)] = 0

        # Replace back with left
        rotation[toIndex(5, 0, 0)][toIndex(2, 0, 0)] = 1
        rotation[toIndex(5, 0, 0)][toIndex(5, 0, 0)] = 0

        rotation[toIndex(5, 0, 1)][toIndex(2, 0, 1)] = 1
        rotation[toIndex(5, 0, 1)][toIndex(5, 0, 1)] = 0

        rotation[toIndex(5, 0, 2)][toIndex(2, 0, 2)] = 1
        rotation[toIndex(5, 0, 2)][toIndex(5, 0, 2)] = 0
    elif f == 1:
        # Replace front with left
        rotation[toIndex(3, 2, 0)][toIndex(2, 2, 0)] = 1
        rotation[toIndex(3, 2, 0)][toIndex(3, 2, 0)] = 0

        rotation[toIndex(3, 2, 1)][toIndex(2, 2, 1)] = 1
        rotation[toIndex(3, 2, 1)][toIndex(3, 2, 1)] = 0

        rotation[toIndex(3, 2, 2)][toIndex(2, 2, 2)] = 1
        rotation[toIndex(3, 2, 2)][toIndex(3, 2, 2)] = 0

        # Replace right with front
        rotation[toIndex(4, 2, 0)][toIndex(3, 2, 0)] = 1
        rotation[toIndex(4, 2, 0)][toIndex(4, 2, 0)] = 0

        rotation[toIndex(4, 2, 1)][toIndex(3, 2, 1)] = 1
        rotation[toIndex(4, 2, 1)][toIndex(4, 2, 1)] = 0

        rotation[toIndex(4, 2, 2)][toIndex(3, 2, 2)] = 1
        rotation[toIndex(4, 2, 2)][toIndex(4, 2, 2)] = 0

        # Replace back with right
        rotation[toIndex(5, 2, 0)][toIndex(4, 2, 0)] = 1
        rotation[toIndex(5, 2, 0)][toIndex(5, 2, 0)] = 0

        rotation[toIndex(5, 2, 1)][toIndex(4, 2, 1)] = 1
        rotation[toIndex(5, 2, 1)][toIndex(5, 2, 1)] = 0

        rotation[toIndex(5, 2, 2)][toIndex(4, 2, 2)] = 1
        rotation[toIndex(5, 2, 2)][toIndex(5, 2, 2)] = 0

        # Replace left with back
        rotation[toIndex(2, 2, 0)][toIndex(5, 2, 0)] = 1
        rotation[toIndex(2, 2, 0)][toIndex(2, 2, 0)] = 0

        rotation[toIndex(2, 2, 1)][toIndex(5, 2, 1)] = 1
        rotation[toIndex(2, 2, 1)][toIndex(2, 2, 1)] = 0

        rotation[toIndex(2, 2, 2)][toIndex(5, 2, 2)] = 1
        rotation[toIndex(2, 2, 2)][toIndex(2, 2, 2)] = 0
    elif f == 2:
        # Replace front with top
        rotation[toIndex(3, 0, 0)][toIndex(0, 0, 0)] = 1
        rotation[toIndex(3, 0, 0)][toIndex(3, 0, 0)] = 0

        rotation[toIndex(3, 1, 0)][toIndex(0, 1, 0)] = 1
        rotation[toIndex(3, 1, 0)][toIndex(3, 1, 0)] = 0

        rotation[toIndex(3, 2, 0)][toIndex(0, 2, 0)] = 1
        rotation[toIndex(3, 2, 0)][toIndex(3, 2, 0)] = 0

        # Replace bottom with front
        rotation[toIndex(1, 0, 0)][toIndex(3, 0, 0)] = 1
        rotation[toIndex(1, 0, 0)][toIndex(1, 0, 0)] = 0

        rotation[toIndex(1, 1, 0)][toIndex(3, 1, 0)] = 1
        rotation[toIndex(1, 1, 0)][toIndex(1, 1, 0)] = 0

        rotation[toIndex(1, 2, 0)][toIndex(3, 2, 0)] = 1
        rotation[toIndex(1, 2, 0)][toIndex(1, 2, 0)] = 0

        # Replace back with bottom
        rotation[toIndex(5, 0, 2)][toIndex(1, 2, 0)] = 1
        rotation[toIndex(5, 0, 2)][toIndex(5, 0, 2)] = 0

        rotation[toIndex(5, 1, 2)][toIndex(1, 1, 0)] = 1
        rotation[toIndex(5, 1, 2)][toIndex(5, 1, 2)] = 0

        rotation[toIndex(5, 2, 2)][toIndex(1, 0, 0)] = 1
        rotation[toIndex(5, 2, 2)][toIndex(5, 2, 2)] = 0

        # Replace top with back
        rotation[toIndex(0, 2, 0)][toIndex(5, 0, 2)] = 1
        rotation[toIndex(0, 2, 0)][toIndex(0, 2, 0)] = 0

        rotation[toIndex(0, 1, 0)][toIndex(5, 1, 2)] = 1
        rotation[toIndex(0, 1, 0)][toIndex(0, 1, 0)] = 0

        rotation[toIndex(0, 0, 0)][toIndex(5, 2, 2)] = 1
        rotation[toIndex(0, 0, 0)][toIndex(0, 0, 0)] = 0
    elif f == 3:
        # Replace top with left
        rotation[toIndex(0, 2, 0)][toIndex(2, 2, 2)] = 1  # Add the 1 that does the operation
        rotation[toIndex(0, 2, 0)][toIndex(0, 2, 0)] = 0  # Remove the 1 from the identity matrix prior

        rotation[toIndex(0, 2, 1)][toIndex(2, 1, 2)] = 1
        rotation[toIndex(0, 2, 1)][toIndex(0, 2, 1)] = 0

        rotation[toIndex(0, 2, 2)][toIndex(2, 0, 2)] = 1
        rotation[toIndex(0, 2, 2)][toIndex(0, 2, 2)] = 0

        # Replace right with top
        rotation[toIndex(4, 0, 0)][toIndex(0, 2, 0)] = 1
        rotation[toIndex(4, 0, 0)][toIndex(4, 0, 0)] = 0

        rotation[toIndex(4, 1, 0)][toIndex(0, 2, 1)] = 1
        rotation[toIndex(4, 1, 0)][toIndex(4, 1, 0)] = 0

        rotation[toIndex(4, 2, 0)][toIndex(0, 2, 2)] = 1
        rotation[toIndex(4, 2, 0)][toIndex(4, 2, 0)] = 0

        # Replace bottom with right
        rotation[toIndex(1, 0, 2)][toIndex(4, 0, 0)] = 1
        rotation[toIndex(1, 0, 2)][toIndex(1, 0, 2)] = 0

        rotation[toIndex(1, 0, 1)][toIndex(4, 1, 0)] = 1
        rotation[toIndex(1, 0, 1)][toIndex(1, 0, 1)] = 0

        rotation[toIndex(1, 0, 0)][toIndex(4, 2, 0)] = 1
        rotation[toIndex(1, 0, 0)][toIndex(1, 0, 0)] = 0

        # Replace left with bottom
        rotation[toIndex(2, 2, 2)][toIndex(1, 0, 2)] = 1
        rotation[toIndex(2, 2, 2)][toIndex(2, 2, 2)] = 0

        rotation[toIndex(2, 1, 2)][toIndex(1, 0, 1)] = 1
        rotation[toIndex(2, 1, 2)][toIndex(2, 1, 2)] = 0

        rotation[toIndex(2, 0, 2)][toIndex(1, 0, 0)] = 1
        rotation[toIndex(2, 0, 2)][toIndex(2, 0, 2)] = 0
    elif f == 4:
        # Replace top with front
        rotation[toIndex(0, 0, 2)][toIndex(3, 0, 2)] = 1
        rotation[toIndex(0, 0, 2)][toIndex(0, 0, 2)] = 0

        rotation[toIndex(0, 1, 2)][toIndex(3, 1, 2)] = 1
        rotation[toIndex(0, 1, 2)][toIndex(0, 1, 2)] = 0

        rotation[toIndex(0, 2, 2)][toIndex(3, 2, 2)] = 1
        rotation[toIndex(0, 2, 2)][toIndex(0, 2, 2)] = 0

        # Replace back with top
        rotation[toIndex(5, 0, 0)][toIndex(0, 2, 2)] = 1
        rotation[toIndex(5, 0, 0)][toIndex(5, 0, 0)] = 0

        rotation[toIndex(5, 1, 0)][toIndex(0, 1, 2)] = 1
        rotation[toIndex(5, 1, 0)][toIndex(5, 1, 0)] = 0

        rotation[toIndex(5, 2, 0)][toIndex(0, 0, 2)] = 1
        rotation[toIndex(5, 2, 0)][toIndex(5, 2, 0)] = 0

        # Replace bottom with back
        rotation[toIndex(1, 2, 2)][toIndex(5, 0, 0)] = 1
        rotation[toIndex(1, 2, 2)][toIndex(1, 2, 2)] = 0

        rotation[toIndex(1, 1, 2)][toIndex(5, 1, 0)] = 1
        rotation[toIndex(1, 1, 2)][toIndex(1, 1, 2)] = 0

        rotation[toIndex(1, 0, 2)][toIndex(5, 2, 0)] = 1
        rotation[toIndex(1, 0, 2)][toIndex(1, 0, 2)] = 0

        # Replace front with bottom
        rotation[toIndex(3, 2, 2)][toIndex(1, 2, 2)] = 1
        rotation[toIndex(3, 2, 2)][toIndex(3, 2, 2)] = 0

        rotation[toIndex(3, 1, 2)][toIndex(1, 1, 2)] = 1
        rotation[toIndex(3, 1, 2)][toIndex(3, 1, 2)] = 0

        rotation[toIndex(3, 0, 2)][toIndex(1, 0, 2)] = 1
        rotation[toIndex(3, 0, 2)][toIndex(3, 0, 2)] = 0
    elif f == 5:
        # Replace top with right
        rotation[toIndex(0, 0, 0)][toIndex(4, 0, 2)] = 1
        rotation[toIndex(0, 0, 0)][toIndex(0, 0, 0)] = 0

        rotation[toIndex(0, 0, 1)][toIndex(4, 1, 2)] = 1
        rotation[toIndex(0, 0, 1)][toIndex(0, 0, 1)] = 0

        rotation[toIndex(0, 0, 2)][toIndex(4, 2, 2)] = 1
        rotation[toIndex(0, 0, 2)][toIndex(0, 0, 2)] = 0

        # Replace right with bottom
        rotation[toIndex(4, 0, 2)][toIndex(1, 2, 2)] = 1
        rotation[toIndex(4, 0, 2)][toIndex(4, 0, 2)] = 0

        rotation[toIndex(4, 1, 2)][toIndex(1, 2, 1)] = 1
        rotation[toIndex(4, 1, 2)][toIndex(4, 1, 2)] = 0

        rotation[toIndex(4, 2, 2)][toIndex(1, 2, 0)] = 1
        rotation[toIndex(4, 2, 2)][toIndex(4, 2, 2)] = 0

        # Replace bottom with left
        rotation[toIndex(1, 2, 2)][toIndex(2, 2, 0)] = 1
        rotation[toIndex(1, 2, 2)][toIndex(1, 2, 2)] = 0

        rotation[toIndex(1, 2, 1)][toIndex(2, 1, 0)] = 1
        rotation[toIndex(1, 2, 1)][toIndex(1, 2, 1)] = 0

        rotation[toIndex(1, 2, 0)][toIndex(2, 0, 0)] = 1
        rotation[toIndex(1, 2, 0)][toIndex(1, 2, 0)] = 0

        # Replace left with top
        rotation[toIndex(2, 2, 0)][toIndex(0, 0, 0)] = 1
        rotation[toIndex(2, 2, 0)][toIndex(2, 2, 0)] = 0

        rotation[toIndex(2, 1, 0)][toIndex(0, 0, 1)] = 1
        rotation[toIndex(2, 1, 0)][toIndex(2, 1, 0)] = 0

        rotation[toIndex(2, 0, 0)][toIndex(0, 0, 2)] = 1
        rotation[toIndex(2, 0, 0)][toIndex(2, 0, 0)] = 0

    rotationMatrices[f] = rotation
    rotationMatrices[-f - 1] = np.dot(rotation, np.dot(rotation, rotation))

def rotate(arr, f):
    return np.dot(rotationMatrices[f], arr)

def print(self):
    for i in range(6):
        printFace(self.getFace(i))
        print()

def __str__(self):
    out = ""
    for f in range(6):
        for i in range(3):
            out += str(self.getFace(f)[i * 3:i * 3 + 3])
            out += "\n"
        out += "\n"
    return out

def printFace(v):
    for i in range(3):
        print(v[i * 3:i * 3 + 3])

def apply_algo(algo, r):
    new_r = r
    for i in algo:
        new_r = rotate(new_r, i)
    return new_r


def stringify_algo(algo: list):
    return ";".join(algo)

def unstringify_algo(algo: str):
    return algo.split(";")

#out = ""
#for i in self.data:
#    if i == 0:
#        out += 'u'
#    elif i == -1:
#        out += 'U'
#    elif i == 1:
#        out += 'd'
#    elif i == -2:
#        out += 'D'
#    elif i == 2:
#        out += 'l'
#    elif i == -3:
#        out += 'L'
#    elif i == 3:
#        out += 'f'
#    elif i == -4:
#        out += 'F'
#    elif i == 4:
#        out += 'r'
#    elif i == -5:
#        out += 'R'
#    elif i == 5:
#        out += 'b'
#    elif i == -6:
#        out += 'B'
#    out += " "
#return out

def randomAlgorithm(size):
    return [r.randint(-6, 5) for _ in range(size)]
