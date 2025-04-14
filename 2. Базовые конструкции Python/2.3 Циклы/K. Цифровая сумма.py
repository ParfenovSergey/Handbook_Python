n = int(input())
result = 0
while n:
    result += n % 10
    n //= 10
else:
    print(result)
