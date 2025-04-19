n, width = int(input()), int(input())
for i in range(1, n + 1):
    for j in range(1, n + 1):
        print(f'{i * j:^{width}}', end=('|'if j != n else '\n'))
    else:
        if i != n:
            print('-' * (width * n + n - 1))
