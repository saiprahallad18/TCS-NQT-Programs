arr = [2,1,5,1,3,2]
k = 3
n = len(arr)

window_sum = 0
for i in range(k):
    window_sum += arr[i]

max_sum = window_sum
for i in range(k,n):
    window_sum = window_sum + arr[i] - arr[i-k]
    if window_sum > max_sum:
        max_sum = window_sum
print(max_sum)