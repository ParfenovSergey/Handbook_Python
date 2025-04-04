p, v, t = int(input()), int(input()), int(input())
a, b, c = p, v, t
if a > b:
    a, b = b, a
if b > c:
    b, c = c, b
if a > b:
    a, b = b, a
m = c
print('Петя' if m == p else 'Вася' if m == v else 'Толя')
