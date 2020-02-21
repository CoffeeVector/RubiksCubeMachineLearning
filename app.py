#!/usr/bin/python3

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
c = np.array([[0, 0, 0, 0, 0, 0, 1, 0, 0],
                 [0, 0, 0, 1, 0, 0, 0, 0, 0],
                 [1, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 1, 0],
                 [0, 0, 0, 0, 1, 0, 0, 0, 0],
                 [0, 1, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 1],
                 [0, 0, 0, 0, 0, 1, 0, 0, 0],
                 [0, 0, 1, 0, 0, 0, 0, 0, 0]])
f = 0 # face

z = np.zeros(9, 9)
i = np.identity(9)

if f == 0:
    cwf = np.vstack([
              np.hstack([c,z,z,z,z,z]),
              np.hstack([z,i,z,z,z,z]),
              np.hstack([z,z,i,z,z,z]),
              np.hstack([z,z,z,i,z,z]),
              np.hstack([z,z,z,z,i,z]),
              np.hstack([z,z,z,z,z,i]),
          ])
