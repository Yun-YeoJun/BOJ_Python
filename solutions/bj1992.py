from sys import stdin

n = int(stdin.readline())
l = [[] for i in range(n)]

for i in range(n):
    l[i] = list(map(int,list(stdin.readline().rstrip())))

def quadTree(x,y,length):
    cnt = 0
    for i in range(x,x+length):
        for j in range(y, y+length):
            cnt += l[i][j]
    if cnt == 0:
        print(0,end='')
    elif cnt == length**2:
        print(1,end='')
    else:
        print("(",end='')
        quadTree(x,y,length//2)
        quadTree(x,y+length//2,length//2)
        quadTree(x+length//2,y,length//2)
        quadTree(x+length//2,y+length//2,length//2)
        print(")",end='')

quadTree(0,0,n)