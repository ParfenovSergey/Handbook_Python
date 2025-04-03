h, m, t = int(input()), int(input()), int(input())
time = 60 * h + m + t
print(f'{time // 60 % 24:02}:{time % 60:02}')
