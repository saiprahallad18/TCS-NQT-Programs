s1 = "listen"
s2 = "silent"
if len(s1) != len(s2):
    print("Not Anagram")
else:
    visited = ""
    flag = 1
    for i in range(len(s1)):
        if s1[i] not in visited:
            count1 = 0
            count2 = 0
            for j in range(len(s1)):
                if s1[i] == s1[j]:
                    count1 += 1
            for j in range(len(s2)):
                if s1[i] == s2[j]:
                    count2 += 1
            if count1 != count2:
                flag = 0
                break
            visited = visited + s1[i]
    if flag == 1:
        print("Anagram")
    else:
        print("Not Anagram")