# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(S, C):
    # Implement your solution here
    N = len(C)
    left, right = 0, 1
    answer = 0

    if N == 1:
        return answer

    while right < N:
        if S[left] == S[right]:
            if C[left] < C[right]:
                answer += C[left]
                left = right
                right +=1
            else:
                answer += C[right]
                right += 1
        else:
            left = right
            right += 1
                    

    return answer