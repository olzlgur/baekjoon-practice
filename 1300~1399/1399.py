# 전쟁 - 전투
# 시간 제한 메모리 제한  제출  정답  맞힌 사람   정답 비율
# 2 초   128 MB  10075   3899    3124    37.711%
# 문제
# 전쟁은 어느덧 전면전이 시작되었다. 결국 전투는 난전이 되었고, 우리 병사와 적국 병사가 섞여 싸우게 되었다. 그러나 당신의 병사들은 흰색 옷을 입고, 적국의 병사들은 파란색 옷을 입었기 때문에 서로가 적인지 아군인지는 구분할 수 있다. 문제는 같은 팀의 병사들은 모이면 모일수록 강해진다는 사실이다.

# N명이 뭉쳐있을 때는 N2의 위력을 낼 수 있다. 과연 지금 난전의 상황에서는 누가 승리할 것인가? 단, 같은 팀의 병사들이 대각선으로만 인접한 경우는 뭉쳐 있다고 보지 않는다.

# 입력
# 첫째 줄에는 전쟁터의 가로 크기 N, 세로 크기 M(1 ≤ N, M ≤ 100)이 주어진다. 그 다음 두 번째 줄에서 M+1번째 줄에는 각각 (X, Y)에 있는 병사들의 옷색이 띄어쓰기 없이 주어진다. 모든 자리에는 병사가 한 명 있다. B는 파란색, W는 흰색이다. 당신의 병사와 적국의 병사는 한 명 이상 존재한다.

# 출력
# 첫 번째 줄에 당신의 병사의 위력의 합과 적국의 병사의 위력의 합을 출력한다.

# 예제 입력 1 
# 5 5
# WBWWW
# WWWWW
# BBBBB
# BBBWW
# WWWWW
# 예제 출력 1 
# 130

w, h = map(int, input().split())
war = []
visited = []
dic = {"W": 0, "B": 0}
for i in range(h):
    war.append(input())
    visited.append([0]*w)
power = 0
def solution():
    global power
    for i in range(h):
        for j in range(w):
            if visited[i][j] == 0:
                power = 1
                dfs(j, i, war[i][j])
                dic[war[i][j]] += power*power
    print(dic['W'], dic['B'])

def dfs(x, y, color):
    global power
    global visited
    visited[y][x] = 1
    if x + 1 < w and war[y][x+1] == color and visited[y][x+1] == 0:
        power += 1
        dfs(x+1, y, color)
    if y + 1 < h and war[y+1][x] == color and visited[y+1][x] == 0:
        power += 1
        dfs(x, y+1, color)
    if x -1 >= 0 and war[y][x-1] == color and visited[y][x-1] == 0:
        power += 1
        dfs(x-1, y, color)
    if y -1 >= 0 and war[y-1][x] == color and visited[y-1][x] == 0:    
        power += 1
        dfs(x, y-1, color)
    return
solution()