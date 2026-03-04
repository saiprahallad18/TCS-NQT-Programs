arr = [2,0,1,2,0]
n = len(arr)

for i in range(n):
    for j in range (i+1 , n):
        if arr[i] > arr[j]:
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp
print(arr)
