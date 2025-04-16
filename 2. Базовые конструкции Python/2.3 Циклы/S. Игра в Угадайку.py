left, right = 0, 1001
while left != right:
    print(left + (right - left) // 2)
    if (command := input()) == 'Больше':
        left += (right - left) // 2
    elif command == 'Меньше':
        right -= (right - left) // 2
    elif command == 'Угадал!':
        left = right = left + (right - left) // 2
else:
    print(left)
