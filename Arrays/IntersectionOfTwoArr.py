arr1 = [1,2,3,4]
arr2 = [2,4,6]

for i in range(len(arr1)):
    for j in range(len(arr2)):
        if arr1[i] == arr2[j]:
            print(arr1[i])

# Compare each element of first array with second array,
# If equal = print common element