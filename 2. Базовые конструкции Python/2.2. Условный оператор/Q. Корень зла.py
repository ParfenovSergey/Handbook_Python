a, b, c = float(input()), float(input()), float(input())
if a == 0 and b == 0 and c == 0:
    print('Infinite solutions')
elif a == 0 and b == 0:
    print('No solution')
elif a == 0 and c == 0:
    print(0)
elif a == 0:
    print(f'{-c / b:.2f}')
elif b == 0 and c == 0:
    print(0, 0)
elif b == 0:
    if c < 0:
        print(f'{-(-c / a) ** 0.5:.2f}')
    else:
        print('No solution')
elif c == 0:
    print(f'{min(0., -b / a):.2f}, {max(0., -b / a):.2f}')
else:
    d = b * b - 4 * a * c
    if d < 0:
        print('No solution')
    elif d == 0:
        print(f'{-b / (2 * a):.2f}')
    else:
        x1 = (-b - d ** 0.5) / (2 * a)
        x2 = (-b + d ** 0.5) / (2 * a)
        print(f'{min(x1, x2):.2f} {max(x1, x2):.2f}')
