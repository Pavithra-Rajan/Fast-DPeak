import pandas as pd
import sys
import numpy as np
from CoverTree import CoverTree



def distance(p,q):
    s=0
    for i in range(len(p)):
        s+=((p[i]-q[i])**2)
    return s**(1/2)


def Local_Density_Peak(X,k,k2,knn_density_set,d_ij,N_ki):
        
    #a list for just checking whether a point is deleted during the iteration or not    
    considered=[1 for i in range(len(X))]

    #to store LDPs
    LDP=set()

    #parent values for each
    parent_node={idx:-1 for idx in range(len(X))}


    #storing nearest point with more density than that particular point
    del_i={idx:-1 for idx in range(len(X))}

    for idx in range(len(X)):
        if considered[idx]:
            flg=True
            for j in N_ki[idx]:
                if knn_density_set[j]>=knn_density_set[idx]:
                    flg=False
                    break
            if flg:
                LDP.add(idx)
                for pt_idx in N_ki[idx]:
                    #marking the nodes as visited
                    considered[pt_idx]=0
                considered[idx]=0
            else:
                min_dij=sys.maxsize
                min_idx=-1
                for j in N_ki[idx]:
                    if knn_density_set[j]>knn_density_set[idx] and d_ij[idx][j]<min_dij:
                        min_dij=d_ij[idx][j]
                        min_idx=j
                parent_node[idx]=min_idx
                del_i[idx]=min_idx


    

    
    
    flg=True
    while len(LDP)>(0.01*len(X)) and k2<=(0.05*len(X)) and flg:
        k2=2*k2
        #constructing query tree for all node belonging to LDP
        QT=CoverTree(distance)
        for ldp in LDP:
            QT.insert(list(X[ldp]))
            
        #for all points in dataset find K2th nearest neighbours in LDP based tree 
        N_k2i={}
        for idx in range(len(X)):
            get_l = QT.knn(list(X[idx]),k2)
            N_k2i[idx]=[]
            for j in get_l:
                if idx!=j[0]:
                    N_k2i[idx].append(j[0])
        test=set([ldp for ldp in LDP])
        
        for ldp in test:
            for each_pt in range(len(X)):
                if len(LDP)<=(0.01*len(X)):
                    flg=False
                    break
                if considered[each_pt]:
                    
                    min_dij=sys.maxsize
                    min_idx=-1
                    for nearest_neighbour in N_k2i[each_pt]:
                        if knn_density_set[nearest_neighbour]>knn_density_set[each_pt] and d_ij[each_pt][nearest_neighbour]<min_dij:
                            min_dij=d_ij[each_pt][nearest_neighbour]
                            min_idx=nearest_neighbour
                    if min_idx!=-1:
                        try:
                            LDP.remove(ldp)
                            parent_node[ldp]=min_idx
                        except:
                            parent_node[ldp]=min_idx

            if len(LDP)<=(0.01*len(X)):
                    flg=False
                    break



    return LDP,parent_node,del_i