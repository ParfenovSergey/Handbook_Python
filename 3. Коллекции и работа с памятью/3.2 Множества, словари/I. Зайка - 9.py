result = dict()
while line := input():
    for word in line.split():
        result[word] = result.get(word, 0) + 1
else:
    for key in result:
        print(f'{key} {result[key]}')
