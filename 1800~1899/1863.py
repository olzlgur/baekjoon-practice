# 스카이라인 쉬운거
# 시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
# 2 초	128 MB	2122	847	672	40.385%
# 문제
# 도시에서 태양이 질 때에 보이는 건물들의 윤곽을 스카이라인이라고 한다. 스카이라인만을 보고서 도시에 세워진 건물이 몇 채인지 알아 낼 수 있을까? 건물은 모두 직사각형 모양으로 밋밋하게 생겼다고 가정한다.

# 정확히 건물이 몇 개 있는지 알아내는 것은 대부분의 경우에 불가능하고, 건물이 최소한 몇 채 인지 알아내는 것은 가능해 보인다. 이를 알아내는 프로그램을 작성해 보자.

# 입력
# 첫째 줄에 n이 주어진다. (1 ≤ n ≤ 50,000) 다음 n개의 줄에는 왼쪽부터 스카이라인을 보아 갈 때 스카이라인의 고도가 바뀌는 지점의 좌표 x와 y가 주어진다. (1 ≤ x ≤ 1,000,000. 0 ≤ y ≤ 500,000) 첫 번째 지점의 x좌표는 항상 1이다.

# 출력
# 첫 줄에 최소 건물 개수를 출력한다.

# 예제 입력 1 
# 10
# 1 1
# 2 2
# 5 1
# 6 3
# 8 1
# 11 0
# 15 2
# 17 3
# 20 2
# 22 1
# 예제 출력 1 
# 6

import sys, heapq

input = sys.stdin.readline

n = int(input())

tower = []
count = 0
tower.append([])
for i in range(n):
    x, y = map(int, input().split())
    if y == 0 :
        if i != n-1:
            tower.append([])
            count += 1
            continue
        else :
            break
    tower[count].append((y))

count = 0
for tow in tower:
    hq = []
    if len(tow) == 0 :
        break
    heapq.heappush(hq, (-tow[0], tow[0]))
    for i in range(1, len(tow)) :        
        if hq[0][1] < tow[i] :
            heapq.heappush(hq, (-tow[i], tow[i]))
        else :
            temp = 500001
            while len(hq) != 0:
                tu = heapq.heappop(hq)
                temp = tu[1]
                if temp <= tow[i]:
                    heapq.heappush(hq, tu)
                    break
                if temp == tow[i] :
                    heapq.heappush(hq, (-tow[i], tow[i]))
                    break
                count += 1
            if (-tow[i], tow[i]) not in hq:
                heapq.heappush(hq, (-tow[i], tow[i]))
    count += len(hq)

print(count)


