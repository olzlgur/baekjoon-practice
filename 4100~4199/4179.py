# 불! 다국어 한국어   
# 시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
# 1 초	256 MB	36460	8071	5494	21.085%
# 문제
# 지훈이는 미로에서 일을 한다. 지훈이를 미로에서 탈출하도록 도와주자!

# 미로에서의 지훈이의 위치와 불이 붙은 위치를 감안해서 지훈이가 불에 타기전에 탈출할 수 있는지의 여부, 그리고 얼마나 빨리 탈출할 수 있는지를 결정해야한다.

# 지훈이와 불은 매 분마다 한칸씩 수평또는 수직으로(비스듬하게 이동하지 않는다) 이동한다.

# 불은 각 지점에서 네 방향으로 확산된다.

# 지훈이는 미로의 가장자리에 접한 공간에서 탈출할 수 있다.

# 지훈이와 불은 벽이 있는 공간은 통과하지 못한다.

# 입력
# 입력의 첫째 줄에는 공백으로 구분된 두 정수 R과 C가 주어진다. 단, 1 ≤ R, C ≤ 1000 이다. R은 미로 행의 개수, C는 열의 개수이다.

# 다음 입력으로 R줄동안 각각의 미로 행이 주어진다.

# 각각의 문자들은 다음을 뜻한다.

# #: 벽
# .: 지나갈 수 있는 공간
# J: 지훈이의 미로에서의 초기위치 (지나갈 수 있는 공간)
# F: 불이 난 공간
# J는 입력에서 하나만 주어진다.

# 출력
# 지훈이가 불이 도달하기 전에 미로를 탈출 할 수 없는 경우 IMPOSSIBLE 을 출력한다.

# 지훈이가 미로를 탈출할 수 있는 경우에는 가장 빠른 탈출시간을 출력한다.

# 예제 입력 1  복사
# 4 4
# ####
# #JF#
# #..#
# #..#
# 예제 출력 1  복사
# 3

import sys, copy

input = sys.stdin.readline

def solution():
    h, w = map(int, input().split())
    miro = []
    q = []
    fireQ = []
    checkQ = []
    checkFireQ = []
    visited = []
    for i in range(h):
        miro.append(list(input()))    
        visited.append([0]*w)
        if miro[i].count('J') == 1:
            if i == 0 or i == h -1 or miro[i].index('J') == 0 or miro[i].index('J') == w-1:
                print(1)
                return
            checkQ.append((i, miro[i].index('J')))
        if miro[i].count('F') == 1:
            checkFireQ.append((i, miro[i].index('F')))


    
    count = 1

    while checkQ:
        q = copy.deepcopy(checkQ)
        checkQ = []
        
        fireQ = copy.deepcopy(checkFireQ)
        checkFireQ = []
        count += 1
        while fireQ:
            y, x = fireQ.pop(0)
            dx = [0, 0, 1, -1]
            dy = [1, -1, 0, 0]
            for i in range(4):
                tx = x + dx[i]
                ty = y + dy[i]
                if 0 <= tx < w and 0 <= ty <h and visited[ty][tx] == 0 and miro[ty][tx] != '#':
                    visited[ty][tx] = 1
                    checkFireQ.append((ty, tx))
                    miro[ty][tx] = 'F'

        while q:
            y, x = q.pop(0)
            dx = [0, 0, 1, -1]
            dy = [1, -1, 0, 0]
            for i in range(4):
                tx = x + dx[i]
                ty = y + dy[i]
                if 0 <= tx < w and 0 <= ty <h and visited[ty][tx] == 0 and miro[ty][tx] == '.':
                    if tx == 0 or tx == w-1 or ty == 0 or ty == h-1:
                        print(count)
                        return
                    checkQ.append((ty, tx))
                    visited[ty][tx] = 1
                    miro[ty][tx] = 'J'
                
        
    print("IMPOSSIBLE")

solution()



