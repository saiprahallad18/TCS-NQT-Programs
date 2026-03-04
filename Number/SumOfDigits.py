n = 1234
sum_val = 0

while n > 0:
    digit = n % 10
    sum_val += digit
    n = n // 10

print(sum_val)