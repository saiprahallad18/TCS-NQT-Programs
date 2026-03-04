matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

rows = len(matrix)
cols = len(matrix[0])

top = 0
bottom = rows - 1
left = 0
right = cols - 1

while top <= bottom and left <= right:

    # top row
    for i in range(left, right+1):
        print(matrix[top][i], end=" ")
    top += 1
    # right column
    for i in range(top, bottom+1):
        print(matrix[i][right], end=" ")
    right -= 1
    # bottom row
    if top <= bottom:
        for i in range(right, left-1, -1):
            print(matrix[bottom][i], end=" ")
        bottom -= 1
    # left column
    if left <= right:
        for i in range(bottom, top-1, -1):
            print(matrix[i][left], end=" ")
        left += 1