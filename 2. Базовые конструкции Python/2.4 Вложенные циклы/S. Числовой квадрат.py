n = int(input())
width = len(str((n + 1) // 2))

for i in range(1, n + 1):
    for j in range(1, n + 1):
        print(f'{min(i, j, n - i + 1, n - j + 1):>{width}}', end=' ')
    else:
        print()
