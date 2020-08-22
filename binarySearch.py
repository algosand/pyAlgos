"""
Binary Search for a function where you want to return the last possible value for when it is true. 
In a sense returning the max value for when it is true.
so the max value for f(x) for when it is true
Note also this specifically works for if f is a monotonically decreasing function
so between option
x=2 and x=3, if x=2 is true and x=3 is true, we want to return 3 
"""
def bst()
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