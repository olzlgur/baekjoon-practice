# -*- coding: utf-8 -*-
# 괄호
# 시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
# 2 초	256 MB	7690	2323	1700	29.935%
# 문제
# ‘(‘, ‘)’ 문자로만 이루어진 문자열을 괄호 문자열이라 한다. 올바른 괄호 문자열이란 다음과 같이 정의된다. ()는 올바른 괄호 문자열이다. S가 올바른 괄호 문자열이라면, (S)도 올바른 괄호 문자열이다. S와 T가 올바른 괄호 문자열이라면, 두 문자열을 이어 붙인 ST도 올바른 괄호 문자열이다. (()())()은 올바른 괄호 문자열이지만 (()은 올바른 괄호 문자열이 아니다. 괄호 문자열이 주어졌을 때 올바른 괄호 문자열인지 확인하는 방법은 여러 가지가 있다.

# 하지만 우리가 궁금한 것은 길이가 L인 올바른 괄호 문자열의 개수이다. 길이 L이 주어졌을 때 길이가 L인 서로 다른 올바른 괄호 문자열의 개수를 출력하는 프로그램을 만들어 보자.

# 입력
# 첫 번째 줄에 테스트케이스의 개수를 나타내는 T (1 ≤ T ≤ 100)가 주어진다. 두 번째 줄부터 각 테스트케이스마다 괄호 문자열의 길이를 나타내는 L이 주어진다. (1 ≤ L ≤ 5000) 

# 출력
# 각 테스트 케이스에 대해 길이가 L인 올바른 괄호 문자열의 개수를 1,000,000,007로 나눈 나머지를 출력하시오.

# 예제 입력 1 
# 3
# 1
# 2
# 4
# 예제 출력 1 
# 0
# 1
# 2

n = int(input())
dp = [0] * 5001
dp[0] = 1

for i in range(2, 5001, 2) :
    for j in range(2, i + 1, 2):
        dp[i] += (dp[j - 2] * dp[i - j]) 
    dp[i] %= 1000000007

for i in range(n):
    print(dp[int(input())])

