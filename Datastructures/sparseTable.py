"""
Implementation of sparse table algorithm for solving range minimum and maximum queries 
that are immutable.  
Answer most queries in O(logn)
https://cp-algorithms.com/data_structures/sparse-table.html
"""
from math import log
MAX=500

lookup=[[0]*MAX for _ in range(MAX)]
print(lookup)

# lookup[i][j] is going to store maximum
# value in A[i...j]. Ideally lookup table
# size fixed and determined by nlogn
def buildSparseTable(A,n):
	"""
	Args:
		A(list): The array to build table from
		n(int): The size of the array
	"""
	# Initialize M for the intervals
	# with length 1
	for i in range(n):
		lookup[i][0]=A[i]
	print(lookup)

	# Compute values from smaller
	# to bigger intervals
	i,j=0,1
	while 1<<j<=n:
		# Compute maximum value for 
		# all intervals
		while i+(1<<j)-1<n:
			if lookup[i][j-1]>lookup[1+(1<<(j-1))][j-1]:
				lookup[i][j]=lookup[i][j-1]
			else:
				lookup[i][j]=lookup[i+(1<<(j-1))][j-1]
			i+=1
		j+=1
	print(lookup)

if __name__=="__main__":
	arr=[6,7,4,5,1,3]
	q=[[0,5],[3,5],[2,4]]
	buildSparseTable(arr,len(arr))