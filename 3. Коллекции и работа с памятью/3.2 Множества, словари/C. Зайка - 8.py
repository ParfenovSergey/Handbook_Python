result = set()
for _ in range(int(input())):
    result |= set(input().split())
else:
    print(*result, sep='\n')
