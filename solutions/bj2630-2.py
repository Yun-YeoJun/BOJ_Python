from sys import stdin

n = int(stdin.readline())
l = []
w_cnt, b_cnt = 0, 0
for i in range(n):
    l.append(list(map(int,stdin.readline().split())))

def divideAndConquer(x,y,N):
    global w_cnt, b_cnt
    tmp_cnt = 0
    for i in range(x, x + N):
        for j in range(y, y + N):
            if l[i][j]:
                tmp_cnt += 1
    if not tmp_cnt:
        w_cnt += 1
    elif tmp_cnt == N * N:
        b_cnt += 1
    else:
        divideAndConquer(x,y,N//2)
        divideAndConquer(x + N//2,y,N//2)
        divideAndConquer(x,y+N//2,N//2)
        divideAndConquer(x+N//2,y+N//2,N//2)
    return

divideAndConquer(0,0,n)
print(w_cnt)
print(b_cnt)