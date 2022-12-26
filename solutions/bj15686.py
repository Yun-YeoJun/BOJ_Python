import sys
import math
input = sys.stdin.readline

n,m = map(int,input().split())


chicken = []
house = []

for i in range(n):
    temp = list(map(int,input().split()))

    for idx,j in enumerate(temp):
        if j == 2:
            chicken.append((i,idx))
        if j == 1:
            house.append((i,idx))


min_chicken_len = math.inf

def backtracking(step,chicken_list,start):
    global m
    global chicken
    global min_chicken_len
    
    if step == m:
        min_chicken_len = min(min_chicken_len,calc_chicken_len(chicken_list))

    else:
        for i in range(start,len(chicken)):
            temp = chicken_list[:]
            temp.append(chicken[i])
            backtracking(step+1,temp,i+1)

def calc_chicken_len(chicken_list):
    global house
    global n

    result = 0

    for hx, hy in house:
        temp = n * n
        for cx, cy in chicken_list:
           temp = min(temp,abs(hx-cx) + abs(hy - cy))
        result += temp

    return result

backtracking(0,[],0)
print(min_chicken_len)