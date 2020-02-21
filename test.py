#!/usr/bin/python3

from typing import Dict
import RubiksCube as rc
import numpy as np

r = rc.solved

scramble = rc.randomAlgorithm(20)
r = rc.apply_algo(scramble, r)

unsearched = {}
searched = {}

unsearched[""] = "".join(str(i) for i in r)

def searchone(unsearched: Dict[str, str], searched: Dict[str, str]):
    algo, data_str = max(unsearched.items(), key= lambda kv: rc.fitness([int(i) for i in list(kv[1])]))
    data = np.array([int(i) for i in list(data_str)])
    for move in range(-6, 6):
        tryAlgo = algo + str(move) + ","
        r_new = rc.rotate(data, move)
        r_new_str = "".join(str(i) for i in r_new)
        algo_len = len(tryAlgo.split(',')) - 1

        if (r_new_str not in searched.values()) and (r_new_str not in unsearched.values() and algo_len <= 20):
            unsearched[tryAlgo] = r_new_str

    # moved to searched
    searched[algo] = data_str
    del unsearched[algo]
    return searched, unsearched

def integrity_check(data: list):
    return data.count(0) == 9 and data.count(1) == 9 and data.count(2) == 9 and data.count(3) == 9 and data.count(4) == 9 and data.count(5) == 9


for _ in range(1000):
    searched, unsearched = searchone(unsearched, searched)
    algo, data_str = max(unsearched.items(), key= lambda kv: rc.fitness([int(i) for i in list(kv[1])]))
    print("{algo}: {data_str}".format(algo=algo, data_str=data_str))
    print("len_u: {len_u}, len_ s: {len_s}".format(len_u=len(unsearched), len_s=len(searched)))
    print("len_algo: {len_algo}".format(len_algo=len(algo.split(',')) - 1))
    if not integrity_check([int(i) for i in list(data_str)]):
        break
