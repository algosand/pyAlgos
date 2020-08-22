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