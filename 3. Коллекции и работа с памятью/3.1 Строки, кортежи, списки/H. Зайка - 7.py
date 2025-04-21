for _ in range(int(input())):
    print(x if (x := input().find('зайка') + 1) > 0 else 'Заек нет =(')
