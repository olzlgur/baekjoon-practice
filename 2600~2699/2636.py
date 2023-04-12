# 치즈 
# 시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
# 1 초	128 MB	23537	12945	9396	54.165%
# 문제
# 아래 <그림 1>과 같이 정사각형 칸들로 이루어진 사각형 모양의 판이 있고, 그 위에 얇은 치즈(회색으로 표시된 부분)가 놓여 있다. 판의 가장자리(<그림 1>에서 네모 칸에 X친 부분)에는 치즈가 놓여 있지 않으며 치즈에는 하나 이상의 구멍이 있을 수 있다.

# 이 치즈를 공기 중에 놓으면 녹게 되는데 공기와 접촉된 칸은 한 시간이 지나면 녹아 없어진다. 치즈의 구멍 속에는 공기가 없지만 구멍을 둘러싼 치즈가 녹아서 구멍이 열리면 구멍 속으로 공기가 들어가게 된다. <그림 1>의 경우, 치즈의 구멍을 둘러싼 치즈는 녹지 않고 ‘c’로 표시된 부분만 한 시간 후에 녹아 없어져서 <그림 2>와 같이 된다.



# <그림 1> 원래 치즈 모양

# 다시 한 시간 후에는 <그림 2>에서 ‘c’로 표시된 부분이 녹아 없어져서 <그림 3>과 같이 된다.



# <그림 2> 한 시간 후의 치즈 모양



# <그림 3> 두 시간 후의 치즈 모양

# <그림 3>은 원래 치즈의 두 시간 후 모양을 나타내고 있으며, 남은 조각들은 한 시간이 더 지나면 모두 녹아 없어진다. 그러므로 처음 치즈가 모두 녹아 없어지는 데는 세 시간이 걸린다. <그림 3>과 같이 치즈가 녹는 과정에서 여러 조각으로 나누어 질 수도 있다.

# 입력으로 사각형 모양의 판의 크기와 한 조각의 치즈가 판 위에 주어졌을 때, 공기 중에서 치즈가 모두 녹아 없어지는 데 걸리는 시간과 모두 녹기 한 시간 전에 남아있는 치즈조각이 놓여 있는 칸의 개수를 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에는 사각형 모양 판의 세로와 가로의 길이가 양의 정수로 주어진다. 세로와 가로의 길이는 최대 100이다. 판의 각 가로줄의 모양이 윗 줄부터 차례로 둘째 줄부터 마지막 줄까지 주어진다. 치즈가 없는 칸은 0, 치즈가 있는 칸은 1로 주어지며 각 숫자 사이에는 빈칸이 하나씩 있다.

# 출력
# 첫째 줄에는 치즈가 모두 녹아서 없어지는 데 걸리는 시간을 출력하고, 둘째 줄에는 모두 녹기 한 시간 전에 남아있는 치즈조각이 놓여 있는 칸의 개수를 출력한다.

# 예제 입력 1  복사
# 13 12
# 0 0 0 0 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 1 1 0 0 0
# 0 1 1 1 0 0 0 1 1 0 0 0
# 0 1 1 1 1 1 1 0 0 0 0 0
# 0 1 1 1 1 1 0 1 1 0 0 0
# 0 1 1 1 1 0 0 1 1 0 0 0
# 0 0 1 1 0 0 0 1 1 0 0 0
# 0 0 1 1 1 1 1 1 1 0 0 0
# 0 0 1 1 1 1 1 1 1 0 0 0
# 0 0 1 1 1 1 1 1 1 0 0 0
# 0 0 1 1 1 1 1 1 1 0 0 0
# 0 0 0 0 0 0 0 0 0 0 0 0
# 예제 출력 1  복사
# 3
# 5

import sys, copy
from collections import deque



def dfs(y, x): 
    visited[y][x] = 1
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    for i in range(4):
        tx = x + dx[i]
        ty = y + dy[i]

        if 0 <= tx < w and 0 <= ty < h and visited[ty][tx] == 0:
            if cheezeMap[ty][tx] == 1:
                meltList.append((ty, tx))
            else:
                dfs(ty, tx)


input = sys.stdin.readline

h, w = map(int, input().split())

cheezeMap = []
meltList = []
cheezeList = deque()

cheezeMap = [list(map(int, input().split())) for _ in range(h)]

Tvisited = [[0]*w for _ in range(h)]


meltList = []
count = 0

while True:
    visited = copy.deepcopy(Tvisited)

    current = 0

    for i in range(h):
        current += cheezeMap[i].count(1) 

    if current == 0:
        break

    for i in range(h):
        if i == 0 or i == h-1:
            for j in range(w):
                if cheezeMap[i][j] == 0 and visited[i][j] == 0:
                    dfs(i, j)
        else :
            dx = [0, h-1]
            for j in range(2):
                x = dx[j]
                if cheezeMap[i][j] == 0 and visited[i][j] == 0:
                    dfs(i, j)

    for tu in meltList:
        cheezeMap[tu[0]][tu[1]] = 0

    ex = current
    count += 1
    meltList = []

print(count)
print(ex)