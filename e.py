#!/usr/bin/python3
import RubiksCube as rc
import numpy as np
import numpy.linalg
import matplotlib.pyplot as plt

moves = range(-6, 6)
print(moves)
P = [None] * len(moves)

#for m in moves:
#    print(np.linalg.det(rc.r[m]))
#
for m in moves:
    w, v = np.linalg.eig(rc.r[m])
    w_round = [round(e_val.imag, 2) for e_val in w]
    plt.imshow([w_round])
    plt.show()

    #print(len(v))
    #P[m] = np.transpose(np.array(v))
    #print(np.linalg.matrix_rank(P[m]))
    #print(w)
#
#for p in P:
#    w, v = np.linalg.eig(p)
#    A = np.transpose(np.array(v))
#    #print(np.linalg.matrix_rank(A))
#    #print(w)

#s = [ [ rc.r[0][i * 18:(i + 1)* 18 , j * 18:(j + 1)*18] for j in range(3)] for i in range(3)]
#
#for i in s:
#    print([np.linalg.det(j) for j in i])
#
#print(np.linalg.det(rc.r[0]))
#
#import matplotlib.pyplot as plt
#
#plt.imshow(rc.r[0])
#plt.show()
