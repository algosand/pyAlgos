is it inclusive of left and right? 
# Segtree for sum
# from collections import Counter
# import math
# class SegTree:
# 	def __init__(self, arr):
# 		self.m = 2**math.ceil(math.log2(len(arr)))
# 		inf = float('inf')
# 		self.arr = arr
# 		self.tree = [inf]*(2*self.m)
# 		self.n = len(arr)
# 		self.build()

# 	def build(self):
# 		for i in range(self.n):
# 			self.tree[self.m + i] = arr[i]
# 		for i in range(self.m - 1, 0, -1):
# 			self.tree[i] = self.tree[i << 1] + self.tree[i << 1 | 1]


# 	def update(self, node, value):
# 		self.tree[node + self.m] = value
# 		i = node + self.m
# 		while i > 1:
# 			self.tree[i >> 1] = self.tree[i] + self.tree[i ^ 1]
# 			i >>= 1

# 	def query(self, l, r):
# 		l += self.m
# 		r += self.m
# 		ans = 0
# 		while l < r:
# 			if l & 1:
# 				ans += self.tree[l]
# 				l += 1

# 			if r & 1:
# 				r -= 1
# 				ans += self.tree[r]
# 			l >>= 1
# 			r >>= 1
# 		return ans
# Segment tree for min
# from collections import Counter
# import math
# class SegTree:
# 	def __init__(self, arr):
# 		self.m = 2**math.ceil(math.log2(len(arr)))
# 		inf = float('inf')
# 		self.arr = arr
# 		self.tree = [inf]*(2*self.m)
# 		self.n = len(arr)
# 		self.build()

# 	def build(self):
# 		for i in range(self.n):
# 			self.tree[self.m + i] = arr[i]
# 		for i in range(self.m - 1, 0, -1):
# 			self.tree[i] = min(self.tree[i << 1], self.tree[i << 1 | 1])

# 	def update(self, node, value):
# 		self.tree[node + self.m] = value
# 		i = node + self.m
# 		while i > 1:
# 			self.tree[i >> 1] = min(self.tree[i], self.tree[i ^ 1])
# 			i >>= 1

# 	def query(self, l, r):
# 		l += self.m
# 		r += self.m
# 		inf = float('inf')
# 		ans = inf
# 		while l < r:
# 			if l & 1:
# 				ans = min(ans, self.tree[l])
# 				l += 1

# 			if r & 1:
# 				r -= 1
# 				ans = min(ans, self.tree[r])
# 			l >>= 1
# 			r >>= 1
# 		return ans

#segment tree for storing the minimum value and the number of times that value appeared.
# from collections import Counter
# import math
# class SegTree:
# 	def __init__(self, arr):
# 		self.m = 2**math.ceil(math.log2(len(arr)))
# 		inf = float('inf')
# 		self.arr = arr
# 		self.tree = [[inf, 0] for _ in range(2*self.m)]
# 		self.n = len(arr)
# 		self.build()
# 	# Number of elements with minimum
# 	def build(self):
# 		for i in range(self.n):
# 			self.tree[self.m  + i] = [self.arr[i], 1]
# 		for i in range(self.m - 1, 0, -1):
# 			if self.tree[i << 1][0] == self.tree[i << 1 | 1][0]:
# 				count = self.tree[i << 1][1] + self.tree[i << 1 | 1][1]
# 				self.tree[i] = [self.tree[i << 1][0], count]
# 			elif self.tree[i << 1][0] < self.tree[i << 1 | 1][0]:
# 				self.tree[i] = [self.tree[i << 1][0], self.tree[i << 1][1]]
# 			else:
# 				self.tree[i] = [self.tree[i << 1 | 1][0], self.tree[i << 1 | 1][1]]

# 	def update(self, node, value):
# 		self.tree[node + self.m] = [value, 1]
# 		i = node + self.m
# 		while i > 1:
# 			if self.tree[i][0] == self.tree[i ^ 1][0]:
# 				count = self.tree[i][1] + self.tree[i ^ 1][1]
# 				self.tree[i >> 1] = [self.tree[i][0], count]
# 			elif self.tree[i][0] < self.tree[i ^ 1][0]:
# 				self.tree[i >> 1] = [self.tree[i][0], self.tree[i][1]]
# 			else:
# 				self.tree[i >> 1] = [self.tree[i ^ 1][0], self.tree[i ^ 1][1]]
# 			i >>= 1

# 	def query(self, l, r):
# 		l += self.m
# 		r += self.m
# 		inf = float('inf')
# 		ans = inf
# 		while l < r:
# 			if l & 1:
# 				if self.tree[l][0] < ans:
# 					count = self.tree[l][1]
# 				elif self.tree[l][0] == ans:
# 					count += self.tree[l][1]
# 				ans = min(ans, self.tree[l][0])
# 				l += 1

