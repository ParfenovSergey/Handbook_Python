result = 0
for i in range(int(input())):
    tmp = 0
    n = int(input())
    while n:
        tmp = max(tmp, n % 10)
        n //= 10
    else:
        result = result * 10 + tmp
else:
    print(result)
