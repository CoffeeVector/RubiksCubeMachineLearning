#!/usr/bin/python3
import RubiksCube as rc
import random as rand

def random_algorithm(size):
    out = [rand.randint(-6, 5) for _ in range(size)]
    return out

def apply_algorithm(cube, algorithm):
    for move in algorithm:
        cube = rc.apply(cube, move)
    return cube

def integrity_check(data):
    data = data.tolist()
    return data.count(0) == 9 and data.count(1) == 9 and data.count(2) == 9 and data.count(3) == 9 and data.count(4) == 9 and data.count(5) == 9

r = rc.solved

r = apply_algorithm(r, random_algorithm(20))

assert integrity_check(r)

rc.print_cube(r)
