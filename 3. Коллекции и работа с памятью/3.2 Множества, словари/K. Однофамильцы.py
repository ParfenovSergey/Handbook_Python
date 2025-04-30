n = int(input())
one, two = set(), set()
for _ in range(n):
    if (name := input()) in two:
        continue
    elif name in one:
        two.add(name)
        one.discard(name)
    else:
        one.add(name)
else:
    print(n - len(one))
