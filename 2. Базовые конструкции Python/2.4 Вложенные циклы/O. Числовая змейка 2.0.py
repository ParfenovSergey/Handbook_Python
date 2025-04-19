n, m = int(input()), int(input())
width = len(str(n * m))
for i in range(n):
    for j in range(m):
        print(f'{j * n + i * ((-1) ** j) + (n if j % 2 else 1):>{width}}', end=' ')
    else:
        print()
