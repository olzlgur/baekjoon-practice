# 문자열 판별 
# 시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
# 2 초	512 MB	4447	1198	883	30.302%
# 문제
# 알파벳 소문자로 이루어진 문자열 S와 단어 목록 A가 주어졌을 때, S를 A에 포함된 문자열을 한 개 이상 공백없이 붙여서 만들 수 있는지 없는지 구하는 프로그램을 작성하시오. A에 포함된 단어를 여러 번 사용할 수 있다.

# 입력
# 첫째 줄에 길이가 100이하인 문자열 S가 주어진다. 둘째 줄에는 A에 포함된 문자열의 개수 N(1 ≤ N ≤ 100)이 주어진다. 셋째 줄부터 N개의 줄에는 A에 포함된 단어가 한 줄에 하나씩 주어진다. A에 포함된 문자열은 알파벳 소문자로만 이루어져 있고, 길이는 100을 넘지 않는다.

# 출력
# A에 포함된 문자열로 S를 만들 수 있으면 1, 없으면 0을 출력한다.

# 예제 입력 1  복사
# softwarecontest
# 2
# software
# contest
# 예제 출력 1  복사
# 1

from collections import deque
import sys

input = sys.stdin.readline

answer = 0
word = input().rstrip()

wordList = []
q = deque()
n = int(input())
for _ in range(n):
    w = input().rstrip()
    wordList.append(w)
wordLen = len(word)    

dp = [0]*(wordLen+1)
dp[0] = 1

for w in wordList:
    for j in range(0, wordLen):
        if word[j:j+len(w)] == w and dp[j] != 0:
            dp[j+len(w)] = dp[j]
            j += len(w)
        
print(dp[-1])



