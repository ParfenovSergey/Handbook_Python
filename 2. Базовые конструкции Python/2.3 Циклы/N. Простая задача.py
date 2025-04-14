count = 0
for i in range(2, int((n := int(input())) ** 0.5) + 1):
    if n % i == 0:
        count += 1
else:
    print('YES' if count == 0 and n != 1 else 'NO')
