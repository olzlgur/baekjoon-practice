# 블로그2 
# 시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
# 2 초	1024 MB	3068	1435	1151	45.530%
# 문제
# neighbor 블로그를 운영하는 일우는 매일 아침 풀고 싶은 문제를 미리 정해놓고 글을 올린다. 그리고 매일 밤 각각의 문제에 대하여, 해결한 경우 파란색, 해결하지 못한 경우 빨간색으로 칠한다. 일우는 각 문제를 칠할 때 아래와 같은 과정을 한 번의 작업으로 수행한다.

# 연속된 임의의 문제들을 선택한다.
# 선택된 문제들을 전부 원하는 같은 색으로 칠한다.


# 예를 들어, 각 문제를 위와 같은 색으로 칠하려고 할 때, 1~2번 문제를 파란색, 3번을 빨간색, 4번을 파란색, 5번을 빨간색, 6~7번을 파란색, 8번을 빨간색으로 칠하는 작업을 순서대로 수행하면 6번의 작업을 거쳐야 한다. 하지만, 1~7번 문제를 파란색, 3번을 빨간색, 5번을 빨간색, 8번을 빨간색으로 순서대로 칠한다면 작업 횟수는 4번으로 가장 적다.

# 일우는 매일 500,000문제까지 시도하기 때문에, 이 작업이 꽤나 귀찮아지기 시작했다. 그래서 가장 효율적인 방법으로 위 작업을 수행하기를 원한다. 일우를 도와 각 문제를 주어진 색으로 칠할 때 필요한 최소한의 작업 횟수를 구하는 프로그램을 작성하라.

# 입력
# 첫째 줄에 색을 칠해야 하는 문제의 수 N (1 ≤ N ≤ 500,000)이 주어진다.

# 둘째 줄에 N개의 문자가 공백 없이 순서대로 주어진다. 각 문자는 i번째 문제를 어떤 색으로 칠해야 하는지를 의미하며, R은 빨간색, B는 파란색을 나타낸다. 그 외에 다른 문자는 주어지지 않는다.

# 출력
# 첫째 줄에 일우가 주어진 모든 문제를 원하는 색으로 칠할 때까지 필요한 작업 횟수의 최솟값을 출력하라.

# 예제 입력 1  복사
# 8
# BBRBRBBR
# 예제 출력 1  복사
# 4

import sys

input = sys.stdin.readline

n = int(input())
answer = list(input().rstrip())
temp = [0]*(len(answer))
cnt = 0

left, right = 0,  len(answer)-1

while left <= right:
    while True:
        if left+1 >= len(answer)-1:
            left += 1
            break
        else:
            if answer[left] != answer[left+1]:
                break
            left += 1
    print(left, right, temp)
    while left<=right:
        if answer[left] == answer[right]:
            temp[right] = answer[left]
            right -= 1
        else:
            break
    print(left, right, temp, cnt)
    left += 1
    cnt += 1

print(cnt)
