n = int(input())
n1, n2, n3 = n // 100 % 10, n // 10 % 10, n // 1 % 10
a, b = n1 + n2, n2 + n3
if a > b:
    a, b = b, a
print(f'{b}{a}')
