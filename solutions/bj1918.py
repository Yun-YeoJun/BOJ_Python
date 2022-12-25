import sys
from collections import deque
input = sys.stdin.readline

l = list(input().strip())

stack = deque()

cnt = 0

priority = {"+":2,"-":2,"*":1,"/":1}

for i in l:
    if "A" <= i <= "Z":
        print(i,end="")
    else:
        if len(stack) == 0:
            stack.append(i)
        elif i == "(":
            stack.append(i)
            cnt += 1
        elif i == ")":
            temp = stack.pop()
            while temp != "(":
                print(temp,end="")
                temp = stack.pop()
            cnt -= 1
        else:
            while len(stack) > 0 and stack[len(stack) - 1] in priority and priority[stack[len(stack) - 1]] <= priority[i]:
                print(stack.pop(),end="")
            stack.append(i)



while len(stack) != 0:
    print(stack.pop(),end="")