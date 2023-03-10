# 적록색약 다국어 한국어   
# 시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
# 1 초	128 MB	47244	27171	20772	56.476%
# 문제
# 적록색약은 빨간색과 초록색의 차이를 거의 느끼지 못한다. 따라서, 적록색약인 사람이 보는 그림은 아닌 사람이 보는 그림과는 좀 다를 수 있다.

# 크기가 N×N인 그리드의 각 칸에 R(빨강), G(초록), B(파랑) 중 하나를 색칠한 그림이 있다. 그림은 몇 개의 구역으로 나뉘어져 있는데, 구역은 같은 색으로 이루어져 있다. 또, 같은 색상이 상하좌우로 인접해 있는 경우에 두 글자는 같은 구역에 속한다. (색상의 차이를 거의 느끼지 못하는 경우도 같은 색상이라 한다)

# 예를 들어, 그림이 아래와 같은 경우에

# RRRBB
# GGBBB
# BBBRR
# BBRRR
# RRRRR
# 적록색약이 아닌 사람이 봤을 때 구역의 수는 총 4개이다. (빨강 2, 파랑 1, 초록 1) 하지만, 적록색약인 사람은 구역을 3개 볼 수 있다. (빨강-초록 2, 파랑 1)

# 그림이 입력으로 주어졌을 때, 적록색약인 사람이 봤을 때와 아닌 사람이 봤을 때 구역의 수를 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 N이 주어진다. (1 ≤ N ≤ 100)

# 둘째 줄부터 N개 줄에는 그림이 주어진다.

# 출력
# 적록색약이 아닌 사람이 봤을 때의 구역의 개수와 적록색약인 사람이 봤을 때의 구역의 수를 공백으로 구분해 출력한다.

# 예제 입력 1  복사
# 5
# RRRBB
# GGBBB
# BBBRR
# BBRRR
# RRRRR
# 예제 출력 1  복사
# 4 3

import sys, copy
sys.setrecursionlimit(10**8)
input = sys.stdin.readline

n = int(input())

def dfs1(y, x):
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]
    visited1[y][x] = 1
    for i in range(4):
        tx = x + dx[i]
        ty = y + dy[i]
        if 0 <= tx < n and 0 <= ty < n and visited1[ty][tx] == 0 and rgbMap1[ty][tx] == rgbMap1[y][x]:
            dfs1(ty, tx)

def dfs2(y, x):
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]
    visited2[y][x] = 1
    for i in range(4):
        tx = x + dx[i]
        ty = y + dy[i]
        if 0 <= tx < n and 0 <= ty < n and visited2[ty][tx] == 0 and rgbMap2[ty][tx] == rgbMap2[y][x]:
            dfs2(ty, tx)

rgbMap1 = []
visited1 = []
visited2 = []
for _ in range(n):
    rgbMap1.append(list(map(str, input().rstrip())))
    visited1.append([0]*(n))
    visited2.append([0]*(n))

rgbMap2 = copy.deepcopy(rgbMap1)
for i in range(n):
    for j in range(n):
        if rgbMap2[i][j] == 'R' :
            rgbMap2[i][j] = 'G'

result1, result2 = 0, 0

for i in range(n):
    for j in range(n):
        if visited1[i][j] == 0 :
            result1 += 1
            dfs1(i, j)
        if visited2[i][j] == 0:
            result2 += 1
            dfs2(i, j)

print(result1, result2)