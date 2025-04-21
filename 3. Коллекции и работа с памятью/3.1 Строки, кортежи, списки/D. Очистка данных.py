while line := input():
    if line.endswith('@@@'):
        continue
    elif line.startswith('##'):
        print(line[2:])
    else:
        print(line)
