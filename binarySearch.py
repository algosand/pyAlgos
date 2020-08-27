"""
Binary Search for a function where you want to return the last possible value for when it is true. 
In a sense returning the max value for when it is true.
so the max value for f(x) for when it is true
Note also this specifically works for if f is a monotonically decreasing function
so between option
x=2 and x=3, if x=2 is true and x=3 is true, we want to return 3 
"""
def bst():
	lo, hi=1,P[-1]-P[0]
	while lo<hi:
	    mid=(lo+hi+1)>>1
	    if f(mid)>=m:
	        lo=mid
	    else:
	        hi=mid-1
	return lo

"""
From my research up to this point.  It seems there are only two binary search templates that are necessary to solve any
problem that can be solved with binary search algorithm.
There is the mid=lo+hi+1 >> 1 or the mid=lo+hi >> 1

1) mid=lo+hi+1 >> 1
for when you want the first true statement from hi to lo.
Example)
Solve a problem that asks to find the min of a max.  Somewhat like if you have a monotonic decreasing function
which is false at some cutoff, but you want to find the first value before the function became false or in other words
passed a certain threshold.  
2) mid=lo+hi >> 1
for when you want the first true statement from lo to hi. 

"""

"""
Binary search with the bisect module in python:  
https://www.tutorialspoint.com/bisect-array-bisection-algorithm-in-python
https://www.tutorialspoint.com/binary-search-bisect-in-python
"""

"""
Binary search with bisect_left to find the first occurrence when scanning from the lo to hi. 
"""

import bisect
def find_left(x,A):
	index=bisect.bisect_left(A,x)
	if 0<=index<len(A) and A[index]==x:
		return index
	else:
		return -1

"""
Finding the greatest value that is smaller than x, in this case it is like scanning from the lo to hi, and returning the smallest
value.  I guess it is like a binary search. 
"""
def find_leftmost(x,A):
	index=bisect.bisect_left(A,x)
	if index
		return index-1
	else:
		return -1

"""
Finding the last occurrence of x so the rightmost x. 
"""
def find_right(x,A):
	index=bisect.bisect(A,x)
	if 0<=index<=len(A) and A[index-1]==x:
		return index-1
	else:
		return -1

if __name__=='__main__':
	A=[2, 3, 4, 4, 5, 8, 12, 36, 36, 36, 85, 89, 96]
	print(find_left(5,A))
	print(find_left(7,A))
	print(find_right(36,A))
	print(find_right(13,A))
	print(find_leftmost(36,A))
	print(find_leftmost(1,A))
	print(find_leftmost(97,A))
