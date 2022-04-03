from CoverTree import CoverTree
from LocalDensityPeak import Local_Density_Peak
from FastFindParent import FastFindParent
from Classifier import distance 
import pandas as pd
import sys
import numpy as np


def FastDPeak(X,K,C,ct):
    K2=K

    
    #k nearest neighbours of ith index
    N_ki={}

    #matrix having distance from ith to jth point

    d_ij=[[0 for i in range(len(X))] for j in range(len(X))]


    for idx_pt1 in range(len(X)):
        for idx_pt2 in range(len(X)):

            dist=distance(X[idx_pt1],X[idx_pt2])
            d_ij[idx_pt1][idx_pt2]=dist
            d_ij[idx_pt2][idx_pt1]=dist
    


    #for storing knn density values for all points
    knn_density_set={}
    for idx in range(len(X)):
        get_l = ct.knn(list(X[idx]),k+1)
        N_ki[idx]=[]
        
        for j in get_l[1:]:
            N_ki[idx].append(j[0])
            
        knn_density_set[idx]=1/(get_l[-1][2])


    #Local_density_peaks
    LDP,parent_nodes,del_i=Local_Density_Peak(X,K,K2,knn_density_set,d_ij,N_ki)
    
    # FastFindParent
    LDP,parent_nodes,del_i = FastFindParent(K,LDP,parent_nodes,del_i,knn_density_set,d_ij,N_ki)

    # the first C points with highest value of δ ×(kNN-Density w. r . t K )
    sorted_LDP=sorted(list(LDP),reverse=True,key=lambda x:del_i[x]*knn_density_set[x])[:C]


    # Label each peak and its subnodes as a cluster

    


