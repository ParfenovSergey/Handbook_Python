number = number_copy = int(input())
number_reversed = 0
while number_copy:
    number_reversed = number_reversed * 10 + number_copy % 10
    number_copy //= 10
else:
    print('YES' if number_reversed == number else 'NO')
