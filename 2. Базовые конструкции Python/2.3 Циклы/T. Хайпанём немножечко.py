hl = 0
fl = False
for i in range(int(input())):
    if not fl:
        b = int(input())
        h = b % 256
        b //= 256
        r = b % 256
        b //= 256
        m = b % 256
        b //= 256
        hn = 37 * (m + r + hl) % 256
        hl = h
        if hn != h or hn > 100:
            print(i)
            fl = True
if not fl:
    print(-1)
