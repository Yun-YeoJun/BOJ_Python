import sys
input = sys.stdin.readline

n,m=map(int,input().split())

def backtracking(start,end,l,m):
    for i in range(start,end+1):
        if m == len(l) + 1:
            temp = l[:]
            temp.append(i)
            for j in temp:
                print(j,end=" ")
            print()
        else:
            temp = l[:]
            temp.append(i)
            backtracking(i,end,temp,m)

backtracking(1,n,[],m)