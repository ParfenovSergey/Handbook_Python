result = 0
for _ in range(int(input())):
    n = int(input())
    if n < 2:
        continue
    tmp = 0
    for i in range(2, int(n ** 0.5) + 1):
        tmp += 1 * (n % i == 0)
    else:
        result += 1 * (tmp == 0)
else:
    print(result)
