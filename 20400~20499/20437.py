# 문자열 게임 2 
# 시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
# 1 초	1024 MB	2888	1252	921	42.170%
# 문제
# 작년에 이어 새로운 문자열 게임이 있다. 게임의 진행 방식은 아래와 같다.

# 알파벳 소문자로 이루어진 문자열 W가 주어진다.
# 양의 정수 K가 주어진다.
# 어떤 문자를 정확히 K개를 포함하는 가장 짧은 연속 문자열의 길이를 구한다.
# 어떤 문자를 정확히 K개를 포함하고, 문자열의 첫 번째와 마지막 글자가 해당 문자로 같은 가장 긴 연속 문자열의 길이를 구한다.
# 위와 같은 방식으로 게임을 T회 진행한다.

# 입력
# 문자열 게임의 수 T가 주어진다. (1 ≤ T ≤ 100)

# 다음 줄부터 2개의 줄 동안 문자열 W와 정수 K가 주어진다. (1 ≤ K ≤ |W| ≤ 10,000) 

# 출력
# T개의 줄 동안 문자열 게임의 3번과 4번에서 구한 연속 문자열의 길이를 공백을 사이에 두고 출력한다.

# 만약 만족하는 연속 문자열이 없을 시 -1을 출력한다.

# 예제 입력 1  복사
# 2
# superaquatornado
# 2
# abcdefghijklmnopqrstuvwxyz
# 5
# 예제 출력 1  복사
# 4 8
# -1
# 첫 번째 문자열에서 3번에서 구한 문자열은 aqua, 4번에서 구한 문자열은 raquator이다.

# 두 번째 문자열에서는 어떤 문자가 5개 포함된 문자열을 찾을 수 없으므로 -1을 출력한다.

# 예제 입력 2  복사
# 1
# abaaaba
# 3
# 예제 출력 2  복사
# 3 4
# 투포인터 시간초과
# import sys
# input = sys.stdin.readline
# answer = []
# for _ in range(int(input())):
#     word = input().rstrip()
#     seq = int(input())
#     answer1, answer2 = 0, 10001
#     left = 0
#     right = 1
#     while left != len(word):
#         if word[left:right].count(word[left]) == seq :
#             answer2 = min(answer2, right-left)
#             if word[right-1] == word[left] :
#                 answer1 = max(answer1, right-left)
#         elif word[left:right].count(word[left]) < seq and right != len(word):
#             right += 1
#         elif word[left:right].count(word[left]) > seq :
#             right -= 1
#         else :
#             left += 1
#     if answer2 == 10001 and answer1 == 0 :
#         print(-1)
#     else:
#         print(answer2, answer1)

import sys
input = sys.stdin.readline

for _ in range(int(input())):
    v = list(map(lambda x: ord(x) - 97, input().strip()))
    k, mn, mx = int(input()), len(v), -1
    pos = [[] for _ in range(26)]
    print(pos)
    for idx, val in enumerate(v):
        pos[val].append(idx)
    for p in pos:
        for i in range(len(p) - k + 1):
            mn = min(mn, p[i + k - 1] - p[i] + 1)
            mx = max(mx, p[i + k - 1] - p[i] + 1)

    print(-1 if mx == -1 else f"{mn} {mx}")