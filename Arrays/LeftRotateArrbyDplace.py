# left rotate arr by D place
def rotate_left(arr, d):
    n = len(arr)
    if n == 0:
        return arr
    
    d = d % n 
    
    def reverse(start, end):
        while start < end:
            arr[start], arr[end] = arr[end], arr[start]
            start += 1
            end -= 1
    reverse(0, d-1)
    reverse(d, n-1)
    reverse(0, n-1)
    return arr
arr = [7,5,2,11,2,23,4,1,1]
d=3
print(rotate_left(arr, d))