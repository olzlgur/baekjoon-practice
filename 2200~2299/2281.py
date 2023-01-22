# -*- coding: utf-8 -*- 
#  문제
# 사악한 라이토는 기발한 방법을 이용하여 L(애칭 섊)을 살해한 뒤 데스노트를 다시 손에 넣었다. 라이토는 이제 이 노트에 n명의 이름을 적어 넣으려고 한다. 이때 다음과 같은 조건을 만족시키면서 이름을 적어 넣으려 한다.

# 우선, 이름을 적어 넣을 때 이미 정해진 순서대로 n명의 이름을 적어 넣어야 한다. 이름을 적을 때도, 노트를 위에서 아래로, 같은 줄에서는 왼쪽 맨 끝에서 오른쪽으로 차례로 적는다고 하자. 또한 이름을 적을 때 각 사람의 이름 사이에 빈 칸을 하나씩 두려고 한다. 한 줄을 적다가 그 줄의 끝에 한 사람의 이름이 다 들어가지 않고 잘리게 되면 반드시 새로운 줄에 이름을 써야 한다. 그렇지 않으면 이름이 중간에 잘려서 자칫하면 두 명의 사람이 죽게 된다. 이때, 각 줄의 끝에 사용하지 않고 남게 되는 칸의 수의 제곱의 합이 최소가 되도록 하려 한다. 이를 계산할 때 제일 마지막 줄은 앞으로 이름을 적을 기회가 있으므로 계산하지 않는다. 예를 들어 노트의 폭(너비)이 20인 다음의 경우를 보자.



# 각 사람의 이름의 길이가 차례로 7, 4, 2, 3, 2, 5, 1, 12, 7, 5, 6 인 경우이다. 위와 같이 적으면 차례로 1, 10, 0칸이 남아서 제곱의 합이 101이 된다. 반면에 아래의 경우에는 5, 6, 0칸이 남아서 제곱의 합이 61이 된다.

# 입력
# 첫째 줄에 n(1 ≤ n ≤ 1,000), m(1 ≤ m ≤ 1,000)이 주어진다. m은 노트의 가로 칸의 개수(폭, 너비)이다. 다음 n개의 줄에는 각 사람의 이름의 길이가 노트에 적어야 할 순서대로 주어진다. 각 길이는 m을 넘지 않는 자연수이다.

# 출력
# 첫째 줄에 남게 되는 칸 수의 제곱의 합의 최솟값을 출력한다.
# dfs 시간초과
import sys
sys.setrecursionlimit(100000)
n, m = map(int, input().split())
dp =[0] * (n+1)
nl = []

answer = 1000000

def solution():
    for i in range(n):
        nl.append(int(input()))
    if len(nl) == 1:
        print(0)
    dfs(1, nl[0], 0)

def dfs(index, ex, value):
    global answer 
    if index == n :
        answer = min(answer, value) 
        return
    if ex + nl[index] + 1 <= m :
        dfs(index + 1, ex + nl[index] + 1,  value)
    dfs(index+1, nl[index], value + (m - ex) ** 2) 

solution()
print(answer)