x = y = 0
while (direction := input()) != 'СТОП':
    step = int(input())
    match direction:
        case 'СЕВЕР':
            y += step
        case 'ЮГ':
            y -= step
        case 'ЗАПАД':
            x -= step
        case 'ВОСТОК':
            x += step
else:
    print(y, x, sep='\n')
