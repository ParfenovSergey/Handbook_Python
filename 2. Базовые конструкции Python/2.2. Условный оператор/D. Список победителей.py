p, v, t = int(input()), int(input()), int(input())
a, b, c = p, v, t
if a > b:
    a, b = b, a
if b > c:
    b, c = c, b
if a > b:
    a, b = b, a
if (c, b, a) == (p, v, t):
    print('1. Петя\n2. Вася\n3. Толя')
elif (c, b, a) == (p, t, v):
    print('1. Петя\n2. Толя\n3. Вася')
elif (c, b, a) == (t, p, v):
    print('1. Толя\n2. Петя\n3. Вася')
elif (c, b, a) == (t, v, p):
    print('1. Толя\n2. Вася\n3. Петя')
elif (c, b, a) == (v, p, t):
    print('1. Вася\n2. Петя\n3. Толя')
else:
    print('1. Вася\n2. Толя\n3. Петя')
