width = int(input())
for _ in range(int(input())):
    print(line if len(line := input()) <= width else line[:width - 3] + '...')
