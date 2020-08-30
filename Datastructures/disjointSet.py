"""
https://cp-algorithms.com/data_structures/disjoint_set_union.html

"""

class DSU:
    def __init__(self,n):
        self.parent=list(range(n+1))
        self.size=[1]*(n+1)
    
    # Returns the root node of the disjoint set
    # Includes path compression notice if you go through 7->5->3->2->1
    # then you return 1, it will set the parent of every node 7,5,3,2 to be 1, thus compressing the path. 
    def find(self,x):
        if self.parent[x]!=x:
            self.parent[x]=self.find(self.parent[x])
        return self.parent[x]
    
    # Union based on size.
    def union(self,x,y):
        x,y=self.find(x),self.find(y)
        if x!=y:
            # Assume that u is in a disjoint set that is a larger size than the disjoinse set that contains v.
            # Because of that if for some reason size of u is smaller make sure to swap
            # so that the next lines work where you are basically attaching the smaller disjoint set that contains v and merging
            # into the larger disjoint set that contains u
            # then you update the size of v parents.  
            if self.size[y]>self.size[x]:
                x,y=y,x
            # Assume node x is part of a larger connected component of nodes.
            # so set the parent of y to x so that the smaller is attached to larger
            self.size[x]+=self.size[y]
            self.size[y]=self.size[x]
            self.parent[y]=x
            return True
        return False

