stack = []
for ch in input().split():
    if ch in '*-+':
        tmp = eval(f'{stack[-2]} {ch} {stack[-1]}')
        stack = stack[:-2]
        stack.append(tmp)
    elif ch == '/':
        tmp = eval(f'{stack[-2]} // {stack[-1]}')
        stack = stack[:-2]
        stack.append(tmp)
    elif ch == '!':
        tmp = stack[-1]
        for i in range(tmp - 1, 1, -1):
            stack[-1] *= i
    elif ch == '~':
        stack[-1] = -stack[-1]
    elif ch == '#':
        stack.append(stack[-1])
    elif ch == '@':
        stack[-3], stack[-2], stack[-1] = stack[-2], stack[-1], stack[-3]
    else:
        stack.append(int(ch))
else:
    print(stack[0])
