def solution(b):
    answer = -1
    temp = b**2

    for i in range(1, b+1):
        for j in range(b+1, 500001):
            if i**2 + temp == j**2:
                return j
            elif i**2 + temp < j**2:
                break
    
    return answer

