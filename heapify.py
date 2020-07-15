"""
Implementation of reheapify for a min-heap with integer array representation.
"""
def reheapify(arr):
	n = len(arr)
	while 2*i + 1 < n:
		i += 1
	j = i - 1
	while j >= 0:
		if arr[2*j + 1] < arr[j]:
			arr[j], arr[2*j + 1] = arr[2*j + 1], arr[j]
		if arr[2*j + 2] < arr[j]:
			arr[j], arr[2*j + 2] = arr[2*j + 2], arr[j]
		j -= 1

"""

"""