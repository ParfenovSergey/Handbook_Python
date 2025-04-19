n = int(input())
max_sum, result = 0, 1
for i in range(2, 11):
    tmp = n
    tmp_sum = 0
    while tmp:
        tmp_sum += tmp % i
        tmp //= i
    else:
        if tmp_sum > max_sum:
            max_sum = tmp_sum
            result = i
else:
    print(result)
