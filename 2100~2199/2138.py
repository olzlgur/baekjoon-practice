# 전구와 스위치
# 시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
# 2 초	128 MB	7765	2848	2223	37.468%
# 문제
# N개의 스위치와 N개의 전구가 있다. 각각의 전구는 켜져 있는 상태와 꺼져 있는 상태 중 하나의 상태를 가진다. i(1 < i < N)번 스위치를 누르면 i-1, i, i+1의 세 개의 전구의 상태가 바뀐다. 즉, 꺼져 있는 전구는 켜지고, 켜져 있는 전구는 꺼지게 된다. 1번 스위치를 눌렀을 경우에는 1, 2번 전구의 상태가 바뀌고, N번 스위치를 눌렀을 경우에는 N-1, N번 전구의 상태가 바뀐다.

# N개의 전구들의 현재 상태와 우리가 만들고자 하는 상태가 주어졌을 때, 그 상태를 만들기 위해 스위치를 최소 몇 번 누르면 되는지 알아내는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 자연수 N(2 ≤ N ≤ 100,000)이 주어진다. 다음 줄에는 전구들의 현재 상태를 나타내는 숫자 N개가 공백 없이 주어진다. 그 다음 줄에는 우리가 만들고자 하는 전구들의 상태를 나타내는 숫자 N개가 공백 없이 주어진다. 0은 켜져 있는 상태, 1은 꺼져 있는 상태를 의미한다.

# 출력
# 첫째 줄에 답을 출력한다. 불가능한 경우에는 -1을 출력한다.

# 예제 입력 1 
# 3
# 000
# 010
# 예제 출력 1 
# 3

import sys, copy

input = sys.stdin.readline

n = int(input())

light = list(map(int, input().rstrip()))
goal = list(map(int, input().rstrip()))
count = 0
light1 = []
def play(l, g):
    count = 0
    for i in range(1,n):
        if l[i-1] != g[i-1] :
            count += 1
            for j in range(i-1, i+2):
                if j<n:
                    l[j] = 1 - l[j]
    if l == g :
        return count
    return n+1

answer = play(copy.deepcopy(light), goal)
light[0] = 1 - light[0]
light[1] = 1 - light[1]
answer = min(answer, play(copy.deepcopy(light), goal) + 1)

if answer == n+1:
    print(-1)
else :
    print(answer)
