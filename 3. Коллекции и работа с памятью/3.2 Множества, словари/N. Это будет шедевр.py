ingredients = set()
result = []
for _ in range(int(input())):
    ingredients.add(input())
for _ in range(int(input())):
    name = input()
    receipt = set()
    for _ in range(int(input())):
        receipt.add(input())
    else:
        if receipt.issubset(ingredients):
            result.append(name)
if result:
    print(*sorted(result), sep='\n')
else:
    print('Готовить нечего')
