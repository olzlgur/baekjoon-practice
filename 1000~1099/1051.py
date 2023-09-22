import sys

input = sys.stdin.readline

N, M = map(int, input().split())

numMap = [list(input().rstrip()) for _ in range(N)]
answer = 1


def check1(y, x1, x2):

    if numMap[y][x1] == numMap[y][x2]:
        check2(y, x1, x2, y+1)
    
    if x2 + 1 < M:
        check1(y, x1, x2+1)

def check2(y1, x1, x2, y2):
    global answer

    if numMap[y1][x1] == numMap[y2][x1] and numMap[y2][x1] == numMap[y2][x2] and y2-y1 == x2 -x1:
        answer = max(answer, (y2-y1+1)*(x2-x1+1))
        return
    if y2 + 1 < N:
        check2(y1, x1, x2, y2+1)

for i in range(N-1):
    for j in range(M-1):
        check1(i, j, j+1)
print(answer)