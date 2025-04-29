hl = 0
fl = False
for i in range(int(input())):
    if not fl:
        b = int(input())
        b, h = divmod(b, 256)
        b, r = divmod(b, 256)
        b, m = divmod(b, 256)
        hn = 37 * (m + r + hl) % 256
        hl = h
        if hn != h or hn > 100:
            print(i)
            fl = True
if not fl:
    print(-1)
