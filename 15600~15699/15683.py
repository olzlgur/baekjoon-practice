# 감시 
# 시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
# 1 초	512 MB	40731	19124	11496	43.781%
# 문제
# 스타트링크의 사무실은 1×1크기의 정사각형으로 나누어져 있는 N×M 크기의 직사각형으로 나타낼 수 있다. 사무실에는 총 K개의 CCTV가 설치되어져 있는데, CCTV는 5가지 종류가 있다. 각 CCTV가 감시할 수 있는 방법은 다음과 같다.

				
# 1번	2번	3번	4번	5번
# 1번 CCTV는 한 쪽 방향만 감시할 수 있다. 2번과 3번은 두 방향을 감시할 수 있는데, 2번은 감시하는 방향이 서로 반대방향이어야 하고, 3번은 직각 방향이어야 한다. 4번은 세 방향, 5번은 네 방향을 감시할 수 있다.

# CCTV는 감시할 수 있는 방향에 있는 칸 전체를 감시할 수 있다. 사무실에는 벽이 있는데, CCTV는 벽을 통과할 수 없다. CCTV가 감시할 수 없는 영역은 사각지대라고 한다.

# CCTV는 회전시킬 수 있는데, 회전은 항상 90도 방향으로 해야 하며, 감시하려고 하는 방향이 가로 또는 세로 방향이어야 한다.

# 0 0 0 0 0 0
# 0 0 0 0 0 0
# 0 0 1 0 6 0
# 0 0 0 0 0 0
# 지도에서 0은 빈 칸, 6은 벽, 1~5는 CCTV의 번호이다. 위의 예시에서 1번의 방향에 따라 감시할 수 있는 영역을 '#'로 나타내면 아래와 같다.

# 0 0 0 0 0 0
# 0 0 0 0 0 0
# 0 0 1 # 6 0
# 0 0 0 0 0 0
# 0 0 0 0 0 0
# 0 0 0 0 0 0
# # # 1 0 6 0
# 0 0 0 0 0 0
# 0 0 # 0 0 0
# 0 0 # 0 0 0
# 0 0 1 0 6 0
# 0 0 0 0 0 0
# 0 0 0 0 0 0
# 0 0 0 0 0 0
# 0 0 1 0 6 0
# 0 0 # 0 0 0
# →	←	↑	↓
# CCTV는 벽을 통과할 수 없기 때문에, 1번이 → 방향을 감시하고 있을 때는 6의 오른쪽에 있는 칸을 감시할 수 없다.

# 0 0 0 0 0 0
# 0 2 0 0 0 0
# 0 0 0 0 6 0
# 0 6 0 0 2 0
# 0 0 0 0 0 0
# 0 0 0 0 0 5
# 위의 예시에서 감시할 수 있는 방향을 알아보면 아래와 같다.

# 0 0 0 0 0 #
# # 2 # # # #
# 0 0 0 0 6 #
# 0 6 # # 2 #
# 0 0 0 0 0 #
# # # # # # 5
# 0 0 0 0 0 #
# # 2 # # # #
# 0 0 0 0 6 #
# 0 6 0 0 2 #
# 0 0 0 0 # #
# # # # # # 5
# 0 # 0 0 0 #
# 0 2 0 0 0 #
# 0 # 0 0 6 #
# 0 6 # # 2 #
# 0 0 0 0 0 #
# # # # # # 5
# 0 # 0 0 0 #
# 0 2 0 0 0 #
# 0 # 0 0 6 #
# 0 6 0 0 2 #
# 0 0 0 0 # #
# # # # # # 5
# 왼쪽 상단 2: ↔, 오른쪽 하단 2: ↔	왼쪽 상단 2: ↔, 오른쪽 하단 2: ↕	왼쪽 상단 2: ↕, 오른쪽 하단 2: ↔	왼쪽 상단 2: ↕, 오른쪽 하단 2: ↕
# CCTV는 CCTV를 통과할 수 있다. 아래 예시를 보자.

# 0 0 2 0 3
# 0 6 0 0 0
# 0 0 6 6 0
# 0 0 0 0 0
# 위와 같은 경우에 2의 방향이 ↕ 3의 방향이 ←와 ↓인 경우 감시받는 영역은 다음과 같다.

# # # 2 # 3
# 0 6 # 0 #
# 0 0 6 6 #
# 0 0 0 0 #
# 사무실의 크기와 상태, 그리고 CCTV의 정보가 주어졌을 때, CCTV의 방향을 적절히 정해서, 사각 지대의 최소 크기를 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 사무실의 세로 크기 N과 가로 크기 M이 주어진다. (1 ≤ N, M ≤ 8)

# 둘째 줄부터 N개의 줄에는 사무실 각 칸의 정보가 주어진다. 0은 빈 칸, 6은 벽, 1~5는 CCTV를 나타내고, 문제에서 설명한 CCTV의 종류이다. 

# CCTV의 최대 개수는 8개를 넘지 않는다.

# 출력
# 첫째 줄에 사각 지대의 최소 크기를 출력한다.

