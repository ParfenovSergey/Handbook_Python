number = int(input())
a = number // 100 % 10
b = number // 10 % 10
c = number // 1 % 10
if a > b:
    a, b = b, a
if b > c:
    b, c = c, b
if a > b:
    a, b = b, a
print('YES' if a + c == 2 * b else 'NO')
