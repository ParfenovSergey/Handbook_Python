count = 0
while (line := input()) != 'Приехали!':
    if 'зайка' in line:
        count += 1
else:
    print(count)
