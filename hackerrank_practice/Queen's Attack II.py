# 5 3
# 4 3
# 5 5
# 4 2
# 2 3
def queensAttack(n, k, r_q, c_q, obstacles):
    answer = 0

    if n == 1:
        return answer 
    
    dx = [-1, -1, 0, 1, 1, 1, 0, -1]
    dy = [0, -1, -1, -1, 0, 1, 1, 1]

    for i in range(8):
        y, x = r_q, c_q
        while True:
            x, y = x + dx[i], y+dy[i]
            if x <= 0 or n < x or y <= 0 or n < y or [y, x] in obstacles:
                break
            answer += 1

    return answer


first_multiple_input = input().rstrip().split()

n = int(first_multiple_input[0])

k = int(first_multiple_input[1])

second_multiple_input = input().rstrip().split()

r_q = int(second_multiple_input[0])

c_q = int(second_multiple_input[1])
obstacles = []

for _ in range(k):    
    obstacles.append(list(map(int, input().rstrip().split())))
result = queensAttack(n, k, r_q, c_q, obstacles)

print(result)