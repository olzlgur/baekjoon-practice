# 틱택토 다국어
# 시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
# 1 초	128 MB	3485	1063	773	29.549%
# 문제
# 틱택토 게임은 두 명의 사람이 번갈아가며 말을 놓는 게임이다. 게임판은 3×3 격자판이며, 처음에는 비어 있다. 두 사람은 각각 X 또는 O 말을 번갈아가며 놓는데, 반드시 첫 번째 사람이 X를 놓고 두 번째 사람이 O를 놓는다. 어느 때든지 한 사람의 말이 가로, 세로, 대각선 방향으로 3칸을 잇는 데 성공하면 게임은 즉시 끝난다. 게임판이 가득 차도 게임은 끝난다.

# 게임판의 상태가 주어지면, 그 상태가 틱택토 게임에서 발생할 수 있는 최종 상태인지를 판별하시오.

# 입력
# 입력은 여러 개의 테스트 케이스로 이루어져 있다. 각 줄은 9개의 문자를 포함하며, 'X', 'O', '.' 중 하나이다. '.'은 빈칸을 의미하며, 9개의 문자는 게임판에서 제일 윗 줄 왼쪽부터의 순서이다. 입력의 마지막에는 문자열 "end"가 주어진다.

# 출력
# 각 테스트 케이스마다 한 줄에 정답을 출력한다. 가능할 경우 "valid", 불가능할 경우 "invalid"를 출력한다.

# 예제 입력 1 
# XXXOO.XXX
# XOXOXOXOX
# OXOXOXOXO
# XXOOOXXOX
# XO.OX...X
# .XXX.XOOO
# X.OO..X..
# OOXXXOOXO
# end
# 예제 출력 1 
# invalid
# valid
# invalid
# valid
# valid
# invalid
# invalid
# invalid

import sys

def solution() :
    global tic
    input = sys.stdin.readline
    temp = []
    while True :
        tic = []
        word = str(input().rstrip())
        if word == "end" :
            break
        temp = list(word)
        oCount = temp.count('O')
        xCount = temp.count('X')
        if oCount > xCount or oCount +1 < xCount :
            print("invalid")
        else:
            for i in range(0, 9, 3):
                tic.append(temp[i:i+3])
            result = max(checkCross('X', oCount, xCount), checkCross('O', oCount, xCount), checkX(oCount, xCount), checkY(oCount, xCount))
            if result == 1 :
                print("valid")
            elif result == 0 and xCount == 5 and oCount == 4:
                print("valid")
            else:
                print("invalid")
def checkCross(w, oCount, xCount):
    global tic
    cnt = 0
    for i in range(3):
        if w == tic[i][i] :
            cnt += 1
    if cnt == 3 :
        if w == 'X' and (xCount ) != (oCount + 1):
            return 2
        elif w == 'O' and oCount != xCount :
            return 2
        return 1
    cnt = 0
    for i in range(3):
            if w == tic[i][2-i] :
                cnt += 1 
    if cnt == 3 :
        if w == 'X' and xCount != (oCount +1) :
            return 2
        elif w == 'O' and oCount != xCount :
            return 2
        return 1
    return 0

def checkX(oCount, xCount):
    global tic
    count = 0
    for i in range(3):
        if tic[i][0] == tic[i][1] and tic[i][1] == tic[i][2] and (tic[i][0] == 'X' or tic[i][0] == 'O') :
            if tic[i][0] == 'O' and oCount != xCount:
                count += 1
            elif tic[i][0] == 'X' and (oCount +1) != xCount :
                count += 1
            count += 1
    return count

def checkY(oCount, xCount):
    global tic
    count = 0
    for i in range(3):
        if tic[0][i] == tic[1][i] and tic[1][i] == tic[2][i] and (tic[0][i] == 'X' or tic[0][i] == 'O'):
            if tic[0][i] == 'O' and oCount != xCount:
                count += 1
            elif tic[0][i] == 'X' and (oCount +1) != xCount :
                count += 1
            count += 1
    return count

solution()
