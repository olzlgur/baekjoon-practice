# 내일 할거야 다국어
# 시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
# 2 초	256 MB	1542	706	564	49.692%
# 문제
# 아 과제 하기 싫다. 아무 것도 안 하고 싶다. 더 적극적이고 격렬하게 아무 것도 안 하고 싶다.

# 있잖아. 내가 아까 책상에다가 n개의 과제 목록을 적어놨어. 각각의 과제 i는 di 일이 걸리고, 오늘로부터 ti 일 안에 끝내야 해. 그러니까 오늘이 0일이면, ti일이 끝나기 전에 제출이야. 과제는 한번 시작하면 쉬지 않고 계속해야 해. 안 그러면 머리 아파 지거든.

# 근데 있잖아. 내가 지금 너무, 너무 아무 것도 안 하고 싶어. 그래서 오늘은 아무 것도 안 할 거야. 더 중요한 게 뭔지 알아? 사실 나 내일도, 모레도, 아무 것도 안 하고 싶어. 한 며칠 동안은 계속 아무 것도 안하려고. 아. 과제가 있을 때 내가 내일부터 연속으로 최대 며칠동안 놀 수 있는지 궁금하다. 궁금하긴 한데, 난 아무 것도 안 하고 싶어.

# 좋은 생각이 났다. 너희가 이걸 대신 구해주면, 내가 너희의 맞은 문제 수를 하나 올려줄게.

# 입력
# 첫째 줄에는 과제의 개수인 정수 n (1 ≤ n ≤ 106)이 주어진다.

# 이후 n개의 줄에 각각의 과제를 나타내는 두 정수 di, ti (1 ≤ di, ti ≤ 109)가 순서대로 주어진다. 오늘은 0일이다.

# 모든 입력에 대해, 오늘 아무 것도 안 해도 과제를 마무리 할 수 있는 방법이 존재함이 보장된다.

# 출력
# 내일(1일)부터 연속으로 최대 며칠 동안 놀 수 있는지를 출력한다. 가령, 답이 0이면, 내일 과제를 해야 하며, 1 이면, 모레에 과제를 해야 한다.

# 예제 입력 1  복사
# 3
# 2 8
# 1 13
# 3 10
# 예제 출력 1  복사
# 5

import sys

input = sys.stdin.readline

n = int(input())

homework = []

for i in range(n):
    du, deadline= map(int, input().split())
    homework.append((du, deadline))

homework.sort(key=lambda x : x[1])
print(homework)

cur = 0
cur = homework[len(homework)-1][1] - homework[len(homework)-1][0]
for i in range(len(homework)-2, -1, -1):
    print(cur, homework[i][0], homework[i][1])
    if homework[i][1] < cur:
        cur = homework[i][1] - homework[i][0]
    else :
        cur = cur - homework[i][0]

print(cur)
