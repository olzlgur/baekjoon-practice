# List of Unique Numbers 
# 시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
# 1 초	32 MB	4594	1683	1225	35.652%
# 문제
# 길이가 N인 수열이 주어질 때, 수열에서 연속한 1개 이상의 수를 뽑았을 때 같은 수가 여러 번 등장하지 않는 경우의 수를 구하는 프로그램을 작성하여라.

# 입력
# 첫 번째 줄에는 수열의 길이 N이 주어진다. (1 ≤ N ≤ 100,000)

# 두 번째 줄에는 수열을 나타내는 N개의 정수가 주어진다. 수열에 나타나는 수는 모두 1 이상 100,000 이하이다.

# 출력
# 조건을 만족하는 경우의 수를 출력한다.

# 예제 입력 1  복사
# 5
# 1 2 3 4 5
# 예제 출력 1  복사
# 15
# 예제 입력 2  복사
# 5
# 1 2 3 1 2
# 예제 출력 2  복사
# 12
# 예제 입력 3  복사
# 5
# 1 1 1 1 1
# 예제 출력 3  복사
# 5

import sys

input = sys.stdin.readline
def calRate(n, count):
    result = 1
    r = 1

    for i in range(n, n-count, -1):
        result *= i


    for i in range(count, 0, -1):
        result /= i

    return int(result)

def cal(n):
    result = 0

    for i in range(1, n+1):
        result += calRate(n, i)

    return result 

answer = 0

n = int(input())
number = list(map(int, input().split()))

visited = [0] * n
check = []

answer = 0

for i in range(n):
    if visited[number[i]] == 1:
        answer += cal(len(check))
        for c in check:
            visited[c] = 0
        visited[number[i]] = 1
        check = [number[i]]
    else:
        visited[number[i]] = 1
        check.append(number[i])
print(answer)
answer += cal(len(check))

print(answer)

