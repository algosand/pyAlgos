"""
Implementation of insertion sort. 

"""

def insertionSort(arr):
	for i in range(len(arr)):
		for j in range(1, i + 1)[::-1]:
			if arr[j - 1] < arr[j]:
				break
			arr[j], arr[j - 1] = arr[j - 1], arr[j]
	return arr

"""
a = [1,2,3,5]
           i
         j
"""
import random
if __name__ == '__main__':
	a = list(range(10000))
	random.shuffle(a)
	print(insertionSort(a))
	b = [1,2,4,5,6,7,8]
	random.shuffle(b)
	print(insertionSort(b))