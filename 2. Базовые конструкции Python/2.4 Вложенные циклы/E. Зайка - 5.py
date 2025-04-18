result = 0
for i in range(int(input())):
    local = False
    while (line := input()) != 'ВСЁ':
        if 'зайка' in line:
            local = True
    else:
        result += local
else:
    print(result)
