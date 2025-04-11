result = 0.
while (price := float(input())) != 0:
    result += price if price < 500 else 0.9 * price
else:
    print(result)