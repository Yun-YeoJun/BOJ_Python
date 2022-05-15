from sys import stdin

n = int(stdin.readline())

divideList = [[] for i in range(4)]
inputList = []
resultB = 0
resultW = 0

for i in range(n):
    inputList.append(list(map(int,stdin.readline().split())))

def divide(List, k):
    global resultB
    global resultW
    l = [[] for i in range(4)]
    for i in range(k):
        if i < k/2:
            l[0].append(List[i][:k//2])
            l[1].append(List[i][k//2:])
        else:
            l[2].append(List[i][:k//2])
            l[3].append(List[i][k//2:])
    for i in l:
        if check(i, k//2):
            if i[0][0] == 1:
                resultB += 1
            else:
                resultW += 1
        else:
            divide(i, k//2)

def check(checkList, k):
    bw = checkList[0][0]
    tf = True
    for i in range(k):
        for j in range(k):
            if checkList[i][j] != bw:
                tf = False
                break
        if tf == False:
            break
    return tf

if check(inputList, n):
    if inputList[0][0] == 1:
        resultB = 1
    else:
        resultW = 1
else:
    divide(inputList, n)

print(resultW)
print(resultB)