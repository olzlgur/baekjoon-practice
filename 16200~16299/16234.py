# 인구 이동
# 시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
# 2 초	512 MB	58571	23686	13817	37.295%
# 문제
# N×N크기의 땅이 있고, 땅은 1×1개의 칸으로 나누어져 있다. 각각의 땅에는 나라가 하나씩 존재하며, r행 c열에 있는 나라에는 A[r][c]명이 살고 있다. 인접한 나라 사이에는 국경선이 존재한다. 모든 나라는 1×1 크기이기 때문에, 모든 국경선은 정사각형 형태이다.

# 오늘부터 인구 이동이 시작되는 날이다.

# 인구 이동은 하루 동안 다음과 같이 진행되고, 더 이상 아래 방법에 의해 인구 이동이 없을 때까지 지속된다.

# 국경선을 공유하는 두 나라의 인구 차이가 L명 이상, R명 이하라면, 두 나라가 공유하는 국경선을 오늘 하루 동안 연다.
# 위의 조건에 의해 열어야하는 국경선이 모두 열렸다면, 인구 이동을 시작한다.
# 국경선이 열려있어 인접한 칸만을 이용해 이동할 수 있으면, 그 나라를 오늘 하루 동안은 연합이라고 한다.
# 연합을 이루고 있는 각 칸의 인구수는 (연합의 인구수) / (연합을 이루고 있는 칸의 개수)가 된다. 편의상 소수점은 버린다.
# 연합을 해체하고, 모든 국경선을 닫는다.
# 각 나라의 인구수가 주어졌을 때, 인구 이동이 며칠 동안 발생하는지 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 N, L, R이 주어진다. (1 ≤ N ≤ 50, 1 ≤ L ≤ R ≤ 100)

# 둘째 줄부터 N개의 줄에 각 나라의 인구수가 주어진다. r행 c열에 주어지는 정수는 A[r][c]의 값이다. (0 ≤ A[r][c] ≤ 100)

# 인구 이동이 발생하는 일수가 2,000번 보다 작거나 같은 입력만 주어진다.

# 출력
# 인구 이동이 며칠 동안 발생하는지 첫째 줄에 출력한다.

# 예제 입력 1  복사
# 2 20 50
# 50 30
# 20 40
# 예제 출력 1  복사
# 1

import sys
from collections import deque


input = sys.stdin.readline

N, L, R = map(int, input().split())
world = []

for _ in range(N):
    world.append(list(map(int, input().split())))

q = deque()

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

answer = 0

while True:
    flag = 0
    cnt = 0
    visited = []
    for _ in range(N):
        visited.append([0]*N)

    for idx1 in range(N):
        for idx2 in range(N):
            if visited[idx1][idx2] == 0:
                checkList = []
                sum = 0
                visited[idx1][idx2] = 1
                checkList.append((idx1, idx2))
                sum += world[idx1][idx2]
                q.append((idx1, idx2))
                while q:
                    y, x = q.popleft()
                    for i in range(4):
                        ty = y + dy[i]
                        tx = x + dx[i]
                        if 0 <= ty < N and 0 <= tx < N and visited[ty][tx] == 0 and L <= abs(world[y][x]- world[ty][tx]) <= R:
                            visited[ty][tx] = 1
                            sum += world[ty][tx]
                            q.append((ty,tx))
                            checkList.append((ty,tx))
                avg = sum // len(checkList)
                
                if len(checkList) != 1:
                    flag = 1
                    for c in checkList:
                        world[c[0]][c[1]] = avg
    if flag == 0:
        break
    answer += 1

print(answer)