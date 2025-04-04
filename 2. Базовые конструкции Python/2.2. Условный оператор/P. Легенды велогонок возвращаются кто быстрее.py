p, v, t = int(input()), int(input()), int(input())
a, b, c = p, v, t
if a > b:
    a, b = b, a
if b > c:
    b, c = c, b
if a > b:
    a, b = b, a
if (c, b, a) == (p, v, t):
    n1, n2, n3 = 'Петя', 'Вася', 'Толя'
elif (c, b, a) == (p, t, v):
    n1, n2, n3 = 'Петя', 'Толя', 'Вася'
elif (c, b, a) == (t, p, v):
    n1, n2, n3 = 'Толя', 'Петя', 'Вася'
elif (c, b, a) == (t, v, p):
    n1, n2, n3 = 'Толя', 'Вася', 'Петя'
elif (c, b, a) == (v, p, t):
    n1, n2, n3 = 'Вася', 'Петя', 'Толя'
else:
    n1, n2, n3 = 'Вася', 'Толя', 'Петя'
print(' ' * 8 + f'{n1:^8}')
print(f'{n2:^8}')
print(' ' * 16 + f'{n3:^8}')
print(f'{'II':^8}' + f'{'I':^8}' + f'{'III':^8}')
