from sys import stdin  
from collections import deque

t = int(stdin.readline())

def D(num):
    num = num * 2
    return num % 10000

def S(num):
    num -= 1
    if num == -1:
        num = 9999
    return num

def L(num):
    d1 = num // 1000
    num %= 1000 
    d2 = num // 100
    num %= 100
    d3 = num // 10
    num %= 10
    d4 = num

    return 1000 * d2 + 100 * d3 + 10 * d4 + d1

def R(num):
    d1 = num // 1000
    num %= 1000
    d2 = num // 100
    num %= 100
    d3 = num // 10
    num %= 10
    d4 = num

    return 1000 * d4 + 100 * d1 + 10 * d2 + d3

def DSLR(num, l, visited):
    d = D(num)
    s = S(num)
    l_ = L(num)
    r = R(num)

    if visited[d] == 0:
        que.append((d, l + 'D'))
        visited[d] +=1
    if visited[s] == 0:
        que.append((s, l + 'S'))
        visited[s] += 1
    if visited[l_] == 0:
        que.append((l_, l + 'L'))
        visited[l_] += 1
    if visited[r] == 0:
        que.append((r, l + 'R'))
        visited[r] += 1

for tc in range(t):
    a, b = map(int, stdin.readline().split()) # a : 레지스터의 초기 값   ,    b : 최종 값
    que = deque()

    visited = [0] * 10000

    DSLR(a, ' ', visited)

    while True:
        num, l = que.popleft()
        if num == b:
            print(l.lstrip())
            break
        DSLR(num, l, visited)