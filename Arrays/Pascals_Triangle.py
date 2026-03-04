n = 5
triangle = []

for i in range(n):
    row = []
    for j in range(i+1):
        if j == 0 or j == i:
            row.append(1)
        else:
            value = triangle[i-1][j-1] + triangle[i-1][j]
            row.append(value)
    triangle.append(row)

for i in range(n):
    for j in range(len(triangle[i])):
        print(triangle[i][j], end=" ")
    print()