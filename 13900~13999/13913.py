# 숨바꼭질 4 스페셜 저지 
# 시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
# 2 초	512 MB	38608	12912	9076	31.165%
# 문제
# 수빈이는 동생과 숨바꼭질을 하고 있다. 수빈이는 현재 점 N(0 ≤ N ≤ 100,000)에 있고, 동생은 점 K(0 ≤ K ≤ 100,000)에 있다. 수빈이는 걷거나 순간이동을 할 수 있다. 만약, 수빈이의 위치가 X일 때 걷는다면 1초 후에 X-1 또는 X+1로 이동하게 된다. 순간이동을 하는 경우에는 1초 후에 2*X의 위치로 이동하게 된다.

# 수빈이와 동생의 위치가 주어졌을 때, 수빈이가 동생을 찾을 수 있는 가장 빠른 시간이 몇 초 후인지 구하는 프로그램을 작성하시오.

# 입력
# 첫 번째 줄에 수빈이가 있는 위치 N과 동생이 있는 위치 K가 주어진다. N과 K는 정수이다.

# 출력
# 첫째 줄에 수빈이가 동생을 찾는 가장 빠른 시간을 출력한다.

# 둘째 줄에 어떻게 이동해야 하는지 공백으로 구분해 출력한다.

# 예제 입력 1  복사
# 5 17
# 예제 출력 1  복사
# 4
# 5 10 9 18 17
# 예제 입력 2  복사
# 5 17
# 예제 출력 2  복사
# 4
# 5 4 8 16 17

import sys
from collections import deque

input = sys.stdin.readline

N, K = map(int, input().split())

def bfs():
    global answer
    if N == K:
        return 0, [N]
    
    if K < N:
        return N-K, [i for i in range(N, K-1, -1)]

    road = [-1] * (2*K+1)
    q = deque()
    q.append(N)
    while q:
        x = q.popleft()

        if x == K:
            break
        
        if 0 <= x - 1 and road[x-1] == -1:
            q.append(x-1)
            road[x-1] = x
        if x + 1 <= 2*K and road[x+1] == -1:
            q.append(x+1)
            road[x+1] = x 
        if x * 2 <= 2*K and road[2*x] == -1:
            q.append(2*x)
            road[2*x] = x

    q = deque()
    q.append(K)
    x = road[K]
    answer = 1
    while x != N:
        q.appendleft(x)
        x = road[x]
        answer += 1
    q.appendleft(N)
    
    return answer, q

answer, route = bfs()
print(answer)
for value in route:
    print(value, end= " ")