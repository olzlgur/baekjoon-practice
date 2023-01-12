# 1, 2, 3 더하기 4
# 시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
# 1 초 (추가 시간 없음)	512 MB	4895	3081	2429	64.310%
# 문제
# 정수 4를 1, 2, 3의 합으로 나타내는 방법은 총 4가지가 있다. 합을 나타낼 때는 수를 1개 이상 사용해야 한다. 합을 이루고 있는 수의 순서만 다른 것은 같은 것으로 친다.

# 1+1+1+1
# 2+1+1 (1+1+2, 1+2+1)
# 2+2
# 1+3 (3+1)
# 정수 n이 주어졌을 때, n을 1, 2, 3의 합으로 나타내는 방법의 수를 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 테스트 케이스의 개수 T가 주어진다. 각 테스트 케이스는 한 줄로 이루어져 있고, 정수 n이 주어진다. n은 양수이며 10,000보다 작거나 같다.

# 출력
# 각 테스트 케이스마다, n을 1, 2, 3의 합으로 나타내는 방법의 수를 출력한다.


# 예제 입력 1 
# 3
# 4
# 7
# 10
# 예제 출력 1 
# 4
# 8
# 14

# dp 
n = int(input())

dp = [1]*10001
for i in range(2, 10001):
    dp[i] += dp[i-2] 

for i in range(3, 10001):
    dp[i] += dp[i-3] 

for i in range(n):
    t = int(input())
    print(dp[t])

# dfs 시간초과
# answer = []

# def solution():
#     global answer
    
#     temp = []
#     n = int(input())

#     for i in range(n):
#         k = int(input())
#         answer = []
#         dfs(0, k, temp)
#         print(len(answer))

# def dfs(n, e, temp):
#     if n == e :
#         temp.sort()
#         if temp not in answer:
#             answer.append(temp) 
#             return
#     else :
#         if n + 1 <= e :
#             t = temp.copy()
#             t.append(1)
#             dfs(n+1, e, t)
#         if n + 2 <= e :
#             t = temp.copy()
#             t.append(2)
#             dfs(n+2, e, t)
#         if n + 3 <= e :
#             t = temp.copy()
#             t.append(3)
#             dfs(n+3, e, t)
# solution()

