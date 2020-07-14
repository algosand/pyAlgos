# Full implementatino of Kruskal's Algorithm.
# With union find optimized with path compression and union by rank
# We are detecting cycles with O(E*log(V))
def union(u, v, parents, rank):
	# union by ranking
	if rank[u] > rank[v]:
		parents[v] = u
	else:
		parents[u] = v
	rank[u] += rank[v]
	rank[v] = rank[u]

def find(v, parents):
	start_node = v
	while parents[v] != -1:
		v = parents[v]
	# Path compression
	if start_node != v:
		parents[start_node] = v 
	return v

def kruskal(n, edges):
	edges.sort(key=lambda e: e[2], reverse=True)  # 
	parents = [-1 for i in range(n + 1)]
	rank = [1 for _ in range(n + 1)]
	total = 0
	while edges:
		u, v, w = edges.pop()
		parent_u = find(u, parents)
		parent_v = find(v, parents)
		# Detecting a cycle, if a cycle just continue, don't add this one to the MST.
		if parent_u == parent_v:
			continue
		union(parent_u, parent_v, parents, rank)
		total += w
	return total

n, m = list(map(int, input().split()))
edges = []
for _ in range(m):
    edges.append(list(map(int, input().split())))
print(kruskal(n, edges))

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