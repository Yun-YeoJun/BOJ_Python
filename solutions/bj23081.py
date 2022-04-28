from sys import stdin

n = int(stdin.readline())

l = []

for i in range(n):
    l.append(list(stdin.readline().rstrip()))

d = [[-1,0], [-1,1], [0,1], [1,1], [1,0], [1,-1], [0,-1], [-1,-1]]

result = -1
resultCoordinate = [-1,-1]
for y in range(n):
    for x in range(n):
        tempResult = 0
        if l[y][x] == '.':
            for dy, dx in d:
                temp = tempResult
                if 0 <= y + dy < n and 0 <= x + dx < n:
                    if l[y + dy][x + dx] == 'W':
                        ty = y + dy
                        tx = x + dx
                        temp += 1
                        if 0<= ty + dy < n and 0 <= tx + dx < n:
                            while l[ty + dy][tx + dx] == 'W':
                                temp += 1
                                ty += dy
                                tx += dx
                                if ty + dy < 0 or ty + dy >= n or tx + dx < 0 or tx + dx >= n:
                                    temp = -1
                                    break
                            if temp == -1:
                                continue
                            if l[ty + dy][tx + dx] == '.':
                                continue
                            tempResult = temp
            if tempResult != 0 and result < tempResult:
                result = tempResult
                resultCoordinate = [x,y]

if result != -1:
    print(resultCoordinate[0],resultCoordinate[1])
    print(result)
else:
    print('PASS')
