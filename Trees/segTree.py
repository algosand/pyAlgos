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


'''
Improved segment tree implementation to try out 
'''


class SegTree:
    def __init__(self, n, combine):
        self.n = n
        self._tree = [0] * (n * 4)
        self._combine = combine

    @staticmethod
    def from_list(a, combine):
        n = len(a)
        tree = SegTree(n, combine)
        tree._build(a, 1, 0, n - 1)
        return tree

    def _build(self, a, v, tl, tr):
        if tl == tr:
            self._tree[v] = a[tl]
        else:
            tm = (tl + tr) // 2
            self._build(a, v * 2, tl, tm)
            self._build(a, v * 2 + 1, tm + 1, tr)
            self._tree[v] = self._combine(
                self._tree[v * 2], self._tree[v * 2 + 1])

    def query(self, l, r):
        return self._query(1, 0, self.n - 1, l, r)

    def _query(self, v, tl, tr, l, r):
        if l > r:
            return 0
        if l == tl and r == tr:
            return self._tree[v]
        tm = (tl + tr) // 2
        return self._combine(
            self._query(v * 2, tl, tm, l, min(r, tm)),
            self._query(v * 2 + 1, tm + 1, tr, max(l, tm + 1), r),
        )

    def update(self, pos, new_val):
        self._update(1, 0, self.n - 1, pos, new_val)

    def _update(self, v, tl, tr, pos, new_val):
        if tl == tr:
            self._tree[v] = new_val
        else:
            tm = (tl + tr) // 2
            if pos <= tm:
                self._update(v * 2, tl, tm, pos, new_val)
            else:
                self._update(v * 2 + 1, tm + 1, tr, pos, new_val)
            self._tree[v] = self._combine(
                self._tree[v * 2], self._tree[v * 2 + 1])


# insert any function you like here
tree = SegTree.from_list([6, 3, 8, 9, 4, 16, 12], math.gcd)


if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5, 6, 7, 8]
    st = SegTree(arr)
    print(st.query(0, 8))
    print(st.query(3, 6))
    st.update(4, 0)
    print(st.query(0, 8))
    print(st.query(3, 6))
