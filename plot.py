#!/usr/bin/python3
import matplotlib.pyplot as plt
import RubiksCube as rc

for move in range(-6, 6):
    plt.imshow(rc.r[move])
    print(f"transform-{move}.png")
    plt.savefig(f"transform-{move}.png")
