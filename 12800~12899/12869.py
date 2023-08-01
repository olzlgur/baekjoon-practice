# 뮤탈리스크 
# 시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
# 2 초	512 MB	6877	3271	2388	47.598%
# 문제
# 수빈이는 강호와 함께 스타크래프트 게임을 하고 있다. 수빈이는 뮤탈리스크 1개가 남아있고, 강호는 SCV N개가 남아있다.

# 각각의 SCV는 남아있는 체력이 주어져있으며, 뮤탈리스크를 공격할 수는 없다. 즉, 이 게임은 수빈이가 이겼다는 것이다.

# 뮤탈리스크가 공격을 할 때, 한 번에 세 개의 SCV를 공격할 수 있다.

# 첫 번째로 공격받는 SCV는 체력 9를 잃는다.
# 두 번째로 공격받는 SCV는 체력 3을 잃는다.
# 세 번째로 공격받는 SCV는 체력 1을 잃는다.
# SCV의 체력이 0 또는 그 이하가 되어버리면, SCV는 그 즉시 파괴된다. 한 번의 공격에서 같은 SCV를 여러 번 공격할 수는 없다.

# 남아있는 SCV의 체력이 주어졌을 때, 모든 SCV를 파괴하기 위해 공격해야 하는 횟수의 최솟값을 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 SCV의 수 N (1 ≤ N ≤ 3)이 주어진다. 둘째 줄에는 SCV N개의 체력이 주어진다. 체력은 60보다 작거나 같은 자연수이다.

# 출력
# 첫째 줄에 모든 SCV를 파괴하기 위한 공격 횟수의 최솟값을 출력한다.

# 예제 입력 1  복사
# 3
# 12 10 4
# 예제 출력 1  복사
# 2
# 예제 입력 2  복사
# 3
# 54 18 6
# 예제 출력 2  복사
# 6
# 예제 입력 3  복사
# 1
# 60
# 예제 출력 3  복사
# 7
# 예제 입력 4  복사
# 3
# 1 1 1
# 예제 출력 4  복사
# 1
# 예제 입력 5  복사
# 2
# 60 40
# 예제 출력 5  복사
# 9

import sys
from itertools import permutations

input = sys.stdin.readline

n = int(input())
scv = list(map(int, input().split()))
scv.extend([0, 0])
dp = [[[0]*61 for _ in range(61)] for _ in range(61)]

dp[scv[0]][scv[1]][scv[2]] = 1
mut = [9, 3, 1]
for i in range(60, -1, -1):
    for j in range(60, -1, -1):
        for k in range(60, -1, -1):
            for tu in permutations(mut, 3):
                if 0 < dp[i][j][k]:
                    val1 = max(0, i - tu[0])
                    val2 = max(0, j - tu[1])
                    val3 = max(0, k - tu[2])

                    if dp[val1][val2][val3] == 0 or dp[val1][val2][val3] > dp[i][j][k]+1:
                        dp[val1][val2][val3] = dp[i][j][k]+1

print(dp[0][0][0]-1)