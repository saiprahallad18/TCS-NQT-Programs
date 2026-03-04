def is_sorted(arr):
    for i in range(1, len(arr)):
        if arr[i] < arr[i - 1]:
            return False
    return True
print(is_sorted([1,2,3,4]))
print(is_sorted([1,3,2,4]))
print(is_sorted([1,1,2,3,3]))