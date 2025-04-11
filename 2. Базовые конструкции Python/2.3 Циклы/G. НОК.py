a, b = int(input()), int(input())
tmp_a, tmp_b = a, b
while b:
    a, b = b, a % b
else:
    print(tmp_a * tmp_b // a)
