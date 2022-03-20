from sys import stdin

m = int(stdin.readline())
n = int(stdin.readline())

l = list(range(m, n + 1))

# m 이상 n 이하의 자연수 중 소수 찾기

for i in range(2, m): # m 이하의 자연수의 배수들 삭제
    for j in range(len(l)):
        if l[j] != -1:
            if l[j] % i == 0:
                l[j] = -1

for i in range(len(l)):
    for j in range(i + 1, len(l)):
        if l[i] == -1:
            break
        if l[j] != -1 and l[i] != -1:
            if l[j] % l[i] == 0:
                l[j] = -1
remove_set = {-1}
l = [i for i in l if i not in remove_set]

if len(l) == 0:
    print(-1)
else:
    result = 0
    for i in l:
        result += i
    print(result)
    print(l[0])