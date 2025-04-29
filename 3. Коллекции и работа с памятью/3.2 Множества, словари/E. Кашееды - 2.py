n, m = int(input()), int(input())
one, two = set(), set()
for _ in range(n + m):
    if (x := input()) in one:
        two.add(x)
        one.discard(x)
    else:
        one.add(x)
else:
    print(x if (x := len(one)) else 'Таких нет')