# 			if r & 1:
# 				r -= 1
# 				if self.tree[r][0] < ans:
# 					count = self.tree[r][1]
# 				elif self.tree[r][0] == ans:
# 					count += self.tree[r][1]
# 				ans = min(ans, self.tree[r][0])
# 			l >>= 1
# 			r >>= 1
# 		return ans, count

# Segment with maximum sum
from collections import Counter
import math
class SegTree:
	def __init__(self, arr):
		self.m = 2**math.ceil(math.log2(len(arr)))
		inf = float('inf')
		self.arr = arr
		self.tree = [inf]*(2*self.m)
		self.n = len(arr)
		self.build()

	def build(self):
		for i in range(self.n):
			self.tree[self.m + i] = arr[i]
		for i in range(self.m - 1, 0, -1):
			self.tree[i] = self.tree[i << 1] + self.tree[i << 1 | 1]


	def update(self, node, value):
		self.tree[node + self.m] = value
		i = node + self.m
		while i > 1:
			self.tree[i >> 1] = self.tree[i] + self.tree[i ^ 1]
			i >>= 1

	def query(self, l, r):
		l += self.m
		r += self.m
		ans = 0
		while l < r:
			if l & 1:
				ans += self.tree[l]
				l += 1

			if r & 1:
				r -= 1
				ans += self.tree[r]
			l >>= 1
			r >>= 1
		return ans

n, m = map(int, input().split())
arr = list(map(int, input().split()))
st = SegTree(arr)
for _ in range(m):
	a, b, c = map(int, input().split())
	if a == 1:
		st.update(b, c)
	else:
		print(st.query(b, c))


import math
class SegTree:
    """
    A segment tree that can solve range queries for both sums and max values in a range of [l,r)
    """
    def __init__(self,arr):
        # Building the size of the leaf of the segment tree, it is always a base 2 values so 2*i is the size of the base of
        # the tree.
        self.m=2**math.ceil(math.log2(len(arr)))
        inf=float('inf')
        self.arr=arr
        # The size of the actual tree will be 2 times the base size.
        self.tree_sum=[0]*(2*self.m)
        self.tree_max=[-inf]*(2*self.m)
        self.n=len(arr)
        self.build_sum()
        self.build_max()
        
    def build_sum(self):
        # filling in the base of the segment tree
        for i in range(self.n):
            self.tree_sum[self.m+i]=self.arr[i]
        # filling in the rest of the segment tree by working backwards from the base.  
        # i<<1|1 is a trick to get the odd value. cause i<<1 is multiply by 2 and then |1 will turn on the 1 bit 
        # thus making it odd. 
        for i in range(self.m-1,0,-1):
            self.tree_sum[i]=self.tree_sum[i<<1]+self.tree_sum[i<<1|1]
        
    def build_max(self):
        # filling in the base of the segment tree
        for i in range(self.n):
            self.tree_max[self.m+i]=self.arr[i]
        # filling in the rest of the segment tree by working backwards from the base.  
        # i<<1|1 is a trick to get the odd value. cause i<<1 is multiply by 2 and then |1 will turn on the 1 bit 
        # thus making it odd. 
        for i in range(self.m-1,0,-1):
            self.tree_max[i]=max(self.tree_max[i<<1],self.tree_max[i<<1|1])
    
    # Note that the r or right point in the range that is queried is exclusive, thus not included. 
    def query_sum(self,l,r):
        """
        Args:
            l(int): left point of range
            r(int): right point of range
        Return:
            int:  The sum in the given range beteen [l,r) 
        """
        l+=self.m
        r+=self.m
        ans=0
        while l<r:
            if l&1:
                ans+=self.tree_sum[l]
                l+=1
            if r&1:
                r-=1
                ans+=self.tree_sum[r]
            l>>=1
            r>>=1
        return ans
    
    def query_max(self,l,r):
        """
        Args:
            l(int): left point of range
            r(int): right point of range
        Return:
            int:  The sum in the given range beteen [l,r) 
        """
        l+=self.m
        r+=self.m
        inf=float('inf')
        ans=-inf
        while l<r:
            if l&1:
                ans=max(ans,self.tree_max[l])
                l+=1
            if r&1:
                r-=1
                ans=max(ans,self.tree_max[r])
            l>>=1
            r>>=1
        return ans
    
class Solution:
    def minCost(self, s,cost):
        left=0
        ans=0
        st=SegTree(cost)
        for i,ch in enumerate(s):
            if ch!=s[left]:
                if i-1>left:
                    su=st.query_sum(left,i)
                    ma=st.query_max(left,i)
                    ans+=(su-ma)
                left=i
        right=len(s)
        if right>left:
            su=st.query_sum(left,right)
            ma=st.query_max(left,right)
            ans+=(su-ma)
        return ans