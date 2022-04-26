from CoverTree import CoverTree
import pandas as pd
import sys
import numpy as np
from FastDPeak import FastDPeak
import decimal
from random import randint
import matplotlib.pyplot as plt
from do_pca import pca,featurescaling

import timeit

start = timeit.default_timer()

def distance(p,q):
    s=0
    for i in range(len(p)):
        s+=((p[i]-q[i])**2)
    return s**(1/2)
    
nRows=5000
nCols=8

#df = pd.read_csv('data.csv',sep=',',header=None)
df = pd.read_csv('shortened.data',sep=',',nrows=nRows)
#df = pd.read_csv('kddcup.data.gz', compression='gzip', header=0, sep=',', quotechar='"', error_bad_lines=False)
df.columns=[i for i in range(1,43)]
df[1]=df[1].astype('int')

for i in range(5,42):
	df[i]=df[i].astype('int')
	
df.drop([2,3,4,42],axis=1,inplace=True)
#print(df.head())
X=featurescaling(df)




X=pca(X,nCols)


#K value
K=50

#C=categories
C=40

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