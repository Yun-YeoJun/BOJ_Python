from sys import stdin
from collections import deque

while True:
    que = deque()
    temp = stdin.readline().rstrip()
    tf = True

    if temp == '.':
        break

    for i in temp:
        if i == '.':
            break
        if i == '(':
            que.append('(')
        elif i == '[':
            que.append('[')
        elif i == ')':
            if len(que) == 0:
                tf = False
                break
            c = que.pop()
            if c == '(':
                continue
            else:
                tf = False
                break
        elif i == ']':
            if len(que) == 0:
                tf = False
                break
            c = que.pop()
            if c == '[':
                continue
            else:
                tf = False
                break

    if len(que) != 0:
        print('no')
        continue

    if tf == True:
        print('yes')
    else:
        print('no')

    
