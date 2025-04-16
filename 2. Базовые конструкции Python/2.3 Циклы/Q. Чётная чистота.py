n = int(input())
result, power = 0, 1
while n:
    if n % 2 != 0:
        result = result + n % 10 * power
        power *= 10
    n //= 10
else:
    print(result)
