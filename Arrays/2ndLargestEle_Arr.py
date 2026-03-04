def second_largest(arr):
    if len(arr) < 2:
        return None
    largest = arr[0]
    second = None
    
    for num in arr:
        if num > largest:
            second = largest
            largest = num
        elif num != largest and (second is None or num > second):
            second = num
    return second
arr = [10,5,8,20,15]
print(second_largest(arr))