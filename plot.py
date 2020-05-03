#!/usr/bin/python3
import matplotlib.pyplot as plt
import RubiksCube as rc

for move in range(-4, 4):
    plt.imshow(rc.r2[move])
    print(f"transform-{move}.png")
    plt.savefig(f"transform-{move}.png")
