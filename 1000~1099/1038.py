# 감소하는 수
# 시간 제한 메모리 제한  제출  정답  맞힌 사람   정답 비율
# 1 초   512 MB  21721   6534    5169    32.966%
# 문제
# 음이 아닌 정수 X의 자릿수가 가장 큰 자릿수부터 작은 자릿수까지 감소한다면, 그 수를 감소하는 수라고 한다. 예를 들어, 321과 950은 감소하는 수지만, 322와 958은 아니다. N번째 감소하는 수를 출력하는 프로그램을 작성하시오. 0은 0번째 감소하는 수이고, 1은 1번째 감소하는 수이다. 만약 N번째 감소하는 수가 없다면 -1을 출력한다.

# 입력
# 첫째 줄에 N이 주어진다. N은 1,000,000보다 작거나 같은 자연수 또는 0이다.

# 출력
# 첫째 줄에 N번째 감소하는 수를 출력한다.

# 예제 입력 1 
# 18
# 예제 출력 1 
# 42
# 예제 입력 2 
# 0
# 예제 출력 2 
# 0
# 예제 입력 3 
# 500000
# 예제 출력 3 
# -1

# 9876543210 감소 가능한 최대 수
from itertools import combinations

nl = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
n = int(input())
answer = []
for i in range(1, 11):
    for t in combinations(nl, i):
        t = list(t)
        t.sort(reverse=True)
        answer.append(int("".join(map(str,t))))

answer.sort()
try :
    print(answer[n])
except :
    print(-1)