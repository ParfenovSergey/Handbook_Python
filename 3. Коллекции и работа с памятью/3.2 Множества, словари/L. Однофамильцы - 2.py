result = dict()
for _ in range(int(input())):
    name = input()
    result[name] = result.get(name, 0) + 1
else:
    if max(result.values()) > 1:
        for name in sorted(result):
            if result[name] > 1:
                print(f'{name} - {result[name]}')
    else:
        print('Однофамильцев нет')
