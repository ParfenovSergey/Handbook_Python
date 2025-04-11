# one-liner
print(f'{input()}\n' * int(input()), end='')

# correct
line = input()
for _ in range(int(input())):
    print(line)
