from sys import stdin

n, r, c = map(int,stdin.readline().split())

cnt = 0
result = -1

def divAndCon(x,y,length):
    global r, c, result, cnt
    if length == 1:
        result = cnt
    else:
        parameter = [(x,y,length // 2), (x, y + length // 2, length // 2), (x + length // 2, y, length // 2), (x + length // 2, y + length // 2, length // 2)]
        ord = -1        
        for i in parameter:
            nx, ny, nl = i
            ord += 1
            if nx <= r < nx + nl and ny <= c < ny + nl:
                cnt += (nl ** 2) * ord
                divAndCon(nx,ny,nl)

divAndCon(0,0,2 ** n)
print(result)