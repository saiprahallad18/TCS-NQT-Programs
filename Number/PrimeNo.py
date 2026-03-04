n = 4
flag = True

for i in range(2, n):
    if n % i == 0:
        flag = False
        break
if flag and n > 1:
    print("Prime")
else:
    print("Not Prime")