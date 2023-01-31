# 월드컵
# 시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
# 1 초	128 MB	8564	2478	1755	31.233%
# 문제
# 월드컵 조별 최종 예선에서는 6개국으로 구성된 각 조별로 동일한 조에 소속된 국가들과 한 번씩, 각 국가별로 총 5번의 경기를 치른다. 조별리그가 끝난 후, 기자가 보내온 각 나라의 승, 무승부, 패의 수가 가능한 결과인지를 판별하려고 한다. 다음은 가능한 결과와 가능하지 않은 결과의 예이다.

# 나라	승	무	패
# A	5	0	0
# B	3	0	2
# C	2	0	3
# D	0	0	5
# E	4	0	1
# F	1	0	4	
# 나라	승	무	패
# A	4	1	0
# B	3	0	2
# C	4	1	0
# D	1	1	3
# E	0	0	5
# F	1	1	3	
# 나라	승	무	패
# A	5	0	0
# B	4	0	1
# C	2	2	1
# D	2	0	3
# E	1	0	4
# F	0	0	5	
# 나라	승	무	패
# A	5	0	0
# B	3	1	1
# C	2	1	1
# D	2	0	3
# E	0	0	5
# F	1	0	4
# 예제 1 가능한 결과	예제 2 가능한 결과	예제 3 불가능한 결과	예제 4 불가능한 결과
# 네 가지의 결과가 주어질 때 각각의 결과에 대하여 가능하면 1, 불가능하면 0을 출력하는 프로그램을 작성하시오.

# 입력
# 첫째 줄부터 넷째 줄까지 각 줄마다 6개국의 결과가 나라별로 승, 무승부, 패의 순서로 빈칸을 하나 사이에 두고 18개의 숫자로 주어진다. 승, 무, 패의 수는 6보다 작거나 같은 자연수 또는 0이다.

# 출력
# 입력에서 주어진 네 가지 결과에 대하여 가능한 결과는 1, 불가능한 결과는 0을 빈칸을 하나 사이에 두고 출력한다.

# 예제 입력 1 
# 6 0 0 3 0 2 2 0 3 0 0 5 4 0 1 1 0 4
# 4 1 0 3 0 2 4 1 0 1 1 3 0 0 5 1 1 3
# 5 0 0 4 0 1 2 2 1 2 0 3 1 0 4 0 0 5
# 5 0 0 3 1 1 2 1 2 2 0 3 0 0 5 1 0 4
# 예제 출력 1 
# 1 1 0 0
import copy

answer = [0, 0, 0, 0]
def solution(result, p):
    dfs(copy.deepcopy(result), 0, 1, -1,copy.deepcopy(result), p)
        

def dfs(re, i, c, r, result, p):
    global answer
    if r == 0 :
        re[i+c-1][2] -= 1
        re[i][0] -= 1 
    elif r == 1:
        re[i+c-1][1] -= 1
        re[i][1] -= 1
    elif r == 2:
        re[i+c-1][0] -= 1
        re[i][2] -= 1
    
    if i == 5 :
        answer[p] = 1
        return

    if i + c == 6 :
        dfs(copy.deepcopy(re), i+1, 1, -1, copy.deepcopy(result), p)
        return
    
    if re[i][0] != 0 and re[i+c][2] != 0:
        dfs(copy.deepcopy(re), i, c+1, 0, result, p)
    if re[i][1] != 0 and re[i+c][1] != 0:
        dfs(copy.deepcopy(re), i, c+1, 1, result, p)
    if re[i][2] != 0 and re[i+c][0] != 0:
        dfs(copy.deepcopy(re), i, c+1, 2, result, p)
    
for p in range(4):
    result = []
    temp = list(map(int, input().split()))
    for i in range(0, 18, 3) :
        result.append(temp[i:i+3])
    solution(result, p)
    for i in range(6):
        if 5 < sum(result[i]) :
            answer[p] = 0  
    print(answer[p])
