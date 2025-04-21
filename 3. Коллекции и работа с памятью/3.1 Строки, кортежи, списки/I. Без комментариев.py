while line := input():
    if line.startswith('#'):
        continue
    print(line.split('#')[0] if '#' in line else line)
