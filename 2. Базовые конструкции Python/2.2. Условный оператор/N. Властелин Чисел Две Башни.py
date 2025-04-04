n = int(input())
a = n // 100 % 10
b = n // 10 % 10
c = n // 1 % 10
if a > b:
    a, b = b, a
if b > c:
    b, c = c, b
if a > b:
    a, b = b, a
if a != 0:
    print(f'{a}{b} {c}{b}')
elif b != 0:
    print(f'{b}{a} {c}{b}')
else:
    print(f'{c}{a} {c}{b}')
