name = input()
price = int(input())
weight = int(input())
money = int(input())

print(f'''================Чек================
Товар:{name:>29}
Цена:{weight:>{(19 - len(str(price)))}}кг * {price}руб/кг
Итого:{weight * price:>26}руб
Внесено:{money:>24}руб
Сдача:{money - weight * price:26}руб
===================================''')

# magic numbers = 35 - len(constant_text), 35 = width of text
