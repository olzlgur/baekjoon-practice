# 타일 코드 다국어
# 시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
# 2 초	128 MB	3722	1550	1235	42.338%
# 문제
# 2×N 크기의 넓은 판을 1×2 (또는 2×1) 크기와 2×2 크기의 타일로 채우려고 한다. 여러 가지 경우가 있을 수 있으므로, 각각을 하나의 코드로 대응시켜서 암호화에 이용하려고 한다.

# 그런데 문제가 생겼다. 넓은 판을 교환하다 보니 좌우 대칭인 경우가 있어, 뒤집히는 경우 코드가 헷갈리게 되는 경우가 발생한 것이다. 예를 들어 아래의 두 경우는 달라 보이지만 좌우 대칭을 이루고 있다.



# N이 주어지면, 전체 타일 코드의 개수를 구하는 프로그램을 작성하시오. (단, 서로 좌우 대칭을 이루는 중복된 표현은 한 가지 경우로만 처리한다.)

# 입력
# 첫째 줄에 타일의 크기 N(1 ≤ N ≤ 30)이 주어진다.

# 출력
# 첫째 줄에 타일 코드의 개수를 출력한다.

# 예제 입력 1 
# 4
# 예제 출력 1 
# 8

# import sys, copy

# input = sys.stdin.readline

# n = int(input())
# count = 0
# sym = 0
# def dfs(x, copyblock, flag):
#     global count, sym
#     if x <= n  :
#         if flag == 1 :
#             copyblock.append(1)
#             copyblock.append(1)
#         if flag == 2 :
#             copyblock.append(2)
#             copyblock.append(2)
#         if flag == 3 :
#             copyblock.append(3)
#         if x < n:
#             dfs(x+2, copy.deepcopy(copyblock), 1)
#             dfs(x+2, copy.deepcopy(copyblock), 2)
#             dfs(x+1, copy.deepcopy(copyblock), 3)
#     if x == n:
#         cl = len(copyblock)
#         if cl  % 2 == 0 and copyblock[:cl//2] != copyblock[cl//2:][::-1] :
#             sym += 1
#         elif cl % 2 != 0 and copyblock[:cl//2] != copyblock[(cl//2)+1:][::-1] :
#             sym += 1
#         count += 1

# block = []
# dfs(0, copy.deepcopy(block), 0)
# print(count - (sym//2))

import sys

input = sys.stdin.readline

n = int(input())

if n == 1 :
    print(1)
elif n == 2 :
    print(3)
else:
    dp = [0]* (n+1)
    dp[1] = 1   
    dp[2] = 3
    for i in range(3, n+1):
        dp[i] = dp[i-1] + dp[i-2]*2

    if n % 2 == 0 :
        print(dp[n] - (dp[n] - (dp[n//2] + dp[n//2-1]*2))//2)
    else:
        print(dp[n] -((dp[n] - dp[n//2])// 2))
