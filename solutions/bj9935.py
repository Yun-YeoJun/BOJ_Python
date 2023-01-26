import sys
input = sys.stdin.readline

s = list(input().strip())

explode_str = input().strip()

len_of_explode_str = len(explode_str)

key = explode_str[len(explode_str) - 1]

stack = []

for idx,c in enumerate(s):
    stack.append(c)
    if c == key:
        temp = 0
        tf = True
        if len(stack) == 0:
            stack.append(c)
            continue
        for i in stack[len(stack)-len_of_explode_str:len(stack)]:
            if i != explode_str[temp]:
                tf = False
                break
            temp += 1
        if tf == True:
            for i in range(len_of_explode_str):
                stack.pop()

if len(stack) == 0:
    print("FRULA")
else:
    print("".join(stack))