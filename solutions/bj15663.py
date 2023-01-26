import sys
input = sys.stdin.readline

n,m = map(int,input().split())

numbers = sorted(list(map(int,input().split())))

result = []

def backtracking(step,m,s,prev):
    if step == m:
        result.append(s.strip())
    else:
        for i in range(len(numbers)):
            if i > 0 and numbers[i] == numbers[i - 1]:
                continue
            
            backtracking(step + 1, m, ' '.join([s,str(numbers[i])]), numbers[i])

backtracking(0,m,'',-1)

#result = sorted(list(dict.fromkeys(result)))
#result = sorted(result)

dup = []

for i in result:
    if i in dup:
        continue
    print(i)
    dup.append(i)