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

"""
A problem on leetcode that shows good use of bisect module for a binary search, 
and the case of FFFFFTTTT
https://leetcode.com/problems/find-right-interval/

"""
def findRightInterval(self, intervals):
	"""
	This is for a binary search problem that is FFFFTTT, and returns the first occurrence of T.
	This is using the bisect module. 
	"""
    start_sorted=sorted((v[0],i) for i,v in enumerate(intervals))
    ans=[]
    for i,v in enumerate(intervals):
        left_index=bisect.bisect_left(start_sorted,(v[1],))
        ans.append(start_sorted[left_index][1] if left_index<len(intervals) else -1)
    return ans

"""

"""

def findRightInterval(self, intervals):
	"""
	This is for a binary search problem that is FFFFTTT, and returns the first occurrence of T.
	This is using binary search algorithm. 
	"""
    start_sorted=sorted((v[0],i) for i,v in enumerate(intervals))
    start_sorted+=[(float('inf'),len(intervals))]
    def possible(val,target):
        return start_sorted[val][0]>=target
    def binary_search(target):
        lo,hi=0,len(intervals)
        while lo < hi:
            mid = lo+hi>>1
            if not possible(mid,target):
                lo=mid+1
            else:
                hi=mid
        return lo
    ans=[]
    for s,e in intervals:
        left_index=binary_search(e)
        ans.append(start_sorted[left_index][1] if left_index<len(intervals) else -1)
    return ans

"""
Case #2 is basically if you have TTTTFFFF instead and you want to return the last true statement

"""

"""
Dialogue:
So what is the main two types of binary search problems to know.  There is basic idea, 
So consider the problem with the magnetic force between two balls. 
In this problem you know you are given positions and a specific number of balls.  
then with a given force you check how many balls you can have in the available positions. 
then if the number of balls is greater it is True
so we say for this monotonically decreaseing function simply because as force increases the number of balls
decreases.
So we have that , at this force we have 10,8,6,5,3,2,1
and maybe m=3,  so we need to use at least 3 balls so to say it is possible.  
notice it is true if the number of balls placed is greater than the cutoff,  so I think this will give an array of 
TTTTFFF, so we want to return the first occurrence of T scanning from hi to lo or in other words
return the last occurrence of T from lo to hi scan. 
Depending which direction relative you scan from. 

What is the other occurrence I would say it is this switch these around and consider
FFFTTTT, now the goal is to return the first occurence of T when scanning from lo to hi

So binary search can be broken down into basically two templates is what I learned by studying Alex.  
So think about this it is either TTTTTFFF or FFFFTTTT.  and you need to always return the first or last occurence of T. 
Another way to think once of these is in terms of bisect module as well.  
I will implement that afterwards to reduce my work but I need to make sure I understand the general principle of binary search first though.



"""

if __name__=='__main__':
	A=[2, 3, 4, 4, 5, 8, 12, 36, 36, 36, 85, 89, 96]
	print(find_left(5,A))
	print(find_left(7,A))
	print(find_right(36,A))
	print(find_right(13,A))
	print(find_leftmost(36,A))
	print(find_leftmost(1,A))
	print(find_leftmost(97,A))
