import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
answer = -1
visited = []

for i in range(N):
    visited.append([[0, 0] for _ in range(M)])

q = deque()
if N == 1 and M == 1:
    answer = 1
else:
    q.append((0, 0, 1, 0))

brickMap = [list(input().rstrip()) for _ in range(N)]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

while q:
    y, x, cnt, brick = q.popleft()

    for i in range(4):
        ty = y + dy[i]
        tx = x + dx[i]
        if 0 <= ty < N and 0 <= tx < M:
            if brickMap[ty][tx] == '1' and visited[ty][tx][1] == 0 and brick == 0:
                q.append((ty, tx, cnt+1, 1))
                visited[ty][tx][1] = 1
            elif ty == N-1 and tx == M-1 :
                answer = cnt+1
                q = deque()
                break
            elif brickMap[ty][tx] == '0':
                if visited[ty][tx][0] == 0 and brick == 0:
                    q.append((ty, tx, cnt+1, 0))
                    visited[ty][tx][0] = 1
                elif visited[ty][tx][1] == 0 and brick == 1:
                    q.append((ty, tx, cnt+1, 1))
                    visited[ty][tx][1] = 1

print(answer)