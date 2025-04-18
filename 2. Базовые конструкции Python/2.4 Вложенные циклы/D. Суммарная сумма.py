result = 0
for i in range(int(input())):
    n = int(input())
    while n:
        result += n % 10
        n //= 10
else:
    print(result)
