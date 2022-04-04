
from CoverTree import CoverTree
import pandas as pd
import sys
import numpy as np
from FastDPeak import FastDPeak
import decimal
from random import randint
import matplotlib.pyplot as plt

def distance(p,q):
    s=0
    for i in range(len(p)):
        s+=((p[i]-q[i])**2)
    return s**(1/2)

df = pd.read_csv('data.csv',sep=',',header=None)
X=df.values[:,:2]

#K value
K=4

#C=categories
C=3

ct=CoverTree(distance)
for point in X:
    ct.insert(list(point))

peaks,clusters=FastDPeak(X,K,C,ct)

colors=['green','orange','red']
for i in range(C):
    plt.scatter([j[0] for j in clusters[i]],[j[1] for j in clusters[i]],color=colors[i])

plt.scatter([i[0] for i in peaks], [i[1] for i in peaks], marker="^",color="blue", s=40, linewidths=5)
plt.show()