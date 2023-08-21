# 탈출 
# 시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
# 1 초	256 MB	4369	1458	1170	32.428%
# 문제
# 홍익이는 홍익대학교 프로그래밍 경진대회의 출제진이다. 홍익이는 새벽에 문제를 만들던 도중 뒤통수에 느껴지는 고통과 함께 정신을 잃었다.

# 홍익이는 좁은 방에서 눈을 떴다. 주변을 살펴보니 벽면에는 LED로 된 다섯 자리 십진수 N이, 그 옆에 T, G라는 알파벳과 함께 또 다른 정수 두 개가 쓰여 있었고, 벽 앞에는 버튼 A, B 두 개가 있었다.



# 버튼을 이리저리 눌러보던 똑똑한 홍익이는 어떻게 해야 방을 탈출할 수 있을지 금방 눈치챘다.

# 버튼과 수에 대해 홍익이가 알아낸 것은 다음과 같다.

# 버튼 A를 누르면 N이 1 증가한다.
# 버튼 B를 누르면 N에 2가 곱해진 뒤, 0이 아닌 가장 높은 자릿수의 숫자가 1 줄어든다. 예를 들어 123→146으로, 5→0으로, 3→5로 변한다. 단, N이 0이면 버튼 B를 눌러도 수가 변하지 않는다.
# LED가 다섯 자리까지밖에 없기 때문에 N이 99,999를 넘어가는 순간 탈출에 실패하게 된다.
# 버튼 B를 눌러 N에 2를 곱한 순간 수가 99,999를 넘어간다면, 높은 자릿수의 수를 1 낮췄을때 99,999를 넘지 않는다고 해도 탈출에 실패하게 된다.
# 또한 홍익이는 최대 T회 버튼을 누를 수 있고, 그 횟수 안에 LED로 표현된 N을 G와 같게 만들어야 탈출할 수 있다는 사실을 알아냈다.

# 똑똑한 홍익이는 이와중에 자존심이 발동해 버튼 누르는 횟수를 최소로 하여 방을 탈출하기로 했다.

# 홍익이의 방 탈출을 기원하며, 탈출에 필요한 최소의 버튼 횟수를 구하자.

# 입력
# 첫 번째 줄에 N (0 ≤ N ≤ 99,999), T (1 ≤ T ≤ 99,999), G (0 ≤ G ≤ 99,999)가 공백 하나를 사이에 두고 주어진다.

# 각각 N은 LED로 표현된 수, T는 버튼을 누를 수 있는 최대 횟수, G는 탈출을 위해 똑같이 만들어야 하는 수를 뜻한다.

# 출력
# 첫 번째 줄에 탈출에 필요한 최소의 버튼 횟수를 출력한다.

# 만약 탈출할 수 없다면 “ANG”을 따옴표 없이 출력한다.

# 예제 입력 1  복사
# 1 7 10
# 예제 출력 1  복사
# 7
# 버튼을 A A A B A A A 순서로 누르면

# 1 -> 2 -> 3 -> 4 -> 7 -> 8 -> 9 -> 10 순서로 숫자가 변한다.

# 예제 입력 2  복사
# 7142 10 7569
# 예제 출력 2  복사
# 3
# 예제 입력 3  복사
# 7142 1 7569
# 예제 출력 3  복사
# ANG
# 예제 입력 4  복사
# 63429 99999 231
# 예제 출력 4  복사
# ANG

import sys
from collections import deque

input = sys.stdin.readline

N, T, G = map(int, input().split())

q = deque()

q.append((N, 0))
flag = 0
visited = [0] * 1000000

while q:
    num, cnt = q.popleft()
    if T < cnt: 
        break
    if num == G: 
        flag = 1
        break
    
    if 2*num <= 99999 and 0 <= 2*num-10**(len(str(2*num))-1) and visited[2*num-10**(len(str(2*num))-1)] == 0:
        q.append((2*num-10**(len(str(2*num))-1), cnt+1))
        visited[2*num-10**(len(str(2*num))-1)] = 1
    if num + 1 <= 99999 and visited[num+1] == 0:
        q.append((num+1, cnt+1))
        visited[num+1] = 1

if flag == 1:
    print(cnt)
else:
    print("ANG")