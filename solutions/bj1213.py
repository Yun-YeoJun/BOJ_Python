from sys import stdin

s = stdin.readline().rstrip()

s = list(s)

l = [0] * 26

for i in range(len(s)):
    l[ord(s[i]) - 65] += 1

odd = 0
oddIdx = 0

for i in range(26):
    if l[i] % 2 == 1:
        odd += 1
        oddIdx = i

if odd > 1:
    print("I'm Sorry Hansoo")
else:
    result = ['_'] * len(s)
    cur = 0
    if odd == 0:
        for i in range(26):
            if l[i] != 0:
                temp = l[i]
                for j in range(l[i] // 2):
                    result[cur + j] = chr(i + 65)
                    result[len(result) - 1 - (cur + j)] = chr(i + 65)
                cur += l[i] // 2
    elif odd == 1:
        result[len(result)//2] = chr(oddIdx + 65)
        l[oddIdx] -= 1
        for i in range(26):
            if l[i] != 0:
                temp = l[i]
                for j in range(l[i] // 2):
                    result[cur + j] = chr(i + 65)
                    result[len(result) - 1 - (cur + j)] = chr(i + 65)
                cur += l[i] // 2
    result = ''.join(result)
    print(result)