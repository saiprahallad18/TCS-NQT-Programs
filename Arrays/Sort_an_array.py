#1)Bubble Sort
arr = [5,3,8,4,2]
n = len(arr)

for i in range(n):
    for j in range(0,n-i-1):
        if arr[j] > arr[j+1]:
            temp = arr[j]
            arr[j] = arr[j+1]
            arr[j+1] = temp
print(arr)

# 2)Selection Sort
arr = [5,3,8,4,2]
n = len(arr)

for i in range(n):
    min_index = i
    for j in range(i+1,n):
        if arr[j] < arr[min_index]:
            min_index = j
    temp = arr[i]
    arr[i] = arr[min_index]
    arr[min_index] = temp
print(arr)

# 3)Insertion Sort
arr = [5,3,8,4,2]
n = len(arr)

for i in range(1,n):
    key = arr[i]
    j = i-1
    while j >= 0 and arr[j] > key:
        arr[j+1] = arr[j]
        j -= 1
    arr[j+1] = key
print(arr)