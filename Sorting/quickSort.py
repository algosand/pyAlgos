"""
Quick Sort Algorithm
Method1:  Choose the last element to be the pivot

"""
def main(arr):
	quickSort(arr, 0, len(arr) - 1)
	return arr

def quickSort(arr, left, right):
	if left >= right:
		return
	pivot = partition(arr, left, right)
	quickSort(arr, left, pivot - 1)
	quickSort(arr, pivot + 1, right)
	return arr

def partition(arr, left, right):
	i = left
	val = arr[right]
	for j in range(left, right):
		if arr[j] < val:
			arr[i], arr[j] = arr[j], arr[i]
			i += 1
	arr[i], arr[right] = arr[right], arr[i]
	return i

"""
Method2:  Optimize, find the optimal pivot point. 
"""