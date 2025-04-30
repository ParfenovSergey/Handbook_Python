can_cook, cooked = set(), set()
for _ in range(int(input())):
    can_cook.add(input())
for _ in range(int(input())):
    for _ in range(int(input())):
        cooked.add(input())
not_cooked = can_cook - cooked
if not_cooked:
    print(*sorted(not_cooked), sep='\n')
else:
    print('Готовить нечего')
