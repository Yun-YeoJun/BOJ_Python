import sys
from collections import deque
input = sys.stdin.readline

s = input().strip()

stack = deque()

for i in s:

    if 'A' <= i <= 'Z': # i가 알파벳이라면
        print(i,end="")

    else: # i가 기호라면

        if len(stack) != 0:
            if i == ")":
                while len(stack) != 0 and stack[len(stack) - 1] != "(":
                    print(stack.pop(),end="")
                if len(stack) != 0:
                    stack.pop()
                if len(stack) != 0 and stack[len(stack) - 1] != "(":
                    print(stack.pop(),end="")
                while len(stack) != 0 and stack[len(stack) - 1] != ")":
                    print(stack.pop(),end="")
            elif i == "(":
                stack.append(i)
            elif len(stack) != 0 and stack[len(stack) - 1] in ["+","-"]:
                if i in ["+","-"]:
                    stack.append(i)
                else:
                    stack.append(i)
            elif len(stack) != 0 and stack[len(stack) - 1] in ["*","/"]:
                if i in ["+","-"]:
                    while len(stack) != 0: # and stack[len_of_stack - 1] == ""
                        print(stack.pop(),end="")
                    stack.append(i)
                else:
                    stack.append(i)
            else:
                stack.append(i)
        
        else:
            stack.append(i)


while len(stack) != 0:
    print(stack.pop(),end="")