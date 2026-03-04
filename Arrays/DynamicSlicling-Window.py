arr = [2,3,1,2,4,3]
target = 7

left = 0
current_sum = 0
min_length = len(arr) + 1

for right in range(len(arr)):
    current_sum += arr[right]

    while current_sum >= target:
        window_length = right - left + 1
        if window_length < min_length:
            min_length = window_length

        current_sum -= arr[left]
        left += 1
if min_length == len(arr) + 1:
    print("No subarray found")
else:
    print("Minimum length:", min_length)