n = 6
sum = 0

for i in range(1, n):
    if n % i == 0:
        sum += i
if sum == n:
    print("Perfect")
else:
    print("Not Perfect")
# 6 = 1 + 2 + 3