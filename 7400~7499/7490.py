# 0 만들기 다국어 한국어   
# 시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
# 1 초	128 MB	6380	3113	2332	47.806%
# 문제
# 1부터 N까지의 수를 오름차순으로 쓴 수열 1 2 3 ... N을 생각하자.

# 그리고 '+'나 '-', 또는 ' '(공백)을 숫자 사이에 삽입하자(+는 더하기, -는 빼기, 공백은 숫자를 이어 붙이는 것을 뜻한다). 이렇게 만든 수식의 값을 계산하고 그 결과가 0이 될 수 있는지를 살피자.

# N이 주어졌을 때 수식의 결과가 0이 되는 모든 수식을 찾는 프로그램을 작성하라.

# 입력
# 첫 번째 줄에 테스트 케이스의 개수가 주어진다(<10).

# 각 테스트 케이스엔 자연수 N이 주어진다(3 <= N <= 9).

# 출력
# 각 테스트 케이스에 대해 ASCII 순서에 따라 결과가 0이 되는 모든 수식을 출력한다. 각 테스트 케이스의 결과는 한 줄을 띄워 구분한다.

# 예제 입력 1  복사
# 2
# 3
# 7
# 예제 출력 1  복사
# 1+2-3

# 1+2-3+4-5-6+7
# 1+2-3-4+5+6-7
# 1-2 3+4+5+6+7
# 1-2 3-4 5+6 7
# 1-2+3+4-5+6-7
# 1-2-3-4-5+6+7

import sys
from collections import deque
import copy

input = sys.stdin.readline


for _ in range(int(input())):
    n = int(input())
    q2 = deque()
    q2.append(("1", "1"))
    for i in range(2, n+1):
        q1 = copy.deepcopy(q2) 
        q2 = deque()
        while q1:
            exp, ans = q1.popleft()
            q2.append((exp+" "+str(i), ans+str(i)))
            q2.append((exp+"+"+str(i), ans+"+"+str(i)))
            q2.append((exp+"-"+str(i), ans+"-"+str(i)))
    for tu in q2:
        if eval(tu[1]) == 0:
            print(tu[0])
    print()
