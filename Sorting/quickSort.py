"""
Quick Sort Algorithm
Method1:  Choose the last element to be the pivot
worst Case O(n^2), best case O(nlogn)

"""
# def main(arr):
# 	quickSort(arr, 0, len(arr) - 1)
# 	return arr

# def quickSort(arr, left, right):
# 	if left >= right:
# 		return
# 	pivot = partition(arr, left, right)
# 	quickSort(arr, left, pivot - 1)
# 	quickSort(arr, pivot + 1, right)
# 	return arr

# def partition(arr, left, right):
# 	i = left
# 	val = arr[right]
# 	for j in range(left, right):
# 		if arr[j] < val:
# 			arr[i], arr[j] = arr[j], arr[i]
# 			i += 1
# 	arr[i], arr[right] = arr[right], arr[i]
# 	return i
"""
Solve problem with quicksort that has a different comparison condition for sorting. 
"""
# import random
# def absSort(arr):
#   random.shuffle(arr)
#   return quicksort(arr, 0, len(arr) - 1)

# def quicksort(arr, left, right):
#   if left >= right:
#     return
#   pivot = partition(arr, left, right)
#   quicksort(arr, pivot + 1, right)
#   quicksort(arr, left, pivot - 1)
#   return arr

# def partition(arr, left, right):
#   j = left
#   for i in range(left, right):
#     if comparison(arr, i, right):
#       arr[j], arr[i] = arr[i], arr[j]
#       j += 1
#   arr[j], arr[right] = arr[right], arr[j]
#   return j
    

# def comparison(arr, i, j):
#   v, u = arr[i], arr[j]
#   if abs(v) < abs(u):
#     return True
#   elif abs(v) == abs(u) and v < u:
#     return True
#   else:
#     return False


if __name__ == '__main__':
	# arr = [1,2,3,4,5,6]
	# print(absSort(arr))
	print(absSort([2,-7,-2,-2,0]))