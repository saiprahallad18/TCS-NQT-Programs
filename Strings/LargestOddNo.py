s = "34528"
result = ""

for i in range(len(s)-1, -1, -1):
    digit = int(s[i])
    if digit % 2 == 1:
        for j in range(i+1):
            result = result + s[j]
        break
print(result)