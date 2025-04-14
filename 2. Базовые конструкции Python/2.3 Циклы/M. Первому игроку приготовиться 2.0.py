n = int(input())
result = input()
for _ in range(n - 1):
    result = min(result, input())
else:
    print(result)
