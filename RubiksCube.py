#!/usr/bin/python3
from typing import List
import numpy as np 
def concat(arr):
    return np.vstack([np.hstack(row) for row in arr])

def apply(cube, f): return np.dot(r[f], cube)

def getFace(cube, f):
    return cube[9 * f:9 * (f + 1)]

def printFace(v):
    for i in range(3):
        print(v[i * 3:i * 3 + 3])

def print_cube(cube):
    for i in range(6):
        printFace(getFace(cube, i))
        print()

def fitness(r):
    out = 0
    for i in range(6):
        face = r.getFace(i)
        for j in face:
            out += 1 if i == j else 0
    return out

solved = [int(i/9) for i in range(54)]

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

# sticker reference

"""
abc
def  -> abcdefxyz
xyz
"""


# Matrix responsible for rotating the rubiks cube face
"""
abc    zda
def -> yeb
zyx    xfc
"""
c = np.array([[0,0,0,0,0,0,1,0,0],
              [0,0,0,1,0,0,0,0,0],
              [1,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,1,0],
              [0,0,0,0,1,0,0,0,0],
              [0,1,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,1],
              [0,0,0,0,0,1,0,0,0],
              [0,0,1,0,0,0,0,0,0]])

z = np.zeros((9, 9), dtype=int)
i = np.identity(9, dtype=int)

r = [None] * 12
a = np.diag([1,1,1,0,0,0,0,0,0]) # copy top
b = i - a # copy not top
r[0] = concat([[c,z,z,z,z,z],
                [z,i,z,z,z,z],
                [z,z,b,a,z,z],
                [z,z,z,b,a,z],
                [z,z,z,z,b,a],
                [z,z,a,z,z,b]])

a = np.diag([0,0,0,0,0,0,1,1,1]) # copy bottom
b = i - a # copy not bottom
r[1] = concat([[i,z,z,z,z,z],
               [z,c,z,z,z,z],
               [z,z,b,z,z,a],
               [z,z,a,b,z,z],
               [z,z,z,a,b,z],
               [z,z,z,z,a,b]])

a = np.diag([1,0,0,1,0,0,1,0,0]) # copy left
b = i - a # copy not left
d = np.flip(np.diag([1,0,0,1,0,0,1,0,0]), axis=1) # right to left
e = np.diag([1,1,0,1,1,0,1,1,0]) # copy not right
f = np.flip(np.diag([1,0,0,1,0,0,1,0,0]), axis=0) # left to right
r[2] = concat([[b,z,z,z,z,d],
               [z,b,z,a,z,z],
               [z,z,c,z,z,z],
               [a,z,z,b,z,z],
               [z,z,z,z,i,z],
               [z,f,z,z,z,e]])

a = np.vstack([np.zeros([6, 9], dtype=int), c[-3:]]) # right to bottom
b = np.hstack([np.zeros([9, 6], dtype=int), c[:, -3:]]) # bottom to left
d = np.vstack([c[:3], np.zeros([6, 9], dtype=int)]) # left to top
e = np.hstack([c[:, :3], np.zeros([9, 6], dtype=int)])# top to right

f = np.diag([0,1,1,0,1,1,0,1,1])# not left
g = np.diag([1,1,0,1,1,0,1,1,0])# not right
h = np.diag([0,0,0,1,1,1,1,1,1])# not top
j = np.diag([1,1,1,1,1,1,0,0,0])# not bottom

r[3] = concat([[j,z,a,z,z,z],
               [z,h,z,z,d,z],
               [z,e,g,z,z,z],
               [z,z,z,c,z,z],
               [b,z,z,z,f,z],
               [z,z,z,z,z,i]])

a = np.diag([0,0,1,0,0,1,0,0,1]) # copy right
b = np.diag([1,1,0,1,1,0,1,1,0]) # not right
d = np.flip(np.diag([1,0,0,1,0,0,1,0,0]), axis=0) # left to right
e = np.flip(np.diag([1,0,0,1,0,0,1,0,0]), axis=1) # right to left
f = np.diag([0,1,1,0,1,1,0,1,1]) # not left

r[4] = concat([[b,z,z,a,z,z],
               [z,b,z,z,z,d],
               [z,z,i,z,z,z],
               [z,a,z,b,z,z],
               [z,z,z,z,c,z],
               [e,z,z,z,z,f]])

k = np.dot(c, np.dot(c, c))

a = np.vstack([np.zeros([6, 9], dtype=int), k[-3:]]) # left to bottom
b = np.hstack([np.zeros([9, 6], dtype=int), k[:, -3:]]) # bottom to right
d = np.vstack([k[:3], np.zeros([6, 9], dtype=int)]) # right to top
e = np.hstack([k[:, :3], np.zeros([9, 6], dtype=int)])# top to left

f = np.diag([0,1,1,0,1,1,0,1,1])# not left
g = np.diag([1,1,0,1,1,0,1,1,0])# not right
h = np.diag([0,0,0,1,1,1,1,1,1])# not top
j = np.diag([1,1,1,1,1,1,0,0,0])# not bottom

r[5] = concat([[h,z,z,z,d,z],
               [z,j,a,z,z,z],
               [e,z,f,z,z,z],
               [z,z,z,i,z,z],
               [z,b,z,z,g,z],
               [z,z,z,z,z,c]])

for i in range(0, 6):
    r[-i - 1] = np.dot(r[i], np.dot(r[i], r[i]))
