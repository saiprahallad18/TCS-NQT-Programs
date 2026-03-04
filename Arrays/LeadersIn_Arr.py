arr = [16,17,4,3,5,2]

n = len(arr)
max_right = arr[n-1]

print(max_right)
for i in range(n-2,-1,-1):
    if arr[i] > max_right:
        max_right = arr[i]
        print(max_right)