# Puyo Puyo
# 시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
# 1 초	256 MB	19118	7549	5460	37.906%
# 문제
# 뿌요뿌요의 룰은 다음과 같다.

# 필드에 여러 가지 색깔의 뿌요를 놓는다. 뿌요는 중력의 영향을 받아 아래에 바닥이나 다른 뿌요가 나올 때까지 아래로 떨어진다.

# 뿌요를 놓고 난 후, 같은 색 뿌요가 4개 이상 상하좌우로 연결되어 있으면 연결된 같은 색 뿌요들이 한꺼번에 없어진다. 이때 1연쇄가 시작된다.

# 뿌요들이 없어지고 나서 위에 다른 뿌요들이 있다면, 역시 중력의 영향을 받아 차례대로 아래로 떨어지게 된다.

# 아래로 떨어지고 나서 다시 같은 색의 뿌요들이 4개 이상 모이게 되면 또 터지게 되는데, 터진 후 뿌요들이 내려오고 다시 터짐을 반복할 때마다 1연쇄씩 늘어난다.

# 터질 수 있는 뿌요가 여러 그룹이 있다면 동시에 터져야 하고 여러 그룹이 터지더라도 한번의 연쇄가 추가된다.

# 남규는 최근 뿌요뿌요 게임에 푹 빠졌다. 이 게임은 1:1로 붙는 대전게임이라 잘 쌓는 것도 중요하지만, 상대방이 터뜨린다면 연쇄가 몇 번이 될지 바로 파악할 수 있는 능력도 필요하다. 하지만 아직 실력이 부족하여 남규는 자기 필드에만 신경 쓰기 바쁘다. 상대방의 필드가 주어졌을 때, 연쇄가 몇 번 연속으로 일어날지 계산하여 남규를 도와주자!

# 입력
# 총 12개의 줄에 필드의 정보가 주어지며, 각 줄에는 6개의 문자가 있다.

# 이때 .은 빈공간이고 .이 아닌것은 각각의 색깔의 뿌요를 나타낸다.

# R은 빨강, G는 초록, B는 파랑, P는 보라, Y는 노랑이다.

# 입력으로 주어지는 필드는 뿌요들이 전부 아래로 떨어진 뒤의 상태이다. 즉, 뿌요 아래에 빈 칸이 있는 경우는 없다.

# 출력
# 현재 주어진 상황에서 몇연쇄가 되는지 출력한다. 하나도 터지지 않는다면 0을 출력한다.

# 예제 입력 1 
# ......
# ......
# ......
# ......
# ......
# ......
# ......
# ......
# .Y....
# .YG...
# RRYG..
# RRYGG.
# 예제 출력 1 
# 3

# 탐색하면서 count, 박살, 재탐색 
import copy
gamemap = []
visited = []
for i in range(12):
    gamemap.append(list(input()))
    visited.append([0]*6)

def dfs(y, x, color):
    global tempvisited, count
    tempvisited[y][x] = 1
    count += 1

    if y + 1 < 12 and color == gamemap[y+1][x] and tempvisited[y+1][x] == 0 :
        dfs(y+1, x, color)
    if x + 1 < 6 and color == gamemap[y][x+1] and tempvisited[y][x+1] == 0 :
        dfs(y, x+1, color)
    if y - 1 >= 0 and color == gamemap[y-1][x] and tempvisited[y-1][x] == 0 :
        dfs(y-1, x, color)
    if x - 1 >= 0 and color == gamemap[y][x-1] and tempvisited[y][x-1] == 0 :
        dfs(y, x-1, color)


def breakColor(y, x, color):
    gamemap[y][x] = '.'

    if y + 1 < 12 and color == gamemap[y+1][x]:
        breakColor(y+1, x, color)
    if x + 1 < 6 and color == gamemap[y][x+1]:
        breakColor(y, x+1, color)
    if y - 1 >= 0 and color == gamemap[y-1][x]:
        breakColor(y-1, x, color)
    if x - 1 >= 0 and color == gamemap[y][x-1]:
        breakColor(y, x-1, color)
    return 

def reuseMap():
    global gamemap
    while True:
        count = 0
        for i in range(6):
            for j in range(11, 0, -1) :
                if gamemap[j][i] == '.' and gamemap[j-1][i] != '.' :
                    gamemap[j][i] = gamemap[j-1][i]
                    gamemap[j-1][i] = '.'
                    count += 1
        if count == 0:
            break
    return

answer = 0
count = 0
temp = []
while True:
    tempvisited = copy.deepcopy(visited)
    for i in range(12):
        for j in range(6):
            if gamemap[i][j] != '.' and tempvisited[i][j] == 0:
                dfs(i, j, gamemap[i][j])
                if count >= 4 :
                    temp.append((i,j))
                count = 0
    if len(temp) > 0 :
        answer += 1
        for tu in temp :
            breakColor(tu[0], tu[1], gamemap[tu[0]][tu[1]])
        temp = []
        reuseMap()
    else :
        break
print(answer)
