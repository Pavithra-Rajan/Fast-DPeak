from FastDPeak import FastDPeak
from CoverTree import CoverTree
import pandas as pd
import sys
import numpy as np


def distance(p,q):
    s=0
    for i in range(len(p)):
        s+=((p[i]-q[i])**2)
    return s**(1/2)

df = pd.read_csv('IRIS.csv')
X=df.values[:,:4]
Y= df.values[:,[4]]

#K value
K=5


#C=categories
C=len(set(Y))

ct=CoverTree(distance)
for point in X:
    ct.insert(list(point))



clusters=FastDPeak(X,K,C,ct,distance)
