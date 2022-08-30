#%%
import numpy as np
import matplotlib.pyplot as plt
import random

#%%
#IMPUT NAME AND FORMAT HERE
name = "15-11_15_11, CONTROL1 VK second tests"
fmt = ".csv"

#INPUT LOWER AND UPPER BOUNDS OF AXES HERE
lbnd = 45
upbnd = 50

#IF THE GRAPH IS AVERAGED AND YOU WOULD LIKE A SIMILAR BUT ALTERED NAME, MAKE THIS TRUE
average = False

#NAME OF SAVED PNG HERE
svname = "Control 1"
filename = svname + " random.csv"

#%%
raw = np.genfromtxt(name + fmt,dtype='float',delimiter=',',skip_header=0)

vald = raw[:,6]
pred = raw[:,7]
deltas = raw[:,10]
temp1 = raw[:,0]
#print("initial temp1:", temp1)
temp2 = raw[:,1]
temp3 = raw[:,2]
temp4 = raw[:,3]
temp5 = raw[:,4]
temp6 = raw[:,5]

datapnts = len(vald)

#%%
inx1 = 0
inx2 = 0
inx3 = 0
inx4 = 0
inx5 = 0
inx6 = 0

x = random.randrange(-50, 50)

for x in temp1:
    r = random.randrange(-50, 50)
    r = r / 100
    temp1[inx1] = temp1[inx1] + r
    inx1 += 1
for x in temp2:
    r = random.randrange(-50, 50)
    r = r / 100
    temp2[inx2] = temp2[inx2] + r
    inx2 += 1
for x in temp3:
    r = random.randrange(-50, 50)
    r = r / 100
    temp3[inx3] = temp3[inx3] + r
    inx3 += 1
for x in temp4:
    r = random.randrange(-50, 50)
    r = r / 100
    temp4[inx4] = temp4[inx4] + r
    inx4 += 1
for x in temp5:
    r = random.randrange(-50, 50)
    r = r / 100
    temp5[inx5] = temp5[inx5] + r
    inx5 += 1
for x in temp6:
    r = random.randrange(-50, 50)
    r = r / 100
    temp6[inx6] = temp6[inx6] + r
    inx6 += 1
    
#%%
time = np.linspace(0, 60, datapnts)
plt.plot(time, temp1, label="final")
#plt.plot(time, noisetemp1, label="initial")
plt.xlabel('time (seconds)') # creates a label 'x' for the x-axis
plt.ylabel('temperature (°C)') # creates a label 'y' for the y-axis
plt.ylim(lbnd, upbnd)
title = 'noise and non noisy graph'
plt.title(title)
plt.legend()
plt.show()

#%%
raw[:,0] = temp1
raw[:,1] = temp2
raw[:,2] = temp3
raw[:,3] = temp4
raw[:,4] = temp5
raw[:,5] = temp6
np.savetxt(filename, raw, delimiter = ',')
