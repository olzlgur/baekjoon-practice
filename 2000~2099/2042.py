# 구간 합 구하기 
# 시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
# 2 초	256 MB	87755	20994	10773	24.998%
# 문제
# 어떤 N개의 수가 주어져 있다. 그런데 중간에 수의 변경이 빈번히 일어나고 그 중간에 어떤 부분의 합을 구하려 한다. 만약에 1,2,3,4,5 라는 수가 있고, 3번째 수를 6으로 바꾸고 2번째부터 5번째까지 합을 구하라고 한다면 17을 출력하면 되는 것이다. 그리고 그 상태에서 다섯 번째 수를 2로 바꾸고 3번째부터 5번째까지 합을 구하라고 한다면 12가 될 것이다.

# 입력
# 첫째 줄에 수의 개수 N(1 ≤ N ≤ 1,000,000)과 M(1 ≤ M ≤ 10,000), K(1 ≤ K ≤ 10,000) 가 주어진다. M은 수의 변경이 일어나는 횟수이고, K는 구간의 합을 구하는 횟수이다. 그리고 둘째 줄부터 N+1번째 줄까지 N개의 수가 주어진다. 그리고 N+2번째 줄부터 N+M+K+1번째 줄까지 세 개의 정수 a, b, c가 주어지는데, a가 1인 경우 b(1 ≤ b ≤ N)번째 수를 c로 바꾸고 a가 2인 경우에는 b(1 ≤ b ≤ N)번째 수부터 c(b ≤ c ≤ N)번째 수까지의 합을 구하여 출력하면 된다.

# 입력으로 주어지는 모든 수는 -263보다 크거나 같고, 263-1보다 작거나 같은 정수이다.

# 출력
# 첫째 줄부터 K줄에 걸쳐 구한 구간의 합을 출력한다. 단, 정답은 -263보다 크거나 같고, 263-1보다 작거나 같은 정수이다.

# 예제 입력 1  복사
# 5 2 2
# 1
# 2
# 3
# 4
# 5
# 1 3 6
# 2 2 5
# 1 5 2
# 2 3 5
# 예제 출력 1  복사
# 17
# 12

# N 숫자 개수, M 변경 횟수, K 구간합 횟수
# a,b,c a가 1이면  b -> c, 2면 b~c 구간함

import sys

# 세그먼트 트리 초기화 함수    
def init(start, end, index):
    global segmentTree

    # 구간의 시작 끝이 같으면 루트 노드
    if start == end:
        segmentTree[index] = number[start-1]
        return segmentTree[index]
    
    # 루트 노드가 아닌 경우
    mid = (start+end) // 2
    # 현재 노드 범위를 나누어 재귀적으로 구간합 연산
    segmentTree[index] = init(start, mid, index*2) + init(mid+1, end, index*2+1)

    return segmentTree[index]

# 구간합 탐색
def find(start, end, index, left, right):

    # 구하고자 하는 구간에 속하지 않는 경우 
    if right < start or end < left:
        return 0
    
    # 현재 노드의 범위가 구하고자 하는 구간에 속하는 경우
    if left <=  start and right >= end:
        # 구간 합 반환
        return segmentTree[index]
    
    # 현재 노드의 구간이 현재 구하고자 하는 구간보다 큰 경우
    mid = (start + end) // 2
    # 구간에 맞는 구간합 탐색 후 연산
    subSum = find(start, mid, index*2, left, right) + find(mid+1, end, index*2+1, left, right)
    return subSum

# 숫자 변경
def update(start, end, index, updateIndex, data):

    # 구간 내에 속하지 않는 경우
    if updateIndex < start or updateIndex > end:
        return
    
    # 속할 경우 업데이트 하고자 +data 
    segmentTree[index] += data

    # 루트 노드인 경우 종료
    if start == end:
        return
    
    mid = (start + end) // 2

    # 탐색
    update(start, mid, index*2, updateIndex, data)
    update(mid+1, end, index*2+1, updateIndex, data)


input = sys.stdin.readline

N, M, K = map(int, input().split())
number = []
segmentTree = [0]*(N*4)

for _ in range(N):
    number.append(int(input()))

# 트리 초기화
init(1, N, 1)

for _ in range(M+K):
    a, b, c = map(int, input().split())

    if a == 1:
        # 변경된 데이터와의 차이만큼 구간합 수정
        temp = c - number[b-1]
        number[b-1] = c
        update(1, N, 1, b, temp)
    
    elif a == 2:
        print(find(1, N, 1, b, c))