from sys import stdin
from collections import deque

dq = deque()

n = int(stdin.readline())

for i in range(n):
    cmd = stdin.readline()
    temp = cmd[:3]

    if temp == 'pus':
        temp2 = cmd[5]

        if temp2 == 'f':
            dq.appendleft(int(cmd[11:]))
        elif temp2 == 'b':
            dq.append(int(cmd[10:]))
            
    elif temp == 'pop':
        temp2 = cmd[4]
        if len(dq) == 0:
            print(-1)
            continue
        if temp2 == 'f':
            print(dq.popleft())
        elif temp2 == 'b':
            print(dq.pop())

    elif temp == 'siz':
        print(len(dq))
    elif temp == 'emp':
        if len(dq) == 0:
            print(1)
        else:
            print(0)
            
    elif temp == 'fro':
        if len(dq) == 0:
            print(-1)
            continue
        print(dq[0])
    elif temp == 'bac':
        if len(dq) == 0:
            print(-1)
            continue
        print(dq[len(dq) - 1])
        
