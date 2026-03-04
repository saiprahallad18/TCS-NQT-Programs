n = 153
temp = n
sum = 0

while n > 0:
    digit = n % 10
    sum = sum + digit*digit*digit
    n = n // 10
if sum == temp:
    print("Armstrong")
else:
    print("Not Armstrong")