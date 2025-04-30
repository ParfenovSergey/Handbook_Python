friends = dict()
result = dict()
while pair := input():
    friends[pair.split()[0]] = friends.get(pair.split()[0], []) + [pair.split()[1]]
    friends[pair.split()[1]] = friends.get(pair.split()[1], []) + [pair.split()[0]]
for name in friends:
    second = []
    for friend in friends[name]:
        second += friends[friend]
    result[name] = set(second) - set(friends[name]) - {name}
for name in sorted(result):
    print(f'{name}: {', '.join(sorted(result[name]))}')
