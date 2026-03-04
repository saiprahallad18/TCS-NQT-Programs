A = [[1,2],[3,4]]
B = [[5,6],[7,8]]

rows = len(A)
cols = len(A[0])
result = []

for i in range(rows):
    row = []
    for j in range(cols):
        row.append(A[i][j] + B[i][j])
    result.append(row)
print(result)