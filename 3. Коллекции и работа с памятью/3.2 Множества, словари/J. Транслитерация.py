letters = {'А': 'A', 'Б': 'B', 'В': 'V', 'Г': 'G',
           'Д': 'D', 'Е': 'E', 'Ё': 'E', 'Ж': 'ZH',
           'З': 'Z', 'И': 'I', 'Й': 'I', 'К': 'K',
           'Л': 'L', 'М': 'M', 'Н': 'N', 'О': 'O',
           'П': 'P', 'Р': 'R', 'С': 'S', 'Т': 'T',
           'У': 'U', 'Ф': 'F', 'Х': 'KH', 'Ц': 'TC',
           'Ч': 'CH', 'Ш': 'SH', 'Щ': 'SHCH', 'Ы': 'Y',
           'Э': 'E', 'Ю': 'IU', 'Я': 'IA', 'Ъ': '', 'Ь': ''}

line = input()
result = ''
for letter in line:
    if letter.upper() in letters:
        if letter.isupper():
            result += letters[letter.upper()].capitalize()
        else:
            result += letters[letter.upper()].lower()
    else:
        result += letter
print(result)
