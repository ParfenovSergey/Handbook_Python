n, m = int(input()), int(input())
width = len(str(n * m))
k = 1
for _ in range(n):
    for _ in range(m):
        print(f'{k:>{width}}', end=' ')
        k += 1
    else:
        print()
