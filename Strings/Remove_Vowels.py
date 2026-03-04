s = "programming"
result = ""

for i in s:
    if i not in "aeiou":
        result = result + i
print(result)