n1, n2 = int(input()), int(input())
n2 += (step := -1 if n1 > n2 else 1)
for i in range(n1, n2, step):
    print(i, end=' ')
