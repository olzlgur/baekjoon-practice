# 동전 분배 
# 시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
# 2 초	128 MB	3334	715	421	20.457%
# 문제
# 윤화와 준희는 솔선수범하여 쓰레기를 줍는 착한 일을 하였다. 원장선생님께서는 윤화와 준희를 칭찬하시고 과자나 사 먹으라고 하시며 동전 몇 개를 윤화와 준희에게 건네 주었다.

# 그런데 돈을 받은 윤화와 준희는 좋아하기보다 고민에 빠지고 말았다. 원장선생님께 받은 이 돈을 어떻게 나누어 할지 고민에 빠진 것이다. 두 사람 모두 상대방이 자기보다 1원이라도 더 받는 것은 도저히 인정할 수 없어 한다. 따라서 돈을 똑같이 둘로 나누어 가져야 두 사람이 모두 만족할 수 있게 된다.

# 하지만 두 사람에게 돈을 똑같이 나누는 것이 불가능한 경우도 있다. 예를 들어 500원짜리 1개와 50원짜리 1개를 받았다면, 이 돈을 두 사람이 똑같이 나누어 가질 수는 없다. 물론 동전을 반으로 잘라서 나누어 가질 수도 있겠지만 그러면 돈으로서의 가치를 잃기 때문에 그렇게 할 수는 없다.

# 이제 우리가 할 일은 다음과 같다. 원장 선생님께서 N가지 종류의 동전을 각각 몇 개씩 주셨을 때, 그 돈을 반으로 나눌 수 있는지 없는지 판단하는 것이다.

# 입력
# 세 개의 입력이 주어진다. 각 입력의 첫째 줄에 동전의 종류 N(1 ≤ N ≤ 100)이 주어진다. 각 입력의 둘째 줄부터 N+1째 줄까지 각각의 동전의 금액과 개수가 빈 칸을 사이에 두고 주어진다. 단, 원장선생님께서 주신 금액의 총 합은 100,000원을 넘지 않는다. 동전의 금액과 개수는 자연수이고, 같은 금액을 가진 동전이 두 번 이상 주어지는 경우는 없다.

# 출력
# 첫째 줄부터 세 줄에 걸쳐, 각 입력에 대하여 반으로 나누는 것이 가능하면 1, 불가능하면 0을 출력한다.

# 예제 입력 1  복사
# 2
# 500 1
# 50 1
# 3
# 100 2
# 50 1
# 10 5
# 3
# 1 1
# 2 1
# 3 1
# 예제 출력 1  복사
# 0
# 1
# 1

import sys

input = sys.stdin.readline
    
def check(coins, sum):
    if sum % 2 == 0:
        total = sum // 2
        dp = [0] * (total+1)
        dp[0] = 1
        for coin in coins:
            for i in range(total, coin[0]-1, -1):
                if dp[i-coin[0]] == 1:
                    for j in range(coin[1]):
                        if i + j*coin[0] <= total:
                            dp[i+j*coin[0]] = 1
            if dp[-1] == 1:
                return 1
    return 0

for _ in range(3):
    n = int(input())

    coins = []
    sum = 0
    for idx in range(n):
        coins.append(tuple(map(int, input().split())))
        sum += coins[idx][0] * coins[idx][1]
    
    print(check(coins, sum))