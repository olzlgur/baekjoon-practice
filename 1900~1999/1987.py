# 알파벳 다국어 한국어   
# 시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
# 2 초	256 MB	100506	32623	19809	29.133%
# 문제
# 세로 R칸, 가로 C칸으로 된 표 모양의 보드가 있다. 보드의 각 칸에는 대문자 알파벳이 하나씩 적혀 있고, 좌측 상단 칸 (1행 1열) 에는 말이 놓여 있다.

# 말은 상하좌우로 인접한 네 칸 중의 한 칸으로 이동할 수 있는데, 새로 이동한 칸에 적혀 있는 알파벳은 지금까지 지나온 모든 칸에 적혀 있는 알파벳과는 달라야 한다. 즉, 같은 알파벳이 적힌 칸을 두 번 지날 수 없다.

# 좌측 상단에서 시작해서, 말이 최대한 몇 칸을 지날 수 있는지를 구하는 프로그램을 작성하시오. 말이 지나는 칸은 좌측 상단의 칸도 포함된다.

# 입력
# 첫째 줄에 R과 C가 빈칸을 사이에 두고 주어진다. (1 ≤ R,C ≤ 20) 둘째 줄부터 R개의 줄에 걸쳐서 보드에 적혀 있는 C개의 대문자 알파벳들이 빈칸 없이 주어진다.

# 출력
# 첫째 줄에 말이 지날 수 있는 최대의 칸 수를 출력한다.

# 예제 입력 1  복사
# 2 4
# CAAB
# ADCB
# 예제 출력 1  복사
# 3
# 예제 입력 2  복사
# 3 6
# HFDFFB
# AJHGDH
# DGAGEH
# 예제 출력 2  복사
# 6
# 예제 입력 3  복사
# 5 5
# IEFCJ
# FHFKC
# FFALF
# HFGCF
# HMCHH
# 예제 출력 3  복사
# 10

import sys

input = sys.stdin.readline

r, c = map(int, input().split())

word = [list(map(lambda x:ord(x)-65, input())) for _ in range(r)]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
visited = [0]*26

answer = 0

def dfs(y, x, cnt):
    global answer
    visited[word[y][x]] = 1

    for i in range(4):
        ty = y + dy[i]
        tx = x + dx[i]
        if 0 <= ty < r and 0 <= tx < c and visited[word[ty][tx]] == 0:
            dfs(ty, tx, cnt+1)
    
    answer = max(answer, cnt)
    visited[word[y][x]] = 0

dfs(0, 0, 1)
print(answer)