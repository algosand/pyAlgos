"""
Implementation of the basic quick select algorithm. 
Example problem: Find the kth smallest element in an array. 
best case O(nlogn), worst case O(n^2)

Another possible problem: Find the kth largest element in an array.  
How would you do that? 
Maybe try sorting in descending order. 
so switch the condition arr[j] < val to arr[j] > val
"""
def kSmallest(arr, k):
	return quickSelect(arr, k, 0, len(arr) - 1)

def kLargest(arr, k):
	return quickSelect2(arr, k, 0, len(arr) - 1)

def quickSelect(arr, k, left, right):
	if left == right:
		return arr[left]
	pivot = partition(arr, left, right)
	if k - 1 == pivot:
		return arr[pivot]
	elif k - 1 < pivot:
		return quickSelect(arr, k, left, pivot - 1)
	else:
		return quickSelect(arr, k, pivot + 1, right)

# For finding the kth smallest element. 
def partition(arr, left, right):
	val = arr[right]
	i = left
	for j in range(left, right):
		if arr[j] < val:
			arr[i], arr[j] = arr[j], arr[i]
			i += 1
	if arr[right] < arr[i]:	
		arr[i], arr[right] = arr[right], arr[i]
	return i

def quickSelect2(arr, k, left, right):
	if left == right:
		return arr[left]
	pivot = partition2(arr, left, right)
	if k - 1 == pivot:
		return arr[pivot]
	elif k - 1 < pivot:
		return quickSelect2(arr, k, left, pivot - 1)
	else:
		return quickSelect2(arr, k, pivot + 1, right)

# For finding the kth largest, partition it in a way that the larger values are on the right
# and smaller values on the left. 
def partition2(arr, left, right):
	val = arr[right]
	i = left
	for j in range(left, right):
		if arr[j] > val:
			arr[i], arr[j] = arr[j], arr[i]
			i += 1
	if arr[right] > arr[i]:	
		arr[i], arr[right] = arr[right], arr[i]
	return i