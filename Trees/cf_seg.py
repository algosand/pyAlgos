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