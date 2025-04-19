n, width = int(input()), 1
for k in range(2):
    i, length = 1, 1
    while i <= n:
        line = ''
        for j in range(0, length):
            if i <= n:
                line += f'{i} '
            i += 1
        else:
            if k == 0:
                width = max(width, len(line))
            else:
                print(f'{line:^{width}}')
            length += 1
