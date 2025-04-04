n = int(input())
n1 = n // 1000 % 10
n2 = n // 100 % 10
n3 = n // 10 % 10
n4 = n // 1 % 10
print('YES' if n1 == n4 and n2 == n3 else 'NO')
