width = int(input())
for i in range(int(input())):
    line = input()
    if len(line) < width - 3:
        print(line)
        width -= len(line)
    else:
        print(line[:width - 3] + '...')
        break
