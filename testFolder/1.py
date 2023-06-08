def bioHazard(n, allergic, poisonous):
    alList = [[] for _ in range(n+1)]
    for i in range(len(allergic)):
        alList[allergic[i]].append(poisonous[i])
        alList[poisonous[i]].append(allergic[i])     
    
    left, right = 1, 2
    answer = 0
    flag = 0
    while True:
        if alList[right] != []:
            for i in range(left, right):
                if i in alList[right]:
                    flag = -1
                    break
            if flag == -1:
                print(left, right)
                answer += count(right-left)
                flag = 0
                if right+2 < n:
                    left = right + 1
                    right = left + 1
                else:
                    print("?")
                    break
            if right+1 < n:
                right += 1
            else:
                print(left, right)
                print("?")
                answer += count(right-left)
                break
        if right+1 < n:
                right += 1
        else:
            print("?")
            print(right, left, n)
            answer += count(right-left)
            break
            
    return answer

def count(k):
    sum = 0
    for i in range(k, 0, -1):
        sum += (fac(k, i)//fac(i, 1))
    return sum
            
def fac(n, e):
    if n == e:
        return n

    return n*fac(n-1, e)
n = int(input().strip())

allergic_count = int(input().strip())

allergic = []

for _ in range(allergic_count):
    allergic_item = int(input().strip())
    allergic.append(allergic_item)

poisonous_count = int(input().strip())

poisonous = []

for _ in range(poisonous_count):
    poisonous_item = int(input().strip())
    poisonous.append(poisonous_item)

result = bioHazard(n, allergic, poisonous)

print(result)


# 1 2 3 4 5 6 7 8

# [2, 3, 4, 3] [8, 5, 6, 4]
# [[], [], [8], [5, 4], [6, 3], [3], [4], [], [2]]