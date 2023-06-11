# 두 동전
# 시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
# 2 초	512 MB	9536	4198	2847	42.360%
# 문제
# N×M 크기의 보드와 4개의 버튼으로 이루어진 게임이 있다. 보드는 1×1크기의 정사각형 칸으로 나누어져 있고, 각각의 칸은 비어있거나, 벽이다. 두 개의 빈 칸에는 동전이 하나씩 놓여져 있고, 두 동전의 위치는 다르다.

# 버튼은 "왼쪽", "오른쪽", "위", "아래"와 같이 4가지가 있다. 버튼을 누르면 두 동전이 버튼에 쓰여 있는 방향으로 동시에 이동하게 된다.

# 동전이 이동하려는 칸이 벽이면, 동전은 이동하지 않는다.
# 동전이 이동하려는 방향에 칸이 없으면 동전은 보드 바깥으로 떨어진다.
# 그 외의 경우에는 이동하려는 방향으로 한 칸 이동한다.이동하려는 칸에 동전이 있는 경우에도 한 칸 이동한다.
# 두 동전 중 하나만 보드에서 떨어뜨리기 위해 버튼을 최소 몇 번 눌러야하는지 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 보드의 세로 크기 N과 가로 크기 M이 주어진다. (1 ≤ N, M ≤ 20)

# 둘째 줄부터 N개의 줄에는 보드의 상태가 주어진다.

# o: 동전
# .: 빈 칸
# #: 벽
# 동전의 개수는 항상 2개이다.

# 출력
# 첫째 줄에 두 동전 중 하나만 보드에서 떨어뜨리기 위해 눌러야 하는 버튼의 최소 횟수를 출력한다. 만약, 두 동전을 떨어뜨릴 수 없거나, 버튼을 10번보다 많이 눌러야 한다면, -1을 출력한다.

# 예제 입력 1  복사
# 1 2
# oo
# 예제 출력 1  복사
# 1
# 예제 입력 2  복사
# 6 2
# .#
# .#
# .#
# o#
# o#
# ##
# 예제 출력 2  복사
# 4
# 예제 입력 3  복사
# 6 2
# ..
# ..
# ..
# o#
# o#
# ##
# 예제 출력 3  복사
# 3
# 예제 입력 4  복사
# 5 3
# ###
# .o.
# ###
# .o.
# ###
# 예제 출력 4  복사
# -1
# 예제 입력 5  복사
# 5 3
# ###
# .o.
# #.#
# .o.
# ###
# 예제 출력 5  복사
# 3

import sys

input = sys.stdin.readline

N, M = map(int, input().split())
coinMap = []
q =[]

for i in range(N):
    coinMap.append(list(input().rstrip()))
    if 'o' in coinMap[i]:
        q.append((1, i, coinMap[i].index('o')))
        if 'o' in coinMap[i][coinMap[i].index('o')+1:] :
            q.append((1, i, "".join(coinMap[i]).rindex('o')))

answer = -1
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
visitPoint = []

while q:
    cnt, ty1, tx1 = q.pop(0)
    cnt, ty2, tx2 = q.pop(0)
    if 10 < cnt:
        break
    for i in range(4):
        x1 = tx1 + dx[i]
        x2 = tx2 + dx[i]
        y1 = ty1 + dy[i]
        y2 = ty2 + dy[i]
        if ((x1 < 0 or M <= x1 or y1 < 0 or N <= y1) and (0 <= x2 < M and 0 <= y2 < N)) or ((x2 < 0 or M <= x2 or y2 < 0 or N <= y2) and (0 <= x1 < M and 0 <= y1 < N)):
            answer = cnt
            q = []
            break
        elif 0 <= x1 < M and 0 <= y1 < N and 0 <= x2 < M and 0 <= y2 <N:
            if coinMap[y1][x1] == '#':
                y1 -= dy[i]
                x1 -= dx[i]
            if coinMap[y2][x2] == '#':
                y2 -= dy[i]
                x2 -= dx[i]
            
            if (y1 != y2 or x1 != x2) and (y1, x1, y2, x2) not in visitPoint :
                q.append((cnt + 1, y1, x1))
                q.append((cnt + 1, y2, x2))
                visitPoint.append((y1, x1, y2, x2))

print(answer)
