"""
Implementation of fenwick trees or Binary Indexed Tree (BIT)
"""

class NumArray:

    def __init__(self, num):
    	self.arr = num

    def update(self, i, val):
        

    def sumRange(self, i, j):
        

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




if __name__ == '__main__':
	