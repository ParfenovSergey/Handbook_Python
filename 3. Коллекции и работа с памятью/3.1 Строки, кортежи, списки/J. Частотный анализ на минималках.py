result, max_letter = 'а', 0
full_line = ''
while (line := input()) != 'ФИНИШ':
    full_line += line.replace(' ', '').lower()
for letter in sorted(full_line):
    if (tmp := full_line.count(letter)) > max_letter:
        max_letter = tmp
        result = letter
else:
    print(result)
