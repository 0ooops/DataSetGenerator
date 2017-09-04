#! /usr/bin/python
#
# Implemented by Jiayu Wang (email: jiayuw6@student.unimelb.edu.au). Copyright reserved.
#

import math
import numpy as np
import matplotlib.pyplot as pl

N = 5000
degree = 570
start = 90
noise = 0

deg2rad = (2 * math.pi) / 360
start *= deg2rad

N1 = int(np.floor(N / 2))
N2 = N - N1

# Two spirals
n = start + np.sqrt(np.random.rand(N1, 1)) * degree * deg2rad
d1 = np.hstack((-np.cos(n) * n + np.random.rand(N1, 1) * noise, np.sin(n) * n + np.random.rand(N1, 1) * noise, np.zeros((N1, 1))))

n = start + np.sqrt(np.random.rand(N1, 1)) * degree * deg2rad
d2 = np.hstack((np.cos(n) * n + np.random.rand(N2, 1) * noise, -np.sin(n) * n + np.random.rand(N2, 1) * noise, np.ones((N2, 1))))

# Distributed anomalies
x = np.random.uniform(-12, 12.5, 50)
y = np.random.uniform(-12, 11.5, 50)

pl.plot(d1[:,1], d1[:,0],'o', d2[:,1], d2[:,0],'o', x, y, 'o')
pl.show()

file = open('./two-spiral-local.csv', 'w')
for i in range(len(d1)):
    line = str(d1[i][0]) + "," + str(d1[i][1]) + ",-1.0"
    file.write(line)
    file.write('\n')

for i in range(len(d2)):
    line = str(d2[i][0]) + "," + str(d2[i][1]) + ",-1.0"
    file.write(line)
    file.write('\n')

for i in range(len(x)):
    line = str(x[i]) + "," + str(y[i]) + ",1.0"
    file.write(line)
    file.write('\n')

file.close()