# 수들의 합
# 시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
# 2 초	128 MB	39611	16105	13706	42.075%
# 문제
# 서로 다른 N개의 자연수의 합이 S라고 한다. S를 알 때, 자연수 N의 최댓값은 얼마일까?

# 입력
# 첫째 줄에 자연수 S(1 ≤ S ≤ 4,294,967,295)가 주어진다.

# 출력
# 첫째 줄에 자연수 N의 최댓값을 출력한다.

# 예제 입력 1 
# 200
# 예제 출력 1 
# 19
import sys

input = sys.stdin.readline

s = int(input())

sum = 0
cnt = 1
answer = 0
while True :
    answer += cnt
    if answer > s :
        break
    cnt += 1
print(cnt-1)
