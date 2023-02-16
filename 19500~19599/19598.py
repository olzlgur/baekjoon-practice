# 최소 회의실 개수
# 시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
# 2 초	256 MB	3872	1594	1206	42.050%
# 문제
# 서준이는 아빠로부터 N개의 회의를 모두 진행할 수 있는 최소 회의실 개수를 구하라는 미션을 받았다. 각 회의는 시작 시간과 끝나는 시간이 주어지고 한 회의실에서 동시에 두 개 이상의 회의가 진행될 수 없다. 단, 회의는 한번 시작되면 중간에 중단될 수 없으며 한 회의가 끝나는 것과 동시에 다음 회의가 시작될 수 있다. 회의의 시작 시간은 끝나는 시간보다 항상 작다. N이 너무 커서 괴로워 하는 우리 서준이를 도와주자.

# 입력
# 첫째 줄에 배열의 크기 N(1 ≤ N ≤ 100,000)이 주어진다. 둘째 줄부터 N+1 줄까지 공백을 사이에 두고 회의의 시작시간과 끝나는 시간이 주어진다. 시작 시간과 끝나는 시간은 231−1보다 작거나 같은 자연수 또는 0이다.

# 출력
# 첫째 줄에 최소 회의실 개수를 출력한다.

# 예제 입력 1 
# 3
# 0 40
# 15 30
# 5 10
# 예제 출력 1 
# 2
# 2개 회의실로 3개 회의를 모두 진행할 수 있다. 예를 들어, 첫번째 회의실에서 첫번째 회의를 진행하고 두번째 회의실에서 두번째 회의와 세번째 회의를 진행하면 된다. 1개 회의실로 3개 회의를 진행할 수 없고 3개 이상의 회의실로 3개 회의를 모두 진행할 수 있지만 최소 회의실 개수를 구해야 하기 때문에 2가 정답이 된다.

# 예제 입력 2 
# 2
# 10 20
# 5 10
# 예제 출력 2 
# 1

import sys
import heapq

input = sys.stdin.readline

n = int(input())

meeting = []

for i in range(n):
    start, end = map(int, input().split())
    meeting.append((start, end))
    
meeting.sort()
room = []

heapq.heappush(room, meeting[0][1])

for i in range(1, len(meeting)):
    if room[0] <= meeting[i][0]:
        heapq.heappop(room)
        heapq.heappush(room, meeting[i][1])
    else :
        heapq.heappush(room, meeting[i][1])
print(len(room))
