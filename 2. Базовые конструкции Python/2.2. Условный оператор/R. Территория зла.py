a, b, c = int(input()), int(input()), int(input())
if a > b:
    a, b = b, a
if b > c:
    b, c = c, b
if a > b:
    a, b = b, a
if a ** 2 + b ** 2 == c ** 2:
    print('100%')
elif a ** 2 + b ** 2 > c ** 2:
    print('крайне мала')
else:
    print('велика')
