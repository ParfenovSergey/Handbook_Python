result = set()
while line := input():
    words = line.split()
    for i, word in enumerate(words):
        if word == 'зайка':
            if i != 0:
                result.add(words[i - 1])
            if i != len(words) - 1:
                result.add(words[i + 1])
print(*result, sep='\n')
