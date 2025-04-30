result = []
for number in input().split():
    number = bin(int(number))
    result.append({'digits': len(number) - 2,
                   'units': number.count('1'),
                   'zeros': number.count('0') - 1})
print(result)
