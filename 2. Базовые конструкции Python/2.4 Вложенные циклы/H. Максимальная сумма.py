max_name = ''
max_number = 0
for i in range(int(input())):
    name = input()
    n = int(input())
    tmp = 0
    while n:
        tmp += n % 10
        n //= 10
    else:
        if tmp >= max_number:
            max_number = tmp
            max_name = name
else:
    print(max_name)
