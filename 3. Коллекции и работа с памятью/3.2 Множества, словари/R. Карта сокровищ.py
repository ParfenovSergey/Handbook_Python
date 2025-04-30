points = dict()
for _ in range(int(input())):
    x, y = input().split()
    x, y = divmod(int(x), 10), divmod(int(y), 10)
    points[(x[0], y[0])] = points.get((x[0], y[0]), []) + [(x[1], y[1])]
print(len(max(points.values(), key=len)))
