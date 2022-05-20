from sys import stdin
from collections import deque

t = int(stdin.readline())

for _ in range(t):
    p = list(stdin.readline().rstrip())
    n = int(stdin.readline())
    tempList = stdin.readline().rstrip()
    queue = deque(tempList[1:-1].split(','))

    if n == 0:
        queue = deque()
    error = False
    reverse = False
    for cmd in p:
        if cmd == 'R':
            reverse = not reverse
        elif cmd == 'D':
            if not queue:
                error = True
                break
            if reverse:
                queue.pop()
            else:
                queue.popleft()

    if error:
        print('error')
    else:            
        if reverse:
            l = list(reversed(queue))
        else:
            l = list(queue)
        print('[',end='')
        cnt = 0
        for i in l:
            print(i,end='')
            cnt += 1
            if cnt != len(l):
                print(',',end='')
        print(']')