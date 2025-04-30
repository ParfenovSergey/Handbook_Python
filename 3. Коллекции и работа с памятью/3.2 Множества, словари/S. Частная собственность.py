toys = dict()
result = set()
for _ in range(int(input())):
    line = input().split(': ')
    for toy in set(line[1].split(', ')):
        toys[toy] = toys.get(toy, 0) + 1
        if toys[toy] == 1:
            result.add(toy)
        else:
            result.discard(toy)
print(*sorted(result), sep='\n')
