result = dict()
numbers = sorted(set(input().split('; ')), key=int)
for i in range(len(numbers)):
    for j in range(len(numbers)):
        if i != j:
            x, y = numbers[i], numbers[j]
            a, b = int(x), int(y)
            while b:
                a, b = b, a % b
            if a == 1:
                result[x] = result.get(x, []) + [y]
for number in result:
    print(f'{number} - {', '.join(result[number])}')
