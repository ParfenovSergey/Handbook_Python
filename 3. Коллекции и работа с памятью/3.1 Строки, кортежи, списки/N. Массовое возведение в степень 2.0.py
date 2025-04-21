result = []
for number in input().split():
    result.append(int(number))
else:
    power = int(input())
for number in result:
    print(number ** power, end=' ')
