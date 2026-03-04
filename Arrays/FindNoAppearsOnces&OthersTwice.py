def single_number(arr):
    result = 0
    for num in arr:
        result ^= num
    return result
arr = [4,1,2,1,2]
print(single_number(arr))