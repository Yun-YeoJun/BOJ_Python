import sys
input = sys.stdin.readline


n = int(input())
m = int(input())
s = input().rstrip()

def checkPn(n,index):
    lenOfPn = 2 * n + 1
    i = 0
    idx = 0
    while index + 2 * idx + 1 < len(s):
        if s[index + 2 * idx] == "O":
            idx -= 1
            break
        if s[index + 2 * idx + 1] == "I":
            i += 1
            break
        i += 1
        idx += 1
    
    result = i - n

    if result < 0:
        result = 0
    return (result, idx * 2)

result = 0
index = 0
while index < m:
    if s[index] == "I":
        r, i = checkPn(n, index)
        result += r
        index += i + 1
    else:
        index += 1

print(result)