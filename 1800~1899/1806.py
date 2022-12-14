# 10,000 이하의 자연수로 이루어진 길이 N짜리 수열이 주어진다. 이 수열에서 연속된 수들의 부분합 중에 그 합이 S 이상이 되는 것 중, 가장 짧은 것의 길이를 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 N (10 ≤ N < 100,000)과 S (0 < S ≤ 100,000,000)가 주어진다. 둘째 줄에는 수열이 주어진다. 수열의 각 원소는 공백으로 구분되어져 있으며, 10,000이하의 자연수이다.

# 출력
# 첫째 줄에 구하고자 하는 최소의 길이를 출력한다. 만일 그러한 합을 만드는 것이 불가능하다면 0을 출력하면 된다.

# 10 15
# 5 1 3 5 10 7 4 9 2 8 

# 2

n, s = map(int, input().split())

li = list(map(int, input().split()))

left = 0
right = 0
sum = 0
answer = n

while True :
    if sum >= s :
        answer = min(answer, right-left)
        sum -= li[left]
        left += 1
    elif right == n :
        break
    elif sum < s :
        sum += li[right]
        right += 1
    
print(answer)

# m = 0 
# temp = 0
# cnt = 0
# answer = n

# for i in range(len(li)):
#     for j in range(i, len(li)) :
#         temp += li[j]
#         cnt += 1
#         if temp >= s :
#             if temp > m  and cnt < answer:
#                 answer = cnt
#             cnt = 0
#             temp = 0
#             break
# print(answer)
