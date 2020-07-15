"""
Implementation of selection sort
"""

def selectionSort(arr):
	for i in range(len(arr)):
		m = i
		for j in range(i + 1, len(arr)):
			if arr[j] < arr[m]:
				m = j
		arr[i], arr[m] = arr[m], arr[i]
	return arr

import random
if __name__ == '__main__':
	a = [1,2,3,4,5,6]
	random.shuffle(a)
	print(selectionSort(a))
	b = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
	random.shuffle(b)
	print(selectionSort(b))
	c = [1, 2]
	random.shuffle(c)
	print(selectionSort(c))
	d = [1]
	print(selectionSort(d))
	e = []
	print(selectionSort(e))
	f = list(range(10000))
	random.shuffle(f)
	print(selectionSort(f))