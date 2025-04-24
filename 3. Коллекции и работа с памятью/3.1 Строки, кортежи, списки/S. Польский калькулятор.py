stack = []
for ch in input().split():
    if ch in ('*', '-', '+'):
        tmp = eval(f'{stack[-2]} {ch} {stack[-1]}')
        stack = stack[:-2]
        stack.append(tmp)
    else:
        stack.append(int(ch))
else:
    print(stack[0])
