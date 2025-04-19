result = 0
for i in range(int(input())):
    number = number_copy = int(input())
    number_reversed = 0
    while number_copy:
        number_reversed = number_reversed * 10 + number_copy % 10
        number_copy //= 10
    else:
        result += number_reversed == number
else:
    print(result)
