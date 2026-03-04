n = 99

while n >= 10:
    sum_val = 0
    while n > 0:
        digit = n % 10
        sum_val += digit
        n = n // 10
    n = sum_val
print(n)