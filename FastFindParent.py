import sys
         

def FastFindParent(k,LDP,parent_nodes,knn_density,d_ij,N_ki):
    ldp_density={idx:knn_density[idx] for idx in LDP}
    
    sldp_density={idx:knn_density for idx,knn_density in sorted(ldp_density.items(),reverse=True,key=lambda x:x[1])}
    sLDP=sldp_density.keys()
    M=len(LDP)
    

    children={node:[] for node in list(set(parent_nodes.values()+parent_nodes.keys()))}

    
    
    for child,parent in parent_nodes:
        children[parent].append(child)

    #getsubnodes of each nodes will be done here
    def getSubNodes(tree,start):
        visited = [] 
        queue = []    
        subnodes=[]
        
        visited.append(start)
        queue.append(start)

        while queue:          
            m = queue.pop(0) 
            subnodes.append(m) 

            for neighbour in tree[m]:
                if neighbour not in visited:
                    visited.append(neighbour)
                    queue.append(neighbour)

        try:
            return subnodes[1:]
        except:
            return []


    childrens={}
    for node in children:
        childrens[node]=getSubNodes(children,node)



    #nodes_considered={idx:1 for idx in children}


    del_i={sLDP[M-1]:sys.maxsize}

    W=M-2
    while W>-1:
        point_i=sLDP[W]
        del_i[point_i]=sys.maxsize

        Q=W+1
        while Q>=M:
            point_j=sLDP[Q]


            flags={q:0 for q in childrens[point_j]}
            visited={subnode:1 for subnode in childrens[point_j]}
            for subnode in childrens[point_j]:
                if visited[subnode] and knn_density[point_i]>knn_density[subnode]:
                    #skip subnode and all subnodes of s
                    visited[subnode]=0
                    for sub_subnode in childrens[subnode]:
                        visited[sub_subnode]=0
                if flags[subnode]:
                    visited[subnode]=0

                if del_i[point_i]>d_ij[point_i][subnode]:
                    parent_nodes[point_i]=subnode
                    continue
                for L in range(k,0,-1):
                    if d_ij[point_i][subnode]>del_i[point_i]+d_ij[subnode][N_ki[subnode][L-1]]:
                        for q in N_ki[:L]:
                            flags[q]=1

                
                




            






