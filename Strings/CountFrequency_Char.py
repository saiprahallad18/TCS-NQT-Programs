s = "banana"
visited = ""

for i in range(len(s)):
    if s[i] not in visited:
        count = 1
        for j in range(i+1,len(s)):
            if s[i] == s[j]:
                count += 1
        print(s[i],":",count)
        visited = visited + s[i]