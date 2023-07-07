# 축구 스페셜 저지 
# 시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
# 2 초	128 MB	2090	1249	954	61.036%
# 문제
# 홍준이는 축구 경기를 보고 있다. 그러다가 홍준이는 역시 두 팀 중 적어도 한 팀이 골을 소수로 득점할 확률이 궁금해 졌다. 축구 경기는 90분동안 이루어지고, 분석을 쉽게하기 위해서 경기를 5분 간격으로 나눴다. 처음 간격은 처음 5분이고, 두 번째 간격은 그 다음 5분, 그리고 이런식으로 나눈다. 경기가 진행되는 동안 각 간격에서 A팀이 득점할 확률과 B팀이 득점할 확률이 주어진다. 그리고, 각 간격에서 두 팀은 각각 많아야 한 골을 득점할 수 있다. 경기가 끝난 후 적어도 한 팀이 골을 소수로 득점할 확률을 구하시오.

# 입력
# 첫째 줄에 A팀이 득점할 확률, 둘째 줄에 B팀이 득점할 확률이 퍼센트 단위로 주어진다. 퍼센트 단위로 주어지는 확률은 모두 0보다 크거나 같고 100보다 작거나 같은 정수이다.

# 출력
# 첫째 줄에 적어도 한 팀이 골을 소수로 득점할 확률을 출력한다. 정답과의 절대/상대 오차가 10-6이내인 경우에 정답이다.

# 예제 입력 1  복사
# 50
# 50
# 예제 출력 1  복사
# 0.5265618908306351
# 예제 입력 2  복사
# 100
# 100
# 예제 출력 2  복사
# 0.0
# 예제 입력 3  복사
# 12
# 89
# 예제 출력 3  복사
# 0.6772047168840167

# 구간이 18개 소수는 2, 3, 5, 7, 11, 13, 17 
# 14 * 13 / 2 * 1

import sys

input = sys.stdin.readline
primeNumber = [2, 3, 5, 7, 11, 13, 17]

def calRate(rate, count):
    result = 1
    r = 1

    for i in range(18, 18-count, -1):
        result *= i
        r *= rate

    for i in range(1, 18-count+1):
        r *= (1-rate)

    for i in range(count, 0, -1):
        result /= i

    return result * r

ARate = int(input()) / 100
BRate = int(input()) / 100

answer = 0
AResult = 0
BResult = 0
for n in primeNumber:
    print(n)
    AResult += calRate(ARate, n)
    BResult += calRate(BRate, n)
    print(AResult, BResult)

print(AResult * (1 - BResult) + BResult * (1 - AResult) + AResult * BResult) 

