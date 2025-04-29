n = int(input()), int(input())
data = [set(), set()]
for i in range(2):
    for j in range(n[i]):
        data[i].add(input())
answer = len(data[0] & data[1])
print(answer if answer else 'Таких нет')
