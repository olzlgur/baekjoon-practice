# 겹치는 건 싫어
# 시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
# 1 초 (추가 시간 없음)	1024 MB	5058	1769	1344	34.621%
# 문제
# 홍대병에 걸린 도현이는 겹치는 것을 매우 싫어한다. 특히 수열에서 같은 원소가 여러 개 들어 있는 수열을 싫어한다. 도현이를 위해 같은 원소가 
# $K$개 이하로 들어 있는 최장 연속 부분 수열의 길이를 구하려고 한다.

#  
# $100\,000$ 이하의 양의 정수로 이루어진 길이가 
# $N$인 수열이 주어진다.  이 수열에서 같은 정수를 
# $K$개 이하로 포함한 최장 연속 부분 수열의 길이를 구하는 프로그램을 작성해보자.

# 입력
# 첫째 줄에 정수 
# $N$ (
# $1 \le N \le 200\,000$)과 
# $K$ (
# $1 \le K \le 100$)가 주어진다.

# 둘째 줄에는 
# ${a_1, a_2, ... a_n}$이 주어진다 (
# $1 \le a_i \le 100\,000$)

# 출력
# 조건을 만족하는 최장 연속 부분 수열의 길이를 출력한다.

# 예제 입력 1 
# 9 2
# 3 2 5 5 6 4 4 5 7
# 예제 출력 1 
# 7
# 예제 입력 2 
# 10 1
# 1 2 3 4 5 6 6 7 8 9
# 예제 출력 2 
# 6

import sys

input = sys.stdin.readline
n, k = map(int, input().split())
seq = list(map(int, input().split()))
left, right = 0, 0

counter = [0] * (max(seq) + 1)
answer = 0
while right < n:
    if counter[seq[right]] < k:
        counter[seq[right]] += 1
        right += 1
    else:
        counter[seq[left]] -= 1
        left += 1
    answer = max(answer, right - left)
print(answer)
