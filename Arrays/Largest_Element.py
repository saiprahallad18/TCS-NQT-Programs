def largestElement(arr):
    largest = arr[0]
    for i in range(len(arr)):
        if arr[i] > largest:
            largest = arr[i]
    return largest
arr = [3,2,1,5,2]
print(largestElement(arr))