# 좋다 
# 시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
# 2 초	256 MB	21089	5260	3786	24.005%
# 문제
# N개의 수 중에서 어떤 수가 다른 수 두 개의 합으로 나타낼 수 있다면 그 수를 “좋다(GOOD)”고 한다.

# N개의 수가 주어지면 그 중에서 좋은 수의 개수는 몇 개인지 출력하라.

# 수의 위치가 다르면 값이 같아도 다른 수이다.

# 입력
# 첫째 줄에는 수의 개수 N(1 ≤ N ≤ 2,000), 두 번째 줄에는 i번째 수를 나타내는 Ai가 N개 주어진다. (|Ai| ≤ 1,000,000,000, Ai는 정수)

# 출력
# 좋은 수의 개수를 첫 번째 줄에 출력한다.

# 예제 입력 1  복사
# 10
# 1 2 3 4 5 6 7 8 9 10
# 예제 출력 1  복사
# 8

# 순열 시간초과
# import sys
# from itertools import combinations

# input = sys.stdin.readline

# n = int(input())
# answer = 0
# number = list(map(int, input().split()))

# for tu in combinations(number, 2):
#     temp = tu[0] + tu[1]
#     if temp in number :
#         number[number.index(temp)] = 0
#         answer += 1
# print(answer)

# 투포인터
n = int(input())
number = list(map(int, input().split()))
number.sort()
answer = 0
for i in range(n):
    tmp = number[:i] + number[i + 1:]
    left, right = 0, len(tmp) - 1
    while left < right:
        t = tmp[left] + tmp[right]
        if t == number[i]:
            answer += 1
            break
        if t < number[i]: left += 1 # t 를 증가시켜야 하므로 left 증가
        else: right -= 1 # t 를 감소시켜야 하므로 right 감소
print(answer)
