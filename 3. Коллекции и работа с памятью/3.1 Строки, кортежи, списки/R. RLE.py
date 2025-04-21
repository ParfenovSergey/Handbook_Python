line = input()
ch0 = line[0]
length = 1
for ch in line[1:]:
    if ch != ch0:
        print(ch0, length)
        ch0 = ch
        length = 1
    else:
        length += 1
else:
    print(ch0, length)
