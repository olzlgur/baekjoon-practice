# 숨바꼭질 2 
# 시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
# 2 초	512 MB	39100	11015	7642	25.804%
# 문제
# 수빈이는 동생과 숨바꼭질을 하고 있다. 수빈이는 현재 점 N(0 ≤ N ≤ 100,000)에 있고, 동생은 점 K(0 ≤ K ≤ 100,000)에 있다. 수빈이는 걷거나 순간이동을 할 수 있다. 만약, 수빈이의 위치가 X일 때 걷는다면 1초 후에 X-1 또는 X+1로 이동하게 된다. 순간이동을 하는 경우에는 1초 후에 2*X의 위치로 이동하게 된다.

# 수빈이와 동생의 위치가 주어졌을 때, 수빈이가 동생을 찾을 수 있는 가장 빠른 시간이 몇 초 후인지 그리고, 가장 빠른 시간으로 찾는 방법이 몇 가지 인지 구하는 프로그램을 작성하시오.

# 입력
# 첫 번째 줄에 수빈이가 있는 위치 N과 동생이 있는 위치 K가 주어진다. N과 K는 정수이다.

# 출력
# 첫째 줄에 수빈이가 동생을 찾는 가장 빠른 시간을 출력한다.

# 둘째 줄에는 가장 빠른 시간으로 수빈이가 동생을 찾는 방법의 수를 출력한다.

# 예제 입력 1  복사
# 5 17
# 예제 출력 1  복사
# 4
# 2

# 수빈이 점 N, 동생 K, 수빈이 걷거나 순간이동 수빈이 위치 1초후에 X-1 or X+1 순간이동 1초후 2X

import sys
from collections import deque

input = sys.stdin.readline
deq = deque()
point = [100001] * 100001
count = 0
N, K = map(int, input().split())
point[N] = 0
point[K] = 100001
deq.append((-1, N))
while deq:
    ex, n = deq.popleft()
    if n == K:
        if ex + 1 == point[n]:
            count += 1
        elif ex + 1 < point[n]:
            point[n] = ex + 1
            count = 1
    elif ex + 1 <= point[K] and (point[n] >= ex + 1):
        point[n] = ex + 1
        if n < 100000 and point[n+1] >= point[n] + 1: 
            deq.append((point[n], n+1))
        if 0 < n and point[n-1] >= point[n] + 1:
            deq.append((point[n], n-1))
        if 2*n <= 100000 and point[2*n] >= point[n] + 1:
            deq.append((point[n], 2*n))

print(point[K])
print(count) 

# input = sys.stdin.readline
# deq = deque()
# point = [100001] * 100001
# count = 0
# N, K = map(int, input().split())
# point[N] = -1
# point[K] = 100001
# def dfs(n, ex):
#     global count
#     if n == K:
#         if point[ex] + 1 == point[n]:
#             count += 1
#         else:
#             point[n] = point[ex] + 1
#             count = 1
#     elif point[ex] + 1 <= point[K]:
#         point[n] = point[ex] + 1
#         if n < 100000 and point[n+1] >= point[n] + 1:
#             dfs(n+1, n)
#         if 0 < n and point[n-1] >= point[n] + 1:
#             dfs(n-1, n)
#         if 2*n < 100000 and point[2*n] >= point[n] + 1:
#             dfs(2*n, n)

# dfs(N, N)