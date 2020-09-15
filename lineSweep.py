"""
https://www.topcoder.com/community/competitive-programming/tutorials/line-sweep-algorithms/
Learning about the line sweep algorithm
https://discuss.codechef.com/t/sweep-line-algorithm/1474/2

There can be some variations of line sweep.  For instance if finding the area of union of rectangles you can use a horizontal and vertical 
line sweep.  

Below is a vary basic implementation of line sweep to merge intervals.  Since we normally need to sort for a line sweep algorithm it has
a time complexity of O(nlog(n)). 
https://leetcode.com/problems/merge-intervals/
"""
def vertical_line_sweep(A):
	"""
	This uses a vertical line to sweep across events to merge overlapping intervals into an interval.
	
	Args:
		A(list[list]):  The list containing intervals [start,end].
	Return:
		list[list]:  Returns all the intervals with merging of overlapping intervals. 
	"""
    events=[]
    for s,e in A:
        events.append((s,1))
        events.append((e,-1))
    count=0
    B=[]
    events.sort(key=lambda x: [x[0],-x[1]])
    for event, inc in events:
        count+=inc
        if count==1 and inc==1:
            start=event
        if count==0 and inc==-1:
            B.append([start,event])
            start=None
    return B
