matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

n = len(matrix)

#Transpose
for i in range(n):
    for j in range(i,n):
        temp = matrix[i][j]
        matrix[i][j] = matrix[j][i]
        matrix[j][i] = temp

# Reverse of rows
for i in range(n):
    left = 0
    right = n-1

    while left < right:
        temp = matrix[i][left]
        matrix[i][left] = matrix[i][right]
        matrix[i][right] = temp

        left += 1
        right -= 1
#  to Print matrix
for i in range(n):
    for j in range(n):
        print(matrix[i][j], end=" ")
    print()