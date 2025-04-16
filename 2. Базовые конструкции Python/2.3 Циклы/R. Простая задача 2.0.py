n = int(input())
i = 2
while n > 1:
    if n % i == 0:
        print(i, end=' * ' if n != i else '')
        n //= i
    else:
        i += 1
