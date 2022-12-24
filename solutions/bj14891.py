import sys
input = sys.stdin.readline

l = [[] for i in range(4)]

for i in range(4):
    l[i] = list(map(int,list(input().strip())))

top = [0,0,0,0,0]

k = int(input())

def turn(top, num, direction):
    if direction == 1: # 시계 방향
        if top[num] == 0:
            top[num] = 7
        else:
            top[num] -= 1
    else: # 반시계 방향
        if top[num] == 7:
            top[num] = 0
        else:
            top[num] += 1

for i in range(k):
    # num : 회전시킨 톱니바퀴 번호
    # direction : 1 = 시계 방향, -1 = 반시계 방향
    num, direction = map(int,input().split())

    connection = [[(top[1] + 2)%8],[(top[2] + 2)%8,(top[2] - 2)%8],[(top[3] + 2)%8,(top[3] - 2)%8],[(top[4] - 2) % 8]]

    is_same = [
        l[0][(top[1] + 2) % 8] == l[1][(top[2] - 2) % 8],
        l[1][(top[2] + 2) % 8] == l[2][(top[3] - 2) % 8],
        l[2][(top[3] + 2) % 8] == l[3][(top[4] - 2) % 8]
    ]

    if num == 1:
        if is_same[0]:
            turn(top,num,direction)
        else:
            if is_same[1]:
                turn(top,num,direction)
                turn(top,2,-direction)
            else:
                if is_same[2]:
                    turn(top,num,direction)
                    turn(top,2,-direction)
                    turn(top,3,direction)
                else:
                    turn(top,num,direction)
                    turn(top,2,-direction)
                    turn(top,3,direction)
                    turn(top,4,-direction)
            
    elif num == 2:
        turn(top,num,direction)
        if not is_same[0]:
            turn(top,1,-direction)
        if not is_same[1]:
            turn(top,3,-direction)
            if not is_same[2]:
                turn(top,4,direction)

    elif num == 3:
        turn(top,num,direction)
        if not is_same[1]:
            turn(top,2,-direction)
            if not is_same[0]:
                turn(top,1,direction)
        if not is_same[2]:
            turn(top,4,-direction)

    elif num == 4:
        turn(top,num,direction)
        if not is_same[2]:
            turn(top,3,-direction)
            if not is_same[1]:
                turn(top,2,direction)
                if not is_same[0]:
                    turn(top,1,-direction)

    
result = 0
if l[0][top[1]] == 1:
    result += 1
if l[1][top[2]] == 1:
    result += 2
if l[2][top[3]] == 1:
    result += 4
if l[3][top[4]] == 1:
    result += 8

print(result)