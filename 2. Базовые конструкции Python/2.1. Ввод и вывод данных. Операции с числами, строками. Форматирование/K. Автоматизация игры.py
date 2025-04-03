number = int(input())
n1 = number // 1000 % 10
n2 = number // 100 % 10
n3 = number // 10 % 10
n4 = number // 1 % 10
print(f'{n2}{n1}{n4}{n3}')