# 예제 입력 1  복사
# 4 6
# 0 0 0 0 0 0
# 0 0 0 0 0 0
# 0 0 1 0 6 0
# 0 0 0 0 0 0
# 예제 출력 1  복사
# 20
# 예제 입력 2  복사
# 6 6
# 0 0 0 0 0 0
# 0 2 0 0 0 0
# 0 0 0 0 6 0
# 0 6 0 0 2 0
# 0 0 0 0 0 0
# 0 0 0 0 0 5
# 예제 출력 2  복사
# 15
# 예제 입력 3  복사
# 6 6
# 1 0 0 0 0 0
# 0 1 0 0 0 0
# 0 0 1 0 0 0
# 0 0 0 1 0 0
# 0 0 0 0 1 0
# 0 0 0 0 0 1
# 예제 출력 3  복사
# 6
# 예제 입력 4  복사
# 6 6
# 1 0 0 0 0 0
# 0 1 0 0 0 0
# 0 0 1 5 0 0
# 0 0 5 1 0 0
# 0 0 0 0 1 0
# 0 0 0 0 0 1
# 예제 출력 4  복사
# 2
# 예제 입력 5  복사
# 1 7
# 0 1 2 3 4 5 6
# 예제 출력 5  복사
# 0
# 예제 입력 6  복사
# 3 7
# 4 0 0 0 0 0 0
# 0 0 0 2 0 0 0
# 0 0 0 0 0 0 4
# 예제 출력 6  복사
# 0

import sys, copy
sys.setrecursionlimit(10**8)

input = sys.stdin.readline
office = []
checkOffice = []

h, w = map(int, input().split())
cctv = 0
cnt = 0

for i in range(h):
    office.append(list(map(int, input().split())))
    cctv += (w - (office[i].count(0) + office[i].count(6)))

for i in range(cctv+1):
    checkOffice.append([])

checkOffice[0].append(copy.deepcopy(office))

def goCheck(y, x, map, flag):
    global checkOffice

    if flag == 1:
        dx = [0, 0, 1, -1]
        dy = [1, -1, 0, 0]
        for i in range(4):
            copyMap = copy.deepcopy(map)
            dfs(y, x, dy[i], dx[i], copyMap)
            checkOffice[cnt+1].append(copyMap)

    elif flag == 2:

        copyMap = copy.deepcopy(map)
        dfs(y, x, 0, -1, copyMap)
        dfs(y, x, 0, 1, copyMap)
        checkOffice[cnt+1].append(copyMap)
        copyMap = copy.deepcopy(map)
        dfs(y, x, 1, 0, copyMap)
        dfs(y, x, -1, 0, copyMap)
        checkOffice[cnt+1].append(copyMap)

    elif flag == 3:
        copyMap = copy.deepcopy(map)
        dfs(y, x, 0, 1, copyMap)
        dfs(y, x, -1, 0, copyMap)
        checkOffice[cnt+1].append(copyMap)
        copyMap = copy.deepcopy(map)
        dfs(y, x, 0, 1, copyMap)
        dfs(y, x, 1, 0, copyMap)
        checkOffice[cnt+1].append(copyMap)
        copyMap = copy.deepcopy(map)
        dfs(y, x, 1, 0, copyMap)
        dfs(y, x, 0, -1, copyMap)
        checkOffice[cnt+1].append(copyMap)
        copyMap = copy.deepcopy(map)
        dfs(y, x, -1, 0, copyMap)
        dfs(y, x, 0, -1, copyMap)
        checkOffice[cnt+1].append(copyMap)

    elif flag == 4:
        copyMap = copy.deepcopy(map)
        dfs(y, x, 0, 1, copyMap)
        dfs(y, x, 0, -1, copyMap)
        dfs(y, x, -1, 0, copyMap)
        checkOffice[cnt+1].append(copyMap)

        copyMap = copy.deepcopy(map)
        dfs(y, x, 0, 1, copyMap)
        dfs(y, x, 0, -1, copyMap)
        dfs(y, x, 1, 0, copyMap)
        checkOffice[cnt+1].append(copyMap)

        copyMap = copy.deepcopy(map)
        dfs(y, x, 1, 0, copyMap)
        dfs(y, x, -1, 0, copyMap)
        dfs(y, x, 0, -1, copyMap)
        checkOffice[cnt+1].append(copyMap)

        copyMap = copy.deepcopy(map)
        dfs(y, x, 1, 0, copyMap)
        dfs(y, x, -1, 0, copyMap)
        dfs(y, x, 0, 1, copyMap)
        checkOffice[cnt+1].append(copyMap)

    elif flag == 5:
        copyMap = copy.deepcopy(map)
        dfs(y, x, 1, 0, copyMap)
        dfs(y, x, -1, 0, copyMap)
        dfs(y, x, 0, 1, copyMap)
        dfs(y, x, 0, -1, copyMap)
        checkOffice[cnt+1].append(copyMap)

def dfs(y, x, ty, tx, copyMap):
    if 0 <= y+ty < h and 0 <= x+tx < w and copyMap[y+ty][x+tx] != 6:
        if copyMap[y+ty][x+tx] == 0:
            copyMap[y+ty][x+tx] = 7
        dfs(y+ty, x+tx, ty, tx, copyMap)
    
for i in range(h):
    for j in range(w):
        if office[i][j] != 0 and office[i][j] != 6:
            for c in checkOffice[cnt]:
                temp = copy.deepcopy(c)
                goCheck(i, j, temp, office[i][j])
            cnt += 1
answer = w*h +1

for c in checkOffice[cctv]:
    count = 0
    for r in c:
        count += r.count(0)
    answer = min(answer, count)

print(answer)


