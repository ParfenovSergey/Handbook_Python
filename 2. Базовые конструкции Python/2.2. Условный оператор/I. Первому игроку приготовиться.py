n1, n2, n3 = input(), input(), input()
a, b, c = n1, n2, n3
if a > b:
    a, b = b, a
if b > c:
    b, c = c, b
if a > b:
    a, b = b, a
m = a
print(n1 if m == n1 else n2 if m == n2 else n3)
