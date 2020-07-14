"""
Implementation of merge sort for an array
split
merge

"""
def mergeSort(arr):
	if len(arr) == 1:
		return arr
	n = len(arr)
	mid = n >> 1
	sorted1 = mergeSort(arr[:mid])
	sorted2 = mergeSort(arr[mid:])
	return merge(sorted1, sorted2)


def merge(a, b):
	merged = []
	na, nb = len(a), len(b)
	i, j = 0, 0
	while i < na or j < nb:
		if i == na:
			merged.append(b[j])
			j += 1
		elif j == nb:
			merged.append(a[i])
			i += 1
		elif a[i] < b[j]:
			merged.append(a[i])
			i += 1
		else:
			merged.append(b[j])
			j += 1
	return merged

"""
Implementation of merge sort for a linked list

"""	
# def mergeSortL(LL):


# Some random tests for running the program. 
import random
if __name__ == '__main__':
	arr = [1,2,3,4,5,6,7,8]
	random.shuffle(arr)
	marr = mergeSort(arr)
	print(marr)
	a = [1,2,3,4,5,6]
	random.shuffle(a)
	ma = mergeSort(a)
	print(ma)
	b = [1,2,3,4,5]
	random.shuffle(b)
	mb = mergeSort(b)
	print(mb)
