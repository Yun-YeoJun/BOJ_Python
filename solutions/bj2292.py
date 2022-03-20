from sys import stdin

n = int(stdin.readline())
i = 1
cnt = 1

while True:
    if n == 1:
        print(1)
        break
    elif i < n <= i + 6 * cnt :
        print(cnt + 1)
        break
    
    i = i + 6 * cnt
    cnt += 1
