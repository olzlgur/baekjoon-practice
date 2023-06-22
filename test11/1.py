# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(S):
    # Implement your solution here
    left, right = 0, len(S) -1
    answer = 0
    if S[left] == S[right]:
        answer += 1
    
    left, right = 1, 0

    for _ in range(1, len(S)):
        if S[left] == S[right]:
            answer += 1
        left += 1
        right += 1

    return answer

# 길이 N인 문자열 s, n-1 작업 적용, S의 첫글자를 끝으로 이동