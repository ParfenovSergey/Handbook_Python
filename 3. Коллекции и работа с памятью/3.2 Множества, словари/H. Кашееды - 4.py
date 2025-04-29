data = dict()
for _ in range(int(input())):
    line = input().split()
    for item in line[1:]:
        data[item] = data.get(item, list()) + [line[0]]
if (x := input()) in data:
    print(*sorted(data[x]), sep='\n')
else:
    print('Таких нет')
