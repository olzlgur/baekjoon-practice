# 상범 빌딩 다국어 한국어   
# 시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
# 1 초	128 MB	17806	6707	5260	37.173%
# 문제
# 당신은 상범 빌딩에 갇히고 말았다. 여기서 탈출하는 가장 빠른 길은 무엇일까? 상범 빌딩은 각 변의 길이가 1인 정육면체(단위 정육면체)로 이루어져있다. 각 정육면체는 금으로 이루어져 있어 지나갈 수 없거나, 비어있어서 지나갈 수 있게 되어있다. 당신은 각 칸에서 인접한 6개의 칸(동,서,남,북,상,하)으로 1분의 시간을 들여 이동할 수 있다. 즉, 대각선으로 이동하는 것은 불가능하다. 그리고 상범 빌딩의 바깥면도 모두 금으로 막혀있어 출구를 통해서만 탈출할 수 있다.

# 당신은 상범 빌딩을 탈출할 수 있을까? 만약 그렇다면 얼마나 걸릴까?

# 입력
# 입력은 여러 개의 테스트 케이스로 이루어지며, 각 테스트 케이스는 세 개의 정수 L, R, C로 시작한다. L(1 ≤ L ≤ 30)은 상범 빌딩의 층 수이다. R(1 ≤ R ≤ 30)과 C(1 ≤ C ≤ 30)는 상범 빌딩의 한 층의 행과 열의 개수를 나타낸다.

# 그 다음 각 줄이 C개의 문자로 이루어진 R개의 행이 L번 주어진다. 각 문자는 상범 빌딩의 한 칸을 나타낸다. 금으로 막혀있어 지나갈 수 없는 칸은 '#'으로 표현되고, 비어있는 칸은 '.'으로 표현된다. 당신의 시작 지점은 'S'로 표현되고, 탈출할 수 있는 출구는 'E'로 표현된다. 각 층 사이에는 빈 줄이 있으며, 입력의 끝은 L, R, C가 모두 0으로 표현된다. 시작 지점과 출구는 항상 하나만 있다.

# 출력
# 각 빌딩에 대해 한 줄씩 답을 출력한다. 만약 당신이 탈출할 수 있다면 다음과 같이 출력한다.

# Escaped in x minute(s).
# 여기서 x는 상범 빌딩을 탈출하는 데에 필요한 최단 시간이다.

# 만일 탈출이 불가능하다면, 다음과 같이 출력한다.

# Trapped!
# 예제 입력 1  복사
# 3 4 5
# S....
# .###.
# .##..
# ###.#

# #####
# #####
# ##.##
# ##...

# #####
# #####
# #.###
# ####E

# 1 3 3
# S##
# #E#
# ###

# 0 0 0
# 예제 출력 1  복사
# Escaped in 11 minute(s).
# Trapped!

import sys
from collections import deque

input = sys.stdin.readline
dx = [0, 0, 1, -1, 0, 0]
dy = [0, 0, 0, 0, 1, -1]
dz = [1, -1, 0, 0, 0, 0]

while True:
    L, R, C = map(int, input().split())
    apart = []
    visited = []
    q = deque()

    if(L == 0):
        break
    
    for idx1 in range(L):
        apart.append([])
        visited.append([])
        for idx2 in range(R):
            apart[idx1].append(list(input().rstrip()))
            if 'S' in apart[idx1][idx2]:
                z = idx1
                y = idx2
                x = apart[idx1][idx2].index('S')
            visited[idx1].append([0]*C)
        input()
    
    visited[z][y][x] = 1
    q.append((0, z, y, x))
    answer = 0
    flag = 0

    while q:
        cnt, az, ay, ax  = q.popleft()

        for i in range(6):
            tz = az + dz[i]
            ty = ay + dy[i]
            tx = ax + dx[i]

            if 0 <= tz <L and 0 <= ty <R and 0 <= tx <C and visited[tz][ty][tx] == 0:
                if apart[tz][ty][tx] == '.':
                    visited[tz][ty][tx] = 1
                    q.append((cnt + 1, tz, ty, tx))
                elif apart[tz][ty][tx] == 'E':
                    answer = cnt+1
                    flag = 1
                    break
        if flag == 1:
            break
    if answer == 0:
        print('Trapped!')
    else:
        answer = 'Escaped in '+ str(answer) + ' minute(s).'
        print(answer)
    

    
    
