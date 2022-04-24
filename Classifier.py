from CoverTree import CoverTree
import pandas as pd
import sys
import numpy as np
from FastDPeak import FastDPeak
import decimal
from random import randint
import matplotlib.pyplot as plt

import timeit

start = timeit.default_timer()

def distance(p,q):
    s=0
    for i in range(len(p)):
        s+=((p[i]-q[i])**2)
    return s**(1/2)

#df = pd.read_csv('data.csv',sep=',',header=None)
df = pd.read_csv('shortened.data',sep=',')
#df = pd.read_csv('kddcup.data.gz', compression='gzip', header=0, sep=',', quotechar='"', error_bad_lines=False)
X=df.values[:,[0]+[i for i in range(4,16)]]
#X=df.values[:,[-1]]
#print(np.unique(X))

#K value
K=4

#C=categories
C=7

ct=CoverTree(distance)
for point in X:
    #print(point)
    
    ct.insert(point)
print("inserted")
peaks,clusters=FastDPeak(X,K,C,ct)

stop = timeit.default_timer()

print('Time: ', stop - start)  

'''
colors=['green','orange','red']
for i in range(C):
    plt.scatter([j[0] for j in clusters[i]],[j[1] for j in clusters[i]],color=colors[i])

plt.scatter([i[0] for i in peaks], [i[1] for i in peaks], marker="^",color="blue", s=40, linewidths=5)
plt.show()
'''