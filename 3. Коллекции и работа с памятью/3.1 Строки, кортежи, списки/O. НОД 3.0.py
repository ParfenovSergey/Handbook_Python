numbers = input().split()
a = int(numbers[0])
for i in numbers[1:]:
    b = int(i)
    while b:
        a, b = b, a % b
else:
    print(a)
