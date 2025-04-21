data = []
for i in range(int(input())):
    data.append(input())
else:
    req = input().lower()
for line in data:
    if req in line.lower():
        print(line)
