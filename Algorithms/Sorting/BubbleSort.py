def BubbleSort(arr):

	for i in arr:
		for j in range(len(arr)-1):
			if arr[j] > arr[j+1]:
				arr[j],arr[j+1] = arr[j+1],arr[j]

	return arr





list = [23,34,13,45,61,82]

print(BubbleSort(list))