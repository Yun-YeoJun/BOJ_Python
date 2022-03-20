from sys import stdin
from collections import deque

queue = deque()

def push(x):
    global queue
    queue.append(x)

def pop():
    global queue
    if len(queue) == 0:
        print('-1')
        return
    print(queue.popleft())

def size():
    global queue
    print(len(queue))

def empty():
    global queue
    if len(queue) == 0:
        print('1')
    else:
        print('0')
        
def front():
    global queue
    if len(queue) == 0:
        print('-1')
        return
    temp = queue.popleft()
    queue.appendleft(temp)
    print(temp)    

def back():
    global queue
    if len(queue) == 0:
        print('-1')
        return
    temp = queue.pop()
    queue.append(temp)
    print(temp)



n = int(stdin.readline())

i = 0
while i < n:
    INPUT = stdin.readline()
    f = INPUT[:3]

    if f == 'pus':
        x = int(INPUT[5:])
        push(x)

    elif f == 'pop':
        pop()
        
    elif f == 'siz':
        size()
        
    elif f == 'emp':
        empty()

    elif f == 'fro':
        front()

    elif f == 'bac':
        back()
        
    i+=1
