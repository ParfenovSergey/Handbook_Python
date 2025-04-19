n = int(input())
i, length = 1, 1
while i < n:
    for j in range(1, length):
        if i <= n:
            print(i, end=' ')
        i += 1
    else:
        print()
        length += 1
