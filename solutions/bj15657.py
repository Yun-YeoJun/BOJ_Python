import sys
input = sys.stdin.readline

n, m = map(int,input().split())

l = list(map(int,input().split()))

l = sorted(l)

def backtracking(step,arr,prev_idx):
    global l
    global n
    global m
    if step == m:
        for i in arr:
            print(i,end=" ")
        print()
        return
    for i in range(prev_idx,n):
        temp = arr[:]
        temp.append(l[i])
        backtracking(step + 1, temp, i)


backtracking(0,[],0)