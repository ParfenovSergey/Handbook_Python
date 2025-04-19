n, m = int(input()), int(input())
width = len(str(n * m))
for i in range(n):
    for j in range(m):
        print(f'{i * m + j * ((-1) ** i) + (m if i % 2 else 1):>{width}}', end=' ')
    else:
        print()
