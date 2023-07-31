# 가장 긴 증가하는 부분 수열 
# 시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
# 1 초	256 MB	142090	56419	37328	37.681%
# 문제
# 수열 A가 주어졌을 때, 가장 긴 증가하는 부분 수열을 구하는 프로그램을 작성하시오.

# 예를 들어, 수열 A = {10, 20, 10, 30, 20, 50} 인 경우에 가장 긴 증가하는 부분 수열은 A = {10, 20, 10, 30, 20, 50} 이고, 길이는 4이다.

# 입력
# 첫째 줄에 수열 A의 크기 N (1 ≤ N ≤ 1,000)이 주어진다.

# 둘째 줄에는 수열 A를 이루고 있는 Ai가 주어진다. (1 ≤ Ai ≤ 1,000)

# 출력
# 첫째 줄에 수열 A의 가장 긴 증가하는 부분 수열의 길이를 출력한다.

# 예제 입력 1  복사
# 6
# 10 20 10 30 20 50
# 예제 출력 1  복사
# 4

import sys

input = sys.stdin.readline

n = int(input())
numberList = list(map(int, input().split()))

if n == 1:
    print(1)
else:
    dp = [0]*n
    dp[0] = 1
    for i in range(1, n):
        maxCnt = 0
        index = 0
        for j in range(i, -1, -1):
            if numberList[j] < numberList[i] and max < dp[j]:
                maxCnt = dp[j]
                index = j
        dp[i] = maxCnt + 1
    
    print(max(dp))
    