import sys


def getsubNodes(adj,nodes):
    start = [None] * 100001
    end = [None] * 100001
    
    
    dfs_order = []
    
    visited = [False] * 100001
    
    subnodes={}

    def dfs(a, b):
    
       
        visited[a] = 1
        b += 1
        start[a] = b
        dfs_order.append(a)
        
        for it in adj[a]:
            if not visited[it]:
                b = dfs(it, b)
        
        end[a] = b
        return b
    
    
    
    
    for i in nodes:
        print('333')
        
        if start[i] != end[i]:
        
            subnodes[i]=[]
            for j in range(start[i]+1, end[i]+1):
            
                subnodes[i].append(dfs_order[j-1])
    return subnodes
                

def FastFindParent(LDP,parent_nodes,knn_density):
    ldp_density={idx:knn_density[idx] for idx in LDP}
    
    sldp_density={idx:knn_density for idx,knn_density in sorted(ldp_density.items(),reverse=True,key=lambda x:x[1])}
    sLDP=sldp_density.keys()
    M=len(LDP)
    

    children={parent:[] for j in parent_nodes.values()}
    
    for child,parent in parent_nodes:
        children[parent].append(child)


    childrens={}
    for parent in children:
        flg=True
        curr=children[parent]
        childrens[parent]=[]
        while flg:
            try:
                childrens[parent].append(curr)
                curr=children[curr]
            except:
                flg=False


    nodes_considered={idx:1 for idx in children}

    
#bfs





    



    del_i={sLDP[M-1]:sys.maxsize}

    W=M-2
    while W>-1:
        point_i=sLDP[W]
        del_i[point_i]=sys.maxsize

        Q=W+1
        while Q>=M:
            point_j=sLDP[Q]

            flags={q:0 for q in childrens[point_j]}








a={1:[2,3,4],2:[5,6,7],3:[10],7:[9,8]}
nodes=[1,2,3,4,5,6,7,8,9,10]
print(getsubNodes(a,nodes))
