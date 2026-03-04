s = "programming"
vowels = 0
consonants = 0

for i in s:
    if i=='a' or i=='e' or i=='i' or i=='o' or i=='u':
        vowels += 1
    else:
        consonants += 1
print("Vowels:",vowels)
print("Consonants:",consonants)