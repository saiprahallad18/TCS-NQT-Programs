s = "abcdef"
k = 2
result = ""

# print from k to end
for i in range(k,len(s)):
    result = result + s[i]

# print first k char
for i in range(k):
    result = result + s[i]
print(result)