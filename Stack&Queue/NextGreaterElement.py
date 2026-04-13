arr = [4,5,2,10,8]
n = len(arr)
stack = []
result = [-1] * n

for i in range(n):
    while len(stack) > 0 and arr[stack[-1]] < arr[i]:
        index = stack.pop()
        result[index] = arr[i]

    stack.append(i)

for r in result:
    print(r, end=" ")