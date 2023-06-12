# 센서 
# 시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
# 2 초	128 MB	12098	5972	4829	48.523%
# 문제
# 한국도로공사는 고속도로의 유비쿼터스화를 위해 고속도로 위에 N개의 센서를 설치하였다. 문제는 이 센서들이 수집한 자료들을 모으고 분석할 몇 개의 집중국을 세우는 일인데, 예산상의 문제로, 고속도로 위에 최대 K개의 집중국을 세울 수 있다고 한다.

# 각 집중국은 센서의 수신 가능 영역을 조절할 수 있다. 집중국의 수신 가능 영역은 고속도로 상에서 연결된 구간으로 나타나게 된다. N개의 센서가 적어도 하나의 집중국과는 통신이 가능해야 하며, 집중국의 유지비 문제로 인해 각 집중국의 수신 가능 영역의 길이의 합을 최소화해야 한다.

# 편의를 위해 고속도로는 평면상의 직선이라고 가정하고, 센서들은 이 직선 위의 한 기점인 원점으로부터의 정수 거리의 위치에 놓여 있다고 하자. 따라서, 각 센서의 좌표는 정수 하나로 표현된다. 이 상황에서 각 집중국의 수신 가능영역의 거리의 합의 최솟값을 구하는 프로그램을 작성하시오. 단, 집중국의 수신 가능영역의 길이는 0 이상이며 모든 센서의 좌표가 다를 필요는 없다.

# 입력
# 첫째 줄에 센서의 개수 N(1 ≤ N ≤ 10,000), 둘째 줄에 집중국의 개수 K(1 ≤ K ≤ 1000)가 주어진다. 셋째 줄에는 N개의 센서의 좌표가 한 개의 정수로 N개 주어진다. 각 좌표 사이에는 빈 칸이 하나 있으며, 좌표의 절댓값은 1,000,000 이하이다.

# 출력
# 첫째 줄에 문제에서 설명한 최대 K개의 집중국의 수신 가능 영역의 길이의 합의 최솟값을 출력한다.

# 예제 입력 1  복사
# 6
# 2
# 1 6 9 3 6 7
# 예제 출력 1  복사
# 5
# 예제 입력 2  복사
# 10
# 5
# 20 3 14 6 7 8 18 10 12 15
# 예제 출력 2  복사
# 7

import sys

input = sys.stdin.readline

N = int(input())
M = int(input())

sensorList = list(map(int, input().split()))
lenList = []
sensorList.sort()
answer = sensorList[-1] - sensorList[0]


for i in range(len(sensorList)-1):
    lenList.append((i, sensorList[i+1]-sensorList[i]))


lenList.sort(key=lambda x : -x[1])
if N < M:
    M = N
for i in range(M-1):
    answer -= lenList[i][1]
print(answer)