# 문자열 교환 
# 시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
# 2 초	128 MB	1061	521	448	54.172%
# 문제
# a와 b로만 이루어진 문자열이 주어질 때,  a를 모두 연속으로 만들기 위해서 필요한 교환의 회수를 최소로 하는 프로그램을 작성하시오.

# 이 문자열은 원형이기 때문에, 처음과 끝은 서로 인접해 있는 것이다.

# 예를 들어,  aabbaaabaaba이 주어졌을 때, 2번의 교환이면 a를 모두 연속으로 만들 수 있다.

# 입력
# 첫째 줄에 문자열이 주어진다. 문자열의 길이는 최대 1,000이다.

# 출력
# 첫째 줄에 필요한 교환의 회수의 최솟값을 출력한다.

# 예제 입력 1  복사
# abababababababa
# 예제 출력 1  복사
# 3
# 예제 입력 2  복사
# ba
# 예제 출력 2  복사
# 0
# 예제 입력 3  복사
# aaaabbbbba
# 예제 출력 3  복사
# 0
# 예제 입력 4  복사
# abab
# 예제 출력 4  복사
# 1
# 예제 입력 5  복사
# aabbaaabaaba
# 예제 출력 5  복사
# 2
# 예제 입력 6  복사
# aaaa
# 예제 출력 6  복사
# 0

word = list(input())
a_cnt = word.count('a')
answer = 999999999999999
left = 0

while left < len(word):
  right = left + a_cnt
  if right > len(word):
    temp = word[left:len(word)] + word[:right-len(word)]
  else:
    temp = word[left:right]
  answer = min(answer, temp.count('b'))
  left += 1

print(answer)