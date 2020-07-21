"""
Implementation of fenwick trees or Binary Indexed Tree (BIT)
"""

class NumArray:

    def __init__(self, num):
        if not num:
            return
        self.arr = num
        self.bit = [0] + num
        for i in range(1, len(self.bit)):
            j = i + (i & -i)
            if j < len(self.bit):
                self.bit[j] += self.bit[i]
        

    def update(self, i, val):
        inc = val - self.arr[i]
        self.arr[i] = val
        i += 1
        while i < len(self.bit):
            self.bit[i] += inc
            i += (i & -i)
            
    def prefixSum(self, i):
        res = 0
        while i:
            res += self.bit[i]
            i -= (i & -i)
        return res
        
    def sumRange(self, i, j):
        return self.prefixSum(j + 1) - self.prefixSum(i)


if __name__ == '__main__':
	arr = NumArray([-1])
	print(arr.sumRange(0,0))
	arr.update(0, 1)
	print(arr.sumRange(0,0))


"""
start time: 6:46PM
approach1: prefix sum array

[1,3,5]
[1,4,9]
sum(i, j) = arr[j] - arr[i] = arr[2] - arr[1] = 9 - 1 = 8
arr[2] - arr[1] = 0

i = 0 to i = 2
arr[2] 
i = 1 to i = 2 
arr[2] - arr[0] = 8
i = 1 to i = 2
arr[2] - arr[1] = 5

- generate the prefix sum array O(n)
- update regenerate the prefix sum array O(1)
- sum Range will just use the prefix array so it will be O(1)

- use binary representation


"""



