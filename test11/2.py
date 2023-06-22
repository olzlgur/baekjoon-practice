# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(S):
    answer = 0
    word = []
    word.append(S.count('B'))
    word.append(S.count('A'))
    word.append(S.count('N'))

    while True:
        if word[0] < 1 or word[1] < 3 or word[2] < 2:
            break
        word[0] -= 1
        word[1] -= 3
        word[2] -= 2
        answer += 1

    return answer

# B 1 A 3 N 2