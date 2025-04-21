result = 0
for i in range(n := int(input())):
    if input().startswith(('а', 'б', 'в')):
        result += 1
else:
    print('YES' if result == n else 'NO')
