from sys import stdin

n, m = map(int,stdin.readline().split())

l = [[] for _ in range(n)]

for i in range(n):
    temp = stdin.readline().rstrip()
    for j in temp:
        l[i].append(j)

curY = 0
curX = 0

result = 0

tf = False

for length in reversed(range(2, min(n,m) + 1)):
    for i in range(n * m):
        cur1X = curX + length - 1 # cur1 : 사각형 오른쪽 위 꼭짓점의 좌표
        cur1Y = curY

        cur2X = curX # cur2 : 사각형 왼쪽 아래 꼭짓점의 좌표
        cur2Y = curY + length - 1

        cur3X = curX + length - 1 # cur3 : 사각형 오른쪽 아래 꼭짓점의 좌표
        cur3Y = curY + length - 1

        if cur1X >= m or cur2X >= m or cur3X >= m:
            curY += 1
            curX = 0
            continue
        if cur1Y >= n or cur2Y >= n or cur3Y >= n:
            curX = 0
            curY = 0
            break

        temp1 = l[curY][curX]
        temp2 = l[cur1Y][cur1X]
        temp3 = l[cur2Y][cur2X]
        temp4 = l[cur3Y][cur3X]

        if temp1 == temp2 == temp3 == temp4:
            result = length
            tf = True
            break
        curX += 1
    if tf == True:
        print(result**2)
        break
if tf == False:
    print(1)