from sys import stdin
TestCase = int(stdin.readline())
for i in range(0, TestCase) :

    InputStr = stdin.readline()

    StrList = list(InputStr)
    TempList = list()

    while len(StrList) > 0:
        temp = StrList.pop()
        if temp == ')':
            TempList.append(')')
        elif temp == '(':
            if len(TempList) == 0:
                TempList.append('1')
                break
            TempList.pop()

    if len(TempList) == 0:
        print("YES")
    else :
        print("NO")
