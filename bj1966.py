from sys import stdin
from collections import deque

testCase = int(stdin.readline())

for i in range(testCase):
  cnt = 1
  n, m = map(int, stdin.readline().split())
  input = deque(map(int, stdin.readline().split()))
  target = input[m]
  idx = m

  while True:
    tf = True
    for j in range(len(input)):
      if input[0] < input[j]:
        tf = False
        break
    if tf == False:
      if idx == 0:
        idx = len(input) - 1
        temp = input.popleft()
        input.append(temp)
      else:
        idx -= 1
        temp = input.popleft()
        input.append(temp)
    else:
      if idx == 0:
        print(cnt)
        break
      else:
        input.popleft()
        idx-=1
        cnt+=1
        
  
