
def insertion_sort(arr):

	for i in range(1,len(arr)):
		for j in range(i):
			if arr[j]>arr[i]:
				arr[i],arr[j] = arr[j],arr[i]

	return arr



arr = [2,1,5,4,3,9,8]
print(arr)
sorted_array = insertion_sort(arr)


print(sorted_array)
