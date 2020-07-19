"""
Implementation of heapify for a min-heap with integer array representation.
For max heap switch the smallest for the largest and switch the comparison operators. 
"""
def heapify(arr, i):
	n = len(arr)
	smallest = i
	sval = arr[i]
	if 2*i + 1 < n:
		left = arr[2*i + 1]
		if left < arr[i]:
			smallest = 2*i + 1
			sval = left
	if 2*i + 2 < n:
		right = arr[2*i + 2]
		if right < sval:
			smallest = 2*i + 2
			sval = right
	if smallest != i:
		arr[i], arr[smallest] = arr[smallest], arr[i]
		heapify(arr, smallest)


def buildMinHeap(arr):
	n = len(arr)
	lastLevel = n // 2
	for i in range(lastLevel, -1, -1):
		heapify(arr, i)

	return arr

"""

"""

if __name__ == '__main__':
	arr = [5,2,3,6,7,9,10,1]
	mh = buildMinHeap(arr)
	print(mh)
	arr = [1, 3, 5, 4, 6, 13, 10, 9, 8, 15, 17]
	ms = buildMinHeap(arr)
	print(ms)