n = int(input())
a = int(input())
for i in range(n - 1):
    b = int(input())
    while b:
        a, b = b, a % b
else:
    print(a)
