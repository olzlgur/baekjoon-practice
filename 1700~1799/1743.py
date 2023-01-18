# 음식물 피하기 다국어
# 시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
# 2 초	128 MB	13374	6278	5012	46.828%
# 문제
# 코레스코 콘도미니엄 8층은 학생들이 3끼의 식사를 해결하는 공간이다. 그러나 몇몇 비양심적인 학생들의 만행으로 음식물이 통로 중간 중간에 떨어져 있다. 이러한 음식물들은 근처에 있는 것끼리 뭉치게 돼서 큰 음식물 쓰레기가 된다. 

# 이 문제를 출제한 선생님은 개인적으로 이러한 음식물을 실내화에 묻히는 것을 정말 진정으로 싫어한다. 참고로 우리가 구해야 할 답은 이 문제를 낸 조교를 맞추는 것이 아니다. 

# 통로에 떨어진 음식물을 피해가기란 쉬운 일이 아니다. 따라서 선생님은 떨어진 음식물 중에 제일 큰 음식물만은 피해 가려고 한다. 

# 선생님을 도와 제일 큰 음식물의 크기를 구해서 “10ra"를 외치지 않게 도와주자.

# 입력
# 첫째 줄에 통로의 세로 길이 N(1 ≤ N ≤ 100)과 가로 길이 M(1 ≤ M ≤ 100) 그리고 음식물 쓰레기의 개수 K(1 ≤ K ≤ N×M)이 주어진다.  그리고 다음 K개의 줄에 음식물이 떨어진 좌표 (r, c)가 주어진다.

# 좌표 (r, c)의 r은 위에서부터, c는 왼쪽에서부터가 기준이다. 입력으로 주어지는 좌표는 중복되지 않는다.

# 출력
# 첫째 줄에 음식물 중 가장 큰 음식물의 크기를 출력하라.

# 예제 입력 1 
# 3 4 5
# 3 2
# 2 2
# 3 1
# 2 3
# 1 1
# 예제 출력 1 
# 4
# 힌트
# # . . .
# . # # .
# # # . .
# 위와 같이 음식물이 떨어져있고 제일큰 음식물의 크기는 4가 된다. (인접한 것은 붙어서 크게 된다고 나와 있음. 대각선으로는 음식물 끼리 붙을수 없고 상하좌우로만 붙을수 있다.)
import sys
sys.setrecursionlimit(100000)

ye, xe, n = map(int, input().split())
condo = []
visited = []
for i in range(ye+1):
    condo.append([0]*(xe+1))
    visited.append([0]*(xe+1))
for i in range(n):
    yp, xp = map(int, input().split())
    condo[yp][xp] = 1   
ts = 1

def solution():
    global ts
    answer = 0
    for i in range(1, ye + 1):
        for j in range(1, xe + 1):
            if condo[i][j] == 1 and visited[i][j] == 0 :
                dfs(i, j)
                answer = max(answer, ts)
                ts = 1
    print(answer)


def dfs(y, x):
    global ts
    visited[y][x] = 1

    if y + 1 <= ye :
        if condo[y+1][x] == 1 and visited[y+1][x] == 0:
            ts += 1
            dfs(y+1, x)
    if y - 1 > 0 :
        if condo[y-1][x] == 1 and visited[y-1][x] == 0:
            ts += 1
            dfs(y-1, x)
    if x + 1 <= xe :
        if condo[y][x+1] == 1 and visited[y][x+1] == 0:
            ts += 1
            dfs(y, x+1)
    if x - 1 > 0 :
        if condo[y][x-1] == 1 and visited[y][x-1] == 0:
            ts += 1
            dfs(y, x-1)

solution()
