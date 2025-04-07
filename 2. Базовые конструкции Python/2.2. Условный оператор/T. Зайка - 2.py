s = input()
result = ''
if 'зайка' in s:
    result = s
s = input()
if 'зайка' in s and (result and s < result or not result):
    result = s
s = input()
if 'зайка' in s and (result and s < result or not result):
    result = s
print(result, len(result))
