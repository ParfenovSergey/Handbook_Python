n, m = int(input()), int(input())
width = len(str(n * m))
for i in range(n):
    for j in range(m):
        print(f'{n * j + i + 1:>{width}}', end=' ')
    else:
        print()
