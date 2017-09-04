#! /usr/bin/python
#
# Implemented by Jiayu Wang (email: jiayuw6@student.unimelb.edu.au). Copyright reserved.
#

import numpy as np
import matplotlib.pyplot as pl

N1 = 2000
N2 = 499
R1 = 20
R2 = 2

# Large circle
phi1 = np.random.rand(N1, 1) * 2 * np.pi
r1 = np.sqrt(np.random.rand(N1, 1))
circle1 = np.hstack((30 + np.cos(phi1) * R1 * r1, 30 + np.sin(phi1) * R1 * r1, np.ones((N1, 1))))

# Large circle
phi2 = np.random.rand(N2, 1) * 2 * np.pi
r2 = np.sqrt(np.random.rand(N2, 1))
circle2 = np.hstack((np.cos(phi2) * R2 * r2, np.sin(phi2) * R2 * r2, np.ones((N2, 1))))

x = 3.3
y = 1.8
# print circle1
pl.plot(circle1[:,0],circle1[:,1],'o', circle2[:,0], circle2[:,1],'o', x, y, 'o')
pl.show()

file = open('./local-one-anomaly.csv', 'w')
for i in range(len(circle1)):
    line = str(circle1[i][0]) + "," + str(circle1[i][1]) + ",-1.0"
    file.write(line)
    file.write('\n')

for i in range(len(circle2)):
    line = str(circle2[i][0]) + "," + str(circle2[i][1]) + ",-1.0"
    file.write(line)
    file.write('\n')

line = str(x) + "," + str(y) + ",1.0"
file.write(line)
file.write('\n')

file.close()