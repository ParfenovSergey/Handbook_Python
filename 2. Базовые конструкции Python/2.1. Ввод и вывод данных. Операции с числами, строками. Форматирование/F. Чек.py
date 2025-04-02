name = input()
money = float(input())
mass = float(input())
payed = int(input())
cashback = int(payed - mass * money)
print(f'''Чек
{name} - {int(mass)}кг - {int(money)}руб/кг
Итого: {int(mass * money)}руб
Внесено: {int(payed)}руб
Сдача: {cashback}руб''')
