import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)


n, m = map(int,input().split())

l = sorted(list(map(int,input().split())))

result = []

def backtracking(step,temp,cur):
    global m

    if step == m:
        if temp not in result:
            result.append(temp)
        return

    for i in range(cur,n):
        if len(temp) == 0:
            backtracking(step + 1, [l[i]], i)
        else:
            backtracking(step + 1, temp[:]+[l[i]], i)

backtracking(0,[],0)

for i in result:
    for j in i:
        print(j,end=' ')
    print()