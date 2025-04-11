a, b = int(input()), int(input())
while b:
    a, b = b, a % b
else:
    print(a)
