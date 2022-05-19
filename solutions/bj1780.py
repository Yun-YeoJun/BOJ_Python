from sys import stdin

n = int(stdin.readline())
paper = []

for i in range(n):
    paper.append(list(map(int,stdin.readline().split())))

result = [0,0,0]

def divAndCon(x,y,length):
    temp = paper[x][y]
    tf = True
    for i in range(x, x + length):
        for j in range(y, y + length):
            if paper[i][j] != temp:
                tf = False
                break
        if tf == False:
            break
    if tf:
        if temp == -1:
            result[0] += 1
        elif temp == 0:
            result[1] += 1
        else:
            result[2] += 1
    else:
        divLength = length//3
        for i in range(3):
            for j in range(3):
                divAndCon(x + divLength * i, y + divLength * j, divLength)

divAndCon(0,0,n)

for i in result:
    print(i)