# 비슷한 단어 
# 시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
# 2 초	128 MB	1968	401	284	25.912%
# 문제
# N개의 영단어들이 주어졌을 때, 가장 비슷한 두 단어를 구해내는 프로그램을 작성하시오.

# 두 단어의 비슷한 정도는 두 단어의 접두사의 길이로 측정한다. 접두사란 두 단어의 앞부분에서 공통적으로 나타나는 부분문자열을 말한다. 즉, 두 단어의 앞에서부터 M개의 글자들이 같으면서 M이 최대인 경우를 구하는 것이다. "AHEHHEH", "AHAHEH"의 접두사는 "AH"가 되고, "AB", "CD"의 접두사는 ""(길이가 0)이 된다.

# 접두사의 길이가 최대인 경우가 여러 개일 때에는 입력되는 순서대로 제일 앞쪽에 있는 단어를 답으로 한다. 즉, 답으로 S라는 문자열과 T라는 문자열을 출력한다고 했을 때, 우선 S가 입력되는 순서대로 제일 앞쪽에 있는 단어인 경우를 출력하고, 그런 경우도 여러 개 있을 때에는 그 중에서 T가 입력되는 순서대로 제일 앞쪽에 있는 단어인 경우를 출력한다.

# 입력
# 첫째 줄에 N(2 ≤ N ≤ 20,000)이 주어진다. 다음 N개의 줄에 알파벳 소문자로만 이루어진 길이 100자 이하의 서로 다른 영단어가 주어진다.

# 출력
# 첫째 줄에 S를, 둘째 줄에 T를 출력한다. 단, 이 두 단어는 서로 달라야 한다. 즉, 가장 비슷한 두 단어를 구할 때 같은 단어는 제외하는 것이다.

# 예제 입력 1  복사
# 9
# noon
# is
# lunch
# for
# most
# noone
# waits
# until
# two
# 예제 출력 1  복사
# noon
# noone
# 예제 입력 2  복사
# 4
# abcd
# abe
# abc
# abchldp
# 예제 출력 2  복사
# abcd
# abc

import sys

input = sys.stdin.readline

n = int(input())
result = []

for _ in range(n):
    result.append(input().rstrip())

word = sorted(list(enumerate(result)),key = lambda x: x[1])

cnt = 0
preWord = ''
minNum = n
wordList = []
for i in range(n-1):
    if word[i][1] != word[i+1][1]:
        if len(word[i][1]) < len(word[i+1][1]):
            wLen = len(word[i][1])
        else:
            wLen = len(word[i+1][1])
        for idx in range(wLen):
            if word[i][1][idx] != word[i+1][1][idx]:
                if cnt < idx:
                    wordList = []
                    preWord = word[i][1][:idx]
                    wordList.append(word[i])
                    wordList.append(word[i+1])
                    minNum = min(word[i][0], word[i+1][0])
                    cnt = idx    
                elif cnt == idx and idx !=0:
                    if preWord != word[i][1][:idx]:
                        if min(word[i][0], word[i+1][0]) < minNum:
                            wordList = []
                            preWord = word[i][1][:idx]
                            wordList.append(word[i])
                            wordList.append(word[i+1])
                            minNum = min(word[i][0], word[i+1][0])
                            cnt = idx
                    else:
                        minNum = min(minNum, word[i][0], word[i+1][0])
                        wordList.append(word[i])
                        wordList.append(word[i+1])
                break
        else:
            if cnt < idx+1:
                wordList = []
                preWord = word[i][1][:idx+1]
                wordList.append(word[i])
                wordList.append(word[i+1])
                minNum = min(word[i][0], word[i+1][0])
                cnt = idx + 1  
            elif cnt == idx+1:
                if preWord != word[i][1][:idx+1]:
                    if min(word[i][0], word[i+1][0]) < minNum:
                        wordList = []
                        wordList.append(word[i])
                        wordList.append(word[i+1])
                        minNum = min(word[i][0], word[i+1][0])
                        cnt = idx+1
                        preWord = word[i][1][:idx+1]
                else:
                    wordList.append(word[i])
                    wordList.append(word[i+1])
                    minNum = min(minNum, word[i][0], word[i+1][0])
wordList = list(set(wordList))

wordList.sort(key=lambda x : x[0])
if len(wordList) == 0:
    print(result[0])
    print(result[1])
else:
    print(wordList[0][1])
    print(wordList[1][1])

