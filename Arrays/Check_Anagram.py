s1 = [1,2,3]
s2 = [3,2,1]

if len(s1) != len(s2):
    print("Not anagram")
else:
    count = 0
    for i in range(len(s1)):
        for j in range(len(s2)):
            if s1[i] == s2[j]:
                count += 1
                break
    if count == len(s1):
        print("Anagram")
    else:
        print("Not anagram")