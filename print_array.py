def printarray(arr,i,n):
    if(i>=n):
        return
    print(arr[i],end=" ")
    printarray(arr,i+1,n)
arr= list(input("Enter array:"))
n = len(arr)
printarray(arr,0,n)
