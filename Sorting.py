
def bub_sort(arr):
	for i in range(len(arr)):
		for j in range(i):
			if arr[i] < arr[j]:
				arr[i], arr[j] = arr[j], arr[i]
	return arr


ARR = [9, 1, 7, 0, 3, 5, 4, 6, 8, 2]


print("Original - ", ARR)
print("bub_sort - ", bub_sort(ARR))

ARR.sort()
print("sort     - ", ARR)
