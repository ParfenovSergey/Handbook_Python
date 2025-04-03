name = input()
number = int(input())
n1 = number // 100 % 10
n2 = number // 10 % 10
n3 = number // 1 % 10
print(f'''Группа №{n1}.
{n3}. {name}.
Шкафчик: {number}.
Кроватка: {n2}.''')
