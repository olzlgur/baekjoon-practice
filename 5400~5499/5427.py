# 불 다국어 한국어   
# 시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
# 1 초	256 MB	32547	8479	5574	24.008%
# 문제
# 상근이는 빈 공간과 벽으로 이루어진 건물에 갇혀있다. 건물의 일부에는 불이 났고, 상근이는 출구를 향해 뛰고 있다.

# 매 초마다, 불은 동서남북 방향으로 인접한 빈 공간으로 퍼져나간다. 벽에는 불이 붙지 않는다. 상근이는 동서남북 인접한 칸으로 이동할 수 있으며, 1초가 걸린다. 상근이는 벽을 통과할 수 없고, 불이 옮겨진 칸 또는 이제 불이 붙으려는 칸으로 이동할 수 없다. 상근이가 있는 칸에 불이 옮겨옴과 동시에 다른 칸으로 이동할 수 있다.

# 빌딩의 지도가 주어졌을 때, 얼마나 빨리 빌딩을 탈출할 수 있는지 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 테스트 케이스의 개수가 주어진다. 테스트 케이스는 최대 100개이다.

# 각 테스트 케이스의 첫째 줄에는 빌딩 지도의 너비와 높이 w와 h가 주어진다. (1 ≤ w,h ≤ 1000)

# 다음 h개 줄에는 w개의 문자, 빌딩의 지도가 주어진다.

# '.': 빈 공간
# '#': 벽
# '@': 상근이의 시작 위치
# '*': 불
# 각 지도에 @의 개수는 하나이다.

# 출력
# 각 테스트 케이스마다 빌딩을 탈출하는데 가장 빠른 시간을 출력한다. 빌딩을 탈출할 수 없는 경우에는 "IMPOSSIBLE"을 출력한다.

# 예제 입력 1  복사
# 5
# 4 3
# ####
# #*@.
# ####
# 7 6
# ###.###
# #*#.#*#
# #.....#
# #.....#
# #..@..#
# #######
# 7 4
# ###.###
# #....*#
# #@....#
# .######
# 5 5
# .....
# .***.
# .*@*.
# .***.
# .....
# 3 3
# ###
# #@#
# ###
# 예제 출력 1  복사
# 2
# 5
# IMPOSSIBLE
# IMPOSSIBLE
# IMPOSSIBLE

import sys, copy

input = sys.stdin.readline

n = int(input())
answer = [0] * n
for p in range(n):
    count = 0
    w, h = map(int, input().split())
    queue = []
    building = []
    fireVisited = []
    visited = []
    for i in range(h):
        building.append(list(input()))
        fireVisited.append([0]*w)
        visited.append([0]*w)
        if building[i].count('@') == 1 :
            y, x = i, building[i].index('@')
            building[y][x] = '.'
    fireQueue = []
    for i in range(h):
        for j in range(w):
            if building[i][j] == '*' :
                fireQueue.append((i, j))
    fireQueue2 = []
    queue.append((y, x))
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    while queue :
        fireQueue2 = copy.deepcopy(fireQueue)
        fireQueue = []
        while fireQueue2:
            y, x = fireQueue2.pop()
            for i in range(4):
                ty = y + dy[i]
                tx = x + dx[i]
                if 0 <= ty < h and 0 <= tx < w and building[ty][tx] == '.' and fireVisited[ty][tx] == 0:
                    fireVisited[ty][tx] = 1
                    fireQueue.append((ty, tx))
                    building[ty][tx] = '*'
        queue2 = copy.deepcopy(queue)
        queue = []
        while queue2 :
            y, x = queue2.pop()
            if y == 0 or x == 0 or y == h-1 or x == w-1 :
                answer[p] = count + 1
                queue = []
                break
            for i in range(4):
                ty = y + dy[i]
                tx = x + dx[i]
                if 0 <= ty < h and 0 <= tx < w and building[ty][tx] == '.' and visited[ty][tx] == 0:
                    visited[ty][tx] = 1
                    queue.append((ty, tx))
        count += 1
for a in answer :
    if a == 0 :
        print("IMPOSSIBLE")
    else :
        print(a)