"""
Implementation of bubble sort.

arr = [1,2,3,5,6]
           i
first pass: iterate to i = 3
second pass: iterate to i = 2
third pass: iterate to i = 1
fourth pass iterate to i = 0
if no swaps made in an iteration sorting is complete so just stop.

"""

def bubbleSort(arr):
	j = len(arr) - 1
	while j > 0:
		swap = False
		for i in range(j):
			if arr[i + 1] < arr[i]:
				arr[i], arr[i + 1] = arr[i + 1], arr[i]
				swap = True
		if not swap:
			break
		j -= 1
	return arr




import random
if __name__ == "__main__":
	a = list(range(10000))
	random.shuffle(a)
	print(bubbleSort(a))
	b = [1,2,4,5,6,7,8]
	random.shuffle(b)
	print(bubbleSort(b))
