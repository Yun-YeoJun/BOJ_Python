import sys
import copy
input = sys.stdin.readline

r,c,t = map(int,input().split())

dust_info = [list(map(int,input().split())) for i in range(r)]

air_cleaner = -1
air_cleaner_position = []
empty_cell = 0

# 상하좌우
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def spread_of_dust():
    global dust_info
    new_dust_info = copy.deepcopy(dust_info)

    for x in range(r):
        for y in range(c):
            if dust_info[x][y] == air_cleaner or dust_info[x][y] == empty_cell:
                continue

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if nx < 0 or nx >= r or ny < 0 or ny >= c:
                    continue

                if dust_info[nx][ny] == air_cleaner:
                    continue

                amount_of_spread_dust = dust_info[x][y] // 5

                new_dust_info[nx][ny] += amount_of_spread_dust
                new_dust_info[x][y] -= amount_of_spread_dust

    dust_info = copy.deepcopy(new_dust_info)

def find_air_cleaner_postion():
    air_cleaner_position = []

    for x in range(r):
        for y in range(c):
            if dust_info[x][y] == -1:
                air_cleaner_position.append((x,y))

    return air_cleaner_position
      



def counterclockwise_rotation(x,y):
    global r
    global c

    prev = dust_info[x][y + 1]
    next = -1
    dust_info[x][1] = 0

    for i in range(y+1,c-1):
        next = dust_info[x][i + 1]
        dust_info[x][i + 1] = prev
        prev = next

    for i in reversed(range(1,x + 1)):
        next = dust_info[i - 1][c - 1]
        dust_info[i - 1][c - 1] = prev
        prev = next

    for i in reversed(range(1,c)):
        next = dust_info[0][i - 1]
        dust_info[0][i - 1] = prev
        prev = next

    for i in range(x - 1):
        next = dust_info[i + 1][0]
        dust_info[i + 1][0] = prev
        prev = next
    

def clockwise_rotation(x,y):
    global r
    global c

    prev = dust_info[x][y + 1]
    next = -1
    dust_info[x][1] = 0

    for i in range(1,c - 1):
        next = dust_info[x][i + 1]
        dust_info[x][i + 1] = prev
        prev = next

    for i in range(x, r - 1):
        next = dust_info[i + 1][c - 1]
        dust_info[i + 1][c - 1] = prev
        prev = next

    for i in reversed(range(1,c)):
        next = dust_info[r - 1][i - 1]
        dust_info[r - 1][i - 1] = prev
        prev = next

    for i in reversed(range(x + 2,r)):
        next = dust_info[i - 1][0]
        dust_info[i - 1][0] = prev
        prev = next


def air_cleaner_work():
    global air_cleaner_position
    
    up_side_x, up_side_y = air_cleaner_position[0]
    down_side_x, down_side_y = air_cleaner_position[1]

    counterclockwise_rotation(up_side_x,up_side_y)
    clockwise_rotation(down_side_x,down_side_y)


air_cleaner_position = find_air_cleaner_postion()

def calc_sum_of_dust():
    global dust_info
    result = 0
    for i in range(r):
        for j in range(c):
            if dust_info[i][j] == -1:
                continue
            result += dust_info[i][j]

    return result

for time in range(t):
    spread_of_dust()
    air_cleaner_work()

print(calc_sum_of_dust())