

def func(arr, l, r):
	if r < l:
		return 1e9
	ans = arr[l]
	for i in range(l + 1, r + 1):
		ans &= arr[i]
	return ans



if __name__ == '__main__':
	arr = [9,12,3,7,15]
	print(func(arr, 0, 1))

	arr = [1000000,1000000,1000000]
	print(func(arr, 0, 2))

	arr = [1,2,4,8,16]
	print(func(arr, 0, 1))	