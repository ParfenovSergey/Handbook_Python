n1 = int(input())
n2 = int(input())
a = n1 // 10 % 10
b = n1 // 1 % 10
c = n2 // 10 % 10
d = n2 // 1 % 10
if a > b:
    a, b = b, a
if b > c:
    b, c = c, b
if c > d:
    c, d = d, c
if a > b:
    a, b = b, a
if b > c:
    b, c = c, b
if a > b:
    a, b = b, a
print(f'{d}{(b + c) % 10}{a}')
