"""
https://cp-algorithms.com/data_structures/disjoint_set_union.html

"""

class DSU:
    def __init__(self, n):
        self.par = list(range(n+1))
        self.size = [1]*(n+1)
    
    # Returns the root node of the disjoint set
    # Includes path compression notice if you go through 7->5->3->2->1
    # then you return 1, it will set the parent of every node 7,5,3,2 to be 1, thus compressing the path. 
    def find(self,v):
        if self.par[v]!=v:
            self.par[v]=self.find(self.par[v])
        return self.par[v]
    
    # Union based on size.
    def union(self,u,v):
        u=self.find(u)
        v=self.find(v)
        if u!=v:
            # Assume that u is in a disjoint set that is a larger size than the disjoinse set that contains v.
            # Because of that if for some reason size of u is smaller make sure to swap
            # so that the next lines work where you are basically attaching the smaller disjoint set that contains v and merging
            # into the larger disjoint set that contains u
            # then you update the size of v parents.  
            if self.size[u]<self.size[v]:
                u,v=v,u
            self.par[v]=u
            self.size[u]+=self.size[v]
            self.size[v]=self.size[u]
            return True
        return False