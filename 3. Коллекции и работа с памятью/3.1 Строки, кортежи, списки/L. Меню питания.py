menu = ('Манная', 'Гречневая', 'Пшённая', 'Овсяная', 'Рисовая')
for i in range(int(input())):
    print(menu[i % 5])
