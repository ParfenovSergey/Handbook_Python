n = int(input())
max_n = 0
while n:
    max_n = max(n % 10, max_n)
    n //= 10
else:
    print(max_n)
