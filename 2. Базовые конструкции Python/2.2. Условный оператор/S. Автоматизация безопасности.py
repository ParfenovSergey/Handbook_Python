x, y = float(input()), float(input())

if x ** 2 + y ** 2 > 10 ** 2:
    print('Вы вышли в море и рискуете быть съеденным акулой!')
elif (x >= 0 and y >= 0 and x ** 2 + y ** 2 <= 5 ** 2 or
      0 <= y <= 5 and -4 <= x <= 0 or
      0 <= 3 * y <= 5 * x + 35 and x <= -4 or
      (x + 1) ** 2 / 4 - 9 <= y <= 0):
    print('Опасность! Покиньте зону как можно скорее!')
else:
    print('Зона безопасна. Продолжайте работу.')
