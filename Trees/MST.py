# Full implementatino of Kruskal's Algorithm.
# With union find optimized with path compression and union by rank
# We are detecting cycles with O(E*log(V))
import sys
sys.path.append("../Datastructures/")
from disjointSet import DSU

def kruskal(n, edges):
	"""
	Finds the minimum spanning tree and returns the total weight of it. 

	Args:
		n(int): The number of nodes in the graph
	    edges(list[list]): The weighted edges in the graph

	Returns:
	    int: The total weight of the minimum spanning tree.
    """
	edges.sort(key=lambda e: e[2], reverse=True)  # 
	dsu=DSU(n)
	total = 0
	while edges:
		u, v, w = edges.pop()
		if dsu.union(u,v):
			total+=w
	return total

# n, m = list(map(int, input().split()))
# edges = []
# for _ in range(m):
#     edges.append(list(map(int, input().split())))
# print(kruskal(n, edges))

# This is a very basic implemention of a union find to detect a cycyle in
# an undirected graph.  

# def union(u, v, parents):
# 	parents[u] = v


# def find(v, parents):
# 		while parents[v] != v:
# 			v = parents[v]
# 		return v

# def isCyclic(n, edges):
# 	parents = [i for i in range(n)]

# 	for u, v in edges:
# 		parent_u = find(u, parents)
# 		parent_v = find(v, parents)
# 		if parent_u == parent_v:
# 			return True
# 		union(parent_u, parent_v, parents)
# 	return False

# # For adjacency list do the following, convert to edge list. 

# # Optimized code by union by rank and path compression

# def union(u, v, parents, rank):
# 	# union by ranking
# 	if rank[u] > rank[v]:
# 		parents[v] = u
# 	else:
# 		parents[u] = v
# 	rank[u] += rank[v]
# 	rank[v] = rank[u]


# def find(v, parents):
# 	start_node = v
# 	while parents[v] != v:
# 		v = parents[v]
# 	# Path compression
# 	parents[start_node] = v
# 	return v

# def isCyclic(n, edges):
# 	parents = [i for i in range(n)]
# 	rank = [1 for _ in range(n)]

# 	for u, v in edges:
# 		parent_u = find(u, parents)
# 		parent_v = find(v, parents)
# 		if parent_u == parent_v:
# 			return True
# 		union(parent_u, parent_v, parents, rank)
# 	return False

if __name__=="__main__":
    edges = [
    [1, 2, 5],
    [2, 3, 6],
    [3, 4, 7],
    [1, 4, 4]]
    n=4
    print(kruskal(n,edges))