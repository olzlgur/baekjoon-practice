# 동전 2
# 시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
# 1 초 (추가 시간 없음)	128 MB	55798	16716	11751	29.215%
# 문제
# n가지 종류의 동전이 있다. 이 동전들을 적당히 사용해서, 그 가치의 합이 k원이 되도록 하고 싶다. 그러면서 동전의 개수가 최소가 되도록 하려고 한다. 각각의 동전은 몇 개라도 사용할 수 있다.

# 사용한 동전의 구성이 같은데, 순서만 다른 것은 같은 경우이다.

# 입력
# 첫째 줄에 n, k가 주어진다. (1 ≤ n ≤ 100, 1 ≤ k ≤ 10,000) 다음 n개의 줄에는 각각의 동전의 가치가 주어진다. 동전의 가치는 100,000보다 작거나 같은 자연수이다. 가치가 같은 동전이 여러 번 주어질 수도 있다.

# 출력
# 첫째 줄에 사용한 동전의 최소 개수를 출력한다. 불가능한 경우에는 -1을 출력한다.

# 예제 입력 1 
# 3 15
# 1
# 5
# 12
# 예제 출력 1 
# 3
import sys

def main():
    input = sys.stdin.readline
    n, v = map(int, input().split())

    coin = [int(input()) for x in range(n)]

    coin = list(set(coin))
    dp = [0 for x in range(v+1)]

    for c in coin:
        for i in range(v+1):
            if i - c >= 0 and (i == c or (dp[i-c] != 0 and (dp[i] == 0 or dp[i] > dp[i-c] + 1))):
                dp[i] = dp[i-c] + 1
    if dp[-1] == 0 :
        print(-1)
        return
    print(dp[-1])
main()
