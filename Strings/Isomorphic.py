# Two strings are isomorphic if characters in the first string can be mapped uniquely to characters in the second string
# s1 = "egg"
# s2 = "add"

s1 = "egg"
s2 = "add"

if len(s1) != len(s2):
    print("Not Isomorphic")
else:
    flag = True
    for i in range(len(s1)):
        for j in range(i+1,len(s1)):
            if s1[i] == s1[j] and s2[i] != s2[j]:
                flag = False
            if s1[i] != s1[j] and s2[i] == s2[j]:
                flag = False
    if flag:
        print("Isomorphic")
    else:
        print("Not Isomorphic")