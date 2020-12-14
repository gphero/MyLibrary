n = int(input())
data = list(map(str, input().split()))

# 동R 북U 서L 남D
dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]
x, y = 1, 1

for i in data:
    if x == 1 and i == 'U':
        continue
    elif y == 1 and i == 'L':
        continue
    elif x == n and i == 'D':
        continue
    elif y == n and i == 'R':
        continue

    if i == 'R':
        x += dx[0]
        y += dy[0]
    elif i == 'U':
        x += dx[1]
        y += dy[1]
    elif i == 'L':
        x += dx[2]
        y += dy[2]
    elif i == 'D':
        x += dx[3]
        y += dy[3]

print(x, y)


