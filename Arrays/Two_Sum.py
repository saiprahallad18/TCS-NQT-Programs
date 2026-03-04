# (Find two numbers whose sum = target)
arr = [2,7,11,15]
target = 9

n = len(arr)

for i in range(n):
    for j in range(i+1, n):
        if arr[i] + arr[j] == target:
            print(f"{arr[i]} + {arr[j]} = {target}")