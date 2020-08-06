"""
Implementation of a segment tree in python
"""

class SegTree:
	def __init__(self, arr):
		self.n = len(arr)
		self.arr = arr
		self.tree = [0]*2*self.n
		self.build()

	def build(self):
		for i in range(self.n):
			self.tree[self.n + i] = arr[i]
		for i in range(self.n - 1, 0, -1):
			self.tree[i] = self.tree[i << 1] + self.tree[i << 1 | 1]


	def update(self, node, value):
		self.tree[node + self.n] = value
		i = node + self.n
		while i > 1:
			self.tree[i >> 1] = self.tree[i] + self.tree[i ^ 1]
			i >>= 1

	def query(self, l, r):
		l += self.n
		r += self.n
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



if __name__ == '__main__':
	arr = [1,2,3,4,5,6,7,8]
	st = SegTree(arr)
	print(st.query(0, 8))
	print(st.query(3,6))
	st.update(4, 0)
	print(st.query(0,8))
	print(st.query(3,6))