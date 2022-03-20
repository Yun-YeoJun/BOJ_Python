from sys import stdin

c = int(stdin.readline())
stack = list()

for i in range(c):
    cmd = stdin.readline()
    temp = cmd[:3]

    if temp == 'pus':
        stack.append(int(cmd[5:]))
    elif temp == 'pop':
        if len(stack) == 0:
            print(-1)
        else :
            print("%d" %(stack.pop()))
    elif temp == 'siz':
        print(len(stack))
    elif temp == 'emp':
        if len(stack) == 0:
            print(1)
        else :
            print(0)
    elif temp == 'top':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[len(stack) - 1])
