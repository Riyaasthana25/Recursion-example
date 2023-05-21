def reverselist(arr, start, end):
	if start >= end:
		return
	arr[start], arr[end] = arr[end], arr[start]
	reverselist(arr, start+1, end-1)
	
arr= list(input("Enter array:"))
reverselist(arr, 0, len(arr)-1)
print(arr)
